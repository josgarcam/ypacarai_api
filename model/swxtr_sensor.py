from model.models import Measurement, Swxtr, Seasons
from model import db


def swxtr_all():
    db.Base.metadata.create_all(db.engine)
    ob = db.session.query(Measurement, Swxtr, Seasons).join(Swxtr, Measurement.mea_id_measurement == Swxtr.swx_id_measurement).\
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
                   'pm': obj.Swxtr.swx_pm,
                   'od_sat': obj.Swxtr.swx_od_sat,
                   'od_ppm': obj.Swxtr.swx_od_ppm,
                   'od_temp': obj.Swxtr.swx_od_temp,
                   'ntu_ntu': obj.Swxtr.swx_ntu_ntu,
                   'ntu_temp': obj.Swxtr.swx_ntu_temp,
                   'sac_dbo': obj.Swxtr.swx_sac_dbo,
                   'sac_dqo': obj.Swxtr.swx_sac_dqo,
                   'sac_cot': obj.Swxtr.swx_sac_cot,
                   'sac_fau': obj.Swxtr.swx_sac_fau,
                   'sac_temp': obj.Swxtr.swx_sac_temp,
                   'sac_sac': obj.Swxtr.swx_sac_sac,
                   'nivel_bateria': obj.Swxtr.swx_nivel_bateria
                   }
        i += 1

    return (data)


def swxtr_season(season, deployment, drone_id):
    db.Base.metadata.create_all(db.engine)

    if deployment:
        if drone_id:
            ob = db.session.query(Measurement, Swxtr, Seasons).join(Swxtr, Measurement.mea_id_measurement == Swxtr.swx_id_measurement). \
                join(Seasons, Measurement.mea_id_movement == Seasons.sea_id_movement).filter(Seasons.sea_season_id == season). \
                filter(Seasons.sea_deployment_id == deployment).filter(Measurement.mea_id_drone == drone_id)
        else:
            ob = db.session.query(Measurement, Swxtr, Seasons).join(Swxtr, Measurement.mea_id_measurement == Swxtr.swx_id_measurement). \
                join(Seasons, Measurement.mea_id_movement == Seasons.sea_id_movement).filter(Seasons.sea_season_id == season). \
                filter(Seasons.sea_deployment_id == deployment)
    else:
        if drone_id:
            ob = db.session.query(Measurement, Swxtr, Seasons).join(Swxtr, Measurement.mea_id_measurement == Swxtr.swx_id_measurement). \
                join(Seasons, Measurement.mea_id_movement == Seasons.sea_id_movement).filter(Seasons.sea_season_id == season). \
                filter(Measurement.mea_id_drone == drone_id)
        else:
            ob = db.session.query(Measurement, Swxtr, Seasons).join(Swxtr, Measurement.mea_id_measurement == Swxtr.swx_id_measurement). \
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
                   'pm': obj.Swxtr.swx_pm,
                   'od_sat': obj.Swxtr.swx_od_sat,
                   'od_ppm': obj.Swxtr.swx_od_ppm,
                   'od_temp': obj.Swxtr.swx_od_temp,
                   'ntu_ntu': obj.Swxtr.swx_ntu_ntu,
                   'ntu_temp': obj.Swxtr.swx_ntu_temp,
                   'sac_dbo': obj.Swxtr.swx_sac_dbo,
                   'sac_dqo': obj.Swxtr.swx_sac_dqo,
                   'sac_cot': obj.Swxtr.swx_sac_cot,
                   'sac_fau': obj.Swxtr.swx_sac_fau,
                   'sac_temp': obj.Swxtr.swx_sac_temp,
                   'sac_sac': obj.Swxtr.swx_sac_sac,
                   'nivel_bateria': obj.Swxtr.swx_nivel_bateria
                   }
        i += 1

    return (data)


def swxtr_droneId(drone_id, season, deployment):
    db.Base.metadata.create_all(db.engine)

    if season:
        if deployment:
            ob = db.session.query(Measurement, Swxtr, Seasons).join(Swxtr, Measurement.mea_id_measurement == Swxtr.swx_id_measurement). \
                join(Seasons, Measurement.mea_id_movement == Seasons.sea_id_movement).filter(Seasons.sea_season_id == season). \
                filter(Seasons.sea_deployment_id == deployment).filter(Measurement.mea_id_drone == drone_id).all()
        else:
            ob = db.session.query(Measurement, Swxtr, Seasons).join(Swxtr, Measurement.mea_id_measurement == Swxtr.swx_id_measurement). \
                join(Seasons, Measurement.mea_id_movement == Seasons.sea_id_movement).filter(Seasons.sea_season_id == season). \
                filter(Measurement.mea_id_drone == drone_id)
    else:
        if deployment:
            ob = db.session.query(Measurement, Swxtr, Seasons).join(Swxtr, Measurement.mea_id_measurement == Swxtr.swx_id_measurement). \
                join(Seasons, Measurement.mea_id_movement == Seasons.sea_id_movement). \
                filter(Seasons.sea_deployment_id == deployment).filter(Measurement.mea_id_drone == drone_id)
        else:
            ob = db.session.query(Measurement, Swxtr, Seasons).join(Swxtr,Measurement.mea_id_measurement == Swxtr.swx_id_measurement). \
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
                   'pm': obj.Swxtr.swx_pm,
                   'od_sat': obj.Swxtr.swx_od_sat,
                   'od_ppm': obj.Swxtr.swx_od_ppm,
                   'od_temp': obj.Swxtr.swx_od_temp,
                   'ntu_ntu': obj.Swxtr.swx_ntu_ntu,
                   'ntu_temp': obj.Swxtr.swx_ntu_temp,
                   'sac_dbo': obj.Swxtr.swx_sac_dbo,
                   'sac_dqo': obj.Swxtr.swx_sac_dqo,
                   'sac_cot': obj.Swxtr.swx_sac_cot,
                   'sac_fau': obj.Swxtr.swx_sac_fau,
                   'sac_temp': obj.Swxtr.swx_sac_temp,
                   'sac_sac': obj.Swxtr.swx_sac_sac,
                   'nivel_bateria': obj.Swxtr.swx_nivel_bateria
                   }
        i += 1

    return (data)