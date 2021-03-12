from datetime import datetime

from model.models import Navegacion
from model import db


def navegacion_all():
    db.Base.metadata.create_all(db.engine)
    ob = db.session.query(Navegacion).all()
    data = {}
    i = 0
    for obj in ob:
        data[i] = {'drone_id': obj.id_drone,
                   'latitude': obj.latitude,
                   'longitude': obj.longitude,
                   'altitude': obj.altitude,
                   'date': obj.date}
        i += 1

    return (data)


def navegacion_drone_id_and_date(drone_id, sdate, edate):

    if sdate and edate:
        ob = db.session.query(Navegacion).filter(Navegacion.id_drone == drone_id). \
            filter(Navegacion.date >= datetime.strptime(sdate, '%m-%d-%y')). \
            filter(Navegacion.date <= datetime.strptime(edate, '%m-%d-%y')) \
            .order_by(Navegacion.date.asc())

    else:
        ob = db.session.query(Navegacion).filter_by(id_drone=drone_id)

    data = {}
    i = 0
    for obj in ob:
        data[i] = {'latitude': obj.latitude,
                   'longitude': obj.longitude,
                   'altitude': obj.altitude,
                   'date': obj.date}
        i += 1

    return (data)