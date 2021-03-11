from model.models import Measurement, Swions
from model import db

def swions_all():

    db.Base.metadata.create_all(db.engine)
    ob = db.session.query(Measurement, Swions).join(Swions, Measurement.id_measurement == Swions.id_measurement).all()
    data = {}

    i = 0
    for obj in ob:
        data[i] = {'date': obj.Measurement.date,
                    'id_drone': obj.Measurement.id_drone,
                    'latitude': obj.Measurement.latitude,
                    'altitude': obj.Measurement.altitude,
                    'longitude': obj.Measurement.longitude,
                    'season': obj.Measurement.season,
                    'deployment': obj.Measurement.deployment,
                    'pm': obj.Swions.pm,
                    'no3_conc': obj.Swions.no3_conc,
                    'nh4_conc': obj.Swions.nh4_conc,
                    'temp': obj.Swions.temper,
                    'no3_volt': obj.Swions.no3_volt,
                    'nh4_volt': obj.Swions.nh4_volt,
                    'nivel_bateria': obj.Swions.nivel_bateria
                   }
        i += 1

    return (data)

def swions_season(season, deployment, drone_id):
    db.Base.metadata.create_all(db.engine)

    if deployment:
        if drone_id:
            ob = db.session.query(Measurement, Swions).join(Swions, Measurement.id_measurement == Swions.id_measurement).\
                filter(Measurement.season == season).filter(Measurement.deployment == deployment). \
                filter(Measurement.id_drone == drone_id)
        else:
            ob = db.session.query(Measurement, Swions).join(Swions, Measurement.id_measurement == Swions.id_measurement).\
                filter(Measurement.season == season).filter(Measurement.deployment == deployment)
    else:
        if drone_id:
            ob = db.session.query(Measurement, Swions).join(Swions, Measurement.id_measurement == Swions.id_measurement) \
                .filter(Measurement.season == season).filter(Measurement.id_drone == drone_id)
        else:
            ob = db.session.query(Measurement, Swions).join(Swions, Measurement.id_measurement == Swions.id_measurement)\
            .filter(Measurement.season == season)

    i = 0
    data = {}

    for obj in ob:
        data[i] = {'date': obj.Measurement.date,
                   'id_drone': obj.Measurement.id_drone,
                   'latitude': obj.Measurement.latitude,
                   'altitude': obj.Measurement.altitude,
                   'longitude': obj.Measurement.longitude,
                   'deployment': obj.Measurement.deployment,
                   'pm': obj.Swions.pm,
                   'no3_conc': obj.Swions.no3_conc,
                   'nh4_conc': obj.Swions.nh4_conc,
                   'temp': obj.Swions.temper,
                   'no3_volt': obj.Swions.no3_volt,
                   'nh4_volt': obj.Swions.nh4_volt,
                   'nivel_bateria': obj.Swions.nivel_bateria
                   }
        i += 1

    return (data)

def swions_droneId(drone_id, season, deployment):
    db.Base.metadata.create_all(db.engine)

    if season:
        if deployment:
            ob = db.session.query(Measurement, Swions).join(Swions, Measurement.id_measurement == Swions.id_measurement). \
                filter(Measurement.id_drone == drone_id).filter(Measurement.season == season). \
                filter(Measurement.deployment == deployment).all()
        else:
            ob = db.session.query(Measurement, Swions).join(Swions, Measurement.id_measurement == Swions.id_measurement). \
                filter(Measurement.id_drone == drone_id).filter(Measurement.season == season).all()
    else:
        if deployment:
            ob = db.session.query(Measurement, Swions).join(Swions, Measurement.id_measurement == Swions.id_measurement). \
                filter(Measurement.id_drone == drone_id).filter(Measurement.deployment == deployment).all()
        else:
            ob = db.session.query(Measurement, Swions).join(Swions, Measurement.id_measurement == Swions.id_measurement). \
                filter(Measurement.id_drone == drone_id)

    i = 0
    data = {}

    for obj in ob:
        data[i] = {'date': obj.Measurement.date,
                   'latitude': obj.Measurement.latitude,
                   'altitude': obj.Measurement.altitude,
                   'longitude': obj.Measurement.longitude,
                   'season': obj.Measurement.season,
                   'deployment': obj.Measurement.deployment,
                   'pm': obj.Swions.pm,
                   'no3_conc': obj.Swions.no3_conc,
                   'nh4_conc': obj.Swions.nh4_conc,
                   'temp': obj.Swions.temper,
                   'no3_volt': obj.Swions.no3_volt,
                   'nh4_volt': obj.Swions.nh4_volt,
                   'nivel_bateria': obj.Swions.nivel_bateria
                   }
        i += 1

    return (data)