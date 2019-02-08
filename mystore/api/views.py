from flask import Blueprint
from flask_restful import Api

from mystore.api.resources.user import UserResource, UserList
from mystore.api.resources.item import ItemResource, ItemList
from mystore.api.resources.track import Province, City, CityById, CityByProvince, Cost, Hello, Courier, ProvinceById
blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint)


api.add_resource(UserResource, '/users/<int:user_id>')
api.add_resource(UserList, '/users')
api.add_resource(ItemResource, '/items/<int:item_id>')
api.add_resource(ItemList, '/items')
api.add_resource(Province, '/tracking/provinces')
api.add_resource(ProvinceById, '/tracking/province/<string:province_id>')
api.add_resource(City, '/tracking/cities')
api.add_resource(CityById, '/tracking/city/<string:city_id>')
api.add_resource(CityByProvince, '/tracking/city-by-province/<string:province_id>')
api.add_resource(Cost, '/tracking/cost')
api.add_resource(Hello, '/')
api.add_resource(Courier, '/tracking/courier')