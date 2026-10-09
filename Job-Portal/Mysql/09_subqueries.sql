
USE job_portal_db;

-- Single-row subquery: jobs paying above average maximum salary
SELECT job_title, salary_max
FROM jobs
WHERE salary_max > (
    SELECT AVG(salary_max)
    FROM jobs
    WHERE salary_max IS NOT NULL
);

-- Multi-row subquery with IN
SELECT company_name
FROM companies
WHERE company_id IN (
    SELECT company_id
    FROM jobs
    WHERE status = 'Open'
);

-- ANY: salary greater than ANY salary minimum in Hyderabad
SELECT job_title, salary_min
FROM jobs
WHERE salary_min > ANY (
    SELECT salary_min
    FROM jobs
    WHERE location = 'Hyderabad'
    AND salary_min IS NOT NULL
);

-- ALL: salary minimum greater than ALL salary minima
-- for jobs in Hyderabad
SELECT job_title, salary_min
FROM jobs
WHERE salary_min > ALL (
    SELECT salary_min
    FROM jobs
    WHERE location = 'Hyderabad'
    AND salary_min IS NOT NULL
);

-- EXISTS: candidates who have applications
SELECT c.candidate_id, c.full_name
FROM candidates c
WHERE EXISTS (
    SELECT 1
    FROM applications a
    WHERE a.candidate_id = c.candidate_id
);

-- NOT EXISTS: candidates who have not applied
SELECT c.candidate_id, c.full_name
FROM candidates c
WHERE NOT EXISTS (
    SELECT 1
    FROM applications a
    WHERE a.candidate_id = c.candidate_id
);

-- Correlated subquery: jobs with more applications
-- than the average application count per job
SELECT j.job_id, j.job_title
FROM jobs j
WHERE (
    SELECT COUNT(*)
    FROM applications a
    WHERE a.job_id = j.job_id
) > (
    SELECT AVG(job_application_count)
    FROM (
        SELECT COUNT(*) AS job_application_count
        FROM applications
        GROUP BY job_id
    ) AS counts_by_job
);