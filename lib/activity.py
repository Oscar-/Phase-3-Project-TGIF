# import sqlite3
# CONN = sqlite3.connect('lib/resources.db', timeout=10)
# CURSOR = CONN.cursor()

from feeling import Feeling
from person import Person 


class Activity: 

    def __init__(self, person_id, activity_name, feeling_id, id=None):
        self.id = id
        self.person_id = person_id
        self.activity_name = activity_name
        self.feeling_id = feeling_id

    def __repr__(self):
        return f"<Activity activity={self.activity_name}, feeling={self.feeling_id}, id={self.id} />"

    @property
    def person_id(self):
        return self._person_id 
    @person_id.setter
    def person_id(self, value):
        if isinstance(value, Person):
            self._person_id = value 
        else: 
            raise ValueError("name has to be an instance of a Person")

    @property
    def activity_name(self):
        return self._activity_name 
    @activity_name.setter
    def activity_name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._activity_name = value 
        else: 
            raise ValueError("activity_name has to be a non-empty string")
    
    @property
    def feeling_id(self):
        return self._feeling_id 
    @feeling_id.setter
    def feeling_id(self, value):
        if isinstance(value, int) and feeling_id(value):
            self._feeling_id = value
        else:
            raise ValueError("feeling ID must be the ID of an existing feeling instance.")



    