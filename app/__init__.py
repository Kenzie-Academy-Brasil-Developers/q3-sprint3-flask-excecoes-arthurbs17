from flask import Flask, jsonify, request
from http import HTTPStatus
from app.exc.already_email import AlreadyEmail
from app.exc.invalides_informations import InvalidsInformations
from app.models.new_user_model import User

app = Flask(__name__)

@app.get("/user")
def get_database():
    return jsonify(User.get_users()), HTTPStatus.OK

@app.post("/user")
def post_in_database():
    try:
        user = User(**request.get_json())
        return user.post_user(), HTTPStatus.CREATED
    except InvalidsInformations:
        return {"message": "Tipos passados errados"}, HTTPStatus.BAD_REQUEST

    except AlreadyEmail:
        return {"message": "Email já cadastrado!"}, HTTPStatus.CONFLICT