from flask import Flask
from flask_restful import Resource, Api
import json
from pymongo import MongoClient
from bson.json_util import dumps, loads
from bson.objectid import ObjectId
from flask import request

app = Flask(__name__)
api = Api(app)

class Home(Resource):
     def get(self):
          return [
            {'URL': 'http://127.0.0.1:5000/getProducts', 'Description': 'Gets all the products'},
            {'URL': 'http://127.0.0.1:5000/getTitles', 'Description': 'Gets all the titles'},
            {'URL': 'http://127.0.0.1:5000/insertProducts', 'Description': 'Inserts data to the database'},
        ]
api.add_resource(Home, '/')     

API_KEY = "login"
# make the class
class InsertProducts(Resource):
        def get(self):
                api_key = request.args.get('api_key')
                if api_key != API_KEY:
                        return {"error": "Invalid API key. Authentication failed."}, 401

                client = MongoClient("mongodb://root:example@localhost:27017/")
                db = client.products
                collection = db.products_data
                # Record to be inserted
                newRecord= {"productId": 1, "title": "apple", "cost": 2.99}
                newRecord2= {"productId": 2, "title": "banana", "cost": 1.99}
                newRecord3= {"productId": 3, "title": "pear", "cost": 2.50}
                newRecord4= {"productId": 4, "title": "kiwi", "cost": 1.25}

                # find it
                res = collection.insert_one(newRecord)
                res = collection.insert_one(newRecord2)
                res = collection.insert_one(newRecord3)
                res = collection.insert_one(newRecord4)
                #return
                return {"status":"inserted"}
api.add_resource(InsertProducts, '/insertProducts')


# make the class
class GetProducts(Resource):
    def get(self):
        client = MongoClient("mongodb://root:example@localhost:27017/")
        db = client.products
        collection = db.products_data

        results = dumps(collection.find())
        return json.loads(results)
api.add_resource(GetProducts, '/getProducts')

# make the class
class GetTitles(Resource):
    def get(self):
        client = MongoClient("mongodb://root:example@localhost:27017/")
        db = client.products
        collection = db.products_data
# ID of the object
        filter = {"_id": 0, "title": 1}
# find it
        results = collection.find({}, filter)
        print(results)
# dump to JSON
        results = dumps(results)
#return
        return json.loads(results)
api.add_resource(GetTitles, '/getTitles')

if __name__ == '__main__':
    app.run(debug=True)
