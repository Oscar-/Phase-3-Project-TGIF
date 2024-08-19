# import sqlite3
# CONN = sqlite3.connect('lib/resources.db', timeout=10)
# CURSOR = CONN.cursor()

from __init__ import CURSOR, CONN
from person import Person
from feeling import Feeling
from activity import Activity

# belongs to feeling through activity
# belongs to people
# belongs to activity

# create fxn:
# created_at(TEXT)
# updated_at

class Results:

    all = {}

    def __init__(self, person_id, feeling_id, activity_id, id=None):
        self.id = id
        self.person = person_id
        self.feeling = feeling_id  
        # (use hasattr so once created cannot be updated)
        self.activity = activity_id

    def __repr__(self):
        return f'<People person={self.person} feeling={self.feeling} activity={self.activity} />'
    
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Results instances """
        sql = """
            CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY,
            person TEXT,
            feeling TEXT,
            activity TEXT,
            FOREIGN KEY (person_id) REFERENCES person(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Results instances """
        sql = """
            DROP TABLE IF EXISTS results;
        """
        CURSOR.execute(sql)
        CONN.commit()

    
    def save(self):
        """ Insert a new row with the person, feeling, and activity values of the current Result object.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        
        if self.id:
            sql="""
                UPDATE result
                SET person = ?, feeling = ?, activity = ?
                WHERE id = ?
            """
            CURSOR.execute(sql, (self.person, self.feeling, self.activity, self.id))
        else:
            sql = """
                INSERT INTO results (person, feeling, activity)
                VALUES (?, ? , ?)
            """ 
            CURSOR.execute(sql, (self.person, self.feeling, self.activity))

            self.id = CURSOR.lastrowid
            
            Results.all[self.id] = self    

        CONN.commit()      
    
    @classmethod
    def create(cls, person, feeling, activity):
        """ Initialize a new Result instance and save the object to the database. Return the new instance. """
        result = cls(person, feeling, activity)
        result.save()
        return result

    @classmethod
    def instance_from_db(cls, row):
        """Return an Result instance having the attribute values from the table row."""
        # Check the dictionary for  existing instance using the row's primary key
        result.id, person, feeling, activity = row

        if results_id in cls.all:
            # return cls.all[result_id]
            result = cls.all[results_id]
            result.person = person
            result.feeling = feeling
            result.activity = activity
            return result

        review = cls(person, feeling, activity, id=results_id)
        cls.all[results_id] = review
        return review


    @classmethod
    def find_by_id(cls, id):
        """Return a Result instance having the attribute values from the table row."""
    
        sql = "SELECT * FROM results WHERE id = ?"
        CURSOR.execute(sql, (id,))
        row = CURSOR.fetchone()
        if row:
            return cls.instance_from_db(row)
        return None    
    
    def update(self):
        """Update the table row corresponding to the current Result instance."""

        sql = """
        UPDATE results
        SET person_id= ?, feeling_id = ?, activity_id = ?
        WHERE id = ?
    """
        CURSOR.execute(sql, (self.person, self.feeling, self.activity, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Result instance,
        delete the dictionary entry, and reassign id attribute"""
        sql = "DELETE FROM results WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        if self.id in Results.all:
            del Results.all[self.id]
        
        self.id = None  # Reassign id attribute to None
    
    @classmethod
    def get_all(cls):
        """Return a list containing one Result instance per table row"""
        sql = "SELECT * FROM results"
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @property
    def activity_id(self):
        return self._activity_id
    @activity_id.setter
    def activity_id(self, activity_id):
        if not isinstance(activity_id, int) or Activity.find_by_id(activity_id) is None:
            raise ValueError("Activity ID must reference a valid activity")
        self._activity_id = activity_id

    @property
    def feeling_id(self):
        return self._feeling_id
    
    ##add hasattr here 
    @feeling_id.setter
    def feeling_id(self, feeling_id):
        if(not hasattr(self, 'feeling_id')) and not isinstance(feeling_id, int) or Feeling.find_by_id(feeling_id) is None:
            raise ValueError("Feeling ID must reference a valid feeling")
        self._feeling_id = feeling_id

    @property
    def person_id(self):
        return self._person_id
    @person_id.setter
    def person_id(self, person_id):
        if not isinstance(person_id, int) or Person.find_by_id(person_id) is None:
            raise ValueError("Person ID must reference a valid person")
        self._person_id = person_id
    


    



