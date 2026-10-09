
-- File: 03_data.sql

USE job_portal_db;

-- Sample candidates
INSERT INTO candidates
(full_name, email, phone, skills, experience_years, location)
VALUES
('Akhil', 'akhil@example.com', '9000000001',
 'Python, SQL, MySQL, Pandas', 2.0, 'Hyderabad'),

('Mahathi', 'mahathi@example.com', '9000000002',
 'Python, Django, SQL, REST API', 3.0, 'Hyderabad'),

('Priya', 'priya@example.com', '9000000003',
 'Java, Spring Boot, MySQL', 4.0, 'Bengaluru'),

('Manisha', 'manisha@example.com', '9000000004',
 'HTML, CSS, JavaScript, React', 1.0, 'Pune'),

('Harshitha', 'harshitha@example.com', '9000000005',
 'Python, Machine Learning, SQL', 5.0, 'Hyderabad');

-- Sample companies
INSERT INTO companies
(company_name, email, phone, location, industry)
VALUES
('Apple', 'hr@apple.example',
 '9100000001', 'Hyderabad', 'Information Technology'),

('Google', 'careers@google.example',
 '9100000002', 'Bengaluru', 'Data Analytics'),

('Microsoft', 'jobs@microsoft.example',
 '9100000003', 'Hyderabad', 'Cloud Computing'),

('SpaceX', 'hr@spacex.example',
 '9100000004', 'Pune', 'Web Development');
 

-- Sample jobs
INSERT INTO jobs
(company_id, job_title, description, required_skills,
 min_experience, salary_min, salary_max, location, job_type, status)
VALUES
(1, 'Python Developer',
 'Develop and maintain Python applications.',
 'Python, SQL, MySQL', 1.0, 400000, 800000,
 'Hyderabad', 'Full-time', 'Open'),

(2, 'Data Analyst',
 'Analyze datasets and prepare business reports.',
 'Python, SQL, Pandas', 2.0, 500000, 900000,
 'Bengaluru', 'Full-time', 'Open'),

(3, 'Machine Learning Engineer',
 'Build and evaluate machine learning models.',
 'Python, Machine Learning, SQL', 3.0, 800000, 1500000,
 'Hyderabad', 'Full-time', 'Open'),

(4, 'React Developer',
 'Build responsive web applications.',
 'HTML, CSS, JavaScript, React', 1.0, 350000, 700000,
 'Texas', 'Full-time', 'Open'),

(1, 'Junior SQL Developer',
 'Write SQL queries and maintain databases.',
 'SQL, MySQL', 0.0, 300000, 500000,
 'Hyderabad', 'Full-time', 'Open'),

(2, 'Senior Data Engineer',
 'Develop data pipelines and database solutions.',
 'Python, SQL, Data Engineering', 5.0, 1000000, 1800000,
 'Bengaluru', 'Full-time', 'Closed');

-- Sample applications
INSERT INTO applications
(candidate_id, job_id, status, cover_letter)
VALUES
(1, 1, 'Shortlisted', 'Interested in Python development.'),
(1, 5, 'Applied', 'Interested in SQL development.'),
(2, 1, 'Under Review', 'Experienced in Python and Django.'),
(2, 2, 'Selected', 'Interested in data analytics.'),
(3, 2, 'Rejected', 'Applying for data analytics.'),
(4, 4, 'Shortlisted', 'Experienced in React development.'),
(5, 3, 'Selected', 'Interested in machine learning.');

-- Sample interviews
INSERT INTO interviews
(application_id, interview_date, interview_mode,
 interview_location, interviewer_name, status, feedback)
VALUES
(1, '2026-10-15 10:00:00', 'Online',
 'Video conference', 'Anita Rao', 'Scheduled', NULL),

(4, '2026-10-16 14:00:00', 'In-person',
 'Bengaluru office', 'Kiran Mehta', 'Scheduled', NULL),

(6, '2026-10-17 11:30:00', 'Online',
 'Video conference', 'Meera Shah', 'Scheduled', NULL);

-- Verify inserted records
SELECT * FROM candidates;
SELECT * FROM companies;
SELECT * FROM jobs;
SELECT * FROM applications;
SELECT * FROM interviews;


SELECT COUNT(*) AS total_candidates FROM candidates;
SELECT COUNT(*) AS total_companies FROM companies;
SELECT COUNT(*) AS total_jobs FROM jobs;
SELECT COUNT(*) AS total_applications FROM applications;
SELECT COUNT(*) AS total_interviews FROM interviews;