from flask import Blueprint
from flask_restful import Api

from mystore.api.resources.user import UserResource, UserList
from mystore.api.resources.item import ItemResource, ItemList
from mystore.api.resources.track import Province, City, CityById, CityByProvince
blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint)


api.add_resource(UserResource, '/users/<int:user_id>')
api.add_resource(UserList, '/users')
api.add_resource(ItemResource, 'items/<int:item_id>')
api.add_resource(ItemList, '/items')
api.add_resource(Province, '/tracking/provinces')
api.add_resource(City, '/tracking/cities')
api.add_resource(CityById, '/tracking/city/<int:city_id>')
api.add_resource(CityByProvince, '/tracking/city-by-province/<int:province_id>')