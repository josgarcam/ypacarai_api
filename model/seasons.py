from model.models import Seasons
from model import db

def seasons_all():
    db.Base.metadata.create_all(db.engine)
    ob = db.session.query(Seasons).all()

    data = {}
    i = 0
    for obj in ob:
        data[i] = {'id_movement': obj.sea_id_movement,
                   'season_id': obj.sea_season_id,
                   'deployment_id': obj.sea_deployment_id,
                   'mission_id': obj.sea_mission_id,
                   'mission_value': obj.sea_mission_value,
                   'season_descp': obj.sea_season_descp,
                   'deployment_descp': obj.sea_deployment_descp,
                   'mission_descp': obj.sea_mission_descp
                   }
        i += 1

    return (data)

def seasons_season(season_id, deployment, mission_id):
    db.Base.metadata.create_all(db.engine)

    if deployment:
        if mission_id:
            ob = db.session.query(Seasons).filter(Seasons.sea_season_id == season_id). \
                filter(Seasons.sea_deployment_id == deployment).filter(Seasons.sea_mission_id == mission_id)
        else:
            ob = db.session.query(Seasons).filter(Seasons.sea_season_id == season_id). \
                filter(Seasons.sea_deployment_id == deployment)

    else:
        if mission_id:
            ob = db.session.query(Seasons).filter(Seasons.sea_season_id == season_id). \
                filter(Seasons.sea_mission_id == mission_id)
        else:
            ob = db.session.query(Seasons).filter(Seasons.sea_season_id == season_id)

    data = {}
    i = 0
    for obj in ob:
        data[i] = {'id_movement': obj.sea_id_movement,
                   'deployment_id': obj.sea_deployment_id,
                   'mission_id': obj.sea_mission_id,
                   'mission_value': obj.sea_mission_value,
                   'season_descp': obj.sea_season_descp,
                   'deployment_descp': obj.sea_deployment_descp,
                   'mission_descp': obj.sea_mission_descp
                   }
        i += 1

    return (data)