import mysql.connector
from mysql.connector import Error

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'admin',
    'database': 'lafsystemdb',
}

def create_connection():
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def create_database():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin"
    )
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS lafsystemdb")
    print("Database created or already exists.")
    cursor.close()
    conn.close()

def create_persons_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Persons (
            PersonID VARCHAR(9) PRIMARY KEY,
            FirstName VARCHAR(50) NOT NULL,
            LastName VARCHAR(50) NOT NULL,
            PhoneNumber VARCHAR(15) NOT NULL,
            Department VARCHAR(50) NOT NULL,
            ProofID VARCHAR(255) NOT NULL
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

def create_items_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Items (
            ItemID VARCHAR(9) PRIMARY KEY,
            Category VARCHAR(50) NOT NULL,
            Name VARCHAR(50) NOT NULL,
            Description VARCHAR(255) NOT NULL,
            Status ENUM('Reported', 'Surrendered', 'Claimed') NOT NULL
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

def create_reported_items_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ReportedItems (
            ItemID VARCHAR(9) PRIMARY KEY,
            DateLost DATETIME NOT NULL,
            LocationLost VARCHAR(100) NOT NULL,
            PersonID VARCHAR(9) NOT NULL,
            FOREIGN KEY (ItemID) REFERENCES Items(ItemID),
            FOREIGN KEY (PersonID) REFERENCES Persons(PersonID)
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

def create_surrendered_items_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS SurrenderedItems (
            ItemID VARCHAR(9) PRIMARY KEY,
            DateFound DATETIME NOT NULL,
            LocationFound VARCHAR(100) NOT NULL,
            PersonID VARCHAR(9) NOT NULL,
            FOREIGN KEY (ItemID) REFERENCES Items(ItemID),
            FOREIGN KEY (PersonID) REFERENCES Persons(PersonID)
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

def create_claimed_items_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ClaimedItems (
            ItemID VARCHAR(9) PRIMARY KEY,
            DateClaimed DATETIME NOT NULL,
            PersonID VARCHAR(9) NOT NULL,
            Source ENUM('Reported', 'Surrendered') NOT NULL,
            OriginalPersonID VARCHAR(9) NOT NULL,
            OriginalDate DATETIME NOT NULL,
            OriginalLocation VARCHAR(100) NOT NULL,
            FOREIGN KEY (ItemID) REFERENCES Items(ItemID),
            FOREIGN KEY (PersonID) REFERENCES Persons(PersonID),
            FOREIGN KEY (OriginalPersonID) REFERENCES Persons(PersonID)
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

def initialize_database():
    create_database()

    global db_config
    db_config['database'] = 'lafsystemdb'
    
    create_persons_table()
    create_items_table()
    create_reported_items_table()
    create_surrendered_items_table()
    create_claimed_items_table()

