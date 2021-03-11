from model import db

from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey


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

    drn_cod_drones = Column(Integer, primary_key=True)
    drn_caracteristicas = Column(String)

    def __init__(self, drn_cod_drones, drn_caracteristicas):

        self.drn_cod_drones = drn_cod_drones
        self.drn_caracteristicas = drn_caracteristicas



class Navegacion(db.Base):
    __tablename__ = 'navegacion'

    nav_cod_navegacion = Column(Integer, primary_key=True)
    nav_fecha_hora = Column(Date)
    nav_cod_drones = Column(Integer)
    nav_latitud = Column(Float)
    nav_longitud = Column(Float)
    nav_altura = Column(Float)
    nav_nivel_bateria_drones = Column(Float)

    def __init__(self, nav_cod_navegacion, nav_fecha_hora, nav_cod_drones, nav_latitud, nav_longitud, nav_altura,
                 nav_nivel_bateria_drones):
        self.nav_cod_navegacion = nav_cod_navegacion
        self.nav_fecha_hora = nav_fecha_hora
        self.nav_cod_drones = nav_cod_drones
        self.nav_latitud = nav_latitud
        self.nav_longitud = nav_longitud
        self.nav_altura = nav_altura
        self.nav_nivel_bateria_drones = nav_nivel_bateria_drones

########## AIRE ##########

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

    def __init__(self, par_aire_cod_parametro, par_aire_fecha_hora, par_aire_cod_drones, par_aire_sepro_lat, par_aire_sepro_log,
                 par_aire_sepro_alt, par_aire_sepro_pm, par_aire_sepro_c02, par_aire_sepro_h2s, par_aire_sepro_o3,
                 par_aire_sepro_hr, par_aire_sepro_pres, par_aire_sepro_temp, par_aire_dron_nivel_bateria):

        self.par_aire_cod_parametro = par_aire_cod_parametro
        self.par_aire_fecha_hora = par_aire_fecha_hora
        self.par_aire_cod_drones = par_aire_cod_drones
        self.par_aire_sepro_lat = par_aire_sepro_lat
        self.par_aire_sepro_log = par_aire_sepro_log
        self.par_aire_sepro_alt = par_aire_sepro_alt
        self.par_aire_sepro_pm = par_aire_sepro_pm
        self.par_aire_sepro_c02 = par_aire_sepro_c02
        self.par_aire_sepro_h2s = par_aire_sepro_h2s
        self.par_aire_sepro_o3 = par_aire_sepro_o3
        self.par_aire_sepro_hr = par_aire_sepro_hr
        self.par_aire_sepro_pres = par_aire_sepro_pres
        self.par_aire_sepro_temp = par_aire_sepro_temp
        self.par_aire_dron_nivel_bateria = par_aire_dron_nivel_bateria

class Measurement(db.Base):
    __tablename__ = 'measurement'

    date = Column(Date)
    id_drone = Column(Integer)
    latitude = Column(Float)
    altitude = Column(Float)
    longitude = Column(Float)
    id_measurement = Column(Integer, primary_key=True)
    season = Column(Integer)
    deployment = Column(Integer)

    def __init__(self, date, id_drone, latitude, altitude, longitude, id_measurement, season, deployment):

        self.date = date
        self.id_drone = id_drone
        self.latitude = latitude
        self.altitude = altitude
        self.longitude = longitude
        self.id_measurement = id_measurement
        self.season = season
        self.deployment = deployment

class Sw(db.Base):
    __tablename__ = 'sw_sensor'

    id = Column(Integer, primary_key=True)
    pm = Column(Float)
    ph = Column(Float)
    od = Column(Float)
    ce = Column(Float)
    orp = Column(Float)
    temper = Column(Float)
    ph_volt = Column(Float)
    od_volt = Column(Float)
    ce_res = Column(Float)
    orp_volt = Column(Float)
    id_measurement = Column(Integer, ForeignKey('id_measurement'))
    season = Column(Integer)
    deployment = Column(Integer)

    def __init__(self, pm, ph, od, ce, orp, temper, ph_volt, od_volt, ce_res, orp_volt, id_measurement, season, deployment):

        self.pm = pm
        self.ph = ph
        self.od = od
        self.ce = ce
        self.orp = orp
        self.temper = temper
        self.ph_volt = ph_volt
        self.od_volt = od_volt
        self.ce_res = ce_res
        self.orp_volt = orp_volt
        self.id_measurement = id_measurement
        self.season = season
        self.deployment = deployment

class Swions(db.Base):
    __tablename__ = 'swions_sensor'

    id = Column(Integer, primary_key=True)
    pm = Column(Float)
    no3_conc = Column(Float)
    nh4_conc = Column(Float)
    temper = Column(Float)
    no3_volt = Column(Float)
    nh4_volt = Column(Float)
    nivel_bateria = Column(Float)
    id_measurement = Column(Integer, ForeignKey('id_measurement'))
    season = Column(Integer)
    deployment = Column(Integer)

    def __init__(self, pm, no3_conc, nh4_conc, temper, no3_volt, nh4_volt, nivel_bateria, id_measurement, season, deployment):

        self.pm = pm
        self.no3_conc = no3_conc
        self.nh4_conc = nh4_conc
        self.temper = temper
        self.no3_volt = no3_volt
        self.nh4_volt = nh4_volt
        self.nivel_bateria = nivel_bateria
        self.id_measurement = id_measurement
        self.season = season
        self.deployment = deployment


class Swxtr(db.Base):
    __tablename__ = 'swxtr_sensor'

    id = Column(Integer, primary_key=True)
    pm = Column(Float)
    od_sat = Column(Float)
    od_ppm = Column(Float)
    od_temp = Column(Float)
    ntu_ntu = Column(Float)
    ntu_temp = Column(Float)
    sac_dbo = Column(Float)
    sac_dqo = Column(Float)
    sac_cot = Column(Float)
    sac_fau = Column(Float)
    sac_temp = Column(Float)
    sac_sac = Column(Float)
    nivel_bateria = Column(Float)
    id_measurement = Column(Integer, ForeignKey('id_measurement'))
    season = Column(Integer)
    deployment = Column(Integer)

    def __init__(self, pm, od_sat, od_ppm, od_temp, ntu_ntu, ntu_temp, sac_dbo, sac_dqo, sac_cot, sac_fau, sac_temp, sac_sac, nivel_bateria, id_measurement, season, deployment):
        self.pm = pm
        self.od_sat = od_sat
        self.od_ppm = od_ppm
        self.od_temp = od_temp
        self.ntu_ntu = ntu_ntu
        self.ntu_temp = ntu_temp
        self.sac_dbo = sac_dbo
        self.sac_dqo = sac_dqo
        self.sac_cot = sac_cot
        self.sac_fau = sac_fau
        self.sac_temp = sac_temp
        self.sac_sac = sac_sac
        self.nivel_bateria = nivel_bateria
        self.id_measurement = id_measurement
        self.season = season
        self.deployment = deployment


class Sepro(db.Base):
    __tablename__ = 'sepro_sensor'

    id = Column(Integer, primary_key=True)
    pm = Column(Float)
    c02 = Column(Float)
    h2s = Column(Float)
    o3 = Column(Float)
    hr = Column(Float)
    pres = Column(Float)
    temper = Column(Float)
    nivel_bateria = Column(Float)
    id_measurement = Column(Integer, ForeignKey('id_measurement'))
    season = Column(Integer)
    deployment = Column(Integer)

    def __init__(self, id, pm, c02, h2s, o3, hr, pres, temper, nivel_bateria, id_measurement, season, deployment):
        self.id = id
        self.pm = pm
        self.c02 = c02
        self.h2s = h2s
        self.o3 = o3
        self.hr = hr
        self.pres = pres
        self.temper = temper
        self.nivel_bateria = nivel_bateria
        self.id_measurement = id_measurement
        self.season = season
        self.deployment = deployment

