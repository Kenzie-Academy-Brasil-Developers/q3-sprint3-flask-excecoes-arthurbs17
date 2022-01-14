from http import HTTPStatus
from app.services.json_database import read_database_json, write_database_json
from app.services.user_service import check_if_email_registred, correctly_email
from app.exc.already_email import AlreadyEmail
from app.exc.invalides_informations import InvalidsInformations

class User:
    
    def __init__(self, email, nome) -> None:
        self.email: str = correctly_email(email)
        self.nome: str = nome.title()
        self.id = len(read_database_json()) + 1 

    def get_users():
        data = read_database_json()
        empty_database_return = {"data": data}
        if len(data) == 0:
            return empty_database_return
        return data
    
    def post_user(self):
        user = self.__dict__

        if check_if_email_registred(user["email"]):
            raise AlreadyEmail

        return write_database_json(user)
