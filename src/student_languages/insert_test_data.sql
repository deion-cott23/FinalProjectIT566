
/* ****************************************************
Insert test data into the student_languages database.
****************************************************** */

-- Switch to the student_languages database. 

USE `student_languages`

-- Insert data into the students table.
INSERT INTO `students` (first_name, middle_name, last_name, birthday, gender, languages, proficiency)
    VALUES ('Deion', 'Denzel', 'Cottingham', '12/10/1995', 'M', 'Spanish, French', '85, 80');

INSERT INTO `instructors` (first_name, middle_name, last_name, languages)
    VALUES ('Rick', 'Warren', 'Miller', 'Portuguese, Mandarin');

INSERT INTO `students` (first_name, middle_name, last_name, birthday, gender, languages, proficiency)
    VALUES ('Jerry', 'Lee', 'Rice', '10/13/1962', 'M', 'Russian', '94');

INSERT INTO `instructors` (first_name, middle_name, last_name, languages)
    VALUES ('Randy', 'Gene', 'Moss', 'Hindi');

INSERT INTO `students` (first_name, middle_name, last_name, birthday, gender, languages, proficiency)
    VALUES ('John', 'William', 'Ferrell', '07/16/1967', 'M', 'Vietnamese', '82');

INSERT INTO `instructors` (first_name, middle_name, last_name, languages)
    VALUES ('Jennifer', 'Joanna', 'Aniston', 'Thai');

INSERT INTO `students` (first_name, middle_name, last_name, birthday, gender, languages, proficiency)
    VALUES ('Trinity', 'Rain', 'Moyer-Rodman', '05/20/2002', 'F', 'Japanese', '90');

INSERT INTO `instructors` (first_name, middle_name, last_name, languages)
    VALUES ('Lisa', 'Deshaun', 'Leslie', 'Cantonese');

INSERT INTO `students` (first_name, middle_name, last_name, birthday, gender, languages, proficiency)
    VALUES ('Marguerite', 'Annie', 'Johnson', '04/04/1928', 'F', 'Arabic', '89');


-- Insert data into the students_status table

INSERT INTO `students_status` (student_id, grade, student_update)
    VALUES (1, 'B', 'Need improvement, can at least get A-');

INSERT INTO `students_status` (student_id, grade, student_update)
    VALUES (2, 'A', 'Great Job! Keep it up!');

INSERT INTO `students_status` (student_id, grade, student_update)
    VALUES (3, 'B-', 'Improvement needed, have potential');

INSERT INTO `students_status` (student_id, grade, student_update)
    VALUES (4, 'A-', 'Doing well, will just need to submit missing assignments for final grade');


-- Insert test data into student_language_xref

INSERT INTO `student_language_xref` (student_id, first_name, middle_name, last_name, languages, proficiency, grade, student_update)
    VALUES (1, 'Deion', 'Denzel', 'Cottingham', 'Spanish, French', '85, 80', 'B', 'Need improvement, can at least get an A-');

 INSERT INTO `student_language_xref` (student_id, first_name, middle_name, last_name, languages, proficiency, grade, student_update)
    VALUES (2, 'Trinity', 'Rain', 'Moyer-Rodman', 'Japanese', '90', 'A-', 'Doing well, will just need to submit missing assignments for final grade');

