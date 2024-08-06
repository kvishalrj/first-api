from flask import request # type: ignore
import uuid
from db.item import ItemDatabase
from flask.views import MethodView # type: ignore
from flask_smorest import Blueprint, abort # type: ignore
from schemas import ItemSchema, ItemGetSchema, SuccessMessageSchema, ItemOptionalQuerySchema, ItemQuerySchema


blp = Blueprint("Items", __name__, description="Operations on items")


@blp.route("/item")
class Item(MethodView):

    def __init__(self):
        self.db = ItemDatabase()

    @blp.arguments(ItemOptionalQuerySchema, location='query')
    @blp.response(200, ItemGetSchema(many=True))
    def get(self, args):
        id = args.get('id')
        if not id:
            return self.db.get_items()
        else:
            result = self.db.get_item(id)
            if not result:
                abort(404, message="Given record doesn't exists")
            return result

    @blp.arguments(ItemSchema)
    @blp.response(200, SuccessMessageSchema)
    def post(self, request_data):
        id = uuid.uuid4().hex
        self.db.add_item(id, request_data)
        return {"message" : "Item added successfully"}, 201

    @blp.arguments(ItemSchema)
    @blp.arguments(ItemQuerySchema, location='query')
    @blp.response(200, SuccessMessageSchema)
    def put(self, request_data, args):
        id = args.get('id')
        if self.db.update_item(id, request_data):
            return {"message" : "Item updated successfully"}
        abort(404, message="Item not found")

    @blp.arguments(ItemQuerySchema, location='query')
    @blp.response(200, SuccessMessageSchema)
    def delete(self, args):
        id = args.get('id')
        if self.db.delete_item(id):
            return {"message" : "Item deleted successfully"}
        abort(404, message="Item not found")

