from datetime import datetime
from models import Air
import db

def air_place():

    db.Base.metadata.create_all(db.engine)
    ob = db.session.query(Air).all()
    data = {}
    i = 0
    for obj in ob:
        data[i] = {'drone_id': obj.par_aire_cod_drones,
                    'date': obj.par_aire_fecha_hora,
                    'latitude': obj.par_aire_sepro_lat,
                    'longitude': obj.par_aire_sepro_log,
                    'altitude': obj.par_aire_sepro_alt
                   }

        i += 1

    return (data)

def air_place_drone_id_and_date(drone_id, sdate, edate):

    if sdate and edate:
        ob = db.session.query(Air).filter(Air.par_aire_cod_drones == drone_id).\
                filter(Air.par_aire_fecha_hora >= datetime.strptime(sdate, '%m-%d-%y')).\
            filter(Air.par_aire_fecha_hora <= datetime.strptime(edate, '%m-%d-%y'))\
            .order_by(Air.par_aire_fecha_hora.asc())

    else:
        ob = db.session.query(Air).filter_by(par_aire_cod_drones=drone_id)

    data = {}
    i = 0
    for obj in ob:
        data[i] = {'date': obj.par_aire_fecha_hora,
                   'latitude': obj.par_aire_sepro_lat,
                   'longitude': obj.par_aire_sepro_log,
                   'altitude': obj.par_aire_sepro_alt
                   }

        i += 1

    return(data)



######## SEPRO SENSOR ########

def air_sepro():

    db.Base.metadata.create_all(db.engine)
    ob = db.session.query(Air).all()
    data = {}
    i = 0
    for obj in ob:
        data[i] = {'drone_id': obj.par_aire_cod_drones,
                    'date': obj.par_aire_fecha_hora,
                   'sepro_pm': obj.par_aire_sepro_pm,
                    'sepro_c02': obj.par_aire_sepro_c02,
                    'sepro_h2s': obj.par_aire_sepro_h2s,
                    'sepro_o3': obj.par_aire_sepro_o3,
                    'sepro_hr': obj.par_aire_sepro_hr,
                    'sepro_pres': obj.par_aire_sepro_pres,
                    'sepro_temp': obj.par_aire_sepro_temp
                   }

        i += 1

    return (data)

def air_sepro_id_and_date(drone_id, sdate, edate):

    if sdate and edate:
        ob = db.session.query(Air).filter(Air.par_aire_cod_drones == drone_id).\
                filter(Air.par_aire_fecha_hora >= datetime.strptime(sdate, '%m-%d-%y')).\
            filter(Air.par_aire_fecha_hora <= datetime.strptime(edate, '%m-%d-%y'))\
            .order_by(Air.par_aire_fecha_hora.asc())

    else:
        ob = db.session.query(Air).filter_by(par_aire_cod_drones=drone_id)

    data = {}
    i = 0
    for obj in ob:
        data[i] = {'date': obj.par_aire_fecha_hora,
                   'sepro_pm': obj.par_aire_sepro_pm,
                   'sepro_c02': obj.par_aire_sepro_c02,
                   'sepro_h2s': obj.par_aire_sepro_h2s,
                   'sepro_o3': obj.par_aire_sepro_o3,
                   'sepro_hr': obj.par_aire_sepro_hr,
                   'sepro_pres': obj.par_aire_sepro_pres,
                   'sepro_temp': obj.par_aire_sepro_temp
                   }

        i += 1

    return (data)