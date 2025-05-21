import database

def add_person(person_id, first_name, last_name, person_contact, person_department, proof_id):
        conn = database.get_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO Persons (PersonID, FirstName, LastName, PhoneNumber, Department, ProofID)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (person_id, first_name, last_name, person_contact, person_department, proof_id))
        conn.commit()
        cursor.close()
        conn.close()

def update_person(person_id, first_name, last_name, person_contact, person_department, proof_id):
        conn = database.get_connection()
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


def add_reported_item(item_id, item_category, item_name, item_description, date_lost, location_lost, person_id):
        conn = database.get_connection()
        cursor = conn.cursor()
    
        try:
                #add to item
                cursor.execute("""
                        INSERT INTO Items (ItemID, Category, Name, Description, Status)
                        VALUES (%s, %s, %s, %s, 'Reported')
                """, (item_id, item_category, item_name, item_description))

                #add to reported item
                cursor.execute("""
                        INSERT INTO ReportedItems (ItemID, DateLost, LocationLost, PersonID)
                        VALUES (%s, %s, %s, %s)
                        """, (item_id, date_lost, location_lost, person_id))
                
                conn.commit()
                print("Reported item added successfully.") # i-change to dialog later

        except Exception as e:
                print("Error:", e)
                conn.rollback()

        finally:
                cursor.close()
                conn.close()

def update_reported_item(item_id, item_category, item_name, item_description, date_lost, location_lost):
        conn = database.get_connection()
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
def claim_reported_item(item_id, date_claimed, person_id):
        conn = database.get_connection()
        cursor = conn.cursor()

        try:
                cursor.execute("""
                        UPDATE Items
                        SET Status = 'Claimed'
                        WHERE ItemID = %s
                """, (item_id))

                cursor.execute("""
                        INSERT INTO ClaimedItems (ItemID, DateClaimed, PersonID)
                        VALUES (%s, %s, %s)
                """, (item_id, date_claimed, person_id))

                cursor.execute("DELETE FROM ReportedItems WHERE ItemID = %s", item_id)

                conn.commit()
                print("Claimed item added succesfully.") # dialog

        except Exception as e:
                print("Error:", e)
                conn.rollback()

        finally:
                cursor.close()
                conn.close()

#only admin should be able to change this
def claim_surrendered_item(item_id, date_claimed, person_id):
        conn = database.get_connection()
        cursor = conn.cursor()

        try:
                cursor.execute("""
                        UPDATE Items
                        SET Status = 'Claimed'
                        WHERE ItemID = %s
                """, (item_id))

                cursor.execute("""
                        INSERT INTO ClaimedItems (ItemID, DateClaimed, PersonID)
                        VALUES (%s, %s, %s)
                """, (item_id, date_claimed, person_id))

                cursor.execute("DELETE FROM SurrenderedItems WHERE ItemID = %s", item_id)

                conn.commit()
                print("Claimed item added succesfully.") # dialog

        except Exception as e:
                print("Error:", e)
                conn.rollback()

        finally:
                cursor.close()
                conn.close()

def add_surrendered_item(item_id, item_category, item_name, item_description, date_found, location_found, person_id):
        conn = database.get_connection()
        cursor = conn.cursor()

        try:
                cursor.execute("""
                        INSERT INTO Items (ItemID, Category, Name, Description, Status)
                        VALUES (%s, %s, %s, %s, 'Surrendered')
                """, (item_id, item_category, item_name, item_description))

                cursor.execute("""
                        INSERT INTO SurrenderedItems (ItemID, DateFound, LocationFound, PersonID)
                        VALUES (%s, %s, %s, %s)
                """, (item_id, date_found, location_found, person_id))

                conn.commit()
                print("Claimed item added succesfully.") # dialog

        except Exception as e:
                print("Error:", e)
                conn.rollback()

        finally:
                cursor.close()
                conn.close()

def update_surrendered_item(item_category, item_name, item_description, date_found, location_found, item_id):
        conn = database.get_connection()
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
        conn = database.get_connection()
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
        conn = database.get_connection()
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

# list of all items
def get_all_items():
        conn = database.get_connection()
        cursor = conn.cursor()

        query = """
                SELECT
                i.ItemID, i.Category, i.Name, i.Description, i.Status,
                COALESCE(ri.LocationLost, si.LocationFound) AS Location,
                COALESCE(ri.DateLost, si.DateFound, ci.DateClaimed) AS Date,
                CONCAT(p.FirstName, ' ', p.LastName) AS Person

                FROM Items i
                LEFT JOIN ReportedItems ri ON i.ItemID = ri.ItemID
                LEFT JOIN SurrenderedItems si ON i.ItemID = si.ItemID
                LEFT JOIN ClaimedItems ci ON i.ItemID = ci.ItemID
                LEFT JOIN Persons p ON p.PersonID = COALESCE(ri.PersonID, si.PersonID, ci.PersonID)
                ORDER BY i.ItemID
"""

        cursor.execute(query)
        list = cursor.fetchall()
        cursor.close()
        conn.close()
        return list