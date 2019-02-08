from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from mystore.models import User
from mystore.extensions import ma, db
from mystore.commons.pagination import paginate


class UserSchema(ma.ModelSchema):

    password = ma.String(load_only=True, required=True)

    class Meta:
        model = User
        sqla_session = db.session


class UserResource(Resource):
    """Single object resource
    """
    method_decorators = [jwt_required]

    @staticmethod
    def get(user_id):
        schema = UserSchema()
        user = User.query.get_or_404(user_id)
        return {"user": schema.dump(user).data}

    @staticmethod
    def put(user_id):
        schema = UserSchema(partial=True)
        user = User.query.get_or_404(user_id)
        user, errors = schema.load(request.json, instance=user)
        if errors:
            return errors, 422

        return {"msg": "user updated", "user": schema.dump(user).data}

    @staticmethod
    def delete(user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()

        return {"msg": "user deleted"}


class UserList(Resource):
    """Creation and get_all
    """
    method_decorators = [jwt_required]

    @staticmethod
    def get():
        schema = UserSchema(many=True)
        query = User.query
        return paginate(query, schema)

    @staticmethod
    def post():
        schema = UserSchema()
        user, errors = schema.load(request.json)
        if errors:
            return errors, 422

        db.session.add(user)
        db.session.commit()

        return {"msg": "user created", "user": schema.dump(user).data}, 201
