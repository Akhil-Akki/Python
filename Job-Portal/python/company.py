
# File: python/company.py

from mysql.connector import Error
from database import get_connection


def register_company():
    """Register a company."""
    name = input("Enter company name: ").strip()
    email = input("Enter company email: ").strip().lower()
    phone = input("Enter company phone (optional): ").strip()
    location = input("Enter company location: ").strip()
    industry = input("Enter industry: ").strip()

    if not all([name, email, location, industry]):
        print("Name, email, location and industry are required.")
        return

    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    try:
        cursor.execute("""
            INSERT INTO companies
            (company_name, email, phone, location, industry)
            VALUES (%s, %s, %s, %s, %s)
        """, (name, email, phone or None, location, industry))

        connection.commit()
        print("Company registered successfully.")
        print("Company ID:", cursor.lastrowid)

    except Error as error:
        connection.rollback()
        print("Unable to register company:", error)

    finally:
        cursor.close()
        connection.close()


def view_companies():
    """Display all registered companies."""
    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT company_id, company_name, email,
                   phone, location, industry
            FROM companies
            ORDER BY company_name
        """)

        companies = cursor.fetchall()

        if not companies:
            print("No companies found.")

        for company in companies:
            print(company)

    except Error as error:
        print("Unable to retrieve companies:", error)

    finally:
        cursor.close()
        connection.close()