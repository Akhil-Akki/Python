
USE job_portal_db;

CREATE OR REPLACE VIEW job_details_view AS
SELECT
    j.job_id,
    j.job_title,
    co.company_name,
    j.location,
    j.salary_min,
    j.salary_max,
    j.min_experience,
    j.required_skills,
    j.status
FROM jobs j
INNER JOIN companies co
    ON j.company_id = co.company_id;

CREATE OR REPLACE VIEW application_details_view AS
SELECT
    a.application_id,
    c.full_name AS candidate_name,
    c.email AS candidate_email,
    j.job_title,
    co.company_name,
    a.application_date,
    a.status AS application_status
FROM applications a
INNER JOIN candidates c
    ON a.candidate_id = c.candidate_id
INNER JOIN jobs j
    ON a.job_id = j.job_id
INNER JOIN companies co
    ON j.company_id = co.company_id;

-- Query the views
SELECT * FROM job_details_view;

SELECT * FROM application_details_view;

-- Open jobs
SELECT *
FROM job_details_view
WHERE status = 'Open';

-- Selected candidates
SELECT *
FROM application_details_view
WHERE application_status = 'Selected';

-- Application status summary
SELECT
    application_status,
    COUNT(*) AS total
FROM application_details_view
GROUP BY application_status
ORDER BY total DESC;