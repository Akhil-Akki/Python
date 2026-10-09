
# File: python/reports.py

from pathlib import Path
from mysql.connector import Error
from database import get_connection


REPORT_FILE = Path(__file__).resolve().parent / "application_report.txt"


def fetch_report(title, query, params=()):
    """Run a report query and return its rows and column names."""
    connection = get_connection()

    if connection is None:
        return None, None

    cursor = connection.cursor()

    try:
        cursor.execute(query, params)
        rows = cursor.fetchall()
        columns = [item[0] for item in cursor.description]
        return columns, rows

    except Error as error:
        print(f"{title} failed:", error)
        return None, None

    finally:
        cursor.close()
        connection.close()


def display_report(title, query, params=()):
    """Print a report to the terminal."""
    columns, rows = fetch_report(title, query, params)

    if columns is None:
        return

    print(f"\n--- {title} ---")

    if not rows:
        print("No records found.")
        return

    print(" | ".join(columns))

    for row in rows:
        print(" | ".join(str(value) for value in row))


def most_applied_jobs():
    display_report(
        "Most Applied Jobs",
        """
        SELECT j.job_title, co.company_name,
               COUNT(a.application_id) AS total_applications
        FROM jobs j
        INNER JOIN companies co ON j.company_id = co.company_id
        LEFT JOIN applications a ON j.job_id = a.job_id
        GROUP BY j.job_id, j.job_title, co.company_name
        ORDER BY total_applications DESC, j.job_title
        LIMIT 10
        """
    )


def top_companies():
    display_report(
        "Companies with the Most Applications",
        """
        SELECT co.company_name,
               COUNT(a.application_id) AS total_applications
        FROM companies co
        LEFT JOIN jobs j ON co.company_id = j.company_id
        LEFT JOIN applications a ON j.job_id = a.job_id
        GROUP BY co.company_id, co.company_name
        ORDER BY total_applications DESC, co.company_name
        LIMIT 10
        """
    )


def average_salary_by_company():
    display_report(
        "Average Salary by Company",
        """
        SELECT co.company_name,
               ROUND(AVG(j.salary_min), 2) AS average_min_salary,
               ROUND(AVG(j.salary_max), 2) AS average_max_salary
        FROM companies co
        LEFT JOIN jobs j ON co.company_id = j.company_id
        GROUP BY co.company_id, co.company_name
        ORDER BY average_max_salary DESC
        """
    )


def open_jobs():
    display_report(
        "Open Jobs",
        """
        SELECT j.job_id, j.job_title, co.company_name,
               j.location, j.salary_min, j.salary_max
        FROM jobs j
        INNER JOIN companies co ON j.company_id = co.company_id
        WHERE j.status = 'Open'
        ORDER BY j.posted_at DESC
        """
    )


def selected_candidates():
    display_report(
        "Selected Candidates",
        """
        SELECT c.full_name, c.email, j.job_title,
               co.company_name, a.application_date
        FROM applications a
        INNER JOIN candidates c ON a.candidate_id = c.candidate_id
        INNER JOIN jobs j ON a.job_id = j.job_id
        INNER JOIN companies co ON j.company_id = co.company_id
        WHERE a.status = 'Selected'
        ORDER BY c.full_name
        """
    )


def application_status_summary():
    display_report(
        "Application Status Summary",
        """
        SELECT status, COUNT(*) AS total_applications
        FROM applications
        GROUP BY status
        ORDER BY total_applications DESC
        """
    )


def export_application_report():
    """Export application details to a UTF-8 text file."""
    columns, rows = fetch_report(
        "Application Report",
        """
        SELECT a.application_id, c.full_name, j.job_title,
               co.company_name, a.application_date, a.status
        FROM applications a
        INNER JOIN candidates c ON a.candidate_id = c.candidate_id
        INNER JOIN jobs j ON a.job_id = j.job_id
        INNER JOIN companies co ON j.company_id = co.company_id
        ORDER BY a.application_date DESC
        """
    )

    if columns is None:
        return

    try:
        with REPORT_FILE.open("w", encoding="utf-8") as file:
            file.write("JOB PORTAL MANAGEMENT SYSTEM\n")
            file.write("APPLICATION REPORT\n")
            file.write("=" * 90 + "\n")

            if not rows:
                file.write("No applications found.\n")
            else:
                file.write(" | ".join(columns) + "\n")
                file.write("-" * 90 + "\n")

                for row in rows:
                    file.write(
                        " | ".join(str(value) for value in row) + "\n"
                    )

        print("Report exported successfully:")
        print(REPORT_FILE)

    except OSError as error:
        print("Unable to write report file:", error)


def reports_menu():
    """Display report options."""
    while True:
        print("\n===== REPORTS MENU =====")
        print("1. Most applied jobs")
        print("2. Companies with the highest number of applications")
        print("3. Average salary by company")
        print("4. Open jobs")
        print("5. Selected candidates")
        print("6. Application status summary")
        print("7. Export application report to text file")
        print("0. Return to main menu")

        choice = input("Enter choice: ").strip()

        actions = {
            "1": most_applied_jobs,
            "2": top_companies,
            "3": average_salary_by_company,
            "4": open_jobs,
            "5": selected_candidates,
            "6": application_status_summary,
            "7": export_application_report
        }

        if choice == "0":
            break

        action = actions.get(choice)

        if action:
            action()
        else:
            print("Invalid choice. Please select 0-7.")