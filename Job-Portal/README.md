
# Job Portal Management System

## Project Overview

A menu-driven Job Portal Management System developed using
Python and MySQL.

The application manages candidates, companies, jobs,
applications, interviews, recommendations and recruitment reports.

## Technologies

- Python 3
- MySQL 8.0+
- mysql-connector-python
- MySQL Workbench
- VS Code

## Project Structure

- `python/`: Python application modules and exported report
- `sql/`: Database setup, sample data, SQL practice and reports
- `README.md`: Project documentation

## Setup Instructions

1. Install Python and MySQL Server.
2. Open the project in VS Code.
3. Open MySQL Workbench and connect to your server.
4. Execute `01_database.sql`.
5. Execute `02_tables.sql`.
6. Execute `03_data.sql`.
7. Execute the remaining SQL practice files as required.
8. Install the Python connector:

   `python -m pip install mysql-connector-python`

9. Update the connection settings in `python/database.py`.
10. Run the application from the project root:

    `python python/main.py`

## Features

- Candidate registration, search, viewing and deletion
- Company registration and listing
- Job posting, viewing and searching
- Job applications and status management
- Interview scheduling
- Skills, experience and location-based job recommendations
- Recruitment reports and text-file export

## Database Tables

- `candidates`
- `companies`
- `jobs`
- `applications`
- `interviews`

## Reports

- Most applied jobs
- Companies with the most applications
- Average salary by company
- Open jobs
- Selected candidates
- Application status summary

The application can export application details to
`python/application_report.txt`.

## Security and Data Integrity

- Parameterized SQL queries are used for user input.
- Database constraints protect relationships and required fields.
- Transactions are committed on success and rolled back on errors.
- Database credentials should not be committed to public repositories.

## Limitations

Job recommendations use keyword matching and simple scoring.
They do not use machine learning or semantic skill matching.