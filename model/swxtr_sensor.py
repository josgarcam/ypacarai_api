from model.models import Measurement, Swxtr, Seasons
from model import db


def swxtr_all():
    db.Base.metadata.create_all(db.engine)
    ob = db.session.query(Measurement, Swxtr, Seasons).join(Swxtr, Measurement.id_measurement == Swxtr.id_measurement).\
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
                   'pm': obj.Swxtr.pm,
                   'od_sat': obj.Swxtr.od_sat,
                   'od_ppm': obj.Swxtr.od_ppm,
                   'od_temp': obj.Swxtr.od_temp,
                   'ntu_ntu': obj.Swxtr.ntu_ntu,
                   'ntu_temp': obj.Swxtr.ntu_temp,
                   'sac_dbo': obj.Swxtr.sac_dbo,
                   'sac_dqo': obj.Swxtr.sac_dqo,
                   'sac_cot': obj.Swxtr.sac_cot,
                   'sac_fau': obj.Swxtr.sac_fau,
                   'sac_temp': obj.Swxtr.sac_temp,
                   'sac_sac': obj.Swxtr.sac_sac,
                   'nivel_bateria': obj.Swxtr.nivel_bateria
                   }
        i += 1

    return (data)


def swxtr_season(season, deployment, drone_id):
    db.Base.metadata.create_all(db.engine)

    if deployment:
        if drone_id:
            ob = db.session.query(Measurement, Swxtr, Seasons).join(Swxtr, Measurement.id_measurement == Swxtr.id_measurement). \
                join(Seasons, Measurement.id_movement == Seasons.id_movement).filter(Seasons.season_id == season). \
                filter(Seasons.deployment_id == deployment).filter(Measurement.id_drone == drone_id)
        else:
            ob = db.session.query(Measurement, Swxtr, Seasons).join(Swxtr, Measurement.id_measurement == Swxtr.id_measurement). \
                join(Seasons, Measurement.id_movement == Seasons.id_movement).filter(Seasons.season_id == season). \
                filter(Seasons.deployment_id == deployment)
    else:
        if drone_id:
            ob = db.session.query(Measurement, Swxtr, Seasons).join(Swxtr, Measurement.id_measurement == Swxtr.id_measurement). \
                join(Seasons, Measurement.id_movement == Seasons.id_movement).filter(Seasons.season_id == season). \
                filter(Measurement.id_drone == drone_id)
        else:
            ob = db.session.query(Measurement, Swxtr, Seasons).join(Swxtr, Measurement.id_measurement == Swxtr.id_measurement). \
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
                   'pm': obj.Swxtr.pm,
                   'od_sat': obj.Swxtr.od_sat,
                   'od_ppm': obj.Swxtr.od_ppm,
                   'od_temp': obj.Swxtr.od_temp,
                   'ntu_ntu': obj.Swxtr.ntu_ntu,
                   'ntu_temp': obj.Swxtr.ntu_temp,
                   'sac_dbo': obj.Swxtr.sac_dbo,
                   'sac_dqo': obj.Swxtr.sac_dqo,
                   'sac_cot': obj.Swxtr.sac_cot,
                   'sac_fau': obj.Swxtr.sac_fau,
                   'sac_temp': obj.Swxtr.sac_temp,
                   'sac_sac': obj.Swxtr.sac_sac,
                   'nivel_bateria': obj.Swxtr.nivel_bateria
                   }
        i += 1

    return (data)


def swxtr_droneId(drone_id, season, deployment):
    db.Base.metadata.create_all(db.engine)

    if season:
        if deployment:
            ob = db.session.query(Measurement, Swxtr, Seasons).join(Swxtr, Measurement.id_measurement == Swxtr.id_measurement). \
                join(Seasons, Measurement.id_movement == Seasons.id_movement).filter(Seasons.season_id == season). \
                filter(Seasons.deployment_id == deployment).filter(Measurement.id_drone == drone_id).all()
        else:
            ob = db.session.query(Measurement, Swxtr, Seasons).join(Swxtr, Measurement.id_measurement == Swxtr.id_measurement). \
                join(Seasons, Measurement.id_movement == Seasons.id_movement).filter(Seasons.season_id == season). \
                filter(Measurement.id_drone == drone_id)
    else:
        if deployment:
            ob = db.session.query(Measurement, Swxtr, Seasons).join(Swxtr, Measurement.id_measurement == Swxtr.id_measurement). \
                join(Seasons, Measurement.id_movement == Seasons.id_movement). \
                filter(Seasons.deployment_id == deployment).filter(Measurement.id_drone == drone_id)
        else:
            ob = db.session.query(Measurement, Swxtr, Seasons).join(Swxtr,Measurement.id_measurement == Swxtr.id_measurement). \
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
                   'pm': obj.Swxtr.pm,
                   'od_sat': obj.Swxtr.od_sat,
                   'od_ppm': obj.Swxtr.od_ppm,
                   'od_temp': obj.Swxtr.od_temp,
                   'ntu_ntu': obj.Swxtr.ntu_ntu,
                   'ntu_temp': obj.Swxtr.ntu_temp,
                   'sac_dbo': obj.Swxtr.sac_dbo,
                   'sac_dqo': obj.Swxtr.sac_dqo,
                   'sac_cot': obj.Swxtr.sac_cot,
                   'sac_fau': obj.Swxtr.sac_fau,
                   'sac_temp': obj.Swxtr.sac_temp,
                   'sac_sac': obj.Swxtr.sac_sac,
                   'nivel_bateria': obj.Swxtr.nivel_bateria
                   }
        i += 1

    return (data)