from flask import request
import requests
from flask_restful import Resource
from mystore.models import Item
import math


class APIParent:
    def __init__(self):
        pass

    type = "starter"
    key = "182561962cf94cd52a5a013a6cc058fa"
    url = 'https://api.rajaongkir.com/' + type + '/'
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8', 'key': key}
    failed = {"msg": "service currently not available"}


class Hello(Resource):
    @staticmethod
    def get():
        return {"msg": "Welcome to Store App"}


class Province(Resource):
    @staticmethod
    def get():
        api = APIParent()
        url = api.url + 'province'
        try:
            r = requests.get(url, headers=api.headers)
            return r.json()
        except requests.exceptions.RequestException as e:
            return e


class ProvinceById(Resource):
    @staticmethod
    def get(province_id):
        api = APIParent()
        url = api.url + 'province?id=' + province_id
        try:
            r = requests.get(url, headers=api.headers)
            return r.json()
        except requests.exceptions.RequestException as e:
            return e


class City(Resource):
    @staticmethod
    def get():
        api = APIParent()
        url = api.url + 'city'
        try:
            r = requests.get(url, headers=api.headers)
            return r.json()
        except requests.exceptions.RequestException as e:
            return e


class CityById(Resource):
    @staticmethod
    def get(city_id):
        api = APIParent()
        url = api.url + 'city?id=' + city_id
        try:
            r = requests.get(url, headers=api.headers)
            return r.json()
        except requests.exceptions.RequestException as e:
            return e


class CityByProvince(Resource):
    @staticmethod
    def get(province_id):
        api = APIParent()
        url = api.url + 'city?province=' + province_id
        try:
            r = requests.get(url, headers=api.headers)
            return r.json()
        except requests.exceptions.RequestException as e:
            return e


class Cost(Resource):
    @staticmethod
    def post():
        data = request.json
        api = APIParent()
        url = api.url + 'cost'
        item_id = int(data['item_id'])
        item = Item.query.get_or_404(item_id)
        weight = str(math.ceil(item.weight))
        payload = "origin="+data['city_from']+"&destination="+data['city_from']+"&weight="+weight+"&courier="\
                  + data['courier']
        try:
            r = requests.post(url,  data=payload, headers={'content-type': 'application/x-www-form-urlencoded',
                                                           'key': api.key})
            return r.json()
        except requests.exceptions.RequestException as e:
            return e


class Courier(Resource):
    @staticmethod
    def get():
        data = {"courier1": "pos", "courier2": "tiki", "courier3": "jne"}
        return data
