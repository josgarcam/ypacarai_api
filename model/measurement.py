from model.models import Measurement, Seasons
from model import db


def measurement_point_all():
    db.Base.metadata.create_all(db.engine)
    ob = db.session.query(Measurement, Seasons).join(Seasons, Measurement.mea_id_movement == Seasons.sea_id_movement)
    data = {}
    i = 0
    for obj in ob:
        data[i] = {'date': obj.Measurement.mea_date,
                   'id_drone': obj.Measurement.mea_id_drone,
                   'latitude': obj.Measurement.mea_latitude,
                   'altitude': obj.Measurement.mea_altitude,
                   'longitude': obj.Measurement.mea_longitude,
                   'id_measurement': obj.Measurement.mea_id_measurement,
                   'season': obj.Seasons.sea_season_id,
                   'deployment': obj.Seasons.sea_deployment_id
                   }
        i += 1

    return (data)

def measurement_point_season(season, deployment, drone_id):
    db.Base.metadata.create_all(db.engine)

    if deployment:
        if drone_id:
            ob = db.session.query(Measurement, Seasons).join(Seasons, Measurement.mea_id_movement == Seasons.sea_id_movement).\
                filter(Seasons.sea_season_id == season).filter(Seasons.sea_deployment_id == deployment).\
                filter(Measurement.mea_id_drone == drone_id)
        else:
            ob = db.session.query(Measurement, Seasons).join(Seasons, Measurement.mea_id_movement == Seasons.sea_id_movement). \
                filter(Seasons.sea_season_id == season).filter(Seasons.sea_deployment_id == deployment)
    else:
        if drone_id:
            ob = db.session.query(Measurement, Seasons).join(Seasons, Measurement.mea_id_movement == Seasons.sea_id_movement). \
                filter(Seasons.sea_season_id == season).filter(Measurement.mea_id_drone == drone_id)
        else:
            ob = db.session.query(Measurement, Seasons).join(Seasons, Measurement.mea_id_movement == Seasons.sea_id_movement). \
                filter(Seasons.sea_season_id == season)

    data = {}
    i = 0
    for obj in ob:
        data[i] = {'date': obj.Measurement.mea_date,
                   'id_drone': obj.Measurement.mea_id_drone,
                   'latitude': obj.Measurement.mea_latitude,
                   'altitude': obj.Measurement.mea_altitude,
                   'longitude': obj.Measurement.mea_longitude,
                   'id_measurement': obj.Measurement.mea_id_measurement,
                   'deployment': obj.Seasons.sea_deployment_id
                   }
        i += 1
    return (data)

def measurement_point_droneId(drone_id, season, deployment):
    db.Base.metadata.create_all(db.engine)

    if season:
        if deployment:
            ob = db.session.query(Measurement, Seasons).join(Seasons, Measurement.mea_id_movement == Seasons.sea_id_movement). \
                filter(Seasons.sea_season_id == season).filter(Seasons.sea_deployment_id == deployment). \
                filter(Measurement.mea_id_drone == drone_id)
        else:
            ob = db.session.query(Measurement, Seasons).join(Seasons, Measurement.mea_id_movement == Seasons.sea_id_movement). \
                filter(Seasons.sea_season_id == season).filter(Measurement.mea_id_drone == drone_id)
    else:
        if deployment:
           ob = db.session.query(Measurement, Seasons).join(Seasons, Measurement.mea_id_movement == Seasons.sea_id_movement).\
                filter(Measurement.mea_id_drone == drone_id).filter(Seasons.sea_deployment_id == deployment)
        else:
            ob = db.session.query(Measurement, Seasons).join(Seasons, Measurement.mea_id_movement == Seasons.sea_id_movement).\
                filter(Measurement.mea_id_drone == drone_id)

    data = {}
    i = 0
    for obj in ob:
        data[i] = {'date': obj.Measurement.mea_date,
                   'latitude': obj.Measurement.mea_latitude,
                   'altitude': obj.Measurement.mea_altitude,
                   'longitude': obj.Measurement.mea_longitude,
                   'id_measurement': obj.Measurement.mea_id_measurement,
                   'season': obj.Seasons.sea_season_id,
                   'deployment': obj.Seasons.sea_deployment_id
                   }
        i += 1
    return (data)
