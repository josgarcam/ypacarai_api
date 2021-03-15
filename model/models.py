from model import db

from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, Boolean


class Water(db.Base):
    __tablename__ = 'parametros_agua'

    par_agua_cod_parametro = Column(Integer, primary_key=True)
    par_agua_fecha_hora = Column(Date)
    par_agua_cod_drone = Column(Integer)
    par_agua_dron_nivel_bateria = Column(Float)
    par_agua_sw_lat = Column(Float)
    par_agua_sw_log = Column(Float)
    par_agua_sw_alt = Column(Float)
    par_agua_sw_pm = Column(Float)
    par_agua_sw_ph = Column(Float)
    par_agua_sw_od = Column(Float)
    par_agua_sw_ce = Column(Float)
    par_agua_sw_orp = Column(Float)
    par_agua_sw_temp = Column(Float)
    par_agua_sw_ph_volt = Column(Float)
    par_agua_sw_od_volt = Column(Float)
    par_agua_sw_ce_res = Column(Float)
    par_agua_sw_orp_volt = Column(Float)
    par_agua_sw_nivel_bateria = Column(Float)
    par_agua_swions_pm = Column(Integer)
    par_agua_swions_no3_conc = Column(Float)
    par_agua_swions_nh4_conc = Column(Float)
    par_agua_swions_temp = Column(Float)
    par_agua_swions_no3_volt = Column(Float)
    par_agua_swions_nh4_volt = Column(Float)
    par_agua_swions_nivel_bateria = Column(Float)
    par_agua_swxtr_pm = Column(Integer)
    par_agua_swxtr_od_sat = Column(Float)
    par_agua_swxtr_od_ppm = Column(Float)
    par_agua_swxtr_od_temp = Column(Float)
    par_agua_swxtr_od_ppm = Column(Float)
    par_agua_swxtr_ntu_ntu = Column(Float)
    paragua_swxtr_ntu_temp = Column(Float)
    par_agua_swxtr_sac_dbo = Column(Float)
    par_agua_swxtr_sac_dqo = Column(Float)
    par_agua_swxtr_sac_cot = Column(Float)
    par_agua_swxtr_sac_fau = Column(Float)
    par_agua_swxtr_sac_temp = Column(Float)
    par_agua_swxtr_sac_sac = Column(Float)
    par_agua_swxtr_nivel_bateria = Column(Float)

    def __init__(self, par_agua_cod_parametro, par_agua_fecha_hora, par_agua_cod_drone, par_agua_dron_nivel_bateria,
                 par_agua_sw_lat,
                 par_agua_sw_log, par_agua_sw_alt, par_agua_sw_pm, par_agua_sw_ph, par_agua_sw_od, par_agua_sw_ce,
                 par_agua_sw_orp,
                 par_agua_sw_temp, par_agua_sw_ph_volt, par_agua_sw_od_volt, par_agua_sw_ce_res,
                 par_agua_sw_orp_volt,
                 par_agua_sw_nivel_bateria, par_agua_swions_pm, par_agua_swions_no3_conc, par_agua_swions_nh4_conc,
                 par_agua_swions_temp,
                 par_agua_swions_no3_volt, par_agua_swions_nh4_volt, par_agua_swions_nivel_bateria, par_agua_swxtr_pm,
                 par_agua_swxtr_od_sat,
                 par_agua_swxtr_od_ppm, par_agua_swxtr_od_temp, par_agua_swxtr_ntu_ntu,
                 paragua_swxtr_ntu_temp,
                 par_agua_swxtr_sac_dbo, par_agua_swxtr_sac_dqo, par_agua_swxtr_sac_cot, par_agua_swxtr_sac_fau,
                 par_agua_swxtr_sac_temp,
                 par_agua_swxtr_sac_sac, par_agua_swxtr_nivel_bateria):

        self.par_agua_cod_parametro = par_agua_cod_parametro
        self.par_agua_fecha_hora = par_agua_fecha_hora
        self.par_agua_cod_drone = par_agua_cod_drone
        self.par_agua_dron_nivel_bateria = par_agua_dron_nivel_bateria
        self.par_agua_sw_lat = par_agua_sw_lat
        self.par_agua_sw_log = par_agua_sw_log
        self.par_agua_sw_alt = par_agua_sw_alt
        self.par_agua_sw_pm = par_agua_sw_pm
        self.par_agua_sw_ph = par_agua_sw_ph
        self.par_agua_sw_od = par_agua_sw_od
        self.par_agua_sw_ce = par_agua_sw_ce
        self.par_agua_sw_orp = par_agua_sw_orp
        self.par_agua_sw_temp = par_agua_sw_temp
        self.par_agua_sw_ph_volt = par_agua_sw_ph_volt
        self.par_agua_sw_od_volt = par_agua_sw_od_volt
        self.par_agua_sw_ce_res = par_agua_sw_ce_res
        self.par_agua_sw_orp_volt = par_agua_sw_orp_volt
        self.par_agua_sw_nivel_bateria = par_agua_sw_nivel_bateria
        self.par_agua_swions_pm = par_agua_swions_pm
        self.par_agua_swions_no3_conc = par_agua_swions_no3_conc
        self.par_agua_swions_nh4_conc = par_agua_swions_nh4_conc
        self.par_agua_swions_temp = par_agua_swions_temp
        self.par_agua_swions_no3_volt = par_agua_swions_no3_volt
        self.par_agua_swions_nh4_volt = par_agua_swions_nh4_volt
        self.par_agua_swions_nivel_bateria = par_agua_swions_nivel_bateria
        self.par_agua_swxtr_pm = par_agua_swxtr_pm
        self.par_agua_swxtr_od_sat = par_agua_swxtr_od_sat
        self.par_agua_swxtr_od_ppm = par_agua_swxtr_od_ppm
        self.par_agua_swxtr_od_temp = par_agua_swxtr_od_temp
        self.par_agua_swxtr_pm = par_agua_swxtr_pm
        self.par_agua_swxtr_ntu_ntu = par_agua_swxtr_ntu_ntu
        self.paragua_swxtr_ntu_temp = paragua_swxtr_ntu_temp
        self.par_agua_swxtr_sac_dbo = par_agua_swxtr_sac_dbo
        self.par_agua_swxtr_sac_dqo = par_agua_swxtr_sac_dqo
        self.par_agua_swxtr_sac_cot = par_agua_swxtr_sac_cot
        self.par_agua_swxtr_sac_fau = par_agua_swxtr_sac_fau
        self.par_agua_swxtr_sac_temp = par_agua_swxtr_sac_temp
        self.par_agua_swxtr_sac_sac = par_agua_swxtr_sac_sac
        self.par_agua_swxtr_nivel_bateria = par_agua_swxtr_nivel_bateria


    def __repr__(self):
        # return f'Water({self.paragua_codparametro}, {self.paragua_coddrone})'
        result = [{"id": self.par_agua_cod_parametro,
                  "temp": self.par_agua_sw_temp}]
        return result

    def __str__(self):
        return self.paragua_codparametro

    def imprime(self):
        print("Hola mundo")


class Drones(db.Base):
    __tablename__ = 'drones'

    dro_id_drone = Column(Integer, primary_key=True)
    dro_drone_features = Column(String)


class Navegacion(db.Base):
    __tablename__ = 'navegacion'

    nav_id = Column(Integer, primary_key=True)
    nav_date = Column(Date)
    nav_id_drone = Column(Integer)
    nav_latitude = Column(Float)
    nav_longitude = Column(Float)
    nav_altitude = Column(Float)
    nav_nivel_bateria = Column(Float)
    nav_id_movement = Column(Integer)


class Air(db.Base):
    __tablename__ = 'parametros_aire'

    par_aire_cod_parametro = Column(Integer, primary_key=True)
    par_aire_fecha_hora = Column(Date)
    par_aire_cod_drones = Column(Integer)
    par_aire_sepro_lat = Column(Float)
    par_aire_sepro_log = Column(Float)
    par_aire_sepro_alt = Column(Float)
    par_aire_dron_nivel_bateria = Column(Float)
    par_aire_sepro_pm = Column(Integer)
    par_aire_sepro_c02 = Column(Float)
    par_aire_sepro_h2s = Column(Float)
    par_aire_sepro_o3 = Column(Float)
    par_aire_sepro_hr = Column(Float)
    par_aire_sepro_pres = Column(Float)
    par_aire_sepro_temp = Column(Float)


class Measurement(db.Base):
    __tablename__ = 'measurement'

    mea_date = Column(Date)
    mea_id_drone = Column(Integer)
    mea_latitude = Column(Float)
    mea_altitude = Column(Float)
    mea_longitude = Column(Float)
    mea_id_measurement = Column(Integer, primary_key=True)
    mea_id_movement = Column(Integer)


class Sw(db.Base):
    __tablename__ = 'sw_sensor'

    sw_id = Column(Integer, primary_key=True)
    sw_pm = Column(Float)
    sw_ph = Column(Float)
    sw_od = Column(Float)
    sw_ce = Column(Float)
    sw_orp = Column(Float)
    sw_temper = Column(Float)
    sw_ph_volt = Column(Float)
    sw_od_volt = Column(Float)
    sw_ce_res = Column(Float)
    sw_orp_volt = Column(Float)
    sw_nivel_bateria = Column(Float)
    sw_id_measurement = Column(Integer, ForeignKey('id_measurement'))


class Swions(db.Base):
    __tablename__ = 'swions_sensor'

    swi_id = Column(Integer, primary_key=True)
    swi_pm = Column(Float)
    swi_no3_conc = Column(Float)
    swi_nh4_conc = Column(Float)
    swi_temper = Column(Float)
    swi_no3_volt = Column(Float)
    swi_nh4_volt = Column(Float)
    swi_nivel_bateria = Column(Float)
    swi_id_measurement = Column(Integer, ForeignKey('id_measurement'))


class Swxtr(db.Base):
    __tablename__ = 'swxtr_sensor'

    swx_id = Column(Integer, primary_key=True)
    swx_pm = Column(Float)
    swx_od_sat = Column(Float)
    swx_od_ppm = Column(Float)
    swx_od_temp = Column(Float)
    swx_ntu_ntu = Column(Float)
    swx_ntu_temp = Column(Float)
    swx_sac_dbo = Column(Float)
    swx_sac_dqo = Column(Float)
    swx_sac_cot = Column(Float)
    swx_sac_fau = Column(Float)
    swx_sac_temp = Column(Float)
    swx_sac_sac = Column(Float)
    swx_nivel_bateria = Column(Float)
    swx_id_measurement = Column(Integer, ForeignKey('id_measurement'))


class Sepro(db.Base):
    __tablename__ = 'sepro_sensor'

    sep_id = Column(Integer, primary_key=True)
    sep_pm = Column(Float)
    sep_c02 = Column(Float)
    sep_h2s = Column(Float)
    sep_o3 = Column(Float)
    sep_hr = Column(Float)
    sep_pres = Column(Float)
    sep_temper = Column(Float)
    sep_nivel_bateria = Column(Float)
    sep_id_measurement = Column(Integer, ForeignKey('id_measurement'))


class Seasons(db.Base):
    __tablename__ = 'seasons'

    sea_id_movement = Column(Integer, primary_key=True)
    sea_season_id = Column(Integer)
    sea_deployment_id = Column(Integer)
    sea_mission_id = Column(Integer)
    sea_mission_value = Column(Boolean)
    sea_season_descp = Column(String)
    sea_deployment_descp = Column(String)
    sea_mission_descp = Column(String)

