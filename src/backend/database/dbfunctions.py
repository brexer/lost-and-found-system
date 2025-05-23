import database

def add_person(person_id, first_name, last_name, person_contact, person_department, proof_id):
        conn = database.create_connection()
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


def add_reported_item(item_id, item_category, item_name, item_description, date_lost, location_lost, person_id):
        conn = database.create_connection()
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

    if not can_claim(item_id):
        print("Item is already claimed.")  # dialog
        return False

    try:
        # get orig info from reported/surrendered items
        cursor.execute("""
            SELECT PersonID, DateLost, LocationLost
            FROM ReportedItems
            WHERE ItemID = %s
        """, (item_id,))
        reported = cursor.fetchone()

        if reported:
            source = "Reported"
            original_person_id, original_date, original_location = reported
        else:
            cursor.execute("""
                SELECT PersonID, DateFound, LocationFound
                FROM SurrenderedItems
                WHERE ItemID = %s
            """, (item_id,))
            surrendered = cursor.fetchone()

            if not surrendered:
                print("Error: Item not found in reported or surrendered.")
                return False

            source = "Surrendered"
            original_person_id, original_date, original_location = surrendered

        cursor.execute("""
            INSERT INTO ClaimedItems (
                ItemID, DateClaimed, PersonID,
                Source, OriginalPersonID, OriginalDate, OriginalLocation
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            item_id, date_claimed, person_id,
            source, original_person_id, original_date, original_location
        ))

        # Update status
        cursor.execute("""
            UPDATE Items
            SET Status = 'Claimed'
            WHERE ItemID = %s
        """, (item_id,))


        conn.commit()
        print(f"Item {item_id} successfully claimed from {source}.")
        return True

    except Exception as e:
        print("Error during claiming:", e)
        conn.rollback()
        return False

    finally:
        cursor.close()
        conn.close()

def add_surrendered_item(item_id, item_category, item_name, item_description, date_found, location_found, person_id):
        conn = database.create_connection()
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

def get_all_persons():
        conn = database.create_connection()
        cursor = conn.cursor()

        query = """
                SELECT PersonID, FirstName, LastName, PhoneNumber, Department, ProofID
                FROM Persons
"""
        cursor.execute(query)
        list = cursor.fetchall()
        cursor.close()
        conn.close()
        return list

# list of all items
def get_all_items():
        conn = database.create_connection()
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
