from model.models import Seasons
from model import db

def seasons_all(season_id):
    db.Base.metadata.create_all(db.engine)
    ob = db.session.query(Seasons).filter(Seasons.season_id == season_id)

    data = {}
    i = 0
    for obj in ob:
        data[i] = {'id_movement': obj.id_movement,
                   'deployment_id': obj.deployment_id,
                   'mission_id': obj.mission_id,
                   'mission_value': obj.mission_value,
                   'season_descp': obj.season_descp,
                   'deployment_descp': obj.deployment_descp,
                   'mission_descp': obj.mission_descp
                   }
        i += 1

    return (data)

def seasons_season(season_id, deployment, mission_id):
    db.Base.metadata.create_all(db.engine)

    if deployment:
        if mission_id:
            ob = db.session.query(Seasons).filter(Seasons.season_id == season_id). \
                filter(Seasons.deployment_id == deployment).filter(Seasons.mission_id == mission_id)
        else:
            ob = db.session.query(Seasons).filter(Seasons.season_id == season_id). \
                filter(Seasons.deployment_id == deployment)

    else:
        if mission_id:
            ob = db.session.query(Seasons).filter(Seasons.season_id == season_id). \
                filter(Seasons.mission_id == mission_id)
        else:
            ob = db.session.query(Seasons).filter(Seasons.season_id == season_id)

    data = {}
    i = 0
    for obj in ob:
        data[i] = {'id_movement': obj.id_movement,
                   'deployment_id': obj.deployment_id,
                   'mission_id': obj.mission_id,
                   'mission_value': obj.mission_value,
                   'season_descp': obj.season_descp,
                   'deployment_descp': obj.deployment_descp,
                   'mission_descp': obj.mission_descp
                   }
        i += 1

    return (data)