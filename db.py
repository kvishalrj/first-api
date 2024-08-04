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
            item_dict['id'] = row[0]
            item_dict['name'] = row[1]
            item_dict['price'] = row[2]
            result.append(item_dict)
        
        return result
            

    def get_item(self, item_id):
        result = []
        query = f"SELECT * FROM item WHERE id = '{item_id}'"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            item_dict = {}
            item_dict['id'] = row[0]
            item_dict['name'] = row[1]
            item_dict['price'] = row[2]
            result.append(item_dict)
        
        return result

    def add_item(self, id, body_object):
        pass

    def put_item(self, id, body_object):
        pass

    def delete_item(self, item_id):
        pass

