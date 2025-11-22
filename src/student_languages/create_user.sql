/* ***************************************************
Drop and create the student_langauges_user
*****************************************************/

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;


-- Create user if not exists
CREATE USER IF NOT EXISTS 'student_languages_user'@'localhost';

GRANT USAGE ON *.* TO `student_languages_user`@`localhost`;
GRANT SELECT, INSERT, UPDATE, DELETE ON `student\_languages`.* TO `student_languages_user`@`localhost`;


ALTER USER 'student_languages_user'@'%'
    REQUIRE NONE WITH MAX_QUERIES_PER_HOUR 0
    MAX_CONNECTIONS_PER_HOUR 0
    MAX_UPDATES_PER_HOUR 0
    MAX_USER_CONNECTIONS 0;
GRANT ALL PRIVILEGES ON `student\_languages\_user\_%`.*
    TO 'student_languages_user'@'%';
GRANT ALL PRIVILEGES ON `student\_languages`.*
    TO 'student_languages_user'@'%' WITH GRANT OPTION;


COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;


