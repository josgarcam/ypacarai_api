from model.models import Measurement, Sepro, Seasons
from model import db


def sepro_all():
    db.Base.metadata.create_all(db.engine)
    ob = db.session.query(Measurement, Sepro, Seasons).join(Sepro, Measurement.id_measurement == Sepro.id_measurement). \
        join(Seasons, Measurement.id_movement == Seasons.id_movement).all()

    data = {}

    i = 0
    for obj in ob:
        data[i] = {'date': obj.Measurement.date,
                   'id_drone': obj.Measurement.id_drone,
                   'latitude': obj.Measurement.latitude,
                   'altitude': obj.Measurement.altitude,
                   'longitude': obj.Measurement.longitude,
                   'season': obj.Seasons.season_id,
                   'deployment': obj.Seasons.deployment_id,
                   'pm': obj.Sepro.pm,
                   'c02': obj.Sepro.c02,
                   'h2s': obj.Sepro.h2s,
                   'o3': obj.Sepro.o3,
                   'hr': obj.Sepro.hr,
                   'pres': obj.Sepro.pres,
                   'temper': obj.Sepro.temper,
                   'nivel_bateria': obj.Sepro.nivel_bateria
                   }
        i += 1

    return (data)


def sepro_season(season, deployment, drone_id):
    db.Base.metadata.create_all(db.engine)

    if deployment:
        if drone_id:
            ob = db.session.query(Measurement, Sepro, Seasons).join(Sepro, Measurement.id_measurement == Sepro.id_measurement). \
                join(Seasons, Measurement.id_movement == Seasons.id_movement).filter(Seasons.season_id == season). \
                filter(Seasons.deployment_id == deployment).filter(Measurement.id_drone == drone_id)
        else:
            ob = db.session.query(Measurement, Sepro, Seasons).join(Sepro, Measurement.id_measurement == Sepro.id_measurement). \
                join(Seasons, Measurement.id_movement == Seasons.id_movement).filter(Seasons.season_id == season). \
                filter(Seasons.deployment_id == deployment)
    else:
        if drone_id:
            ob = db.session.query(Measurement, Sepro, Seasons).join(Sepro, Measurement.id_measurement == Sepro.id_measurement). \
                join(Seasons, Measurement.id_movement == Seasons.id_movement).filter(Seasons.season_id == season). \
                filter(Measurement.id_drone == drone_id)
        else:
            ob = db.session.query(Measurement, Sepro, Seasons).join(Sepro, Measurement.id_measurement == Sepro.id_measurement). \
                join(Seasons, Measurement.id_movement == Seasons.id_movement).filter(Seasons.season_id == season)


    i = 0
    data = {}

    for obj in ob:
        data[i] = {'date': obj.Measurement.date,
                   'id_drone': obj.Measurement.id_drone,
                   'latitude': obj.Measurement.latitude,
                   'altitude': obj.Measurement.altitude,
                   'longitude': obj.Measurement.longitude,
                   'deployment': obj.Seasons.deployment_id,
                   'pm': obj.Sepro.pm,
                   'c02': obj.Sepro.c02,
                   'h2s': obj.Sepro.h2s,
                   'o3': obj.Sepro.o3,
                   'hr': obj.Sepro.hr,
                   'pres': obj.Sepro.pres,
                   'temper': obj.Sepro.temper,
                   'nivel_bateria': obj.Sepro.nivel_bateria
                   }
        i += 1

    return (data)


def sepro_droneId(drone_id, season, deployment):
    db.Base.metadata.create_all(db.engine)

    if season:
        if deployment:
            ob = db.session.query(Measurement, Sepro, Seasons).join(Sepro, Measurement.id_measurement == Sepro.id_measurement). \
                join(Seasons, Measurement.id_movement == Seasons.id_movement).filter(Seasons.season_id == season). \
                filter(Seasons.deployment_id == deployment).filter(Measurement.id_drone == drone_id).all()
        else:
            ob = db.session.query(Measurement, Sepro, Seasons).join(Sepro, Measurement.id_measurement == Sepro.id_measurement). \
                join(Seasons, Measurement.id_movement == Seasons.id_movement).filter(Seasons.season_id == season). \
                filter(Measurement.id_drone == drone_id)
    else:
        if deployment:
            ob = db.session.query(Measurement, Sepro, Seasons).join(Sepro, Measurement.id_measurement == Sepro.id_measurement). \
                join(Seasons, Measurement.id_movement == Seasons.id_movement). \
                filter(Seasons.deployment_id == deployment).filter(Measurement.id_drone == drone_id)
        else:
            ob = db.session.query(Measurement, Sepro, Seasons).join(Sepro, Measurement.id_measurement == Sepro.id_measurement). \
                join(Seasons, Measurement.id_movement == Seasons.id_movement).filter(Measurement.id_drone == drone_id)

    i = 0
    data = {}

    for obj in ob:
        data[i] = {'date': obj.Measurement.date,
                   'latitude': obj.Measurement.latitude,
                   'altitude': obj.Measurement.altitude,
                   'longitude': obj.Measurement.longitude,
                   'season': obj.Seasons.season_id,
                   'deployment': obj.Seasons.deployment_id,
                   'pm': obj.Sepro.pm,
                   'c02': obj.Sepro.c02,
                   'h2s': obj.Sepro.h2s,
                   'o3': obj.Sepro.o3,
                   'hr': obj.Sepro.hr,
                   'pres': obj.Sepro.pres,
                   'temper': obj.Sepro.temper,
                   'nivel_bateria': obj.Sepro.nivel_bateria
                   }
        i += 1

    return (data)
