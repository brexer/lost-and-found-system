from src.backend.database import database

def add_person(first_name, last_name, person_contact, person_department):
    conn = database.create_connection()
    cursor = conn.cursor()
    query = """
        INSERT INTO Persons (FirstName, LastName, PhoneNumber, Department)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (first_name, last_name, person_contact, person_department))
    person_id = cursor.lastrowid
    conn.commit()
    cursor.close()
    conn.close()
    return person_id

# def add_person(person_id, first_name, last_name, person_contact, person_department, proof_id):
#         conn = database.create_connection()
#         cursor = conn.cursor()
#         query = """
#             INSERT INTO Persons (FirstName, LastName, PhoneNumber, Department, ProofID)
#             VALUES (%s, %s, %s, %s, %s)
#         """
#         cursor.execute(query, (person_id, first_name, last_name, person_contact, person_department, proof_id))
#         conn.commit()
#         cursor.close()
#         conn.close()

def update_person(person_id, first_name, last_name, person_contact, person_department, proof_id):
        conn = database.create_connection()
        cursor = conn.cursor()
        try:
                query = """
                        UPDATE Persons
                        SET FirstName = %s, LastName = %s, PhoneNumber = %s, Department = %s, ProofID = %s
                        WHERE PersonID = %s        
                """ 

                cursor.execute(query, (first_name, last_name, person_contact, person_department, proof_id, person_id))
                conn.commit()
                print("Person information updated.") # dialog

        except Exception as e:
                print("Error:", e)
                conn.rollback()

        finally:
                cursor.close()
                conn.close()

# def add_reported_item(item_category, item_name, item_description, date_lost, location_lost, person_id):
#     conn = database.create_connection()
#     cursor = conn.cursor()

#     try:
#         # Add item
#         cursor.execute("""
#             INSERT INTO Items (Category, Name, Description, Status)
#             VALUES (%s, %s, %s, 'Reported')
#         """, (item_category, item_name, item_description))
#         item_id = cursor.lastrowid

#         # Add reported item
#         cursor.execute("""
#             INSERT INTO ReportedItems (ItemID, DateLost, LocationLost, PersonID)
#             VALUES (%s, %s, %s, %s)
#         """, (item_id, date_lost, location_lost, person_id))

#         conn.commit()
#         print("Reported item added successfully.")  # Replace with dialog later
#         return item_id

#     except Exception as e:
#         print("Error:", e)
#         conn.rollback()
#         return None

#     finally:
#         cursor.close()
#         conn.close()

def add_reported_item(category, name, description, date_lost, location_lost, person_id):
    conn = database.create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO Items (Category, Name, Description, Status, ReportedBy, DateLost, LocationLost)
            VALUES (%s, %s, %s, 'Reported', %s, %s, %s)
        """, (category, name, description, person_id, date_lost, location_lost))
        item_id = cursor.lastrowid
        conn.commit()
        return item_id
    except Exception as e:
        print("Error:", e)
        conn.rollback()
        return None
    finally:
        cursor.close()
        conn.close()

# def add_reported_item(item_id, item_category, item_name, item_description, date_lost, location_lost, person_id):
#         conn = database.create_connection()
#         cursor = conn.cursor()
    
#         try:
#                 #add to item
#                 cursor.execute("""
#                         INSERT INTO Items (ItemID, Category, Name, Description, Status)
#                         VALUES (%s, %s, %s, %s, 'Reported')
#                 """, (item_id, item_category, item_name, item_description))

#                 #add to reported item
#                 cursor.execute("""
#                         INSERT INTO ReportedItems (ItemID, DateLost, LocationLost, PersonID)
#                         VALUES (%s, %s, %s, %s)
#                         """, (item_id, date_lost, location_lost, person_id))
                
#                 conn.commit()
#                 print("Reported item added successfully.") # i-change to dialog later

#         except Exception as e:
#                 print("Error:", e)
#                 conn.rollback()

#         finally:
#                 cursor.close()
#                 conn.close()

def update_reported_item(item_id, item_category, item_name, item_description, date_lost, location_lost):
        conn = database.create_connection()
        cursor = conn.cursor()

        try:
                cursor.execute("""
                        UPDATE Items
                        SET Category = %s, Name = %s, Description = %s
                        WHERE ItemID = %s
                """, (item_category, item_name, item_description, item_id))
                               
                cursor.execute("""
                        UPDATE ReportedItems
                        SET DateLost = %s, LocationLost = %s
                        WHERE ItemID = %s
                """, (date_lost, location_lost, item_id))

                conn.commit()
                print("Item has been edited successfully.") # dialog

        except Exception as e:
                print("Error:", e)
                conn.rollback()

        finally:
                cursor.close()
                conn.close()

#only admin should be able to change this
def claim_item(item_id, date_claimed, person_id):
    conn = database.create_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT Status FROM Items WHERE ItemID = %s
        """, (item_id,))
        result = cursor.fetchone()

        if not result:
            print("Error: Item not found.")
            return False

        status = result[0]
        if status == 'Claimed':
            print("Item is already claimed.")
            return False

        # Insert into ClaimedItems
        cursor.execute("""
            INSERT INTO ClaimedItems (
                ItemID, DateClaimed, PersonID
            )
            VALUES (%s, %s, %s)
        """, (item_id, date_claimed, person_id))

        # Update Items status to 'Claimed'
        cursor.execute("""
            UPDATE Items
            SET Status = 'Claimed'
            WHERE ItemID = %s
        """, (item_id,))

        conn.commit()
        print(f"Item {item_id} successfully claimed.")
        return True

    except Exception as e:
        print("Error during claiming:", e)
        conn.rollback()
        return False

    finally:
        cursor.close()
        conn.close()
        
# def claim_item(item_id, date_claimed, person_id):
#     conn = database.create_connection()
#     cursor = conn.cursor()

#     if not can_claim(item_id):
#         print("Item is already claimed.")  # dialog
#         return False

#     try:
#         # Check if item exists in ReportedItems
#         cursor.execute("""
#             SELECT 1 FROM ReportedItems WHERE ItemID = %s
#         """, (item_id,))
#         reported_exists = cursor.fetchone() is not None

#         # Check if item exists in SurrenderedItems
#         cursor.execute("""
#             SELECT 1 FROM SurrenderedItems WHERE ItemID = %s
#         """, (item_id,))
#         surrendered_exists = cursor.fetchone() is not None

#         if not reported_exists and not surrendered_exists:
#             print("Error: Item not found in reported or surrendered.")
#             return False

#         # Insert into ClaimedItems (only allowed columns)
#         cursor.execute("""
#             INSERT INTO ClaimedItems (
#                 ItemID, DateClaimed, PersonID
#             )
#             VALUES (%s, %s, %s)
#         """, (item_id, date_claimed, person_id))

#         # Update item status
#         cursor.execute("""
#             UPDATE Items
#             SET Status = 'Claimed'
#             WHERE ItemID = %s
#         """, (item_id,))

#         conn.commit()
#         print(f"Item {item_id} successfully claimed.")
#         return True

#     except Exception as e:
#         print("Error during claiming:", e)
#         conn.rollback()
#         return False

#     finally:
#         cursor.close()
#         conn.close()

# def add_surrendered_item(item_category, item_name, item_description, date_found, location_found, person_id):
#     conn = database.create_connection()
#     cursor = conn.cursor()

#     try:
#         # Add item
#         cursor.execute("""
#             INSERT INTO Items (Category, Name, Description, Status)
#             VALUES (%s, %s, %s, 'Surrendered')
#         """, (item_category, item_name, item_description))
#         item_id = cursor.lastrowid

#         # Add reported item
#         cursor.execute("""
#             INSERT INTO SurrenderedItems (ItemID, DateFound, LocationFound, PersonID)
#             VALUES (%s, %s, %s, %s)
#         """, (item_id, date_found, location_found, person_id))

#         conn.commit()
#         print("Surrendered item added successfully.")  # Replace with dialog later
#         return item_id

#     except Exception as e:
#         print("Error:", e)
#         conn.rollback()
#         return None

#     finally:
#         cursor.close()
#         conn.close()

def add_surrendered_item(category, name, description, date_found, location_found, person_id):
    conn = database.create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO Items (Category, Name, Description, Status, SurrenderedBy, DateFound, LocationFound)
            VALUES (%s, %s, %s, 'Surrendered', %s, %s, %s)
        """, (category, name, description, person_id, date_found, location_found))
        item_id = cursor.lastrowid
        conn.commit()
        return item_id
    except Exception as e:
        print("Error:", e)
        conn.rollback()
        return None
    finally:
        cursor.close()
        conn.close()

# def add_surrendered_item(item_id, item_category, item_name, item_description, date_found, location_found, person_id):
#         conn = database.create_connection()
#         cursor = conn.cursor()

#         try:
#                 cursor.execute("""
#                         INSERT INTO Items (ItemID, Category, Name, Description, Status)
#                         VALUES (%s, %s, %s, %s, 'Surrendered')
#                 """, (item_id, item_category, item_name, item_description))

#                 cursor.execute("""
#                         INSERT INTO SurrenderedItems (ItemID, DateFound, LocationFound, PersonID)
#                         VALUES (%s, %s, %s, %s)
#                 """, (item_id, date_found, location_found, person_id))

#                 conn.commit()
#                 print("Claimed item added succesfully.") # dialog

#         except Exception as e:
#                 print("Error:", e)
#                 conn.rollback()

#         finally:
#                 cursor.close()
#                 conn.close()

def update_surrendered_item(item_category, item_name, item_description, date_found, location_found, item_id):
        conn = database.create_connection()
        cursor = conn.cursor()

        try:
                cursor.execute("""
                        UPDATE Items
                        SET Category = %s, Name = %s, Description = %s
                        WHERE ItemID = %s
                """, (item_category, item_name, item_description, item_id))
                               
                cursor.execute("""
                        UPDATE SurrenderedItems
                        SET DateFound = %s, LocationFound = %s
                        WHERE ItemID = %s
                """, (date_found, location_found, item_id))

                conn.commit()
                print("Item has been updated successfully.") # dialog

        except Exception as e:
                print("Error:", e)
                conn.rollback()

        finally:
                cursor.close()
                conn.close()

# add confirmation before delete(both person and item), admin only access
def delete_person(person_id):
        conn = database.create_connection()
        cursor = conn.cursor()

        try:
                cursor.execute("""
                        DELETE FROM Persons
                        WHERE PersonID = %s
                """, (person_id))

                conn.commit()
                print("Person has been deleted successfully.") # dialo+g

        except Exception as e:
                print("Error:", e)
                conn.rollback()

        finally:
                cursor.close()
                conn.close()

def delete_item(item_id):
        conn = database.create_connection()
        cursor = conn.cursor()
        
        try:
                cursor.execute("""
                        DELETE FROM Items
                        WHERE ItemID = %s
                """, (item_id))

                conn.commit()
                print("Item has been deleted succesfully.") # dialog

        except Exception as e:
                print("Error: ", e)
                conn.rollback()

        finally:
                cursor.close()
                conn.close()

def get_all_persons(current_page, page_size, search_text=""):
    conn = database.create_connection()
    cursor = conn.cursor()

    offset = current_page * page_size
    like_pattern = f"%{search_text}%"

    query = """
        SELECT *
        FROM Persons
        WHERE
            PersonID LIKE %s OR
            FirstName LIKE %s OR
            LastName LIKE %s OR
            PhoneNumber LIKE %s OR
            Department LIKE %s
        LIMIT %s OFFSET %s
    """

    cursor.execute(query, (like_pattern,) * 5 + (page_size, offset))
    data = cursor.fetchall()

    total_records = get_total_persons(search_text)

    cursor.close()
    conn.close()
    return data, total_records

def get_total_persons(search_text=""):
    conn = database.create_connection()
    cursor = conn.cursor()

    like_pattern = f"%{search_text}%"

    query = """
        SELECT COUNT(*)
        FROM Persons
        WHERE
            PersonID LIKE %s OR
            FirstName LIKE %s OR
            LastName LIKE %s OR
            PhoneNumber LIKE %s OR
            Department LIKE %s
    """
    cursor.execute(query, (like_pattern,) * 5)
    total_records = cursor.fetchone()[0]

    cursor.close()
    conn.close()
    return total_records

# def get_all_persons():
#         conn = database.create_connection()
#         cursor = conn.cursor()

#         query = """
#                 SELECT PersonID, FirstName, LastName, PhoneNumber, Department, ProofID
#                 FROM Persons
#         """
#         cursor.execute(query)
#         list = cursor.fetchall()
#         cursor.close()
#         conn.close()
#         return list

# list of all items
def get_all_items(page=0, page_size=5):
        conn = database.create_connection()
        cursor = conn.cursor()

        offset = page * page_size
        query = """
                SELECT ItemID, Category, Name, Description, Status
                FROM Items
                LIMIT %s OFFSET %s
        """
        cursor.execute(query, (page_size, offset))
        data = cursor.fetchall()

        cursor.execute("SELECT COUNT(*) FROM Items")
        total_records = cursor.fetchone()[0]

        cursor.close()
        conn.close()
        return data, total_records
  
def get_total_items():
        conn = database.create_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(*) FROM items")
        total_records = cursor.fetchone()[0]

        cursor.close()
        conn.close()
        return total_records

def get_all_reported_items(current_page, page_size, search_text=""):
    conn = database.create_connection()
    cursor = conn.cursor(dictionary=True)

    offset = current_page * page_size
    like_pattern = f"%{search_text}%"

    query = """
        SELECT 
            i.ItemID,
            i.Category,
            i.Name,
            i.Description,
            i.Status,
            i.LocationLost,
            i.DateLost,
            CONCAT(p.FirstName, ' ', p.LastName) AS ReportedBy,
            i.ImagePath
        FROM 
            Items i
        JOIN 
            Persons p ON i.ReportedBy = p.PersonID
        WHERE 
            i.Status = 'Reported' AND (
                i.Category LIKE %s OR
                i.Name LIKE %s OR
                i.Description LIKE %s OR
                i.LocationLost LIKE %s OR
                CONCAT(p.FirstName, ' ', p.LastName) LIKE %s
            )
        ORDER BY 
            i.DateLost DESC
        LIMIT %s OFFSET %s
    """
    cursor.execute(query, (like_pattern,) * 5 + (page_size, offset))
    results = cursor.fetchall()

    total_records = get_total_reported_items(search_text)

    cursor.close()
    conn.close()

    return results, total_records


def get_total_reported_items(search_text=""):
    conn = database.create_connection()
    cursor = conn.cursor()

    like_pattern = f"%{search_text}%"

    query = """
        SELECT COUNT(*)
        FROM Items i
        JOIN Persons p ON i.ReportedBy = p.PersonID
        WHERE i.Status = 'Reported' AND (
            i.Category LIKE %s OR
            i.Name LIKE %s OR
            i.Description LIKE %s OR
            i.LocationLost LIKE %s OR
            CONCAT(p.FirstName, ' ', p.LastName) LIKE %s
        )
    """
    cursor.execute(query, (like_pattern,) * 5)
    total_records = cursor.fetchone()[0]

    cursor.close()
    conn.close()
    return total_records

def get_all_surrendered_items(current_page, page_size, search_text=""):
    conn = database.create_connection()
    cursor = conn.cursor(dictionary=True)

    offset = current_page * page_size
    like_pattern = f"%{search_text}%"

    query = """
        SELECT 
            i.ItemID,
            i.Category,
            i.Name,
            i.Description,
            i.Status,
            i.LocationFound,
            i.DateFound,
            CONCAT(p.FirstName, ' ', p.LastName) AS SurrenderedBy,
            i.ImagePath
        FROM 
            Items i
        JOIN 
            Persons p ON i.SurrenderedBy = p.PersonID
        WHERE 
            i.Status = 'Surrendered' AND (
                i.Category LIKE %s OR
                i.Name LIKE %s OR
                i.Description LIKE %s OR
                i.LocationFound LIKE %s OR
                CONCAT(p.FirstName, ' ', p.LastName) LIKE %s
            )
        ORDER BY 
            i.DateFound DESC
        LIMIT %s OFFSET %s
    """
    cursor.execute(query, (like_pattern,) * 5 + (page_size, offset))
    results = cursor.fetchall()

    total_records = get_total_surrendered_items(search_text)

    cursor.close()
    conn.close()

    return results, total_records

def get_total_surrendered_items(search_text=""):
    conn = database.create_connection()
    cursor = conn.cursor()

    like_pattern = f"%{search_text}%"

    query = """
        SELECT COUNT(*)
        FROM Items i
        JOIN Persons p ON i.SurrenderedBy = p.PersonID
        WHERE i.Status = 'Surrendered' AND (
            i.Category LIKE %s OR
            i.Name LIKE %s OR
            i.Description LIKE %s OR
            i.LocationFound LIKE %s OR
            CONCAT(p.FirstName, ' ', p.LastName) LIKE %s
        )
    """
    cursor.execute(query, (like_pattern,) * 5)
    total_records = cursor.fetchone()[0]

    cursor.close()
    conn.close()
    return total_records

def get_all_claimed_items(current_page, page_size, search_text=""):
    conn = database.create_connection()
    cursor = conn.cursor(dictionary=True)

    offset = current_page * page_size
    like_pattern = f"%{search_text}%"

    query = """
        SELECT 
            i.ItemID,
            i.Category,
            i.Name,
            i.Description,
            i.Status,
            i.LocationFound,
            i.DateFound,
            c.DateClaimed,
            CONCAT(p.FirstName, ' ', p.LastName) AS ClaimedBy,
            i.ImagePath
        FROM 
            ClaimedItems c
        JOIN 
            Items i ON c.ItemID = i.ItemID
        JOIN 
            Persons p ON c.PersonID = p.PersonID
        WHERE 
            i.Status = 'Claimed' AND (
                i.Category LIKE %s OR
                i.Name LIKE %s OR
                i.Description LIKE %s OR
                i.LocationFound LIKE %s OR
                CONCAT(p.FirstName, ' ', p.LastName) LIKE %s
            )
        ORDER BY 
            c.DateClaimed DESC
        LIMIT %s OFFSET %s
    """
    cursor.execute(query, (like_pattern, like_pattern, like_pattern, like_pattern, like_pattern, page_size, offset))
    results = cursor.fetchall()

    total_records = get_total_claimed_items(search_text)

    cursor.close()
    conn.close()

    return results, total_records


def get_total_claimed_items(search_text=""):
    conn = database.create_connection()
    cursor = conn.cursor()

    like_pattern = f"%{search_text}%"

    query = """
        SELECT COUNT(*)
        FROM ClaimedItems c
        JOIN Items i ON c.ItemID = i.ItemID
        JOIN Persons p ON c.PersonID = p.PersonID
        WHERE i.Status = 'Claimed' AND (
            i.Category LIKE %s OR
            i.Name LIKE %s OR
            i.Description LIKE %s OR
            i.LocationFound LIKE %s OR
            CONCAT(p.FirstName, ' ', p.LastName) LIKE %s
        )
    """
    cursor.execute(query, (like_pattern, like_pattern, like_pattern, like_pattern, like_pattern))
    total_records = cursor.fetchone()[0]

    cursor.close()
    conn.close()
    return total_records

# def get_all_items():
#         conn = database.create_connection()
#         cursor = conn.cursor()

#         query = """
#                 SELECT
#                 i.ItemID, i.Category, i.Name, i.Description, i.Status,
#                 COALESCE(ri.LocationLost, si.LocationFound) AS Location,
#                 COALESCE(ri.DateLost, si.DateFound, ci.DateClaimed) AS Date,
#                 CONCAT(p.FirstName, ' ', p.LastName) AS Person

#                 FROM Items i
#                 LEFT JOIN ReportedItems ri ON i.ItemID = ri.ItemID
#                 LEFT JOIN SurrenderedItems si ON i.ItemID = si.ItemID
#                 LEFT JOIN ClaimedItems ci ON i.ItemID = ci.ItemID
#                 LEFT JOIN Persons p ON p.PersonID = COALESCE(ri.PersonID, si.PersonID, ci.PersonID)
#                 ORDER BY i.ItemID
# """

#         cursor.execute(query)
#         list = cursor.fetchall()
#         cursor.close()
#         conn.close()
#         return list
def get_existing_person_id(first_name, last_name, department):
    query = """
        SELECT PersonID FROM Persons
        WHERE FirstName = %s AND LastName = %s AND Department = %s
        LIMIT 1
    """
    try:
        conn = database.create_connection()
        cursor = conn.cursor()
        cursor.execute(query, (first_name, last_name, department))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result[0] if result else None
    
    except Exception as e:
        print("Database error:", e)
        return None


def can_claim(item_id):
        conn = database.create_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT Status FROM Items WHERE ItemID = %s", (item_id,))
        result = cursor.fetchone()
        status = result[0]
        
        cursor.close()
        conn.close()
        return status != 'Claimed'

def get_item_history(item_id):
    conn = database.create_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        cursor.execute("SELECT * FROM ReportedItems WHERE ItemID = %s", (item_id,))
        reported = cursor.fetchone()

        cursor.execute("SELECT * FROM SurrenderedItems WHERE ItemID = %s", (item_id,))
        surrendered = cursor.fetchone()

        return {
            "Reported": reported,      #kani gamiton for history
            "Surrendered": surrendered #kani gamiton for history
        }

    except Exception as e:
        print("Error:", e)
        return None

    finally:
        cursor.close()
        conn.close()

def merge_items(source_item_id, target_item_id):
    conn = database.create_connection()
    cursor = conn.cursor()

    try:
        # move reporteditems to 
        cursor.execute("""
            UPDATE ReportedItems
            SET ItemID = %s
            WHERE ItemID = %s
        """, (target_item_id, source_item_id))

        # delete old item
        cursor.execute("DELETE FROM Items WHERE ItemID = %s", (source_item_id,))

        conn.commit()
        print("Items merged successfully.")
    except Exception as e:
        print("Error during merge:", e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def update_item_image_path(item_id, image_path):
    conn = database.create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE items SET ImagePath = %s WHERE ItemID = %s", (image_path, item_id))
    conn.commit()
    conn.close()

def update_person_proof_id(person_id, proof_id_path):
    conn = database.create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE Persons SET ProofID = %s WHERE PersonID = %s", (proof_id_path, person_id))
        conn.commit()
    except Exception as e:
        print("Error updating proof ID:", e)
        conn.rollback()

def clear_person_image(person_id):
    conn = database.create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE Persons SET ProofID = NULL WHERE PersonID = %s", (person_id,))
        conn.commit()
    finally:
        cursor.close()
        conn.close()