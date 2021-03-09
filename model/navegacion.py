from datetime import datetime

from model.models import Navegacion
from model import db


def navegacion_all():
    db.Base.metadata.create_all(db.engine)
    ob = db.session.query(Navegacion).all()
    data = {}
    i = 0
    for obj in ob:
        data[i] = {'drone_id': obj.nav_cod_drones,
                   'latitude': obj.nav_latitud,
                   'longitude': obj.nav_longitud,
                   'altitude': obj.nav_altura,
                   'date': obj.nav_fecha_hora}
        i += 1

    return (data)


def navegacion_drone_id_and_date(drone_id, sdate, edate):
    print(sdate)
    print(edate)
    if sdate and edate:
        ob = db.session.query(Navegacion).filter(Navegacion.nav_cod_drones == drone_id). \
            filter(Navegacion.nav_fecha_hora >= datetime.strptime(sdate, '%m-%d-%y')). \
            filter(Navegacion.nav_fecha_hora <= datetime.strptime(edate, '%m-%d-%y')) \
            .order_by(Navegacion.nav_fecha_hora.asc())

    else:
        ob = db.session.query(Navegacion).filter_by(nav_cod_drones=drone_id)

    data = {}
    i = 0
    for obj in ob:
        data[i] = {'latitude': obj.nav_latitud,
                   'longitude': obj.nav_longitud,
                   'altitude': obj.nav_altura,
                   'date': obj.nav_fecha_hora}
        i += 1

    return (data)

#
# def drones_id(id):
#
#     db.Base.metadata.create_all(db.engine)
#     ob = db.session.query(Navegacion).filter_by(drn_cod_drones=id)
#     data = {}
#     for obj in ob:
#         data[int(obj.drn_cod_drones)] = {'features': obj.drn_caracteristicas}
#
#     return (data)
