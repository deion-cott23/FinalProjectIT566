/* ************************************************************
Drop and Create the tables for the student langauges teaching database.
*************************************************************** */

-- Switch to student_languages database
USE `student_languages`

-- Drop the table if it exists
DROP TABLE IF EXISTS `students`;

DROP TABLE IF EXISTS `instructors`;

-- Create the table 
CREATE TABLE IF NOT EXISTS `students` (
    `id` int(11) NOT NULL,
    `first_name` varchar(25) NOT NULL,
    `middle_name` varchar(25) NOT NULL,
    `last_name` varchar(25) NOT NULL,
    `birthday` varchar(25) NOT NULL,
    `gender` char(1) NOT NULL,
    `languages` varchar(50) NOT NULL,
    `proficiency` varchar(99) NOT NULL
);

CREATE TABLE IF NOT EXISTS `instructors` (
    `id` int(11) NOT NULL,
    `first_name` varchar(25) NOT NULL,
    `middle_name` varchar(25) NOT NULL,
    `last_name` varchar(25) NOT NULL,
    `languages` varchar(50) NOT NULL

);

-- Designate the 'id' column as the primary key
ALTER TABLE `students`
    ADD PRIMARY KEY(`id`);

ALTER TABLE `instructors`
    ADD PRIMARY KEY(`id`);

-- Make 'id' column auto increment on inserts
ALTER TABLE `students`
    MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `instructors`
    MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

-- Drop student_status table if it exists
DROP TABLE IF EXISTS `students_status`;

-- Create students_status table providing grade and descriptive update of how students are doing

CREATE TABLE IF NOT EXISTS `students_status` (
    `student_id` int(11) NOT NULL,
    `grade` char(2) NOT NULL,
    `student_update` varchar(99) NOT NULL
);

-- Make students_status.id column primary key and create index 
ALTER TABLE `students_status`
    ADD PRIMARY KEY (`student_id`),
    ADD KEY `students_status_ibfk_1` (`student_id`);

-- Make students_status.id column Auto Increment
ALTER TABLE `students_status`
    MODIFY `student_id` int(11) NOT NULL AUTO_INCREMENT;


-- Add Cascade Delete Constraint
ALTER TABLE `students_status`
    ADD CONSTRAINT `students_status_ibfk_1`
    FOREIGN KEY (`student_id`) REFERENCES `students` (`id`)
    ON DELETE CASCADE 
    ON UPDATE CASCADE;

-- ***************************************************************************************************

-- STUDENT_LANGUAGE_XREF TABLE

-- Drop student_language_xref if it exists
DROP TABLE IF EXISTS `student_language_xref`;

-- Create student_language_xref table
CREATE TABLE IF NOT EXISTS `student_language_xref` (
    `student_id` int(11) NOT NULL,
    `first_name` varchar(25) NOT NULL,
    `middle_name` varchar(25) NOT NULL,
    `last_name` varchar(25) NOT NULL,
    `languages` varchar(50) NOT NULL,
    `proficiency` varchar(99) NOT NULL,
    `grade` char(2) NOT NULL,
    `student_update` varchar(99) NOT NULL
);

-- Create indexes for student_id and languages
ALTER TABLE `student_language_xref`
    ADD KEY `student_language_xref_ibfk_1` (`student_id`),
    ADD KEY `student_language_xref_ibfk_2` (`languages`);

-- Add Cascade Delete Constraint on student_id column
ALTER TABLE `student_language_xref`
    ADD CONSTRAINT `student_language_ibfk_1`
    FOREIGN KEY (`student_id`) REFERENCES `students_status` (`student_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE;

-- Add Cascade Delete Constraint on languages column (Need to ask Professor about this one)
/* ALTER TABLE `student_language_xref`
    ADD CONSTRAINT `student_language_ibfk_2`
    FOREIGN KEY (`languages`) REFERENCES `students` (`languages`)
    ON UPDATE CASCADE;
*/




    