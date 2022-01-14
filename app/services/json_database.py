import os
from json import JSONDecodeError, dump, load
from dotenv import load_dotenv
from itsdangerous import json

load_dotenv()
filename = os.environ['DATABASE_FILENAME']

def read_database_json():
    try:
        with open(filename + 'database.json', "r") as json_database:
            return load(json_database)
    except (FileNotFoundError, JSONDecodeError):
        os.makedirs(filename, exist_ok=True)
        with open(filename  + 'database.json', "w") as json_database:
            dump([], json_database)
            return []

def write_database_json(new_user: dict):
    database_list = read_database_json()
    database_list.append(new_user)
    with open(filename + "database.json", "w") as json_database:
        dump(database_list, json_database, indent=2)
    
    return new_user
