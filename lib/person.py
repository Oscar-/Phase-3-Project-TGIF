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
            sql= """
                INSERT INTO persons (name) VALUES (?)
                """
            CURSOR.execute(sql, (self.name, ))
            CONN.commit()
            self.id= CURSOR.lastrowid
            # not sure if this is needed 
            # type(self).all[self.id] = self
        except Exception as z: 
            print(f'something went wrong: {z}')