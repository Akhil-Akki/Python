
USE job_portal_db;

-- INSERT
INSERT INTO candidates
(full_name, email, skills, experience_years, location)
VALUES
('Test Candidate', 'test.candidate@example.com',
 'Python, SQL', 1.0, 'Hyderabad');

-- SELECT
SELECT * FROM candidates;

-- UPDATE
UPDATE candidates
SET location = 'Hyderabad'
WHERE email = 'test.candidate@example.com';

-- Verify UPDATE
SELECT * FROM candidates
WHERE email = 'test.candidate@example.com';

-- DELETE
DELETE FROM candidates
WHERE email = 'test.candidate@example.com';

-- Verify DELETE
SELECT * FROM candidates
WHERE email = 'test.candidate@example.com';