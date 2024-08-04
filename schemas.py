from marshmallow import Schema, fields  # type: ignore

class ItemSchema(Schema):
    name = fields.Str(required=True)
    price = fields.Int(required=True)


class ItemGetSchema(Schema):
    id = fields.Str(dump_only=True)
    item = fields.Nested(ItemSchema)


class SuccessMessageSchema(Schema):
    message = fields.Str(dump_only=True)


class ItemQuerySchema(Schema):
    id = fields.Str(required=True)


class ItemOptionalQuerySchema(Schema):
    id = fields.Str(required=False)
