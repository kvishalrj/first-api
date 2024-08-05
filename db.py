import pyodbc 


class ItemDatabase:
    def __init__(self):
        self.conn = pyodbc.connect('DRIVER={SQL Server};SERVER=LAPTOP-54CDFJTF;DATABASE=cafe')
        self.cursor = self.conn.cursor()
    
    def get_items(self):
        result = []
        query = "SELECT * FROM item"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            item_dict = {}
            item_dict['id'], item_dict['name'], item_dict['price'] = row
            result.append(item_dict)
        
        return result
            

    def get_item(self, item_id):
        result = []
        query = f"SELECT * FROM item WHERE id = '{item_id}'"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            item_dict = {}
            item_dict['id'], item_dict['name'], item_dict['price']  = row
            result.append(item_dict)
        
        return result


    def add_item(self, id, body):
        query = f"INSERT INTO item(id, name, price) VALUES('{id}', '{body['name']}', {body['price']})"
        self.cursor.execute(query)
        self.conn.commit()


    def update_item(self, id, body):
        query = f"UPDATE item SET name = '{body['name']}', price = '{body['price']}' WHERE id = '{id}'"
        self.cursor.execute(query)
        if self.cursor.rowcount == 0:
            return False
        else:
            self.conn.commit()
            return True


    def delete_item(self, id):
        query = f"DELETE FROM item WHERE id = '{id}'"
        self.cursor.execute(query)
        if self.cursor.rowcount == 0:
            return False
        else:
            self.conn.commit()
            return True


