from http import HTTPStatus
from mailbox import NotEmptyError
from app.services.json_database import read_database_json, write_database_json
import io

class User:
    
    def __init__(self, email, nome) -> None:
        self.email: str = email.lower()
        self.nome: str = nome.title()
        self.id = len(read_database_json()) + 1 

    def get_users():
        try:
            data = read_database_json()
            if data == []:
                return {"data": data}
            return data
        except io.UnsupportedOperation:
            return read_database_json()
    
    def post_user(self):
        user = self.__dict__

        try:
            return write_database_json(user)
        except (io.UnsupportedOperation, TypeError):
            return write_database_json(user)
