"""Implements AppServices Class and the application service layer."""

from student_languages.application_base import ApplicationBase
from student_languages.persistence_layer.mysql_persistence_wrapper import MySQLPersistenceWrapper
import inspect
import json
from typing import List
from student_languages.infrastructure_layer.students import Students
from student_languages.infrastructure_layer.instructors import Instructors
from student_languages.infrastructure_layer.languages import Languages
from student_languages.infrastructure_layer.student_language_xref import Student_Language_xref



class AppServices(ApplicationBase):
    """AppServices Class Definition."""
    def __init__(self, config:dict)->None:
        """Initializes object. """
        self._config_dict = config
        self.META = config["meta"]
        super().__init__(subclass_name=self.__class__.__name__, 
				   logfile_prefix_name=self.META["log_prefix"])
        self.DB = MySQLPersistenceWrapper(config)
        self._logger.log_debug(f'{inspect.currentframe().f_code.co_name}:It works!')


    def get_all_students(self)->List[Students]:
        """Returns a list of student objects."""
        self._logger.log_debug(f'In {inspect.currentframe().f_code.co_name}()...')
        student_dict = {}
        student_dict['students'] = []

        try:
            results = self.DB.select_all_students()
            return results
        
        except Exception as e:
            self._logger.log_debug(f'{inspect.currentframe().f_code.co_name}: {e}')


    def create_student(self, student:Students)->Students:
        """Creates a new student in the database."""

        self._logger.log_debug(f'In {inspect.currentframe().f_code.co_name}()...')
        try:
            results = self.DB.create_student(student)
            return results
        
        except Exception as e:
            self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')

 

    def get_all_instructors(self)->List[Instructors]:
        """Returns a list of instructor objects."""
        self._logger.log_debug(f'In {inspect.currentframe().f_code.co_name}()...')
        instructor_dict = {}
        instructor_dict['instructors'] = []

        try:
            results = self.DB.select_all_instructors()
            return results
        
        except Exception as e:
            self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')


    def create_instructor(self, instructor:Instructors)->Instructors:
        """Creates a new instructor in the database."""
        self._logger.log_debug(f'In {inspect.currentframe().f_code.co_name}()...')
        try:
            results = self.DB.create_instructor(instructor)
            return results
        
        except Exception as e:
            self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')




    def get_all_students_with_languages(self)->List[Languages]:
        """Returns a list of languages."""
        self._logger.log_debug(f'In {inspect.currentframe().f_code.co_name}()...')
        language_dict = {}
        student_dict = {}
        language_dict['languages'] = []
        student_dict['students'] = []

        try:
            results = self.DB.select_all_students_with_languages()
            # results_student = self.DB.select_all_students()

            return results
        
        except Exception as e:
            self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')



    def create_language(self, language:Languages)->Languages:
        """Creates a new language in the database."""
        self._logger.log_debug(f'In {inspect.currentframe().f_code.co_name}()...')
        try:
            results = self.DB.create_language(language)
            return results
        
        except Exception as e:
            self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')



    
    def get_all_student_languages_xref(self)->List[Student_Language_xref]:
        """Returns a list of students and their grade reports."""
        self._logger.log_debug(f'In {inspect.currentframe().f_code.co_name}()...')
        student_language_xref_dict = {}
        student_language_xref_dict['student_language_xref'] = []

        try:
            results = self.DB.select_students_status_from_student_id()

            return results
        
        except Exception as e:
            self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')


        




    
    """
    def get_all_students_as_json(self)->str:
           Return all students as JSON String
        self._logger.log_debug(f'In {inspect.currentframe().f_code.co_name}()...')
        try:
            results = self.DB.select_all_students()
            return json.dumps(results)
        
        except Exception as e:
            self._logger.log_error(f'{inspect.currentframe().f_code.co_name}:{e}')



    def get_all_instructors_as_json(self)->str:
        Return all instructors as JSON string
        self._logger.log_debug(f'In {inspect.currentframe().f_code.co_name}()...')
        try:
            results = self.DB.select_all_instructors()
            return json.dumps(results)
        
        except Exception as e:
            self._logger.log_error(f'{inspect.currentframe().f_code.co_name}:{e}')
    """


    