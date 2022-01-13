from flask import Flask

app = Flask(__name__)

@app.get("/user")
def get_database():
    ...

@app.post("/user")
def post_in_database():
    ...