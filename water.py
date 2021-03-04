from datetime import datetime
from models import Water
import db



def water_place():

    db.Base.metadata.create_all(db.engine)
    ob = db.session.query(Water).all()
    data = {}
    i = 0
    for obj in ob:
        data[i] = {'drone_id': obj.par_agua_cod_drone,
                    'date': obj.par_agua_fecha_hora,
                    'latitude': obj.par_agua_sw_lat,
                    'longitude': obj.par_agua_sw_log,
                    'height': obj.par_agua_sw_alt
                   }

        i += 1

    return (data)


def water_drone_id_and_date(drone_id, sdate, edate):
    print(sdate)
    print(edate)
    if sdate and edate:
        ob = db.session.query(Water).filter(Water.par_agua_cod_drone == drone_id).\
                filter(Water.par_agua_fecha_hora >= datetime.strptime(sdate, '%m-%d-%y')).\
            filter(Water.par_agua_fecha_hora <= datetime.strptime(edate, '%m-%d-%y'))\
            .order_by(Water.par_agua_fecha_hora.asc())

    else:
        ob = db.session.query(Water).filter_by(par_agua_cod_drone=drone_id)

    data = {}
    i = 0
    for obj in ob:
        data[i] = {'drone_id': obj.par_agua_cod_drone,
                   'fecha': obj.par_agua_fecha_hora,
                   'lat': obj.par_agua_sw_lat,
                   'log': obj.par_agua_sw_log,
                   'alt': obj.par_agua_sw_alt,
                   'fecha': obj.par_agua_fecha_hora
                   }

        i += 1

    return(data)


######## SW SENSOR ########

def water_sw():

    db.Base.metadata.create_all(db.engine)
    ob = db.session.query(Water).all()
    data = {}
    i = 0
    for obj in ob:
        data[i] = {'drone_id': obj.par_agua_cod_drone,
                    'date': obj.par_agua_fecha_hora,
                   'sw_pm': obj.par_agua_sw_pm,
                   'sw_ph': obj.par_agua_sw_ph,
                   'sw_od': obj.par_agua_sw_od,
                   'sw_ce': obj.par_agua_sw_ce,
                   'sw_orp': obj.par_agua_sw_orp,
                   'sw_temp': obj.par_agua_sw_temp}

        i += 1

    return (data)


def water_sw_id_and_date(drone_id, sdate, edate):

    if sdate and edate:
        ob = db.session.query(Water).filter(Water.par_agua_cod_drone == drone_id).\
                filter(Water.par_agua_fecha_hora >= datetime.strptime(sdate, '%m-%d-%y')).\
            filter(Water.par_agua_fecha_hora <= datetime.strptime(edate, '%m-%d-%y'))\
            .order_by(Water.par_agua_fecha_hora.asc())

    else:
        ob = db.session.query(Water).filter_by(par_agua_cod_drone=drone_id)

    data = {}
    i = 0
    for obj in ob:
        data[i] = {
                    'date': obj.par_agua_fecha_hora,
                   'sw_pm': obj.par_agua_sw_pm,
                   'sw_ph': obj.par_agua_sw_ph,
                   'sw_od': obj.par_agua_sw_od,
                   'sw_ce': obj.par_agua_sw_ce,
                   'sw_orp': obj.par_agua_sw_orp,
                   'sw_temp': obj.par_agua_sw_temp}

        i += 1

    return (data)


######## SWIONS SENSOR ########

def water_swions():

    db.Base.metadata.create_all(db.engine)
    ob = db.session.query(Water).all()
    data = {}
    i = 0
    for obj in ob:
        data[i] = {'drone_id': obj.par_agua_cod_drone,
                    'date': obj.par_agua_fecha_hora,
                   'swions_pm': obj.par_agua_swions_pm,
                    'swions_no3_conc': obj.par_agua_swions_no3_conc,
                    'swions_nh4_conc': obj.par_agua_swions_nh4_conc,
                    'swions_temp': obj.par_agua_swions_temp}

        i += 1

    return (data)


def water_swions_id_and_date(drone_id, sdate, edate):

    if sdate and edate:
        ob = db.session.query(Water).filter(Water.par_agua_cod_drone == drone_id).\
                filter(Water.par_agua_fecha_hora >= datetime.strptime(sdate, '%m-%d-%y')).\
            filter(Water.par_agua_fecha_hora <= datetime.strptime(edate, '%m-%d-%y'))\
            .order_by(Water.par_agua_fecha_hora.asc())

    else:
        ob = db.session.query(Water).filter_by(par_agua_cod_drone=drone_id)

    data = {}
    i = 0
    for obj in ob:
        data[i] = {'drone_id': obj.par_agua_cod_drone,
                    'fecha': obj.par_agua_fecha_hora,
                   'swions_pm': obj.par_agua_swions_pm,
                    'swions_no3_conc': obj.par_agua_swions_no3_conc,
                    'swions_nh4_conc': obj.par_agua_swions_nh4_conc,
                    'swions_temp': obj.par_agua_swions_temp}

        i += 1

    return (data)


######## SWXTR SENSOR ########

def water_swxtr():

    db.Base.metadata.create_all(db.engine)
    ob = db.session.query(Water).all()
    data = {}
    i = 0
    for obj in ob:
        data[i] = {'drone_id': obj.par_agua_cod_drone,
                    'date': obj.par_agua_fecha_hora,
                   'swxtr_pm': obj.par_agua_swxtr_pm,
        'swxtr_od_sat': obj.par_agua_swxtr_od_sat,
        'swxtr_od_ppm': obj.par_agua_swxtr_od_ppm,
        'swxtr_od_temp': obj.par_agua_swxtr_od_temp,
        'swxtr_ntu_ntu': obj.par_agua_swxtr_ntu_ntu,
        'swxtr_ntu_temp': obj.paragua_swxtr_ntu_temp,
        'swxtr_sac_temp': obj.par_agua_swxtr_sac_temp}

        i += 1

    return (data)

def water_swxtr_id_and_date(drone_id, sdate, edate):

    if sdate and edate:
        ob = db.session.query(Water).filter(Water.par_agua_cod_drone == drone_id).\
                filter(Water.par_agua_fecha_hora >= datetime.strptime(sdate, '%m-%d-%y')).\
            filter(Water.par_agua_fecha_hora <= datetime.strptime(edate, '%m-%d-%y'))\
            .order_by(Water.par_agua_fecha_hora.asc())

    else:
        ob = db.session.query(Water).filter_by(par_agua_cod_drone=drone_id)

    data = {}
    i = 0
    for obj in ob:
        data[i] = {'date': obj.par_agua_fecha_hora,
                   'swxtr_pm': obj.par_agua_swxtr_pm,
                   'swxtr_od_sat': obj.par_agua_swxtr_od_sat,
                   'swxtr_od_ppm': obj.par_agua_swxtr_od_ppm,
                   'swxtr_od_temp': obj.par_agua_swxtr_od_temp,
                   'swxtr_ntu_ntu': obj.par_agua_swxtr_ntu_ntu,
                   'swxtr_ntu_temp': obj.paragua_swxtr_ntu_temp,
                   'swxtr_sac_temp': obj.par_agua_swxtr_sac_temp}

        i += 1

    return (data)