
-- File: 02_tables.sql

USE job_portal_db;

-- 1. Candidates
CREATE TABLE IF NOT EXISTS candidates (
    candidate_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    phone VARCHAR(20) UNIQUE,
    skills TEXT NOT NULL,
    experience_years DECIMAL(4,1) NOT NULL DEFAULT 0.0,
    location VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT chk_candidate_experience
        CHECK (experience_years >= 0)
);

-- 2. Companies
CREATE TABLE IF NOT EXISTS companies (
    company_id INT AUTO_INCREMENT PRIMARY KEY,
    company_name VARCHAR(150) NOT NULL UNIQUE,
    email VARCHAR(150) NOT NULL UNIQUE,
    phone VARCHAR(20),
    location VARCHAR(100) NOT NULL,
    industry VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 3. Jobs
CREATE TABLE IF NOT EXISTS jobs (
    job_id INT AUTO_INCREMENT PRIMARY KEY,
    company_id INT NOT NULL,
    job_title VARCHAR(150) NOT NULL,
    description TEXT,
    required_skills TEXT NOT NULL,
    min_experience DECIMAL(4,1) NOT NULL DEFAULT 0.0,
    salary_min DECIMAL(12,2),
    salary_max DECIMAL(12,2),
    location VARCHAR(100) NOT NULL,
    job_type VARCHAR(30) NOT NULL DEFAULT 'Full-time',
    status VARCHAR(20) NOT NULL DEFAULT 'Open',
    posted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_jobs_company
        FOREIGN KEY (company_id)
        REFERENCES companies(company_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,

    CONSTRAINT chk_job_experience
        CHECK (min_experience >= 0),

    CONSTRAINT chk_job_salary
        CHECK (
            salary_min IS NULL
            OR salary_max IS NULL
            OR salary_min <= salary_max
        ),

    CONSTRAINT chk_job_status
        CHECK (status IN ('Open', 'Closed', 'On Hold'))
);

-- 4. Applications
CREATE TABLE IF NOT EXISTS applications (
    application_id INT AUTO_INCREMENT PRIMARY KEY,
    candidate_id INT NOT NULL,
    job_id INT NOT NULL,
    application_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(30) NOT NULL DEFAULT 'Applied',
    cover_letter TEXT,

    CONSTRAINT fk_applications_candidate
        FOREIGN KEY (candidate_id)
        REFERENCES candidates(candidate_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,

    CONSTRAINT fk_applications_job
        FOREIGN KEY (job_id)
        REFERENCES jobs(job_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,

    CONSTRAINT uq_candidate_job
        UNIQUE (candidate_id, job_id),

    CONSTRAINT chk_application_status
        CHECK (
            status IN (
                'Applied',
                'Under Review',
                'Shortlisted',
                'Selected',
                'Rejected'
            )
        )
);

-- 5. Interviews
CREATE TABLE IF NOT EXISTS interviews (
    interview_id INT AUTO_INCREMENT PRIMARY KEY,
    application_id INT NOT NULL,
    interview_date DATETIME NOT NULL,
    interview_mode VARCHAR(30) NOT NULL DEFAULT 'Online',
    interview_location VARCHAR(200),
    interviewer_name VARCHAR(100),
    status VARCHAR(30) NOT NULL DEFAULT 'Scheduled',
    feedback TEXT,

    CONSTRAINT fk_interviews_application
        FOREIGN KEY (application_id)
        REFERENCES applications(application_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,

    CONSTRAINT chk_interview_mode
        CHECK (
            interview_mode IN ('Online', 'In-person', 'Phone')
        ),

    CONSTRAINT chk_interview_status
        CHECK (
            status IN (
                'Scheduled',
                'Completed',
                'Cancelled'
            )
        )
);

-- Verify all tables
SHOW TABLES;

-- Inspect table structures
DESCRIBE candidates;
DESCRIBE companies;
DESCRIBE jobs;
DESCRIBE applications;
DESCRIBE interviews;