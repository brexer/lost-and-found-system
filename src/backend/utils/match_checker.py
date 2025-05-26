from src.backend.database import database

def check_reported_matches(category, date_found):
    conn = database.create_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        query = """
            SELECT * FROM Items
            WHERE Status = 'Reported'
              AND Category = %s
              AND ABS(DATEDIFF(DateLost, %s)) <= 5
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