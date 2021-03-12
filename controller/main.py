from flask import Flask, request
from model.navegacion import navegacion_all, navegacion_drone_id_and_date
from model.drones import drones_all, drones_id
from model.measurement import measurement_point_all, measurement_point_season, measurement_point_droneId
from model.seasons import seasons_all, seasons_season
from model.sepro_sensor import sepro_all, sepro_season, sepro_droneId
from model.sw_sensor import sw_all, sw_season, sw_droneId
from model.swions_sensor import swions_all, swions_season, swions_droneId
from model.swxtr_sensor import swxtr_all, swxtr_season, swxtr_droneId
from view.view import to_json

app = Flask(__name__)

#### ********* Navegacion ******** ####
@app.route('/Navegacion/', methods=['GET'])
def navegacion():
    return to_json(navegacion_all())

@app.route('/Navegacion/Drone/<int:drone_id>', methods=['GET'])
def navegacion_filter_by_drone_id_and_date(drone_id):
    sdate = request.args.get('sdate','')
    edate = request.args.get('edate','')
    return to_json(navegacion_drone_id_and_date(drone_id, sdate, edate))

#### ********* Drones ******** ####

@app.route('/Drones/', methods=['GET'])
def drones():
    return to_json(drones_all())

@app.route('/Drones/<int:id>')
def drones_filter_id(id):
    return to_json(drones_id(id))

#### ********* Measurement Point ******** ####

@app.route('/Measurement_points', methods=['GET'])
def measurement_point_all_controller():
    return to_json(measurement_point_all())

@app.route('/Measurement_points/Season/<int:season>', methods=['GET'])
def measurement_point_season_controller(season):
    deployment = request.args.get('deployment', '')
    id_drone = request.args.get('id_drone', '')
    return to_json(measurement_point_season(season, deployment, id_drone))

@app.route('/Measurement_points/Drone/<int:id_drone>', methods=['GET'])
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


##### ********* Swxtr sensor ******** ####
@app.route('/Swxtr', methods=['GET'])
def swxtr_all_controller():
    return to_json(swxtr_all())

@app.route('/Swxtr/Season/<int:season>', methods=['GET'])
def swxtr_season_controller(season):
    deployment = request.args.get('deployment', '')
    id_drone = request.args.get('id_drone', '')
    return to_json(swxtr_season(season, deployment, id_drone))

@app.route('/Swxtr/Drone/<int:id_drone>', methods=['GET'])
def swxtr_droneId_controller(id_drone):
    season = request.args.get('season', '')
    deployment = request.args.get('deployment', '')
    return to_json(swxtr_droneId(id_drone, season, deployment))


##### ********* Sepro sensor ******** ####
@app.route('/Sepro', methods=['GET'])
def sepro_all_controller():
    return to_json(sepro_all())

@app.route('/Sepro/Season/<int:season>', methods=['GET'])
def sepro_season_controller(season):
    deployment = request.args.get('deployment', '')
    id_drone = request.args.get('id_drone', '')
    return to_json(sepro_season(season, deployment, id_drone))

@app.route('/Sepro/Drone/<int:id_drone>', methods=['GET'])
def sepro_droneId_controller(id_drone):
    season = request.args.get('season', '')
    deployment = request.args.get('deployment', '')
    return to_json(sepro_droneId(id_drone, season, deployment))

##### ********* Seasons ******** ####
@app.route('/Seasons', methods=['GET'])
def seasons_all_controller():
    return to_json(seasons_all())

@app.route('/Seasons/<int:id_season>', methods=['GET'])
def seasons_season_all_controller(id_season):
    mission_id = request.args.get('mission_id', '')
    deployment = request.args.get('deployment', '')
    return to_json(seasons_season(id_season, deployment, mission_id))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)