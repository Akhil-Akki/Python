
USE job_portal_db;

-- WHERE and AND
SELECT * FROM jobs
WHERE location = 'Hyderabad'
AND status = 'Open';

-- OR
SELECT * FROM jobs
WHERE location = 'Hyderabad'
OR location = 'Pune';

-- NOT
SELECT * FROM jobs
WHERE NOT status = 'Closed';

-- BETWEEN
SELECT * FROM jobs
WHERE salary_min BETWEEN 300000 AND 600000;

-- IN
SELECT * FROM jobs
WHERE location IN ('Hyderabad', 'Bengaluru');

-- LIKE: title containing Developer
SELECT * FROM jobs
WHERE job_title LIKE '%Developer%';

-- ORDER BY
SELECT * FROM jobs
ORDER BY salary_max DESC;

-- LIMIT
SELECT * FROM jobs
ORDER BY posted_at DESC
LIMIT 3;

-- Multiple conditions
SELECT * FROM candidates
WHERE experience_years BETWEEN 1 AND 4
AND skills LIKE '%Python%'
ORDER BY experience_years DESC
LIMIT 5;