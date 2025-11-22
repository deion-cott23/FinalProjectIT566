"""Contains the definition for a ConsoleUI class."""

from student_languages.service_layer.app_services import AppServices
from student_languages.application_base import ApplicationBase


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
        print(f"\t\tStudent Languages Application Menu")
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

    
    def start(self)->None:
        self.display_menu()
