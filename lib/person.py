from __init__ import CURSOR, CONN

class Person:

    def __init__(self,name, id=None):
        self.name = name
        self.id = id

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value 
        else: 
            raise ValueError("Name has to be a non-empty string")
    
    def __repr__(self):
        return f"<person={self.name}, id={self.id} />"
  
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS persons(
                    id INTEGER PRIMARY KEY,
                    name TEXT
                );
            """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS persons;
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def save(self):
        try:
            if self.id is None:
                sql = """
                    INSERT INTO persons (name) VALUES (?)
                """
                CURSOR.execute(sql, (self.name, ))
                CONN.commit()
                self.id= CURSOR.lastrowid
            else:
                sql = """
                    UPDATE persons SET name = ? WHERE id = ?
                """
                CURSOR.execute(sql, (self.name, self.id))
                CONN.commit()
        except Exception as z: 
            print(f'something went wrong: {z}')

    def delete(self):
        try:
            if self.id is not None:
                sql = """
                    DELETE FROM persons WHERE id = ?
                """
                CURSOR.execute(sql, (self.id,))
                CONN.commit()
                print(f"Person with ID {self.id} has been deleted.")
            else:
                print("Cannot delete a person that hasn't been saved yet.")
        except Exception as e:
            print(f"Something went wrong: {e}")        


    @classmethod
    def find_by_id(cls, id):
        """Return a Person instance having the attribute values from the table row."""
        sql = "SELECT * FROM persons WHERE id = ?"
        CURSOR.execute(sql, (id,))
        row = CURSOR.fetchone()
        if row:
            return cls.instance_from_db(row)
        return None
    
    @classmethod
    def instance_from_db(cls, row):
        """Create an instance from a database row."""
        id, name = row
        return cls(id=id, name=name)            
    
    @classmethod
    def get_all(cls):
        """Return all Person instances from the database."""
        sql = "SELECT * FROM persons"
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def create(cls, name):
        """Initialize a new Person instance and save it to the database."""
        person = cls(name=name)
        person.save()
        return person
    
    

    