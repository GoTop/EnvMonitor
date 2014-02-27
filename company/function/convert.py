#coding=utf-8
__author__ = 'GoTop'

from company.models import Company, Station
from company.db_baise_models import T_Compinfo, T_AllStation, T_Adminarea
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def get_company_info_func():
    """
    从DB_balse数据库的T_Compinfo表中读取监测点位的信息，
    保存到EnvMonitor数据库Company的表中
    """
    all_t_company = T_Compinfo.objects.all()
    for t_company in all_t_company:
        new_company = Company(name=t_company.station_name,
                              tel=t_company.tel,
                              organ_code=t_company.organcode,
                              fax=t_company.fax,
                              post_code=t_company.postcode,
                              law_person=t_company.lawperson,
                              email=t_company.email,
                              setup_time=t_company.setuptime,
                              contact=t_company.contactman,
                              address=t_company.address
        )

        new_company.save()
        return all_t_company


def get_station_info_func():
    """
    从DB_balse数据库的T_Allstation表中读取监测点位的信息，
    保存到EnvMonitor数据库的Station表中
    """


    #all_t_station = T_Adminarea.objects.using('DB_baise').all()

    all_t_station = T_AllStation.objects.using('DB_baise').all()
    for t_station in all_t_station:
        t_station.station_name = t_station.station_name.encode('utf-8')

    if t_station.kind_id == '32':
        type = 'water'
    else:
        type = 'gas'

        new_station = Station(mn=t_station.station_id,
                              name=t_station.station_name,
                              type=type,
        )
        new_station.save()
    return all_t_station
