from __init__ import CURSOR, CONN


class Feeling: 

    def __init__(self, feeling_name, id=None,):
        self.feeling_name = feeling_name
        self.id = id 

    def __repr__(self):
        return f"<feeling={self.feeling_name}, id={self.id} />"


    @property
    def feeling_name(self):
        return self._feeling_name 
    @feeling_name.setter
    def feeling_name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._feeling_name = value 
        else: 
            raise ValueError("feeling_name has to be a non-empty string")
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE feelings(
                    id INTEGER PRIMARY KEY,
                    feeling_name TEXT
                );
            """
        CURSOR.execute(sql)
        CONN.commit()
    

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS feelings;
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def save(self):
        try:
            sql= """
                INSERT INTO feelings (feeling_name) VALUES (?)
                """
            CURSOR.execute(sql, (self.feeling_name, ))
            CONN.commit()
            self.id= CURSOR.lastrowid
            # not sure if this is needed 
            type(self).all[self.id] = self
        except Exception as x: 
            print(f'something went wrong: {x}')
