#!/bin/bash

#create logs directory if not there
echo 'Creating logs directory if it does not already exist...'
mkdir -p logs
echo 'Deleting old log files if they exists...'
rm -f logs/*

d=($date)
echo $d

# Create Database Version 1
echo "Running DB Version 1 Scripts..."
echo $d': Dropping database...' | tee -a logs/drop_database.log
mysql.exe < src/student_languages/db_version_1/drop_database.sql 2>&1 | tee -a logs/drop_database.log
echo $d': Dropping user...' | tee -a logs/drop_user.log
mysql.exe < src/student_languages/db_version_1/drop_user.sql 2>&1 | tee -a logs/drop_user.log
#echo $d': Dropping tables...' | tee -a logs/drop_tables.log
#mysql.exe < src/student_languages/db_version_1/drop_tables.sql 2>&1 | tee -a logs/drop_tables.log
echo $d': Creating database...' | tee -a logs/create_database.log
mysql.exe < src/student_languages/create_database.sql 2>&1 | tee -a logs/create_database.log
echo $d': Creating user...' | tee -a logs/create_user.log
mysql.exe < src/student_languages/create_user.sql 2>&1 | tee -a logs/create_user.log
echo $d': Creating tables...' | tee -a  logs/create_tables.log
mysql.exe < src/student_languages/create_tables.sql 2>&1 | tee -a logs/create_tables.log
echo $d': Inserting test data...' | tee -a logs/insert_test_data.log
mysql.exe < src/student_languages/insert_test_data.sql 2>&1 | tee -a logs/insert_test_data.log


# Create Database Version 2
echo "Running DB Version 2 Scripts..."
echo $d': Altering students table...' | tee -a logs/alter_students_table.log
mysql < src/student_languages/db_version_2/alter_students_table.sql 2>&1 | tee -a logs/alter_students_table.log
