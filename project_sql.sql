CREATE database Project;
use Project;

SELECT * from diseases;
SELECT * from medication;
SELECT * from patients;
SELECT * from testsnn;

ALTER TABLE diseases 
RENAME COLUMN Disease_Description TO DISEASES_DESCRIPTION;

ALTER TABLE diseases 
RENAME COLUMN SEVERITY1 TO SEVERITY;

ALTER TABLE diseases 
RENAME COLUMN PATIENT TO PATIENT_ID;

ALTER TABLE medication 
RENAME COLUMN PATIENT TO PATIENT_ID;

ALTER TABLE testsnn 
RENAME COLUMN PATIENT TO PATIENT_ID;

ALTER TABLE testsnn 
RENAME COLUMN SOP_DESCRIPTION TO Test_name;

ALTER TABLE patients
ADD COLUMN Birthdate_date DATE,
ADD COLUMN Birthdate_time TIME;
SET SQL_SAFE_UPDATES = 0;
-- Run the update query
UPDATE patients 
SET Birthdate_date = DATE(BIRTHDATE),
    Birthdate_time = TIME(BIRTHDATE);
-- Re-enable safe update mode 
SET SQL_SAFE_UPDATES = 1;

ALTER TABLE patients DROP COLUMN BIRTHDATE;
ALTER TABLE patients DROP COLUMN Birthdate_time;

ALTER TABLE testsnn
RENAME TO tests;

SELECT * from test;