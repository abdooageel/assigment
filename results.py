from database import CursorFromConnectionPool

class Results:
    def __init__(self, center_Number, center_Name, valid_Votes, id=None):
        self.center_Number= center_Number
        self.center_Name =center_Name
        self.valid_Votes = valid_Votes
        self.id = id

    def __repr__(self):
        return "<User {}>".format(self.center_Number)

    def save_to_db(self):
        # This is creating a new connection pool every time! Very expensive...
        with CursorFromConnectionPool() as cursor:
            cursor.execute('INSERT INTO results ("center_Number", "center_Name", "valid_Votes") VALUES (%s, %s, %s)',
                            (self.center_Number, self.center_Name, self.valid_Votes))

    @classmethod
    def load_from_db(cls, center_Number):
        with CursorFromConnectionPool() as cursor:
            cursor.execute('SELECT * FROM results WHERE "center_Number"=%s', (center_Number,))
            user_data = cursor.fetchone()
            print(user_data)
            return cls(center_Number=user_data[1],center_Name=user_data[2],valid_Votes=user_data[3],id=user_data[0])