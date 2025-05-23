from src.backend.database import dbfunctions

def report_item(data):
    dbfunctions.add_reported_item(
        data["item_id"], data["category"], data["name"],
        data["description"], data["date_lost"], data["location_lost"],
        data["person_id"]
    )

def surrender_item(data):
    dbfunctions.add_surrendered_item(
        data["item_id"], data["category"], data["name"],
        data["description"], data["date_found"], data["location_found"],
        data["person_id"]
    )

def claim_item(item_id, person_id, date_claimed):
    if not dbfunctions.can_claim(item_id):
        return False
    dbfunctions.claim_item(item_id, date_claimed, person_id)
    return True