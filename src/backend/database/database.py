import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
load_dotenv()
import os

db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME')
}

def create_connection():
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def create_database():
    conn = create_connection()
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
            PersonID INT(8) UNSIGNED NOT NULL AUTO_INCREMENT,
            FirstName VARCHAR(50) NOT NULL,
            LastName VARCHAR(50) NOT NULL,
            PhoneNumber VARCHAR(15) NOT NULL,
            Department VARCHAR(50) NOT NULL,
            ProofID VARCHAR(255),
            IsDeleted BOOLEAN DEFAULT FALSE,
            PRIMARY KEY (PersonID)
        );
    """)
    conn.commit()
    cursor.close()
    conn.close()

def create_items_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Items (
            ItemID INT(8) UNSIGNED NOT NULL AUTO_INCREMENT,
            Category VARCHAR(50) NOT NULL,
            Name VARCHAR(50) NOT NULL,
            Description VARCHAR(255) NOT NULL,
            Status ENUM('Reported', 'Surrendered', 'Claimed') NOT NULL,
            ImagePath VARCHAR(255),
            ReportedBy INT(8) UNSIGNED,
            DateLost DATETIME,
            LocationLost VARCHAR(100),
            SurrenderedBy INT(8) UNSIGNED,
            DateFound DATETIME,
            LocationFound VARCHAR(100),
            IsDeleted BOOLEAN DEFAULT FALSE,
            PRIMARY KEY (ItemID),
            FOREIGN KEY (ReportedBy) REFERENCES Persons(PersonID),
            FOREIGN KEY (SurrenderedBy) REFERENCES Persons(PersonID)
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

#def create_surrendered_items_table():
#    conn = create_connection()
#    cursor = conn.cursor()
#    cursor.execute("""
#        CREATE TABLE IF NOT EXISTS SurrenderedItems (
#            ItemID INT(8) UNSIGNED NOT NULL,
#            DateFound DATETIME NOT NULL,
#            LocationFound VARCHAR(50) NOT NULL,
#            PersonID INT(8) UNSIGNED NOT NULL,
#            PRIMARY KEY (ItemID),
#            FOREIGN KEY (ItemID) REFERENCES Items(ItemID),
#            FOREIGN KEY (PersonID) REFERENCES Persons(PersonID)
#        )
#    """)
#    conn.commit()
#    cursor.close()
#    conn.close()

#def create_reported_items_table():
#    conn = create_connection()
#    cursor = conn.cursor()
#    cursor.execute("""
#        CREATE TABLE IF NOT EXISTS ReportedItems (
#            ItemID INT(8) UNSIGNED NOT NULL,
#            DateLost DATETIME NOT NULL,
#            LocationLost VARCHAR(50) NOT NULL,
#            PersonID INT(8) UNSIGNED NOT NULL,
#            PRIMARY KEY (ItemID),
#            FOREIGN KEY (ItemID) REFERENCES Items(ItemID),
#            FOREIGN KEY (PersonID) REFERENCES Persons(PersonID)
#        )
#    """)
#    conn.commit()
#    cursor.close()
#    conn.close()

def create_claimed_items_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ClaimedItems (
            ItemID INT(8) UNSIGNED NOT NULL,
            DateClaimed DATETIME NOT NULL,
            PersonID INT(8) UNSIGNED NOT NULL,
            PRIMARY KEY (ItemID),
            FOREIGN KEY (ItemID) REFERENCES Items(ItemID),
            FOREIGN KEY (PersonID) REFERENCES Persons(PersonID)
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
    create_claimed_items_table()

