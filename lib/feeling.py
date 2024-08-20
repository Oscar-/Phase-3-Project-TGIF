from __init__ import CURSOR, CONN


class Feeling: 
    all=[]

    def __init__(self, feeling_name, id=None,):
        self.feeling_name = feeling_name
        self.id = id 
        Feeling.all.append(self)

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
            CREATE TABLE IF NOT EXISTS feelings(
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
        except Exception as x: 
            print(f'something went wrong: {x}')

    @classmethod
    def find_by_id(cls, id):
        """Return a Feeling instance having the attribute values from the table row."""
        sql = "SELECT * FROM feelings WHERE id = ?"
        CURSOR.execute(sql, (id,))
        row = CURSOR.fetchone()
        if row:
            return cls.instance_from_db(row)
        return None

    @classmethod
    def instance_from_db(cls, row):
        """Create an instance from a database row."""
        id, feeling_name = row
        return cls(feeling_name=feeling_name, id=id)
    
    @classmethod
    def get_all(cls):
        """Return all Feeling instances from the database."""
        sql = "SELECT * FROM feelings"
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def get_feelings_for_person(cls, person_id):
        """Return all feelings associated with the given person_id."""
        sql = """
            SELECT feelings.id, feelings.feeling_name
            FROM feelings
            JOIN activity ON feelings.id = activity.feeling_id 
            WHERE activity.person_id = ?
        """;
        CURSOR.execute(sql, (person_id,))
        rows = CURSOR.fetchall()
        return [cls.instance_from_db(row) for row in rows]