
/* ****************************************************
Insert test data into the student_languages database.
****************************************************** */

-- Switch to the student_languages database. 

USE `student_languages`

-- Insert data into the students table.
INSERT INTO `students` (id, first_name, middle_name, last_name, birthday, gender)
    VALUES (1, 'Deion', 'Denzel', 'Cottingham', '12/10/1995', 'M');

INSERT INTO `instructors` (first_name, middle_name, last_name, languages, critiques)
    VALUES ('Rick', 'Warren', 'Miller', 'Portuguese, Mandarin', 'Can teach many languages and computer languages, great skills.');

INSERT INTO `students` (id, first_name, middle_name, last_name, birthday, gender)
    VALUES (2, 'Jerry', 'Lee', 'Rice', '10/13/1962', 'M');

INSERT INTO `instructors` (first_name, middle_name, last_name, languages, critiques)
    VALUES ('Randy', 'Gene', 'Moss', 'Hindi', 'Arabic and Hindi are fairly well verse.');

INSERT INTO `students` (id, first_name, middle_name, last_name, birthday, gender)
    VALUES (3, 'John', 'William', 'Ferrell', '07/16/1967', 'M');

INSERT INTO `instructors` (first_name, middle_name, last_name, languages, critiques)
    VALUES ('Jennifer', 'Joanna', 'Aniston', 'Thai', 'Pretty well verse in Vietnamese as well. Good at both languages.');

INSERT INTO `students` (id, first_name, middle_name, last_name, birthday, gender)
    VALUES (4, 'Trinity', 'Rain', 'Moyer-Rodman', '05/20/2002', 'F');

INSERT INTO `instructors` (first_name, middle_name, last_name, languages, critiques)
    VALUES ('Lisa', 'Deshaun', 'Leslie', 'Cantonese', 'Need to provide more thought provoking assignments');

INSERT INTO `students` (id, first_name, middle_name, last_name, birthday, gender)
    VALUES (5, 'Marguerite', 'Annie', 'Johnson', '04/04/1928', 'F');

INSERT INTO `instructors` (first_name, middle_name, last_name, languages, critiques)
    VALUES ('Kerry', 'Marisa', 'Washington', 'Japanese', 'Good at only this Asian language, may need to offer more courses for students.');


-- Insert data into the students_status table

INSERT INTO `languages` (languages_id, language, dialect, description)
    VALUES (1, 'Spanish, French','North America/South America, Europe', 'This language originates in multiple areas of the world.');

INSERT INTO `languages` (languages_id, language, dialect, description)
    VALUES (2, 'Russian', 'East Slavic', 'This language comes from the Indo-European language family.');

INSERT INTO `languages` (languages_id, language, dialect, description)
    VALUES (3, 'Vietnamese', 'Northern/Central/Southern', 'This language stems from the Austroasiatic language.');

INSERT INTO `languages` (languages_id, language, dialect, description)
    VALUES (4, 'Japanese', 'Eastern/Western',  'This language stems from the Tokyo dialect between modern Japanese and Kansai-ben.');

INSERT INTO `languages` (languages_id, language, dialect, description)
    VALUES (5, 'Arabic', 'Egyption/Gulf/Mesopotamian', 'This language stems from multiple areas and forms Modern Standard Arabic.');

-- Insert test data into student_language_xref

INSERT INTO `student_language_xref` (students_id, language_id, proficiency, grade, student_update)
    VALUES (1, 1, '85, 80', 'B', 'Need improvement, can at least get an A-');

INSERT INTO `student_language_xref` (students_id, language_id, proficiency, grade, student_update)
    VALUES (2, 2, '94', 'A-', 'Keep up the good work, great job!');

INSERT INTO `student_language_xref` (students_id, language_id, proficiency, grade, student_update)
    VALUES (3, 3, '82', 'B-', 'Good job! Just have to make sure assignments are submitted on time!');

INSERT INTO `student_language_xref` (students_id, language_id, proficiency, grade, student_update)
    VALUES (4, 4, '90', 'A-', 'Great job performing, just need to submit other missing assignments for A+');

INSERT INTO `student_language_xref` (students_id, language_id, proficiency, grade, student_update)
    VALUES (5, 5, '89', 'B+', 'Amazing job for such a hard language, will be able to obtain A- before end of semester.');



-- Insert trst data into student_instructor_language_xref

INSERT INTO `student_instructor_language_xref` (students_instructor_id, language_instructor_id, instructor_critiques)
    VALUES (2, 4, 'Pair well together!');

INSERT INTO `student_instructor_language_xref` (students_instructor_id, language_instructor_id, instructor_critiques)
    VALUES (1, 3, 'Bad match!');

INSERT INTO `student_instructor_language_xref` (students_instructor_id, language_instructor_id, instructor_critiques)
    VALUES (3, 5, 'Pairs okay together, good match!');

INSERT INTO `student_instructor_language_xref` (students_instructor_id, language_instructor_id, instructor_critiques)
    VALUES (4, 2, 'Pair well together!');

INSERT INTO `student_instructor_language_xref` (students_instructor_id, language_instructor_id, instructor_critiques)
    VALUES (5, 1, 'Pair well together!');