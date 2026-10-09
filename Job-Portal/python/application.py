
# File: python/application.py

from datetime import datetime
from mysql.connector import Error
from database import get_connection


APPLICATION_STATUSES = (
    "Applied",
    "Under Review",
    "Shortlisted",
    "Selected",
    "Rejected"
)


def apply_for_job():
    """Submit an application for an open job."""
    try:
        candidate_id = int(input("Enter candidate ID: "))
        job_id = int(input("Enter job ID: "))

        if candidate_id <= 0 or job_id <= 0:
            print("IDs must be positive integers.")
            return

    except ValueError:
        print("Candidate ID and job ID must be integers.")
        return

    cover_letter = input("Enter cover letter (optional): ").strip()

    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    try:
        cursor.execute("""
            SELECT job_id
            FROM jobs
            WHERE job_id = %s AND status = 'Open'
        """, (job_id,))

        if cursor.fetchone() is None:
            print("Job not found or the job is not open.")
            return

        cursor.execute("""
            INSERT INTO applications
            (candidate_id, job_id, cover_letter)
            VALUES (%s, %s, %s)
        """, (candidate_id, job_id, cover_letter or None))

        connection.commit()
        print("Application submitted successfully.")
        print("Application ID:", cursor.lastrowid)

    except Error as error:
        connection.rollback()
        print("Unable to submit application:", error)

    finally:
        cursor.close()
        connection.close()


def view_applications():
    """Display applications with candidate, job and company details."""
    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT
                a.application_id,
                c.full_name AS candidate_name,
                j.job_title,
                co.company_name,
                a.application_date,
                a.status
            FROM applications a
            INNER JOIN candidates c
                ON a.candidate_id = c.candidate_id
            INNER JOIN jobs j
                ON a.job_id = j.job_id
            INNER JOIN companies co
                ON j.company_id = co.company_id
            ORDER BY a.application_date DESC
        """)

        applications = cursor.fetchall()

        if not applications:
            print("No applications found.")

        for application in applications:
            print(application)

    except Error as error:
        print("Unable to retrieve applications:", error)

    finally:
        cursor.close()
        connection.close()


def update_application_status():
    """Update the status of an existing application."""
    try:
        application_id = int(input("Enter application ID: "))

        if application_id <= 0:
            print("Application ID must be positive.")
            return

    except ValueError:
        print("Application ID must be an integer.")
        return

    print("Allowed statuses:", ", ".join(APPLICATION_STATUSES))
    status = input("Enter new status: ").strip().title()

    if status not in APPLICATION_STATUSES:
        print("Invalid application status.")
        return

    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    try:
        cursor.execute("""
            UPDATE applications
            SET status = %s
            WHERE application_id = %s
        """, (status, application_id))

        if cursor.rowcount == 0:
            connection.rollback()
            print("Application not found, or no change was made.")
            return

        connection.commit()
        print("Application status updated successfully.")

    except Error as error:
        connection.rollback()
        print("Unable to update status:", error)

    finally:
        cursor.close()
        connection.close()


def schedule_interview():
    """Schedule an interview for an existing application."""
    try:
        application_id = int(input("Enter application ID: "))

        if application_id <= 0:
            print("Application ID must be positive.")
            return

        date_text = input(
            "Enter interview date and time (YYYY-MM-DD HH:MM): "
        ).strip()

        interview_date = datetime.strptime(
            date_text, "%Y-%m-%d %H:%M"
        )

        if interview_date <= datetime.now():
            print("Interview must be scheduled for a future time.")
            return

    except ValueError:
        print("Enter a valid ID and date in YYYY-MM-DD HH:MM format.")
        return

    mode = input("Enter mode (Online/In-person/Phone): ").strip()

    if mode not in ("Online", "In-person", "Phone"):
        print("Invalid interview mode.")
        return

    location = input("Enter interview location or meeting link: ").strip()
    interviewer = input("Enter interviewer name: ").strip()

    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    try:
        cursor.execute("""
            SELECT application_id
            FROM applications
            WHERE application_id = %s
        """, (application_id,))

        if cursor.fetchone() is None:
            print("Application not found.")
            return

        cursor.execute("""
            INSERT INTO interviews
            (application_id, interview_date, interview_mode,
             interview_location, interviewer_name)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            application_id, interview_date, mode,
            location or None, interviewer or None
        ))

        connection.commit()
        print("Interview scheduled successfully.")
        print("Interview ID:", cursor.lastrowid)

    except Error as error:
        connection.rollback()
        print("Unable to schedule interview:", error)

    finally:
        cursor.close()
        connection.close()