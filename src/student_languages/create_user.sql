/* ***************************************************
Drop and create the student_langauges_user
*****************************************************/

-- Drop user if exists
DROP USER IF EXISTS 'student_languages_user'@'%';

-- Create user if not exists
CREATE USER IF NOT EXISTS 'student_languages_user'@'%';
GRANT ALL PRIVILEGES ON *.* TO 'student_languages_user'@'%';
ALTER USER 'student_languages_user'@'%'
    REQUIRE NONE WITH MAX_QUERIES_PER_HOUR 0
    MAX_CONNECTIONS_PER_HOUR 0
    MAX_UPDATES_PER_HOUR 0
    MAX_USER_CONNECTIONS 0;
GRANT ALL PRIVILEGES ON `student\_languages\_user\_%`.*
    TO 'student_languages_user'@'%';
GRANT ALL PRIVILEGES ON `student\_languages`.*
    TO 'student_languages_user'@'%' WITH GRANT OPTION;

