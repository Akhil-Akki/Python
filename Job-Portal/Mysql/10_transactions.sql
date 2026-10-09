
USE job_portal_db;

-- Example 1: transaction and rollback
START TRANSACTION;

UPDATE jobs
SET status = 'On Hold'
WHERE job_id = 1;

SAVEPOINT job_status_saved;

UPDATE jobs
SET status = 'Closed'
WHERE job_id = 2;

-- Undo only the second update
ROLLBACK TO SAVEPOINT job_status_saved;

-- Permanently save the first update
COMMIT;

SELECT job_id, job_title, status
FROM jobs
WHERE job_id IN (1, 2);

-- Example 2: full rollback
START TRANSACTION;

UPDATE jobs
SET status = 'Closed'
WHERE job_id = 1;

ROLLBACK;

-- Verify job 1 retains its previously committed status
SELECT job_id, job_title, status
FROM jobs
WHERE job_id = 1;

-- Restore sample job 1 to Open for subsequent practice
UPDATE jobs
SET status = 'Open'
WHERE job_id = 1;