from app.services.json_database import read_database_json

def check_if_email_registred(email:str) -> bool:
    users_list = read_database_json()
    for user in users_list:
        if user["email"] == email:
            return True
    
    return False