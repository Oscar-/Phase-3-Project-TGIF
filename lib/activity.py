from feeling import Feeling
from person import Person 
from __init__ import CURSOR, CONN


class Activity: 

    def __init__(self, activity_name, feeling_id, person_id, id=None):

        self.activity_name = activity_name
        self.feeling_id = feeling_id
        self.person_id = person_id
        self.id = id
     

    def __repr__(self):
        return f"<Activity activity={self.activity_name}, feeling={self.feeling_id}, id={self.id} />"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS activity(
                    id INTEGER PRIMARY KEY,
                    activity_name TEXT,
                    feeling_id INT,
                    person_id INT,
                    FOREIGN KEY (person_id) REFERENCES person(id),
                    FOREIGN KEY (feeling_id) REFERENCES feeling(id)
                );
            """
        CURSOR.execute(sql)
        CONN.commit()
    

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS activity;
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def save(self):
        try:
            sql= """
                INSERT INTO activity (activity_name) VALUES (?)
                """
            CURSOR.execute(sql, (self.activity_name, ))
            CONN.commit()
            self.id= CURSOR.lastrowid
            # not sure if this is needed 
        except Exception as x: 
            print(f'something went wrong: {x}')




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
        if hasattr(self, '_feeling_id'):
            raise AttributeError("feeling_id cannot be updated once set.")
        if isinstance(value, Feeling):
        # and Feeling(value):
            self._feeling_id = value
        else:
            raise ValueError("Feeling ID must be the ID of an existing feeling instance.")

    # @classmethod 
    # def get_feeling_name(cls, id):
    #     sql = """ 
    #         SELECT feeling.id FROM feelings JOIN activity ON feeling.id = activity.id WHERE feeling.id = ?;
    #         """
    #     return[cls.create_instance(row) for row in CURSOR.execute(sql, (id, )).fetchall()]
    
    @classmethod
    def get_all_feeling(cls):
        """Return a list containing one Activity instance per table row"""
        sql = "SELECT * FROM activity"
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod 
    def create_instance(cls, row):
        app = cls(
            id=row[0],
            activity=row[1],
            feeling=row[2],
            person=row[3]
        )
        return app

        