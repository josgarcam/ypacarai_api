from model.models import Measurement
from model import db


def measurement_point_all():
    db.Base.metadata.create_all(db.engine)
    ob = db.session.query(Measurement).all()
    data = {}
    i = 0
    for obj in ob:
        data[i] = {'date': obj.date,
                   'id_drone': obj.id_drone,
                   'latitude': obj.latitude,
                   'altitude': obj.altitude,
                   'longitude': obj.longitude,
                   'id_measurement': obj.id_measurement,
                   'season': obj.season,
                   'deployment': obj.deployment
                   }
        i += 1

    return (data)

def measurement_point_season(season, deployment, drone_id):
    db.Base.metadata.create_all(db.engine)

    if deployment:
        if drone_id:
            ob = db.session.query(Measurement).filter(Measurement.season == season).filter(
                Measurement.deployment == deployment). \
                filter(Measurement.id_drone == drone_id)
        else:
            ob = db.session.query(Measurement).filter(Measurement.season == season).filter(
                Measurement.deployment == deployment)
    else:
        if drone_id:
            ob = db.session.query(Measurement).filter(Measurement.season == season).filter(Measurement.id_drone == drone_id)
        else:
            ob = db.session.query(Measurement).filter(Measurement.season == season)

    data = {}
    i = 0
    for obj in ob:
        data[i] = {'date': obj.date,
                   'id_drone': obj.id_drone,
                   'latitude': obj.latitude,
                   'altitude': obj.altitude,
                   'longitude': obj.longitude,
                   'id_measurement': obj.id_measurement,
                   'season': obj.season,
                   'deployment': obj.deployment
                   }
        i += 1
    return (data)

def measurement_point_droneId(drone_id, season, deployment):
    db.Base.metadata.create_all(db.engine)

    if season:
        if deployment:
            ob = db.session.query(Measurement). filter(Measurement.id_drone == drone_id).filter(Measurement.season == season).\
                filter(Measurement.deployment == deployment)
        else:
            ob = db.session.query(Measurement).filter(Measurement.id_drone == drone_id).filter(
                Measurement.season == season)
    else:
        if deployment:
            ob = db.session.query(Measurement).filter(Measurement.id_drone == drone_id).filter(Measurement.deployment == deployment)
        else:
            ob = db.session.query(Measurement).filter(Measurement.id_drone == drone_id)

    data = {}
    i = 0
    for obj in ob:
        data[i] = {'date': obj.date,
                   'latitude': obj.latitude,
                   'altitude': obj.altitude,
                   'longitude': obj.longitude,
                   'id_measurement': obj.id_measurement,
                   'season': obj.season,
                   'deployment': obj.deployment
                   }
        i += 1
    return (data)
