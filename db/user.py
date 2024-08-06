import pyodbc  # type: ignore


class UserDatabase:
    def __init__(self):
        self.conn = pyodbc.connect('DRIVER={SQL Server};SERVER=LAPTOP-54CDFJTF;DATABASE=cafe')
        self.cursor = self.conn.cursor()
    

    def get_user(self, id):
        query = f"SELECT * FROM users WHERE id = '{id}'"
        self.cursor.execute(query)
        user_dict = {}
        result = self.cursor.fetchone()
        if result:
            user_dict['id'], user_dict['username'], user_dict['password']  =  result
        return user_dict


    def add_user(self, username, password):
        query = f"INSERT INTO users(username, password) VALUES('{username}', '{password}')"
        try:
            self.cursor.execute(query)
            self.conn.commit()
            return True
        except pyodbc.IntegrityError:
            return False


    def delete_user(self, id):
        query = f"DELETE FROM users WHERE id = '{id}'"
        self.cursor.execute(query)
        if self.cursor.rowcount == 0:
            return False
        else:
            self.conn.commit()
            return True
        
    
    def verify_user(self, username, password):
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        if result:
            return result[0]



