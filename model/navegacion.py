from datetime import datetime

from model.models import Navegacion, Seasons
from model import db


def navegacion_all():
    db.Base.metadata.create_all(db.engine)
    ob = db.session.query(Navegacion).all()
    data = {}
    i = 0
    for obj in ob:
        data[i] = {'drone_id': obj.nav_id_drone,
                   'latitude': obj.nav_latitude,
                   'longitude': obj.nav_longitude,
                   'altitude': obj.nav_altitude,
                   'date': obj.nav_date}
        i += 1

    return (data)


def navegacion_drone_id_and_date(drone_id, sdate, edate):

    if sdate and edate:
        ob = db.session.query(Navegacion).filter(Navegacion.nav_id_drone == drone_id). \
            filter(Navegacion.nav_date >= datetime.strptime(sdate, '%m-%d-%y')). \
            filter(Navegacion.nav_date <= datetime.strptime(edate, '%m-%d-%y')) \
            .order_by(Navegacion.nav_date.asc())

    else:
        ob = db.session.query(Navegacion).filter_by(nav_id_drone=drone_id)

    data = {}
    i = 0
    for obj in ob:
        data[i] = {'latitude': obj.nav_latitude,
                   'longitude': obj.nav_longitude,
                   'altitude': obj.nav_altitude,
                   'date': obj.nav_date}
        i += 1

    return (data)

def navegacion_season(season, deployment, drone_id):
    db.Base.metadata.create_all(db.engine)

    if deployment:
        if drone_id:
            ob = db.session.query(Navegacion, Seasons).join(Seasons, Navegacion.nav_id_movement == Seasons.sea_id_movement).\
                filter(Seasons.sea_season_id == season).filter(Seasons.sea_deployment_id == deployment).\
                filter(Navegacion.nav_id_drone == drone_id)
        else:
            ob = db.session.query(Navegacion, Seasons).join(Seasons, Navegacion.nav_id_movement == Seasons.sea_id_movement). \
                filter(Seasons.sea_season_id == season).filter(Seasons.sea_deployment_id == deployment)
    else:
        if drone_id:
            ob = db.session.query(Navegacion, Seasons).join(Seasons, Navegacion.nav_id_movement == Seasons.sea_id_movement). \
                filter(Seasons.sea_season_id == season).filter(Navegacion.nav_id_drone == drone_id)
        else:
            ob = db.session.query(Navegacion, Seasons).join(Seasons, Navegacion.nav_id_movement == Seasons.sea_id_movement). \
                filter(Seasons.sea_season_id == season)

    data = {}
    i = 0
    for obj in ob:
        data[i] = {'date': obj.Navegacion.nav_date,
                   'latitude': obj.Navegacion.nav_latitude,
                   'altitude': obj.Navegacion.nav_altitude,
                   'longitude': obj.Navegacion.nav_longitude,
                   'id_drone': obj.Navegacion.nav_id_drone,
                   'deployment': obj.Seasons.sea_deployment_id,
                   }
        i += 1
    return (data)