from flask import Flask, request, jsonify
from model.drones import drones_all, drones_id
from model.navegacion import navegacion_all, navegacion_drone_id_and_date
from model.water import water_place, water_drone_id_and_date, water_sw, water_sw_id_and_date, water_swions, water_swions_id_and_date, water_swxtr, water_swxtr_id_and_date
from model.air import air_place, air_place_drone_id_and_date, air_sepro, air_sepro_id_and_date
from model.measurement import measurement_point_all, measurement_point_season, measurement_point_droneId
from model.sw_sensor import sw_all, sw_season, sw_droneId
from model.swions_sensor import swions_all, swions_season, swions_droneId

from view.view import to_json

app = Flask(__name__)


#### ********* Measurement Point ******** ####

@app.route('/Measurement_points', methods=['GET'])
def measurement_point_all_controller():
    return to_json(measurement_point_all())

@app.route('/Measurement_point/Season/<int:season>', methods=['GET'])
def measurement_point_season_controller(season):
    deployment = request.args.get('deployment', '')
    id_drone = request.args.get('id_drone', '')
    return to_json(measurement_point_season(season, deployment, id_drone))

@app.route('/Measurement_point/Drone/<int:id_drone>', methods=['GET'])
def measurement_point_droneId_controller(id_drone):
    season = request.args.get('season', '')
    deployment = request.args.get('deployment', '')
    return to_json(measurement_point_droneId(id_drone,season,deployment))


##### ********* SW sensor ******** ####
@app.route('/Sw', methods=['GET'])
def sw_all_controller():
    return to_json(sw_all())

@app.route('/Sw/Season/<int:season>', methods=['GET'])
def sw_season_controller(season):
    deployment = request.args.get('deployment', '')
    id_drone = request.args.get('id_drone', '')
    return to_json(sw_season(season, deployment, id_drone))

@app.route('/Sw/Drone/<int:id_drone>', methods=['GET'])
def sw_droneId_controller(id_drone):
    season = request.args.get('season', '')
    deployment = request.args.get('deployment', '')
    return to_json(sw_droneId(id_drone, season, deployment))


##### ********* Swions sensor ******** ####
@app.route('/Swions', methods=['GET'])
def swions_all_controller():
    return to_json(swions_all())

@app.route('/Swions/Season/<int:season>', methods=['GET'])
def swions_season_controller(season):
    deployment = request.args.get('deployment', '')
    id_drone = request.args.get('id_drone', '')
    return to_json(swions_season(season, deployment, id_drone))

@app.route('/Swions/Drone/<int:id_drone>', methods=['GET'])
def swions_droneId_controller(id_drone):
    season = request.args.get('season', '')
    deployment = request.args.get('deployment', '')
    return to_json(swions_droneId(id_drone, season, deployment))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)