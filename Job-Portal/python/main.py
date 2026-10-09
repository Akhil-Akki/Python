
# File: python/main.py

from candidate import (
    register_candidate,
    view_candidates,
    search_candidate,
    delete_candidate
)

from company import (
    register_company,
    view_companies
)

from jobs import (
    post_job,
    view_jobs,
    search_jobs,
    recommend_jobs
)

from application import (
    apply_for_job,
    view_applications,
    update_application_status,
    schedule_interview
)

from reports import reports_menu


def display_menu():
    """Display the main application menu."""
    print("\n" + "=" * 45)
    print("     JOB PORTAL MANAGEMENT SYSTEM")
    print("=" * 45)
    print("1.  Register Candidate")
    print("2.  View Candidates")
    print("3.  Search Candidate")
    print("4.  Register Company")
    print("5.  View Companies")
    print("6.  Post Job")
    print("7.  View Jobs")
    print("8.  Search Jobs")
    print("9.  Apply for Job")
    print("10. View Applications")
    print("11. Update Application Status")
    print("12. Schedule Interview")
    print("13. Recommend Jobs")
    print("14. Generate Reports")
    print("15. Delete Candidate")
    print("16. Exit")
    print("=" * 45)


def main():
    """Run the menu-driven application."""

    actions = {
        "1": register_candidate,
        "2": view_candidates,
        "3": search_candidate,
        "4": register_company,
        "5": view_companies,
        "6": post_job,
        "7": view_jobs,
        "8": search_jobs,
        "9": apply_for_job,
        "10": view_applications,
        "11": update_application_status,
        "12": schedule_interview,
        "13": recommend_jobs,
        "14": reports_menu,
        "15": delete_candidate,
        "16": exit
    }

    print("Welcome to the Job Portal Management System!")

    while True:
        try:
            display_menu()
            choice = input("Enter your choice (1-16): ").strip()

            if choice == "16":
                print("Thank you for using the Job Portal!")
                break

            action = actions.get(choice)

            if action is None:
                print("Invalid choice. Please enter a number from 1 to 16.")
                continue

            action()

        except (KeyboardInterrupt, EOFError):
            print("\nApplication closed.")
            break

        except Exception as error:
            # Unexpected errors are reported without terminating the menu.
            print("An unexpected error occurred:", error)


if __name__ == "__main__":
    main()