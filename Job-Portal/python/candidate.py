
# File: python/candidate.py

import re
from mysql.connector import Error
from database import get_connection


def register_candidate():
    """Register a new job candidate."""
    name = input("Enter full name: ").strip()
    email = input("Enter email: ").strip().lower()
    phone = input("Enter phone number: ").strip()
    skills = input("Enter skills separated by commas: ").strip()
    location = input("Enter preferred location: ").strip()

    if not name or not skills or not location or not email:
        print("Name, email, skills and location are required.")
        return

    if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
        print("Invalid email format.")
        return

    try:
        experience = float(input("Enter years of experience: "))

        if experience < 0 or experience > 999.9:
            print("Experience must be between 0 and 999.9.")
            return

    except ValueError:
        print("Experience must be a valid number.")
        return

    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    try:
        query = """
            INSERT INTO candidates
            (full_name, email, phone, skills,
             experience_years, location)
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        cursor.execute(
            query,
            (name, email, phone or None, skills,
             experience, location)
        )

        connection.commit()
        print("Candidate registered successfully.")
        print("Candidate ID:", cursor.lastrowid)

    except Error as error:
        connection.rollback()
        print("Unable to register candidate:", error)

    finally:
        cursor.close()
        connection.close()


def view_candidates():
    """Display all registered candidates."""
    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT candidate_id, full_name, email, phone,
                   skills, experience_years, location
            FROM candidates
            ORDER BY candidate_id
        """)

        candidates = cursor.fetchall()

        if not candidates:
            print("No candidates found.")
            return

        for candidate in candidates:
            print("-" * 55)

            for field, value in candidate.items():
                print(f"{field}: {value}")

    except Error as error:
        print("Unable to retrieve candidates:", error)

    finally:
        cursor.close()
        connection.close()


def search_candidate():
    """Search candidates by name or skill."""
    keyword = input("Enter candidate name or skill: ").strip()

    if not keyword:
        print("Search text cannot be empty.")
        return

    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor(dictionary=True)

    try:
        pattern = f"%{keyword}%"

        cursor.execute("""
            SELECT candidate_id, full_name, email,
                   skills, experience_years, location
            FROM candidates
            WHERE full_name LIKE %s
               OR skills LIKE %s
            ORDER BY full_name
        """, (pattern, pattern))

        results = cursor.fetchall()

        if not results:
            print("No matching candidates found.")

        for candidate in results:
            print(candidate)

    except Error as error:
        print("Candidate search failed:", error)

    finally:
        cursor.close()
        connection.close()
        
        

def delete_candidate():
    """Delete a candidate only when no applications depend on them."""
    try:
        candidate_id = int(input("Enter candidate ID to delete: "))

        if candidate_id <= 0:
            print("Candidate ID must be positive.")
            return

    except ValueError:
        print("Candidate ID must be an integer.")
        return

    confirm = input(
        f"Delete candidate {candidate_id}? Enter YES to confirm: "
    ).strip()

    if confirm != "YES":
        print("Deletion cancelled.")
        return

    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    try:
        cursor.execute("""
            DELETE FROM candidates
            WHERE candidate_id = %s
        """, (candidate_id,))

        if cursor.rowcount == 0:
            print("Candidate not found.")
            connection.rollback()
            return

        connection.commit()
        print("Candidate deleted successfully.")

    except Error as error:
        connection.rollback()
        print(
            "Unable to delete candidate. They may have existing "
            "applications or dependent records:",
            error
        )

    finally:
        cursor.close()
        connection.close()