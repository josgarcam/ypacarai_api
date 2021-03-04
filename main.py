from flask import Flask, request, jsonify
from models import Water, Drones
import db
from drones import drones_all, drones_id
from navegacion import navegacion_all, navegacion_drone_id_and_date
from water import water_place, water_drone_id_and_date, water_sw, water_sw_id_and_date, water_swions, water_swions_id_and_date, water_swxtr, water_swxtr_id_and_date
from air import air_place, air_place_drone_id_and_date, air_sepro, air_sepro_id_and_date

app = Flask(__name__)

#### ********* Water place ******** ####

@app.route('/Water/measurement_place', methods=['GET'])
def water_measurement_place():
    return jsonify(water_place())

# Ejemplo de uso
@app.route('/Water/measurement_place/<int:drone_id>', methods=['GET'])
def water_filter_by_drone_id_and_date(drone_id):
    sdate = request.args.get('sdate','')
    edate = request.args.get('edate','')

    # Los valores esperados para sdate y edate son %m-%d-%y. P.ej: 02-09-21
    return jsonify(water_drone_id_and_date(drone_id, sdate, edate))

#### ********* Water SW ******** ####

@app.route('/Water/sw', methods=['GET'])
def water_measurement_sw():
    return jsonify(water_sw())

@app.route('/Water/sw/<int:drone_id>', methods=['GET'])
def water_measurement_sw_filter_by_drone_id_and_date(drone_id):
    sdate = request.args.get('sdate', '')
    edate = request.args.get('edate', '')
    return jsonify(water_sw_id_and_date(drone_id, sdate, edate))

#### ********* Water SWIONS ******** ####

@app.route('/Water/swions', methods=['GET'])
def water_measurement_swions():
    return jsonify(water_swions())

@app.route('/Water/swions/<int:drone_id>', methods=['GET'])
def water_measurement_swions_filter_by_drone_id_and_date(drone_id):
    sdate = request.args.get('sdate', '')
    edate = request.args.get('edate', '')
    return jsonify(water_swions_id_and_date(drone_id, sdate, edate))

#### ********* Water SWXTR ******** ####

@app.route('/Water/swxtr', methods=['GET'])
def water_measurement_swxtr():
    return jsonify(water_swxtr())

@app.route('/Water/swxtr/<int:drone_id>', methods=['GET'])
def water_measurement_swxtr_filter_by_drone_id_and_date(drone_id):
    sdate = request.args.get('sdate', '')
    edate = request.args.get('edate', '')
    return jsonify(water_swxtr_id_and_date(drone_id, sdate, edate))




#### ********* Drones ******** ####

@app.route('/Drones/', methods=['GET'])
def drones():
    return jsonify(drones_all())

@app.route('/Drones/<int:id>')
def drones_filter_id(id):
    return jsonify(drones_id(id))



#### ********* Navegacion ******** ####

@app.route('/Navegacion/', methods=['GET'])
def navegacion():
    return jsonify(navegacion_all())

@app.route('/Navegacion/<int:drone_id>', methods=['GET'])
def navegacion_filter_by_drone_id_and_date(drone_id):
    sdate = request.args.get('sdate','')
    edate = request.args.get('edate','')

    # Los valores esperados para sdate y edate son %m-%d-%y. P.ej: 02-09-21
    return jsonify(navegacion_drone_id_and_date(drone_id, sdate, edate))


#### ********* Air place ******** ####

@app.route('/Air/measurement_place', methods=['GET'])
def air_measurement_place():
    return jsonify(air_place())

# Ejemplo de uso
@app.route('/Air/measurement_place/<int:drone_id>', methods=['GET'])
def air_filter_by_drone_id_and_date(drone_id):
    sdate = request.args.get('sdate','')
    edate = request.args.get('edate','')

    # Los valores esperados para sdate y edate son %m-%d-%y. P.ej: 02-09-21
    return jsonify(air_place_drone_id_and_date(drone_id, sdate, edate))

#### ********* Air SEPRO ******** ####

@app.route('/Air/sepro', methods=['GET'])
def air_measurement_sepro():
    return jsonify(air_sepro())

@app.route('/Air/sepro/<int:drone_id>', methods=['GET'])
def air_measurement_sepro_filter_by_drone_id_and_date(drone_id):
    sdate = request.args.get('sdate', '')
    edate = request.args.get('edate', '')
    return jsonify(air_sepro_id_and_date(drone_id, sdate, edate))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)