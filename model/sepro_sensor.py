from model.models import Measurement, Sepro, Seasons
from model import db


def sepro_all():
    db.Base.metadata.create_all(db.engine)
    ob = db.session.query(Measurement, Sepro, Seasons).join(Sepro, Measurement.mea_id_measurement == Sepro.sep_id_measurement). \
        join(Seasons, Measurement.mea_id_movement == Seasons.sea_id_movement).all()

    data = {}

    i = 0
    for obj in ob:
        data[i] = {'date': obj.Measurement.mea_date,
                   'id_drone': obj.Measurement.mea_id_drone,
                   'latitude': obj.Measurement.mea_latitude,
                   'altitude': obj.Measurement.mea_altitude,
                   'longitude': obj.Measurement.mea_longitude,
                   'season': obj.Seasons.sea_season_id,
                   'deployment': obj.Seasons.sea_deployment_id,
                   'pm': obj.Sepro.sep_pm,
                   'c02': obj.Sepro.sep_c02,
                   'h2s': obj.Sepro.sep_h2s,
                   'o3': obj.Sepro.sep_o3,
                   'hr': obj.Sepro.sep_hr,
                   'pres': obj.Sepro.sep_pres,
                   'temper': obj.Sepro.sep_temper,
                   'nivel_bateria': obj.Sepro.sep_nivel_bateria
                   }
        i += 1

    return (data)


def sepro_season(season, deployment, drone_id):
    db.Base.metadata.create_all(db.engine)

    if deployment:
        if drone_id:
            ob = db.session.query(Measurement, Sepro, Seasons).join(Sepro, Measurement.mea_id_measurement == Sepro.sep_id_measurement). \
                join(Seasons, Measurement.mea_id_movement == Seasons.sea_id_movement).filter(Seasons.sea_season_id == season). \
                filter(Seasons.sea_deployment_id == deployment).filter(Measurement.mea_id_drone == drone_id)
        else:
            ob = db.session.query(Measurement, Sepro, Seasons).join(Sepro, Measurement.mea_id_measurement == Sepro.sep_id_measurement). \
                join(Seasons, Measurement.mea_id_movement == Seasons.sea_id_movement).filter(Seasons.sea_season_id == season). \
                filter(Seasons.sea_deployment_id == deployment)
    else:
        if drone_id:
            ob = db.session.query(Measurement, Sepro, Seasons).join(Sepro, Measurement.mea_id_measurement == Sepro.sep_id_measurement). \
                join(Seasons, Measurement.mea_id_movement == Seasons.sea_id_movement).filter(Seasons.sea_season_id == season). \
                filter(Measurement.mea_id_drone == drone_id)
        else:
            ob = db.session.query(Measurement, Sepro, Seasons).join(Sepro, Measurement.mea_id_measurement == Sepro.sep_id_measurement). \
                join(Seasons, Measurement.mea_id_movement == Seasons.sea_id_movement).filter(Seasons.sea_season_id == season)


    i = 0
    data = {}

    for obj in ob:
        data[i] = {'date': obj.Measurement.mea_date,
                   'id_drone': obj.Measurement.mea_id_drone,
                   'latitude': obj.Measurement.mea_latitude,
                   'altitude': obj.Measurement.mea_altitude,
                   'longitude': obj.Measurement.mea_longitude,
                   'deployment': obj.Seasons.sea_deployment_id,
                   'pm': obj.Sepro.sep_pm,
                   'c02': obj.Sepro.sep_c02,
                   'h2s': obj.Sepro.sep_h2s,
                   'o3': obj.Sepro.sep_o3,
                   'hr': obj.Sepro.sep_hr,
                   'pres': obj.Sepro.sep_pres,
                   'temper': obj.Sepro.sep_temper,
                   'nivel_bateria': obj.Sepro.sep_nivel_bateria
                   }
        i += 1

    return (data)


def sepro_droneId(drone_id, season, deployment):
    db.Base.metadata.create_all(db.engine)

    if season:
        if deployment:
            ob = db.session.query(Measurement, Sepro, Seasons).join(Sepro, Measurement.mea_id_measurement == Sepro.sep_id_measurement). \
                join(Seasons, Measurement.mea_id_movement == Seasons.sea_id_movement).filter(Seasons.sea_season_id == season). \
                filter(Seasons.sea_deployment_id == deployment).filter(Measurement.mea_id_drone == drone_id).all()
        else:
            ob = db.session.query(Measurement, Sepro, Seasons).join(Sepro, Measurement.mea_id_measurement == Sepro.sep_id_measurement). \
                join(Seasons, Measurement.mea_id_movement == Seasons.sea_id_movement).filter(Seasons.sea_season_id == season). \
                filter(Measurement.mea_id_drone == drone_id)
    else:
        if deployment:
            ob = db.session.query(Measurement, Sepro, Seasons).join(Sepro, Measurement.mea_id_measurement == Sepro.sep_id_measurement). \
                join(Seasons, Measurement.mea_id_movement == Seasons.sea_id_movement). \
                filter(Seasons.sea_deployment_id == deployment).filter(Measurement.mea_id_drone == drone_id)
        else:
            ob = db.session.query(Measurement, Sepro, Seasons).join(Sepro, Measurement.mea_id_measurement == Sepro.sep_id_measurement). \
                join(Seasons, Measurement.mea_id_movement == Seasons.sea_id_movement).filter(Measurement.mea_id_drone == drone_id)

    i = 0
    data = {}

    for obj in ob:
        data[i] = {'date': obj.Measurement.mea_date,
                   'latitude': obj.Measurement.mea_latitude,
                   'altitude': obj.Measurement.mea_altitude,
                   'longitude': obj.Measurement.mea_longitude,
                   'season': obj.Seasons.sea_season_id,
                   'deployment': obj.Seasons.sea_deployment_id,
                   'pm': obj.Sepro.sep_pm,
                   'c02': obj.Sepro.sep_c02,
                   'h2s': obj.Sepro.sep_h2s,
                   'o3': obj.Sepro.sep_o3,
                   'hr': obj.Sepro.sep_hr,
                   'pres': obj.Sepro.sep_pres,
                   'temper': obj.Sepro.sep_temper,
                   'nivel_bateria': obj.Sepro.sep_nivel_bateria
                   }
        i += 1

    return (data)
