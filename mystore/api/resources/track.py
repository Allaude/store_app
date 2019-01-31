from flask import request
import requests
from flask_restful import Resource


class APIParent():
    type = "starter"
    key = "182561962cf94cd52a5a013a6cc058fa"
    url = 'https://api.rajaongkir.com/' + type + '/'
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8', 'key': key}
    failed = {"msg": "service currently not available"}


class Hello(Resource):
    def get(self):
        return {"msg": "Welcome to Store App"}


class Province(Resource):
    def get(self):
        api = APIParent()
        url = api.url + 'province'
        try:
            r = requests.get(url, headers=api.headers)
            return r.json()
        except requests.exceptions.RequestException as e:
            return e


class City(Resource):
    def get(self):
        api = APIParent()
        url = api.url + 'city'
        try:
            r = requests.get(url, headers=api.headers)
            return r.json()
        except requests.exceptions.RequestException as e:
            return e


class CityById(Resource):
    def get(self, city_id):
        api = APIParent()
        url = api.url + 'city?id=' + city_id
        try:
            r = requests.get(url, headers=api.headers)
            return r.json()
        except requests.exceptions.RequestException as e:
            return e


class CityByProvince(Resource):
    def get(self, province_id):
        api = APIParent()
        url = api.url + 'city?province=' + province_id
        try:
            r = requests.get(url, headers=api.headers)
            return r.json()
        except requests.exceptions.RequestException as e:
            return e


class Cost(Resource):
    def post(self):
        data = request.json
        api = APIParent()
        url = api.url + 'cost'
        payload = "origin="+data['city_from']+"&destination="+data['city_from']+"&weight="+data['city_from']+"&courier="+data['courier']
        try:
            r = requests.post(url,  data=payload, headers={'content-type': 'application/x-www-form-urlencoded', 'key': api.key})
            return r.json()
        except requests.exceptions.RequestException as e:
            return e


class Courier(Resource):
    def get(self):
        data = {"courier1": "pos", "courier2": "tiki", "courier3": "jne"}
        return data
