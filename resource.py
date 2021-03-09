from flask import Blueprint, jsonify, Flask
from flask_restful import Api
from model.drones import drones_all


prueba_api = Blueprint('prueba_api', __name__)




app = Flask(__name__)
app.run(port='5002')


api = Api(prueba_api)
api.add_resource(jsonify(drones_all()), '/index')


# api.add_resource(FilmResource, '/api/v1.0/films/<int:film_id>', endpoint='film_resource')