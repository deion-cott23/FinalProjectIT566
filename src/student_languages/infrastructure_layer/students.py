"""Contains the definition for the Students class."""

import json
from student_languages.infrastructure_layer.languages import Languages
from typing import List


class Students():
    """Implements a Student Entity"""
    def __init__(self)->None:
        self.id:int = 0
        self.first_name:str = ""
        self.middle_name:str = ""
        self.last_name:str = ""
        self.birthday:str = ""
        self.gender:str = ""
        self.languages:List[Languages] = []


    def __str__(self)->str:
        return self.to_json()
    

    def __repr__(self)->str:
        return self.to_json()
    

    def to_json(self)->str:
        students_dict = {}
        students_dict['id'] = self.id
        students_dict['first_name'] = self.first_name
        students_dict['middle_name'] = self.middle_name
        students_dict['last_name'] = self.last_name
        students_dict['birthday'] = self.birthday
        students_dict['gender'] = self.gender
        students_dict['languages'] = []


        for item in self.languages:
            students_dict['languages'].append(item.__dict__)

        return json.dumps(students_dict)
    
    