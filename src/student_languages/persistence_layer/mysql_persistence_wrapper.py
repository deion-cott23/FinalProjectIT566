"""Defines the MySQLPersistenceWrapper class."""

from student_languages.application_base import ApplicationBase
from mysql import connector 
from mysql.connector.pooling import (MySQLConnectionPool)
import inspect
import json
from typing import List
from student_languages.infrastructure_layer.students import Students
from student_languages.infrastructure_layer.languages import Languages
from student_languages.infrastructure_layer.instructors import Instructors
from student_languages.infrastructure_layer.student_language_xref import Student_Language_xref
from enum import Enum



class MySQLPersistenceWrapper(ApplicationBase):
	"""Implements the MySQLPersistenceWrapper class."""

	def __init__(self, config:dict)->None:
		"""Initializes object. """
		self._config_dict = config
		#self.META = dict(config["meta"])
		self.META = config["meta"]
		#self.DATABASE = dict(config["database"])
		self.DATABASE = config["database"]
		super().__init__(subclass_name=self.__class__.__name__, 
				   logfile_prefix_name=self.META["log_prefix"])
		self._logger.log_debug(f'{inspect.currentframe().f_code.co_name}:It works!')

		# Database Configuration Constants
		self.DB_CONFIG = {}
		self.DB_CONFIG['database'] = \
			self.DATABASE["connection"]["config"]["database"]
		self.DB_CONFIG['user'] = self.DATABASE["connection"]["config"]["user"]
		self.DB_CONFIG['host'] = self.DATABASE["connection"]["config"]["host"]
		self.DB_CONFIG['port'] = self.DATABASE["connection"]["config"]["port"]

		self._logger.log_debug(f'{inspect.currentframe().f_code.co_name}: DB Connection Config Dict: {self.DB_CONFIG}')

		# Database Connection
		self._connection_pool = \
			self._initialize_database_connection_pool(self.DB_CONFIG)
		

		# Student Column ENUMS
		self.StudentColumns = \
			Enum('StudentColumns', [('id', 0), ('first_name', 1), ('middle_name', 2), ('last_name', 3), ('birthday', 4), ('gender', 5)])
		
		# Instructors Column ENUMS
		self.InstructorColumns = \
			Enum('InstructorColumns', [('id', 0), ('first_name', 1), ('middle_name', 2), ('last_name', 3), ('languages', 4), ('critiques', 5)])

		#Languages Column ENUMS
		self.LanguageColumns = \
			Enum('LanguageColumns', [('language_id', 0), ('language', 4), ('dialect', 5), ('description', 6)])
		
		#Student Language XRef ENUMS
		self.Student_Language_XrefColumns = \
			Enum('Student_Language_XrefColumns', [('students_id', 0), ('grade', 1), ('student_update', 2)])





		# SQL String Constants
		self.SELECT_ALL_STUDENTS = \
			f"SELECT id, first_name, middle_name, last_name, birthday, gender " \
			f"FROM students"
		
		self.SELECT_ALL_INSTRUCTORS = \
			f"SELECT id, first_name, middle_name, last_name, languages, critiques " \
			f"FROM instructors"
		
		self.SELECT_ALL_STUDENTS_WITH_LANGUAGES = \
			f"SELECT `students`.id, first_name, middle_name, last_name, " \
				f"language, dialect, description, proficiency, grade, student_update " \
			f"FROM students, languages, student_language_xref " \
			f"WHERE (`students`.id = students_id) AND (`languages`.languages_id = language_id)"
		
		self.SELECT_STUDENTS_STATUS_FROM_STUDENT_ID = \
			f"SELECT students_id, grade, student_update " \
			f"FROM student_language_xref " \
	
		
		self.INSERT_STUDENT = \
			f"INSERT INTO students " \
			f"(first_name, middle_name, last_name, birthday, gender) " \
			f"values(%s, %s, %s, %s, %s)"
		

		self.INSERT_INSTRUCTOR = \
			f"INSERT INTO instructors " \
			f"(first_name, middle_name, last_name, languages, critiques) " \
			f"values(%s, %s, %s, %s, %s)"
		
		
		self.INSERT_ALL_STUDENTS_WITH_LANGUAGES = \
			f"INSERT INTO languages " \
			f"(language, dialect, description) " \
			f"values(%s, %s, %s)"
		


	# MySQLPersistenceWrapper Methods
		
	def select_all_students(self)->List[Students]:
		"""Returns a list of all user rows."""
		cursor = None
		results = None
		students_list = []
		try:
			connection = self._connection_pool.get_connection()
			with connection:
				cursor = connection.cursor()
				with cursor:
					cursor.execute(self.SELECT_ALL_STUDENTS)
					results = cursor.fetchall()
					self._logger.log_debug(f'{inspect.currentframe().f_code.co_name} {results}')
					students_list = self._populate_student_objects(results)
			
			# for student in students_list:
			# 	languages_list = \
			# 		self.select_all_students_with_languages(student.id)
			# 	self._logger.log_debug(f'{inspect.currentframe().f_code.co_name}: \
			# 			   {languages_list}')
			# 	student.language = self._populate_language_objects(languages_list)

			return students_list
		
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')


	
	def select_all_instructors(self)->List[Instructors]:
		"""Returns a list of all instructor rows"""
		cursor = None
		results = None
		instructors_list = []
		try:
			connection = self._connection_pool.get_connection()
			with connection:
				cursor = connection.cursor()
				with cursor:
					cursor.execute(self.SELECT_ALL_INSTRUCTORS)
					results = cursor.fetchall()
					instructors_list = self._populate_instructor_objects(results)

			# for instructors in instructors_list:
			# 	languages_list = \
			# 		self.select_all_students_with_languages(instructors.id)
			# 	self._logger.log_debug(f'{inspect.currentframe().f_code.co_name}: \
			# 			   {languages_list}')
			# 	instructors.language = self._populate_language_objects(languages_list)

			return instructors_list
		
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')
 



	def select_all_students_with_languages(self)->List[Languages]:
		"""Returns a list of all student rows with languages."""
		cursor = None
		results = None
		languages_list = []
		try:
			connection = self._connection_pool.get_connection()
			with connection:
				cursor = connection.cursor()
				with cursor:
					cursor.execute(self.SELECT_ALL_STUDENTS_WITH_LANGUAGES)
					results = cursor.fetchall()
					languages_list = self._populate_language_objects(results)

			# for students in languages_list:
			# 	languages_list = \
			# 		self.select_all_students_with_languages(students)
			# 	self._logger.log_debug(f'{inspect.currentframe().f_code.co_name}: {languages_list}')
			# 	students.language_id = self._populate_language_objects(languages_list)
			
			return languages_list
		
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')


		

	def select_students_status_from_student_id(self)->List[Student_Language_xref]:
		"""Returns a list of language rows for student id."""
		cursor = None
		results = None
		student_language_xrefs = []
		try:
			connection = self._connection_pool.get_connection()
			with connection:
				cursor = connection.cursor()
				with cursor:
					cursor.execute(self.SELECT_STUDENTS_STATUS_FROM_STUDENT_ID)
					results = cursor.fetchall()
					student_language_xrefs = self._populate_student_language_xref_objects(results)

			return student_language_xrefs
		
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')

	

	def create_student(self, student:Students)->Students:
		"""Create a new record in the students table."""
		cursor = None
		try:
			connection = self._connection_pool.get_connection()
			with connection:
				cursor = connection.cursor()
				with cursor:
					cursor.execute(self.INSERT_STUDENT, ([student.first_name, student.middle_name, student.last_name,
						student.birthday, student.gender]))
					connection.commit()
					self._logger.log_debug(f'Updated {cursor.rowcount} row.')
					self._logger.log_debug(f'Last Row ID: {cursor.lastrowid}.')
					student.id = cursor.lastrowid

			return student
		
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')


	
	def create_instructor(self, instructor:Instructors)->Instructors:
		"""Create a new record in instructors table."""
		cursor = None
		try:
			connection = self._connection_pool.get_connection()
			with connection:
				cursor = connection.cursor()
				with cursor:
					cursor.execute(self.INSERT_INSTRUCTOR, ([instructor.first_name, instructor.middle_name, 
						instructor.last_name, instructor.languages, instructor.critiques]))
					connection.commit()
					self._logger.log_debug(f'Updated {cursor.rowcount} row.')
					self._logger.log_debug(f'Last Row ID: {cursor.lastrowid}.')
					instructor.id = cursor.lastrowid
				
			return instructor
		
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')



	def create_language(self, language:Languages)->Languages:
		"""Create a new record in languages table."""
		cursor = None
		try:
			connection = self._connection_pool.get_connection()
			with connection:
				cursor = connection.cursor()
				with cursor:
					cursor.execute(self.INSERT_ALL_STUDENTS_WITH_LANGUAGES, ([language.language, language.dialect, 
								language.description]))
					connection.commit()
					self._logger.log_debug(f'Updated {cursor.rowcount} row.')
					self._logger.log_debug(f'Last Row ID: {cursor.lastrowid}.')
					language.language_id = cursor.lastrowid
			
			return language
		
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')


		

	##### Private Utility Methods #####

	def _initialize_database_connection_pool(self, config:dict)->MySQLConnectionPool:
		"""Initializes database connection pool."""
		try:
			self._logger.log_debug(f'Creating connection pool...')
			cnx_pool = \
				MySQLConnectionPool(pool_name = self.DATABASE["pool"]["name"],
					pool_size=self.DATABASE["pool"]["size"],
					pool_reset_session=self.DATABASE["pool"]["reset_session"],
					use_pure=self.DATABASE["pool"]["use_pure"],
					**config)
			self._logger.log_debug(f'{inspect.currentframe().f_code.co_name}: Connection pool successfully created!')
			return cnx_pool
		except connector.Error as err:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: Problem creating connection pool: {err}')
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: Check DB cnfg:\n{json.dumps(self.DATABASE)}')
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}:Problem creating connection pool: {e}')
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}:Check DB conf:\n{json.dumps(self.DATABASE)}')
	



	def _populate_student_objects(self, results:List)->List[Students]:
		"""Populates and returns a list of Student objects."""
		student_list = []
		try:
			for row in results:
				student = Students()
				student.id = row[self.StudentColumns['id'].value]
				student.first_name = row[self.StudentColumns['first_name'].value]
				student.middle_name = row[self.StudentColumns['middle_name'].value]
				student.last_name = row[self.StudentColumns['last_name'].value]
				student.birthday = row[self.StudentColumns['birthday'].value]
				student.gender = row[self.StudentColumns['gender'].value]
				student_list.append(student)

			return student_list
		
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')

	
	def _populate_instructor_objects(self, results:List)->List[Instructors]:
		"""Populates and returns a list of Instructor objects."""
		instructor_list = []
		try:
			for row in results:
				instructor = Instructors()
				instructor.id = row[self.InstructorColumns['id'].value]
				instructor.first_name = row[self.InstructorColumns['first_name'].value]
				instructor.middle_name = row[self.InstructorColumns['middle_name'].value]
				instructor.last_name = row[self.InstructorColumns['last_name'].value]
				instructor.languages = row[self.InstructorColumns['languages'].value]
				instructor.critiques = row[self.InstructorColumns['critiques'].value]
				instructor_list.append(instructor)

			return instructor_list
		
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')



	def _populate_language_objects(self, results:List)->List[Languages]:
		"""Populates and returns a list of Language objects."""
		language_list = []
		try:
			for row in results:
				languages = Languages()
				languages.language_id = row[self.LanguageColumns['language_id'].value]
				languages.language = row[self.LanguageColumns['language'].value]
				languages.dialect = row[self.LanguageColumns['dialect'].value]
				languages.description = row[self.LanguageColumns['description'].value]
				language_list.append(languages)

			return language_list
		
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')



	def _populate_student_language_xref_objects(self, results:List)->List[Languages]:
		"""Populates and returns a list of student language xref."""
		student_language_list = []
		try:
			for row in results:
				student_language_xref = Student_Language_xref()
				student_language_xref.students_id = row[self.Student_Language_XrefColumns['students_id'].value]
				student_language_xref.grade = row[self.Student_Language_XrefColumns['grade'].value]
				student_language_xref.student_update = row[self.Student_Language_XrefColumns['student_update'].value]
				student_language_list.append(student_language_xref)

			return student_language_list
		
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')


 