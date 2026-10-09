
USE job_portal_db;

-- Overall application count
SELECT COUNT(*) AS total_applications
FROM applications;

-- Salary statistics
SELECT
    COUNT(*) AS jobs_with_salary,
    SUM(salary_min) AS total_minimum_salary,
    AVG(salary_max) AS average_maximum_salary,
    MIN(salary_min) AS lowest_minimum_salary,
    MAX(salary_max) AS highest_maximum_salary
FROM jobs
WHERE salary_min IS NOT NULL
AND salary_max IS NOT NULL;

-- Applications per job
SELECT
    j.job_id,
    j.job_title,
    COUNT(a.application_id) AS application_count
FROM jobs j
LEFT JOIN applications a
    ON j.job_id = a.job_id
GROUP BY j.job_id, j.job_title
ORDER BY application_count DESC;

-- Companies with more than one application
SELECT
    co.company_id,
    co.company_name,
    COUNT(a.application_id) AS total_applications
FROM companies co
LEFT JOIN jobs j
    ON co.company_id = j.company_id
LEFT JOIN applications a
    ON j.job_id = a.job_id
GROUP BY co.company_id, co.company_name
HAVING COUNT(a.application_id) > 1;

-- Average salary range by company
SELECT
    co.company_name,
    ROUND(AVG(j.salary_min), 2) AS average_min_salary,
    ROUND(AVG(j.salary_max), 2) AS average_max_salary
FROM companies co
INNER JOIN jobs j
    ON co.company_id = j.company_id
GROUP BY co.company_id, co.company_name
ORDER BY average_max_salary DESC;