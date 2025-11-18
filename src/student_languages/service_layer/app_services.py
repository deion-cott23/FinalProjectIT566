"""Implements AppServices Class."""

from student_languages.application_base import ApplicationBase
from student_languages.persistence_layer.mysql_persistence_wrapper import MySQLPersistenceWrapper
import inspect

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

    """
    def select_all_users(self)->list(students):
    	Returns a list of all user rows
		
        return self.DB_SELECT_ALL_USERS()
    """
		
		