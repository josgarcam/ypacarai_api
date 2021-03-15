from model.models import Measurement, Sw, Seasons
from model import db

def sw_all():

    db.Base.metadata.create_all(db.engine)
    ob = db.session.query(Measurement, Sw, Seasons).join(Sw, Measurement.mea_id_measurement == Sw.sw_id_measurement).\
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
                    'pm': obj.Sw.sw_pm,
                    'ph': obj.Sw.sw_ph,
                    'od': obj.Sw.sw_od,
                    'ce': obj.Sw.sw_ce,
                    'orp': obj.Sw.sw_orp,
                    'temp': obj.Sw.sw_temper,
                    'ph_volt': obj.Sw.sw_ph_volt,
                    'od_volt': obj.Sw.sw_od_volt,
                    'ce_res': obj.Sw.sw_ce_res,
                    'orp_volt': obj.Sw.sw_orp_volt,
                    'nivel_bateria': obj.Sw.sw_nivel_bateria
                   }
        i += 1

    return (data)

def sw_season(season, deployment, drone_id):
    db.Base.metadata.create_all(db.engine)

    if deployment:
        if drone_id:
            ob = db.session.query(Measurement, Sw, Seasons).join(Sw, Measurement.mea_id_measurement == Sw.sw_id_measurement). \
                join(Seasons, Measurement.mea_id_movement == Seasons.sea_id_movement).filter(Seasons.sea_season_id == season). \
                filter(Seasons.sea_deployment_id == deployment).filter(Measurement.mea_id_drone == drone_id)
        else:
            ob = db.session.query(Measurement, Sw, Seasons).join(Sw, Measurement.mea_id_measurement == Sw.sw_id_measurement). \
                join(Seasons, Measurement.mea_id_movement == Seasons.sea_id_movement).filter(Seasons.sea_season_id == season). \
                filter(Seasons.sea_deployment_id == deployment)
    else:
        if drone_id:
            ob = db.session.query(Measurement, Sw, Seasons).join(Sw, Measurement.mea_id_measurement == Sw.sw_id_measurement). \
                join(Seasons, Measurement.mea_id_movement == Seasons.sea_id_movement).filter(Seasons.sea_season_id == season). \
                filter(Measurement.mea_id_drone == drone_id)
        else:
            ob = db.session.query(Measurement, Sw, Seasons).join(Sw, Measurement.mea_id_measurement == Sw.sw_id_measurement). \
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
                    'pm': obj.Sw.sw_pm,
                    'ph': obj.Sw.sw_ph,
                    'od': obj.Sw.sw_od,
                    'ce': obj.Sw.sw_ce,
                    'orp': obj.Sw.sw_orp,
                    'temp': obj.Sw.sw_temper,
                    'ph_volt': obj.Sw.sw_ph_volt,
                    'od_volt': obj.Sw.sw_od_volt,
                    'ce_res': obj.Sw.sw_ce_res,
                    'orp_volt': obj.Sw.sw_orp_volt,
                    'nivel_bateria': obj.Sw.sw_nivel_bateria
                   }
        i += 1

    return (data)

def sw_droneId(drone_id, season, deployment):
    db.Base.metadata.create_all(db.engine)

    if season:
        if deployment:
            ob = db.session.query(Measurement, Sw, Seasons).join(Sw, Measurement.mea_id_measurement == Sw.sw_id_measurement). \
                join(Seasons, Measurement.mea_id_movement == Seasons.sea_id_movement).filter(Seasons.sea_season_id == season). \
                filter(Seasons.sea_deployment_id == deployment).filter(Measurement.mea_id_drone == drone_id).all()
        else:
            ob = db.session.query(Measurement, Sw, Seasons).join(Sw, Measurement.mea_id_measurement == Sw.sw_id_measurement). \
                join(Seasons, Measurement.mea_id_movement == Seasons.sea_id_movement).filter(Seasons.sea_season_id == season).\
                filter(Measurement.mea_id_drone == drone_id)
    else:
        if deployment:
            ob = db.session.query(Measurement, Sw, Seasons).join(Sw, Measurement.mea_id_measurement == Sw.sw_id_measurement). \
                join(Seasons, Measurement.mea_id_movement == Seasons.sea_id_movement).\
                filter(Seasons.sea_deployment_id == deployment).filter(Measurement.mea_id_drone == drone_id)
        else:
            ob = db.session.query(Measurement, Sw, Seasons).join(Sw, Measurement.mea_id_measurement == Sw.sw_id_measurement). \
                join(Seasons, Measurement.mea_id_movement == Seasons.sea_id_movement).filter(Measurement.mea_id_drone == drone_id)

    i = 0
    data = {}

    for obj in ob:
        data[i] = {'date': obj.Measurement.mea_date,
                   'id_drone': obj.Measurement.mea_id_drone,
                   'latitude': obj.Measurement.mea_latitude,
                   'altitude': obj.Measurement.mea_altitude,
                   'longitude': obj.Measurement.mea_longitude,
                   'season': obj.Seasons.sea_season_id,
                   'deployment': obj.Seasons.sea_deployment_id,
                   'pm': obj.Sw.sw_pm,
                   'ph': obj.Sw.sw_ph,
                   'od': obj.Sw.sw_od,
                   'ce': obj.Sw.sw_ce,
                   'orp': obj.Sw.sw_orp,
                   'temp': obj.Sw.sw_temper,
                   'ph_volt': obj.Sw.sw_ph_volt,
                   'od_volt': obj.Sw.sw_od_volt,
                   'ce_res': obj.Sw.sw_ce_res,
                   'orp_volt': obj.Sw.sw_orp_volt,
                   'nivel_bateria': obj.Sw.sw_nivel_bateria
                   }

        i += 1

    return (data)