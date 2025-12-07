"""Contains definition for Student Language XREF """

import json
from typing import List
from student_languages.infrastructure_layer.languages import Languages
from student_languages.infrastructure_layer.students import Students


class Student_Language_xref():
    """Implement student language xref"""

    def __init__(self)->None:
        self.students_id:int = 0
        self.grade:str = ""
        self.student_update:str = ""



    def __str__(self)->str:
        return self.to_json()
    
    
    def __repr__(self)->str:
        return self.to_json()
    


    def to_json(self)->str:
        student_language_xref_dict = {}
        student_language_xref_dict['students_id'] = self.students_id
        student_language_xref_dict['grade'] = self.grade
        student_language_xref_dict['student_update'] = self.student_update

        # for item in self.students_id:
        #     student_language_xref_dict['students_id'].append(item.__dict__)

        # return json.dumps(student_language_xref_dict)