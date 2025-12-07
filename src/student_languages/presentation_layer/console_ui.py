"""Contains the definition for a ConsoleUI class."""

from student_languages.service_layer.app_services import AppServices
from student_languages.application_base import ApplicationBase
from student_languages.infrastructure_layer.students import Students
from student_languages.infrastructure_layer.instructors import Instructors
from student_languages.infrastructure_layer.languages import Languages
from prettytable import PrettyTable
import sys
import inspect
from datetime import datetime



class ConsoleUI(ApplicationBase):
    """Defines the ConsoleUI class."""
    def __init__(self, config:dict)->None:
        """Initializes object."""
        self._config_dict = config
        self.META = config["meta"]
        super().__init__(subclass_name=self.__class__.__name__, 
                         logfile_prefix_name=self.META["log_prefix"])
        self.app_services = AppServices(config)


    # Public Methods
    def display_menu(self)->None:
        """Display the menu"""
        print(f"\n\n\t\tStudent Languages Application Menu")
        print()
        print(f"\t1. List Students")
        print(f"\t2. List Instructors")
        print(f"\t3. List Languages")
        print(f"\t4. Add Student")
        print(f"\t5. Add Instructor")
        print(f"\t6. Add Language")
        print(f"\t7. Record Students and Languages Studied")
        print(f"\t8. Exit")
        print()

    def process_menu_choice(self)->None:
        """Processes users menu choice."""
        menu_choice = input("\tMenu Choice: ")

        match menu_choice[0]:
            case '1': self.list_students()
            case '2': self.list_instructors()
            case '3': self.list_languages()
            case '4': self.add_student()
            case '5': self.add_instructor()
            case '6': self.add_language()
            case '7': self.record_students_and_languages()
            case '8': sys.exit()
            case _: print(f"Invalid Menu Choice {menu_choice[0]}")



    def start(self)->None:
        while True:
            self.display_menu()
            self.process_menu_choice()

    
    def list_students(self)->None:
        """List students."""
        print("list_students() method stub called...")
        students = self.app_services.get_all_students()
        students_table = PrettyTable()
        students_table.field_names = ['id', 'First Name', 'Middle Name', 'Last Name', 'Birthday', 'Gender']
        for students in students:
            # for languages in students.languages:
            #     languages_table.add_row([languages.languages_id, languages.language, languages.dialect, languages.description])
            students_table.add_row([students.id, students.first_name, students.middle_name, students.last_name, 
                                    students.birthday, students.gender])
            students_table.add_divider()
           #  languages_table.clear_rows()
        print(students_table)


    def add_student(self)->None:
        """Add student."""
        print("\n\tAdd Student...")
        # new_student_list = PrettyTable()
        student = Students()
        try:
            student.first_name = input('First Name: ')
            student.middle_name = input('Middle Name: ')
            student.last_name = input('Last Name: ')
            birthday_input = input('Birthday (mm/dd/yyyy): ')
            student.birthday = datetime.strptime(birthday_input, '%m/%d/%Y')
            student.gender = input('Gender (M/F): ')
            student = self.app_services.create_student(student=student)
            print(f'New Student id: {student.id}')

        except Exception as e:
            self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')

            


    def list_instructors(self)->None:
        """List instructors."""
        print("list_instructors() method stub called...")
        instructors = self.app_services.get_all_instructors()
        instructors_table = PrettyTable()
        instructors_table.field_names = ['id', 'First Name', 'Middle Name', 'Last Name', 'Languages', 'Critiques']
        languages_table = PrettyTable()
        languages_table.field_names = ['Languages id', "Languages", "Dialect", "Description"]
        for instructors in instructors:
            #   for languages in instructors.languages:
            #     languages_table.add_row([languages.languages_id, languages.language, languages.dialect, languages.description])

            instructors_table.add_row([instructors.id, instructors.first_name, instructors.middle_name, instructors.last_name,
                                            instructors.languages, instructors.critiques])
            instructors_table.add_divider()
            languages_table.clear_rows()
        print(instructors_table)


    def add_instructor(self)->None:
        """Add instructor."""
        print("\n\tAdd Instructor...")
        instructor = Instructors()
        try:
            instructor.first_name = input('First Name: ')
            instructor.middle_name = input('Middle Name: ')
            instructor.last_name = input('Last Name: ')
            instructor.languages = input('Languages: ')
            instructor.critiques = input('Critiques: ')
            instructor = self.app_services.create_instructor(instructor=instructor)
            print(f'New Instructor id: {instructor.id}')

        except Exception as e:
            self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')
            


    def list_languages(self)->None:
        """List Languages"""
        print("list_languages() method stub called....")
        languages = self.app_services.get_all_students_with_languages()
        language_table = PrettyTable()
        language_table.field_names = ['Language ID', 'Language', 'Dialect', 'Description']
        # student_table = PrettyTable()
        # student_table.field_names = ['id', 'First Name', 'Middle Name', 'Last Name', 'Birthday', 'Gender']
        for lang in languages:
            # for students in students:
            #     student_table.add_row([students.id, students.first_name, students.middle_name, students.last_name, 
            #                 students.birthday, students.gender])
            language_table.add_row([lang.language_id, lang.language, lang.dialect, lang.description])
            language_table.add_divider()
            # language_table.clear_rows()
        print(language_table)




    def add_language(self)->None:
        """Add new language."""
        print("\n\tAdd Language...")
        languages = Languages()
        try:
            languages.language = input('New Language: ')
            languages.dialect = input('Known Dialect(Region): ')
            languages.description = input('Description of Language: ')
            languages = self.app_services.create_language(language=languages)
            print(f'New Language ID: {languages.language_id}')

        except Exception as e:
            self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')





    def record_students_and_languages(self)->None:
        """Record students and their respective languages."""
        print("\n\tRecord of students and Languages...")
        student_language_xref = self.app_services.get_all_student_languages_xref()
        student_language_xref_table  = PrettyTable()
        student_language_xref_table.field_names = ['Students ID', 'Grade', 'Students Update']
        for student_language_xref in student_language_xref:
            student_language_xref_table.add_row([student_language_xref.students_id, student_language_xref.grade, 
                    student_language_xref.student_update])
            student_language_xref.add_divider()
            student_language_xref.clear_rows()
        print(student_language_xref)

