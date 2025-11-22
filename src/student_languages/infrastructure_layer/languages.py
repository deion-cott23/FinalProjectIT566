"""Contains the definition for the Language class."""

import json

class Languages():
    """Implements a Languages entity."""

    def __init__(self)->None:
        self.language:str = ""
        self.dialect:str = ""
        self.description:str = ""
    

    def __str__(self)->str:
        return self.to_json()
    
    
    def __repr__(self)->str:
        return self.to_json()
    

    def to_json(self)->str:
        languages_dict = {}
        languages_dict['language'] = self.language
        languages_dict['dialect'] = self.dialect
        languages_dict['description'] = self.description
        return json.dumps(languages_dict)
