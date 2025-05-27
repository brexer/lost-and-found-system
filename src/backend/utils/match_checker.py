from src.backend.database import database

def check_reported_matches(category, date_found):
    conn = database.create_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        query = """
            SELECT 
                i.ItemID, i.Name, i.Category, i.DateLost, i.LocationLost,
                CONCAT(p.FirstName, ' ', p.LastName) AS ReportedBy
            FROM Items i
            JOIN Persons p ON i.ReportedBy = p.PersonID
            WHERE i.Status = 'Reported'
            AND i.Category = %s
            AND ABS(DATEDIFF(i.DateLost, %s)) <= 5
        """

        cursor.execute(query, (category, date_found))
        matches = cursor.fetchall()
        return matches

    except Exception as e:
        print("Match check error:", e)
        return []

    finally:
        cursor.close()
        conn.close()