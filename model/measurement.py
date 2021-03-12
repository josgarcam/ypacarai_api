from model.models import Measurement, Seasons
from model import db


def measurement_point_all():
    db.Base.metadata.create_all(db.engine)
    ob = db.session.query(Measurement, Seasons).join(Seasons, Measurement.id_movement == Seasons.id_movement)
    data = {}
    i = 0
    for obj in ob:
        data[i] = {'date': obj.Measurement.date,
                   'id_drone': obj.Measurement.id_drone,
                   'latitude': obj.Measurement.latitude,
                   'altitude': obj.Measurement.altitude,
                   'longitude': obj.Measurement.longitude,
                   'id_measurement': obj.Measurement.id_measurement,
                   'season': obj.Seasons.season_id,
                   'deployment': obj.Seasons.deployment_id
                   }
        i += 1

    return (data)

def measurement_point_season(season, deployment, drone_id):
    db.Base.metadata.create_all(db.engine)

    if deployment:
        if drone_id:
            ob = db.session.query(Measurement, Seasons).join(Seasons, Measurement.id_movement == Seasons.id_movement).\
                filter(Seasons.season_id == season).filter(Seasons.deployment_id == deployment).\
                filter(Measurement.id_drone == drone_id)
        else:
            ob = db.session.query(Measurement, Seasons).join(Seasons, Measurement.id_movement == Seasons.id_movement). \
                filter(Seasons.season_id == season).filter(Seasons.deployment_id == deployment)
    else:
        if drone_id:
            ob = db.session.query(Measurement, Seasons).join(Seasons, Measurement.id_movement == Seasons.id_movement). \
                filter(Seasons.season_id == season).filter(Measurement.id_drone == drone_id)
        else:
            ob = db.session.query(Measurement, Seasons).join(Seasons, Measurement.id_movement == Seasons.id_movement). \
                filter(Seasons.season_id == season)

    data = {}
    i = 0
    for obj in ob:
        data[i] = {'date': obj.Measurement.date,
                   'id_drone': obj.Measurement.id_drone,
                   'latitude': obj.Measurement.latitude,
                   'altitude': obj.Measurement.altitude,
                   'longitude': obj.Measurement.longitude,
                   'id_measurement': obj.Measurement.id_measurement,
                   'deployment': obj.Seasons.deployment_id
                   }
        i += 1
    return (data)

def measurement_point_droneId(drone_id, season, deployment):
    db.Base.metadata.create_all(db.engine)

    if season:
        if deployment:
            ob = db.session.query(Measurement, Seasons).join(Seasons, Measurement.id_movement == Seasons.id_movement). \
                filter(Seasons.season_id == season).filter(Seasons.deployment_id == deployment). \
                filter(Measurement.id_drone == drone_id)
        else:
            ob = db.session.query(Measurement, Seasons).join(Seasons, Measurement.id_movement == Seasons.id_movement). \
                filter(Seasons.season_id == season).filter(Measurement.id_drone == drone_id)
    else:
        if deployment:
           ob = db.session.query(Measurement, Seasons).join(Seasons, Measurement.id_movement == Seasons.id_movement).\
                filter(Measurement.id_drone == drone_id).filter(Seasons.deployment_id == deployment)
        else:
            ob = db.session.query(Measurement, Seasons).join(Seasons, Measurement.id_movement == Seasons.id_movement).\
                filter(Measurement.id_drone == drone_id)

    data = {}
    i = 0
    for obj in ob:
        data[i] = {'date': obj.Measurement.date,
                   'latitude': obj.Measurement.latitude,
                   'altitude': obj.Measurement.altitude,
                   'longitude': obj.Measurement.longitude,
                   'id_measurement': obj.Measurement.id_measurement,
                   'season': obj.Seasons.season_id,
                   'deployment': obj.Seasons.deployment_id
                   }
        i += 1
    return (data)
