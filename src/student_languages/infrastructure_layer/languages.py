"""Contains the definition for the Language class."""

import json
from typing import List


class Languages():
    """Implements a Languages entity."""

    def __init__(self)->None:
        self.language_id:int = 0
        self.language:List = []
        self.dialect:str = ""
        self.description:str = ""
    

    def __str__(self)->str:
        return self.to_json()
    
    
    def __repr__(self)->str:
        return self.to_json()
    

    def to_json(self)->str:
        languages_dict = {}
        languages_dict['language_id'] = self.language_id
        languages_dict['language'] = self.language
        languages_dict['dialect'] = self.dialect
        languages_dict['description'] = self.description
        return json.dumps(languages_dict)
    
