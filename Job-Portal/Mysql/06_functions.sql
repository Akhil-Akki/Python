
USE job_portal_db;

-- String functions
SELECT
    full_name,
    UPPER(full_name) AS uppercase_name,
    LOWER(email) AS lowercase_email,
    LENGTH(full_name) AS name_length,
    CONCAT(full_name, ' - ', location) AS candidate_info,
    TRIM(skills) AS cleaned_skills
FROM candidates;

-- Numeric functions
SELECT
    job_title,
    salary_min,
    salary_max,
    ROUND((salary_min + salary_max) / 2, 2) AS midpoint_salary,
    CEIL(salary_min / 12) AS monthly_minimum_rounded_up,
    FLOOR(salary_max / 12) AS monthly_maximum_rounded_down
FROM jobs
WHERE salary_min IS NOT NULL
AND salary_max IS NOT NULL;

-- Date functions
SELECT
    job_id,
    job_title,
    posted_at,
    CURDATE() AS today,
    DATEDIFF(CURDATE(), DATE(posted_at)) AS days_since_posted,
    DATE_ADD(DATE(posted_at), INTERVAL 30 DAY) AS review_date
FROM jobs;

-- Application date and time
SELECT
    application_id,
    application_date,
    DATE_FORMAT(application_date, '%d-%m-%Y') AS formatted_date
FROM applications;