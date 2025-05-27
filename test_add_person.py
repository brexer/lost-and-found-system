from src.backend.database import dbfunctions

# Example data
person_id = "P00000001"
first_name = "John"
last_name = "Doe"
person_contact = "09123456789"
person_department = "IT"
proof_id = "ID123456"

dbfunctions.add_person(person_id, first_name, last_name, person_contact, person_department, proof_id)
print("Person added!")