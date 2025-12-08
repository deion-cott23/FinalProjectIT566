/* ************************************************************
Drop and Create the tables for the student langauges teaching database.
*************************************************************** */
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;


-- Switch to student_languages database
USE `student_languages`

-- Drop the table if it exists
/* DROP TABLE IF EXISTS `students`;

DROP TABLE IF EXISTS `instructors`;
*/
-- Create the table 
CREATE TABLE IF NOT EXISTS `students` (
    `id` int(11) NOT NULL,
    `first_name` varchar(25) NOT NULL,
    `middle_name` varchar(25) NOT NULL,
    `last_name` varchar(25) NOT NULL,
    `birthday` varchar(25) NOT NULL,
    `gender` char(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Store students data.';

-- RELATIONSHIPS FOR TABLE `students`:
--
--

-- -------------------------------------------------------------------------------------

-- Create table for instructors.
--

CREATE TABLE IF NOT EXISTS `instructors` (
    `id` int(11) NOT NULL,
    `first_name` varchar(25) NOT NULL,
    `middle_name` varchar(25) NOT NULL,
    `last_name` varchar(25) NOT NULL,
    `languages` varchar(50) NOT NULL,
    `critiques` varchar(99) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Store instructors data.';

-- RELATIONSHIPS FOR TABLE `instructors`:
--

-- ----------------------------------------------------------------------------------------



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
-- DROP TABLE IF EXISTS `languages`;

-- Create languages table providing languages, dialect and description of where language originates

CREATE TABLE IF NOT EXISTS `languages` (
    `languages_id` int(11) NOT NULL,
    `language` varchar(50) NOT NULL,
    `dialect` varchar(99) NOT NULL,
    `description` varchar(99) NOT NULL,
    PRIMARY KEY (`languages_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Stores languages data.';

-- Make languages.id column primary key and create index 
ALTER TABLE `languages`
    MODIFY `languages_id` int(11) NOT NULL AUTO_INCREMENT,
    ADD KEY `languages_ibfk_1` (`languages_id`);

ALTER TABLE `languages`
    -- ADD PRIMARY KEY(`languages_id`),
    MODIFY `languages_id` int(11) NOT NULL AUTO_INCREMENT;

 /* -- Add Cascade Delete Constraint
ALTER TABLE `languages`
    ADD CONSTRAINT `languages_ibfk_1`,
    FOREIGN KEY (`languages_id`) REFERENCES `students` (`id`),
    -- DROP FOREIGN KEY `languages_ibfk_1`,
    -- DROP INDEX `languages_ibfk_1`;
    ON UPDATE CASCADE; */
 
-- ***************************************************************************************************

-- STUDENT_LANGUAGE_XREF TABLE

-- Drop student_language_xref if it exists
-- DROP TABLE IF EXISTS `student_language_xref`;

-- Create student_language_xref table
CREATE TABLE IF NOT EXISTS `student_language_xref` (
    `students_id` int(11) NOT NULL,
    `language_id` int(11) NOT NULL,
    `proficiency` varchar(99) NOT NULL,
    `grade` char(2) NOT NULL,
    `student_update` varchar(99) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Relates students to languages being studied.';

 -- Create indexes for student_id and languages
ALTER TABLE `student_language_xref`
    ADD KEY `student_language_xref_ibfk_1` (`students_id`),
    ADD KEY `student_language_xref_ibfk_2` (`language_id`);


-- Add Cascade Delete Constraint on student_id key column
ALTER TABLE `student_language_xref`
    ADD CONSTRAINT `student_language_xref_ibfk_1`
    FOREIGN KEY (`students_id`) REFERENCES `students` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE;

-- Add Cascade Delete Constraint on language_id key column (Need to ask Professor about this one)
ALTER TABLE `student_language_xref`
    ADD CONSTRAINT `student_language_xref_ibfk_2`
    FOREIGN KEY (`language_id`) REFERENCES `languages` (`languages_id`)
    ON UPDATE CASCADE;



-- ALTER TABLE `student_language_xref`
--     ADD FOREIGN KEY (`students_id`) REFERENCES `students` (`id`)
--     ON DELETE CASCADE,
--     ADD FOREIGN KEY (`language_id`) REFERENCES `languages` (`language_id`)
--     on DELETE CASCADE;



-- STUDENT_INSTRUCTOR_LANGUAGE_XREF (showing what teachers would teach what class)

-- Drop student_instructor_language_xref if it exists

-- DROP TABLE IF EXISTS `student_instructor_language_xref`;

-- Create student_instructor_language_xref table
CREATE TABLE IF NOT EXISTS `student_instructor_language_xref` (
    `students_instructor_id` int(11) NOT NULL,
    `language_instructor_id` int(11) NOT NULL,
    `instructor_critiques` varchar(99) NOT NULL
);

 -- Create indexes for students_instructor_id and instructor_critiques
ALTER TABLE `student_instructor_language_xref`
    ADD KEY `student_instructor_language_xref_ibfk_1` (`students_instructor_id`),
    ADD KEY `student_instructor_language_xref_ibfk_2` (`language_instructor_id`);

-- Add Cascade Delete Constraint on student_id key column
ALTER TABLE `student_instructor_language_xref`
    ADD CONSTRAINT `student_instructor_language_xref_ibfk_1`
    FOREIGN KEY (`students_instructor_id`) REFERENCES `instructors` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE;

-- Add Cascade Delete Constraint on language_id key column
 ALTER TABLE `student_instructor_language_xref`
    ADD CONSTRAINT `student_instructor_language_xref_ibfk_2`
    FOREIGN KEY (`language_instructor_id`) REFERENCES `student_language_xref` (`language_id`)
    ON UPDATE CASCADE;

COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

