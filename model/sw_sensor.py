from model.models import Measurement, Sw
from model import db

def sw_all():

    db.Base.metadata.create_all(db.engine)
    ob = db.session.query(Measurement, Sw).join(Sw, Measurement.id_measurement == Sw.id_measurement).all()
    data = {}

    i = 0
    for obj in ob:
        data[i] = {'date': obj.Measurement.date,
                    'id_drone': obj.Measurement.id_drone,
                    'latitude': obj.Measurement.latitude,
                    'altitude': obj.Measurement.altitude,
                    'longitude': obj.Measurement.longitude,
                    'season': obj.Measurement.season,
                    'deployment': obj.Measurement.deployment,
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
            ob = db.session.query(Measurement, Sw).join(Sw, Measurement.id_measurement == Sw.id_measurement).\
                filter(Measurement.season == season).filter(Measurement.deployment == deployment). \
                filter(Measurement.id_drone == drone_id)
        else:
            ob = db.session.query(Measurement, Sw).join(Sw, Measurement.id_measurement == Sw.id_measurement).\
                filter(Measurement.season == season).filter(Measurement.deployment == deployment)
    else:
        if drone_id:
            ob = db.session.query(Measurement, Sw).join(Sw, Measurement.id_measurement == Sw.id_measurement) \
                .filter(Measurement.season == season).filter(Measurement.id_drone == drone_id)
        else:
            ob = db.session.query(Measurement, Sw).join(Sw, Measurement.id_measurement == Sw.id_measurement)\
            .filter(Measurement.season == season)

    i = 0
    data = {}

    for obj in ob:
        data[i] = {'date': obj.Measurement.date,
                    'id_drone': obj.Measurement.id_drone,
                    'latitude': obj.Measurement.latitude,
                    'altitude': obj.Measurement.altitude,
                    'longitude': obj.Measurement.longitude,
                    'deployment': obj.Sw.deployment,
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
            ob = db.session.query(Measurement, Sw).join(Sw, Measurement.id_measurement == Sw.id_measurement). \
                filter(Measurement.id_drone == drone_id).filter(Measurement.season == season). \
                filter(Measurement.deployment == deployment).all()
        else:
            ob = db.session.query(Measurement, Sw).join(Sw, Measurement.id_measurement == Sw.id_measurement). \
                filter(Measurement.id_drone == drone_id).filter(Measurement.season == season).all()
    else:
        if deployment:
            ob = db.session.query(Measurement, Sw).join(Sw, Measurement.id_measurement == Sw.id_measurement). \
                filter(Measurement.id_drone == drone_id).filter(Measurement.deployment == deployment)
        else:
            ob = db.session.query(Measurement, Sw).join(Sw, Measurement.id_measurement == Sw.id_measurement). \
            filter(Measurement.id_drone == drone_id)

    i = 0
    data = {}

    for obj in ob:
        data[i] = {'date': obj.Measurement.date,
                    'latitude': obj.Measurement.latitude,
                    'altitude': obj.Measurement.altitude,
                    'longitude': obj.Measurement.longitude,
                    'season': obj.Sw.season,
                    'deployment': obj.Sw.deployment,
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