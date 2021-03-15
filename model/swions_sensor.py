from model.models import Measurement, Swions, Seasons
from model import db

def swions_all():

    db.Base.metadata.create_all(db.engine)
    ob = db.session.query(Measurement, Swions, Seasons).join(Swions, Measurement.mea_id_measurement == Swions.swi_id_measurement).\
        join(Seasons, Measurement.mea_id_movement == Seasons.sea_id_movement)


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
                    'pm': obj.Swions.swi_pm,
                    'no3_conc': obj.Swions.swi_no3_conc,
                    'nh4_conc': obj.Swions.swi_nh4_conc,
                    'temp': obj.Swions.swi_temper,
                    'no3_volt': obj.Swions.swi_no3_volt,
                    'nh4_volt': obj.Swions.swi_nh4_volt,
                    'nivel_bateria': obj.Swions.swi_nivel_bateria
                   }
        i += 1

    return (data)

def swions_season(season, deployment, drone_id):
    db.Base.metadata.create_all(db.engine)

    if deployment:
        if drone_id:
            ob = db.session.query(Measurement, Swions, Seasons).join(Swions, Measurement.mea_id_measurement == Swions.swi_id_measurement). \
                join(Seasons, Measurement.mea_id_movement == Seasons.sea_id_movement).filter(Seasons.sea_season_id == season). \
                filter(Seasons.sea_deployment_id == deployment).filter(Measurement.mea_id_drone == drone_id)
        else:
            ob = db.session.query(Measurement, Swions, Seasons).join(Swions, Measurement.mea_id_measurement == Swions.swi_id_measurement). \
                join(Seasons, Measurement.mea_id_movement == Seasons.sea_id_movement).filter(Seasons.sea_season_id == season). \
                filter(Seasons.sea_deployment_id == deployment)
    else:
        if drone_id:
            ob = db.session.query(Measurement, Swions, Seasons).join(Swions, Measurement.mea_id_measurement == Swions.swi_id_measurement). \
                join(Seasons, Measurement.mea_id_movement == Seasons.sea_id_movement).filter(Seasons.sea_season_id == season). \
                filter(Measurement.mea_id_drone == drone_id)
        else:
            ob = db.session.query(Measurement, Swions, Seasons).join(Swions, Measurement.mea_id_measurement == Swions.swi_id_measurement). \
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
                   'pm': obj.Swions.swi_pm,
                   'no3_conc': obj.Swions.swi_no3_conc,
                   'nh4_conc': obj.Swions.swi_nh4_conc,
                   'temp': obj.Swions.swi_temper,
                   'no3_volt': obj.Swions.swi_no3_volt,
                   'nh4_volt': obj.Swions.swi_nh4_volt,
                   'nivel_bateria': obj.Swions.swi_nivel_bateria
                   }
        i += 1

    return (data)

def swions_droneId(drone_id, season, deployment):
    db.Base.metadata.create_all(db.engine)

    if season:
        if deployment:
            ob = db.session.query(Measurement, Swions, Seasons).join(Swions, Measurement.mea_id_measurement == Swions.swi_id_measurement). \
                join(Seasons, Measurement.mea_id_movement == Seasons.sea_id_movement).filter(Seasons.sea_season_id == season). \
                filter(Seasons.sea_deployment_id == deployment).filter(Measurement.mea_id_drone == drone_id).all()
        else:
            ob = db.session.query(Measurement, Swions, Seasons).join(Swions, Measurement.mea_id_measurement == Swions.swi_id_measurement). \
                join(Seasons, Measurement.mea_id_movement == Seasons.sea_id_movement).filter(Seasons.sea_season_id == season). \
                filter(Measurement.mea_id_drone == drone_id)
    else:
        if deployment:
            ob = db.session.query(Measurement, Swions, Seasons).join(Swions, Measurement.mea_id_measurement == Swions.swi_id_measurement). \
                join(Seasons, Measurement.mea_id_movement == Seasons.sea_id_movement). \
                filter(Seasons.sea_deployment_id == deployment).filter(Measurement.mea_id_drone == drone_id)
        else:
            ob = db.session.query(Measurement, Swions, Seasons).join(Swions, Measurement.mea_id_measurement == Swions.swi_id_measurement). \
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
                   'pm': obj.Swions.swi_pm,
                   'no3_conc': obj.Swions.swi_no3_conc,
                   'nh4_conc': obj.Swions.swi_nh4_conc,
                   'temp': obj.Swions.swi_temper,
                   'no3_volt': obj.Swions.swi_no3_volt,
                   'nh4_volt': obj.Swions.swi_nh4_volt,
                   'nivel_bateria': obj.Swions.swi_nivel_bateria
                   }
        i += 1

    return (data)