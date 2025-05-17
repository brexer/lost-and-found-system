import mysql.connector
from mysql.connector import Error

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'admin',
    'database': 'lafdb'
}

def create_connection():
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None


def createItem(self, item_id, category, name, description, status='Unclaimed'):
    try:
        cursor = self.connection.cursor()
        query = """
        INSERT INTO Items (ItemID, Category, Name, Description, Status)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (item_id, category, name, description, status))
        self.connection.commit()
        print(f"Item {item_id} created successfully")
        return True
    except Error as err:
            print(f"Error: '{err}'")
            return False
    
def update_item_status(self, item_id, new_status):
    try:
        cursor = self.connection.cursor()
        query = """
        UPDATE Items
        SET Status = %s
        WHERE ItemID = %s
        """
        cursor.execute(query, (new_status, item_id))
        self.connection.commit()
        print(f"Item {item_id} status updated to {new_status}")
        return True
    except Error as err:
        print(f"Error: '{err}'")
        return False
    

def surrender_item(self, item_id, location_found, person_id):
    try:
        cursor = self.connection.cursor()
            

        query = """
        INSERT INTO SurrenderedItems (ItemID, DateFound, LocationFound, PersonID)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (item_id, datetime.now(), location_found, person_id))
            
        self.update_item_status(item_id, 'Unclaimed')
            
        self.connection.commit()
        print(f"Item {item_id} surrendered successfully")
        return True
    except Error as err:
        print(f"Error: '{err}'")
        return False
    

