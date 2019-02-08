from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from mystore.models import Item
from mystore.extensions import ma, db
from mystore.commons.pagination import paginate


class ItemSchema(ma.ModelSchema):

    class Meta:
        model = Item
        sqla_session = db.session


class ItemResource(Resource):

    method_decorators = [jwt_required]

    @staticmethod
    def get(item_id):
        schema = ItemSchema()
        item = Item.query.get_or_404(item_id)
        return {"item": schema.dump(item).data}

    @staticmethod
    def put(item_id):
        schema = ItemSchema(partial=True)
        item = Item.query.get_or_404(item_id)
        item, errors = schema.load(request.json, instance=item)
        if errors:
            return errors, 422

        return {"msg": "item was updated ", "item": schema.dump(item).data}

    @staticmethod
    def delete(item_id):
        user = Item.query.get_or_404(item_id)
        db.session.delete(user)
        db.session.commit()
        return {"msg": "user was deleted"}


class ItemList(Resource):

    method_decorators = [jwt_required]

    @staticmethod
    def get():
        schema = ItemSchema(many=True)
        query = Item.query
        return paginate(query, schema)

    @staticmethod
    def post():
        schema = ItemSchema()
        item, errors = schema.load(request.json)

        if errors:
            return errors, 422

        user_id = get_jwt_identity()
        item.user_id = user_id
        db.session.add(item)
        db.session.commit()

        return {"msg": "item created", "item": schema.dump(item).data}, 201
