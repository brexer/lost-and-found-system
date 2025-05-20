from database import database

def add_person(person_id, first_name, last_name, person_contact, person_department, proof_id):
        conn = dbfunctions.get_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO Persons (PersonID, FirstName, LastName, PhoneNumber, Department, ProofID)
            VALUES (%s, %s, %s, %s, %s, %s)
    """
        cursor.execute(query, (person_id, first_name, last_name, person_contact, person_department, proof_id))
        conn.commit()
        cursor.close()
        conn.close()

def add_reported_item(item_id, item_category, item_name, item_description, item_status, date_lost, location_lost, person_id):
        conn = conn
        cursor = conn.cursor()
    
        try:
                #add to item
                cursor.execute("""
                        INSERT INTO Items (ItemID, Category, Name, Description, Status)
                        VALUES (%s, %s, %s, %s, 'Reported')
                """, (item_id, item_category, item_name, item_description, item_status))

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

def add_claimed_item(item_id, item_category, item_name, item_description, item_status, date_claimed, person_id):
        conn = conn
        cursor = conn.cursor()

        try:
                cursor.execute("""
                        INSERT INTO Items (ItemID, Category, Name, Description, Status)
                        VALUES (%s, %s, %s, %s, 'Claimed')
                """, (item_id, item_category, item_name, item_description))

                cursor.execute("""
                        INSERT INTO ClaimedItems (ItemID, DateClaimed, PersonID)
                        VALUES (%s, %s, %s)
                """, (item_id, date_claimed, person_id))

                conn.commit()
                print("Claimed item added succesfully.") # dialog

        except Exception as e:
                print("Error:", e)
                conn.rollback()

        finally:
                cursor.close()
                conn.close()

def add_surrendered_item(item_id, item)
    