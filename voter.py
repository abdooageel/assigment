from database import CursorFromConnectionPool

class Voter:
    def __init__(self, first_name, second_name,
                 third_name,family_name,date_birth,
                 place_birth,province,district,city,
                 ,quarter,status,type,national_id_no,family_book_no, id=None):
        self.first_name= first_name
        self.second_name =second_name
        self.third_name = third_name
        self.family_name = family_name
        self.date_birth = date_birth
        self.place_birth = place_birth
        self.province = province
        self.district = district
        self.city = city
        self.quarter = quarter
        self.status = status
        self.type = type
        self.national_id_no = national_id_no
        self.family_book_no = family_book_no
        self.id = id


    def __repr__(self):
        return "<Voter {}>".format(self.first_name)

    def save_to_db(self):
        # This is creating a new connection pool every time! Very expensive...
        with CursorFromConnectionPool() as cursor:
            cursor.execute('INSERT INTO Voter  VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s)',
                            (self.first_name, self.second_name, self.third_name,
                             self.family_name, self.date_birth, self.place_birth,
                             self.province, self.district, self.city,
                             self.quarter, self.status, self.type,
                             self.national_id_no, self.family_book_no))

    @classmethod
    def load_from_db(cls, national_id_no):
        with CursorFromConnectionPool() as cursor:
            # Note the (email,) to make it a tuple!
            cursor.execute('SELECT * FROM Voter WHERE national_id_no=%s', (national_id_no,))
            user_data = cursor.fetchone()
            return cls()

