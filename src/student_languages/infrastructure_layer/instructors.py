"""Contains the definition for the Instructors class."""

import json
from student_languages.infrastructure_layer.languages import Languages
from typing import List

class Instructors():
    """Implement an Instructors entity."""
    def __init__(self)->None:
        self.id:int = 0
        self.first_name:str = ""
        self.middle_name:str = ""
        self.last_name:str = ""
        self.languages:List = []
        self.critiques:str = ""

    
    def __str__(self)->str:
        return self.to_json()
    

    def __repr__(self)->str:
        return self.to_json()
    

    def to_json(self)->str:

        instructors_dict = {}
        instructors_dict['id'] = self.id
        instructors_dict['first_name'] = self.first_name
        instructors_dict['middle_name'] = self.middle_name
        instructors_dict['last_name'] = self.last_name
        instructors_dict['languages'] = self.languages
        instructors_dict['critiques'] = self.critiques

        for item in self.languages:
            instructors_dict['languages'].append(item.__dict__)

        return json.dumps(instructors_dict)


    
