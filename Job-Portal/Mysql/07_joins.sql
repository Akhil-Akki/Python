
USE job_portal_db;

-- INNER JOIN: jobs and their companies
SELECT
    j.job_id,
    j.job_title,
    c.company_name,
    j.location,
    j.salary_min,
    j.salary_max
FROM jobs j
INNER JOIN companies c
    ON j.company_id = c.company_id;

-- LEFT JOIN: include candidates with no applications
SELECT
    c.candidate_id,
    c.full_name,
    a.application_id,
    a.status
FROM candidates c
LEFT JOIN applications a
    ON c.candidate_id = a.candidate_id;

-- RIGHT JOIN: include companies with no jobs
SELECT
    c.company_name,
    j.job_title
FROM jobs j
RIGHT JOIN companies c
    ON j.company_id = c.company_id;

-- Three-table join: candidate, application and job
SELECT
    c.full_name,
    j.job_title,
    co.company_name,
    a.status
FROM applications a
INNER JOIN candidates c
    ON a.candidate_id = c.candidate_id
INNER JOIN jobs j
    ON a.job_id = j.job_id
INNER JOIN companies co
    ON j.company_id = co.company_id;

-- Interviews with candidate and job details
SELECT
    i.interview_id,
    c.full_name,
    j.job_title,
    i.interview_date,
    i.interview_mode,
    i.status
FROM interviews i
INNER JOIN applications a
    ON i.application_id = a.application_id
INNER JOIN candidates c
    ON a.candidate_id = c.candidate_id
INNER JOIN jobs j
    ON a.job_id = j.job_id;