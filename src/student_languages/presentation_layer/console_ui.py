"""Contains the definition for a ConsoleUI class."""

from student_languages.service_layer.app_services import AppServices
from student_languages.application_base import ApplicationBase
from prettytable import PrettyTable
import sys


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

    
    def list_students(self)->None:
        """List students."""
        print("list_students() method stub called...")
        students = self.app_services.get_all_students()
        students_table = PrettyTable()
        students_table.field_names = ['id', 'First Name', 'Middle Name', 'Last Name', 'Birthday', 'Gender']
        languages_table = PrettyTable()
        languages_table.field_names = ['Languages id', "Languages", "Dialect", "Description"]
        languages_table.align = 'l'
        for students in students:
            # for languages in students.languages:
            #     languages_table.add_row([languages.languages_id, languages.language, languages.dialect, languages.description])
            students_table.add_row([students.id, students.first_name, students.middle_name, students.last_name, 
                                    students.birthday, students.gender])
            students_table.add_divider()
           # languages_table.clear_rows()
        print(students_table)


    def list_instructors(self)->None:
        """List instructors."""
        print("list_instructors() method stub called...")
        instructors = self.app_services.get_all_instructors()
        instructors_table = PrettyTable()
        instructors_table.field_names = ['id', 'First Name', 'Middle Name', 'Last Name', 'Languages', 'Critiques']
        languages_table = PrettyTable()
        languages_table.field_names = ['Languages id', "Languages", "Dialect", "Description"]
        for instructors in instructors:
            # for languages in instructors.languages:
            #     languages_table.add_row([languages.languages_id, languages.language, languages.dialect, languages.description])

            instructors_table.add_row([instructors.id, instructors.first_name, instructors.middle_name, instructors.last_name,
                                           instructors.languages, instructors.critiques])
            instructors_table.add_divider()
            # languages_table.clear_rows()
        print(instructors_table)
            


    def list_languages(self)->None:
        """List Languages"""
        print("list_languages() method stub called....")
        language_table = PrettyTable()
        language_table.field_names = ['Language ID', 'Language', 'Dialect', 'Description']
        for language in language:
            language_table.add_row([language.languages_id, language.language, language.dialect, language.description])
            language_table.add_divider()
           #  language_table.clear_rows()
        print(language_table)



    def add_student(self)->None:
        """Add student."""
        print("add_student() method stub called...")

    def add_instructor(self)->None:
        """Add instructor."""
        print("add_instructor() method stub called...")

    def add_language(self)->None:
        """Add new language."""
        print("add_language() method stub called...")

    def record_students_and_languages(self)->None:
        """Record students and their respective languages."""
        print("record_students_and_languages() method stub called...")

    
    def start(self)->None:
        while True:
            self.display_menu()
            self.process_menu_choice()
