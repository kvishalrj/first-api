import hashlib
from flask import request # type: ignore
import uuid
from db.user import UserDatabase
from flask.views import MethodView # type: ignore
from flask_smorest import Blueprint, abort # type: ignore
from schemas import UserSchema, UserQuerySchema, SuccessMessageSchema


blp = Blueprint("Users", __name__, description="Operations on users")


@blp.route("/user")
class User(MethodView):

    def __init__(self):
        self.db = UserDatabase()

    @blp.response(200, UserSchema)
    @blp.arguments(UserQuerySchema, location='query')
    def get(self, args):
        id = args.get('id')
        result = self.db.get_user(id)
        if not result:
            abort(404, message="User doesn't exists")
        return result

    @blp.arguments(UserSchema)
    @blp.response(200, SuccessMessageSchema)
    def post(self, request_data):
        username = request_data['username']
        password = hashlib.sha256(request_data['password'].encode('utf-8')).hexdigest()
        if self.db.add_user(username, password):
            return {"message" : "User added successfully"}, 201
        abort(403, message="User already exists")

    @blp.arguments(UserQuerySchema, location='query')
    @blp.response(200, SuccessMessageSchema)
    def delete(self, args):
        id = args.get('id')
        if self.db.delete_user(id):
            return {"message" : "User deleted successfully"}
        abort(404, message="User not found")

