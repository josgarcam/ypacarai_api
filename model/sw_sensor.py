from model.models import Measurement, Sw, Seasons
from model import db

def sw_all():

    db.Base.metadata.create_all(db.engine)
    ob = db.session.query(Measurement, Sw, Seasons).join(Sw, Measurement.id_measurement == Sw.id_measurement).\
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
                    'pm': obj.Sw.pm,
                    'ph': obj.Sw.ph,
                    'od': obj.Sw.od,
                    'ce': obj.Sw.ce,
                    'orp': obj.Sw.orp,
                    'temp': obj.Sw.temper,
                    'ph_volt': obj.Sw.ph_volt,
                    'od_volt': obj.Sw.od_volt,
                    'ce_res': obj.Sw.ce_res,
                    'orp_volt': obj.Sw.orp_volt
                   }
        i += 1

    return (data)

def sw_season(season, deployment, drone_id):
    db.Base.metadata.create_all(db.engine)

    if deployment:
        if drone_id:
            ob = db.session.query(Measurement, Sw, Seasons).join(Sw, Measurement.id_measurement == Sw.id_measurement). \
                join(Seasons, Measurement.id_movement == Seasons.id_movement).filter(Seasons.season_id == season). \
                filter(Seasons.deployment_id == deployment).filter(Measurement.id_drone == drone_id)
        else:
            ob = db.session.query(Measurement, Sw, Seasons).join(Sw, Measurement.id_measurement == Sw.id_measurement). \
                join(Seasons, Measurement.id_movement == Seasons.id_movement).filter(Seasons.season_id == season). \
                filter(Seasons.deployment_id == deployment)
    else:
        if drone_id:
            ob = db.session.query(Measurement, Sw, Seasons).join(Sw, Measurement.id_measurement == Sw.id_measurement). \
                join(Seasons, Measurement.id_movement == Seasons.id_movement).filter(Seasons.season_id == season). \
                filter(Measurement.id_drone == drone_id)
        else:
            ob = db.session.query(Measurement, Sw, Seasons).join(Sw, Measurement.id_measurement == Sw.id_measurement). \
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
                    'pm': obj.Sw.pm,
                    'ph': obj.Sw.ph,
                    'od': obj.Sw.od,
                    'ce': obj.Sw.ce,
                    'orp': obj.Sw.orp,
                    'temp': obj.Sw.temper,
                    'ph_volt': obj.Sw.ph_volt,
                    'od_volt': obj.Sw.od_volt,
                    'ce_res': obj.Sw.ce_res,
                    'orp_volt': obj.Sw.orp_volt
                   }
        i += 1

    return (data)

def sw_droneId(drone_id, season, deployment):
    db.Base.metadata.create_all(db.engine)

    if season:
        if deployment:
            ob = db.session.query(Measurement, Sw, Seasons).join(Sw, Measurement.id_measurement == Sw.id_measurement). \
                join(Seasons, Measurement.id_movement == Seasons.id_movement).filter(Seasons.season_id == season). \
                filter(Seasons.deployment_id == deployment).filter(Measurement.id_drone == drone_id).all()
        else:
            ob = db.session.query(Measurement, Sw, Seasons).join(Sw, Measurement.id_measurement == Sw.id_measurement). \
                join(Seasons, Measurement.id_movement == Seasons.id_movement).filter(Seasons.season_id == season).\
                filter(Measurement.id_drone == drone_id)
    else:
        if deployment:
            ob = db.session.query(Measurement, Sw, Seasons).join(Sw, Measurement.id_measurement == Sw.id_measurement). \
                join(Seasons, Measurement.id_movement == Seasons.id_movement).\
                filter(Seasons.deployment_id == deployment).filter(Measurement.id_drone == drone_id)
        else:
            ob = db.session.query(Measurement, Sw, Seasons).join(Sw, Measurement.id_measurement == Sw.id_measurement). \
                join(Seasons, Measurement.id_movement == Seasons.id_movement).filter(Measurement.id_drone == drone_id)

    i = 0
    data = {}

    for obj in ob:
        data[i] = {'date': obj.Measurement.date,
                   'id_drone': obj.Measurement.id_drone,
                   'latitude': obj.Measurement.latitude,
                   'altitude': obj.Measurement.altitude,
                   'longitude': obj.Measurement.longitude,
                   'season': obj.Seasons.season_id,
                   'deployment': obj.Seasons.deployment_id,
                   'pm': obj.Sw.pm,
                   'ph': obj.Sw.ph,
                   'od': obj.Sw.od,
                   'ce': obj.Sw.ce,
                   'orp': obj.Sw.orp,
                   'temp': obj.Sw.temper,
                   'ph_volt': obj.Sw.ph_volt,
                   'od_volt': obj.Sw.od_volt,
                   'ce_res': obj.Sw.ce_res,
                   'orp_volt': obj.Sw.orp_volt
                   }

        i += 1

    return (data)