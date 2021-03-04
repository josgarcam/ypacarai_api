from models import Drones
import db


def drones_all():
    db.Base.metadata.create_all(db.engine)
    ob = db.session.query(Drones).all()
    i = 0
    data = {}
    for obj in ob:
        data[i] = {'drone_id': obj.drn_cod_drones,
                    'name': obj.drn_caracteristicas}
        i += 1

    return (data)

def drones_id(id):

    db.Base.metadata.create_all(db.engine)
    ob = db.session.query(Drones).filter_by(drn_cod_drones=id)
    data = {}
    for obj in ob:
        data[int(obj.drn_cod_drones)] = {'name': obj.drn_caracteristicas}

    return (data)
