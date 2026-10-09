
# File: python/jobs.py

from mysql.connector import Error
from database import get_connection


def post_job():
    """Create a new job posting."""
    try:
        company_id = int(input("Enter registered company ID: "))
        min_experience = float(
            input("Enter minimum experience in years: ")
        )

        if company_id <= 0 or not 0 <= min_experience <= 999.9:
            print("Enter valid company ID and experience.")
            return

        salary_min = float(input("Enter minimum annual salary: "))
        salary_max = float(input("Enter maximum annual salary: "))

        if salary_min < 0 or salary_max < salary_min:
            print("Invalid salary range.")
            return

    except ValueError:
        print("IDs, experience and salaries must be numeric.")
        return

    title = input("Enter job title: ").strip()
    description = input("Enter job description: ").strip()
    skills = input("Enter required skills, comma-separated: ").strip()
    location = input("Enter job location: ").strip()
    job_type = input("Enter job type (Full-time/Part-time/Contract): ").strip()

    if not all([title, skills, location, job_type]):
        print("Title, skills, location and job type are required.")
        return

    if job_type not in ("Full-time", "Part-time", "Contract"):
        print("Invalid job type.")
        return

    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    try:
        cursor.execute("""
            INSERT INTO jobs
            (company_id, job_title, description, required_skills,
             min_experience, salary_min, salary_max,
             location, job_type)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            company_id, title, description, skills,
            min_experience, salary_min, salary_max,
            location, job_type
        ))

        connection.commit()
        print("Job posted successfully.")
        print("Job ID:", cursor.lastrowid)

    except Error as error:
        connection.rollback()
        print("Unable to post job:", error)

    finally:
        cursor.close()
        connection.close()


def view_jobs():
    """Display all open job postings."""
    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT j.job_id, j.job_title, co.company_name,
                   j.required_skills, j.min_experience,
                   j.salary_min, j.salary_max,
                   j.location, j.job_type
            FROM jobs j
            INNER JOIN companies co
                ON j.company_id = co.company_id
            WHERE j.status = 'Open'
            ORDER BY j.posted_at DESC
        """)

        jobs = cursor.fetchall()

        if not jobs:
            print("No open jobs found.")

        for job in jobs:
            print("-" * 55)
            print(job)

    except Error as error:
        print("Unable to retrieve jobs:", error)

    finally:
        cursor.close()
        connection.close()


def search_jobs():
    """Search open jobs by title, skill or location."""
    keyword = input("Enter job title, skill or location: ").strip()

    if not keyword:
        print("Search text cannot be empty.")
        return

    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor(dictionary=True)
    pattern = f"%{keyword}%"

    try:
        cursor.execute("""
            SELECT j.job_id, j.job_title, co.company_name,
                   j.required_skills, j.min_experience,
                   j.salary_min, j.salary_max, j.location
            FROM jobs j
            INNER JOIN companies co
                ON j.company_id = co.company_id
            WHERE j.status = 'Open'
              AND (
                  j.job_title LIKE %s
                  OR j.required_skills LIKE %s
                  OR j.location LIKE %s
              )
            ORDER BY j.salary_max DESC
        """, (pattern, pattern, pattern))

        results = cursor.fetchall()

        if not results:
            print("No matching open jobs found.")

        for job in results:
            print(job)

    except Error as error:
        print("Job search failed:", error)

    finally:
        cursor.close()
        connection.close()


def recommend_jobs():
    """Recommend open jobs using skills, experience and location."""
    skills_input = input(
        "Enter your skills, separated by commas: "
    ).strip()

    location = input("Enter preferred location: ").strip()

    try:
        experience = float(input("Enter experience in years: "))

        if experience < 0 or experience > 999.9:
            print("Enter a valid experience value.")
            return

    except ValueError:
        print("Experience must be numeric.")
        return

    if not skills_input or not location:
        print("Skills and location are required.")
        return

    # Normalize skill input into a set of unique keywords.
    skills = {
        skill.strip().lower()
        for skill in skills_input.split(",")
        if skill.strip()
    }

    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT j.job_id, j.job_title, co.company_name,
                   j.required_skills, j.min_experience,
                   j.salary_min, j.salary_max, j.location
            FROM jobs j
            INNER JOIN companies co
                ON j.company_id = co.company_id
            WHERE j.status = 'Open'
              AND j.min_experience <= %s
              AND LOWER(j.location) = LOWER(%s)
            ORDER BY j.salary_max DESC
        """, (experience, location))

        jobs = cursor.fetchall()
        recommendations = []

        for job in jobs:
            required = {
                skill.strip().lower()
                for skill in job["required_skills"].split(",")
                if skill.strip()
            }

            # Score exact skill matches, then sort by score.
            matched_skills = skills.intersection(required)
            score = len(matched_skills)

            if score > 0:
                job["matched_skills"] = sorted(matched_skills)
                job["match_score"] = round(
                    score / max(len(required), 1) * 100, 1
                )
                recommendations.append(job)

        recommendations.sort(
            key=lambda item: (
                item["match_score"],
                item["salary_max"] or 0
            ),
            reverse=True
        )

        if not recommendations:
            print(
                "No suitable jobs found. Try a different location "
                "or review your skills."
            )
            return

        print("\nRecommended jobs:")

        for job in recommendations:
            print("-" * 55)
            print("Job ID:", job["job_id"])
            print("Title:", job["job_title"])
            print("Company:", job["company_name"])
            print("Location:", job["location"])
            print("Required skills:", job["required_skills"])
            print("Matched skills:", ", ".join(job["matched_skills"]))
            print("Match score:", f'{job["match_score"]}%')
            print("Salary range:", job["salary_min"], "-", job["salary_max"])
            print("Minimum experience:", job["min_experience"])

    except Error as error:
        print("Recommendation failed:", error)

    finally:
        cursor.close()
        connection.close()