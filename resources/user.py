import pymysql
from flask_restful import Resource,reqparse
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username')
    parser.add_argument('password')

    def post(self):
        data = UserRegister.parser.parse_args()

        duplicate_user = UserModel.find_by_username(data['username'])
        if duplicate_user:
            return {"message":"User already exists"},400

        user = UserModel(**data)
        user.save_to_db()

        return {"message":"User registered successfully"},201