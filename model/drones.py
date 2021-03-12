from model.models import Drones
from model import db


def drones_all():
    db.Base.metadata.create_all(db.engine)
    ob = db.session.query(Drones).all()
    i = 0
    data = {}
    for obj in ob:
        data[i] = {'drone_id': obj.id_drone,
                   'name': obj.drone_features}
        i += 1

    return (data)

def drones_id(id_drone):
    db.Base.metadata.create_all(db.engine)
    ob = db.session.query(Drones).filter_by(id_drone=id_drone)
    i = 0
    data = {}
    for obj in ob:
        data[i] = {'descp': obj.drone_features}
        i += 1

    return (data)