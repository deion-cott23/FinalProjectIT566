"""Persistence Layer Unit Tests."""
from tests.context import MySQLPersistenceWrapper
import pytest
import json
import os

@pytest.fixture(scope="class")
def mysql_persistence_wrapper():
    print(f'\nSetting up mysql_persistence_wrapper_fixture...')
    working_dir = os.getcwd()
    config_dir = 'config'
    config_file_name = 'student_languages_app_config.json'
    config_dir_path = os.path.join(working_dir, config_dir, config_file_name )
    config_dict = None
    with open(config_dir_path, 'r') as f:
        config_dict = json.loads(f.read())
    db = MySQLPersistenceWrapper(config_dict)
    yield db
    print(f'\nTearing down mysql_peristence_wrapper_fixture...')

class TestPersistenceLayer:
        """Defines a group of related unit tests."""
        def test_select_all_students(self, mysql_persistence_wrapper):
             students_list = mysql_persistence_wrapper.select_all_students()
             assert len(students_list) > 0


