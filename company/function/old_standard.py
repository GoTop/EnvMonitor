# coding=utf-8
from __future__ import unicode_literals
from company.models import Station

__author__ = 'GoTop'


def get_sugar_old_standard(mn_list):
    """
    获取糖厂的旧标准信息
    """
    station_old_standard_info = []
    for mn in mn_list:
        station_old_standard_info.append(
            get_water_station_old_standard_info(mn, '20141001', 100, 0, 8, 0))
    return station_old_standard_info


def get_power_plant_old_standard(mn_list):
    """
    获取电厂的旧标准信息
    """
    station_old_standard_info = []
    for mn in mn_list:
        station_old_standard_info.append(
            get_gas_station_old_standard_info(mn, '20140701', 400, 0, 450, 0))
    return station_old_standard_info


def get_water_station_old_standard_info(mn, standard_change_date, CODcr_standard_max, CODcr_standard_min,
                                        NH_standard_max, NH_standard_min):
    """
    设置mn 废水监控点位旧的排放标准
    """
    t_station = Station.objects.get(station_id=mn)
    old_standard_info = {
        'station_name': t_station.name,
        'mn': mn,
        'old_standard':
            {
                #就标准改为新标准的日期（该日期使用新标准）
                'standard_change_date': standard_change_date,
                'CODcr':
                    {
                        'standard_max': CODcr_standard_max,
                        'standard_min': CODcr_standard_min
                    },

                'NH':
                    {
                        'standard_max': NH_standard_max,
                        'standard_min': NH_standard_min
                    }
            }
    }

    return old_standard_info


def get_gas_station_old_standard_info(mn, standard_change_date, SO2_standard_max, SO2_standard_min, NOx_standard_max,
                                      NOx_standard_min
):
    """
    设置mn 废气监控点位旧的排放标准
    """
    t_station = Station.objects.get(station_id=mn)
    old_standard_info = {
        'station_name': t_station.name,
        'mn': mn,
        'old_standard':
            {
                #就标准改为新标准的日期（该日期使用新标准）
                'standard_change_date': standard_change_date,
                'SO2':
                    {
                        'standard_max': SO2_standard_max,
                        'standard_min': SO2_standard_min
                    },

                'NOx':
                    {
                        'standard_max': NOx_standard_max,
                        'standard_min': NOx_standard_min
                    }
            }
    }

    return old_standard_info


def get_special_standard():
    """
    获取特殊点位的旧标准信息
    """
    station_old_standard_info = []

    #广西百色银海发电有限公司
    station_old_standard_info.append(get_gas_station_old_standard_info('45007760002601', '20140701', 800, 0, 450, 0))
    #广西百色银海发电有限公司
    station_old_standard_info.append(get_gas_station_old_standard_info('45007760002602', '20140701', 800, 0, 450, 0))

    #田阳南华纸业有限公司
    station_old_standard_info.append(get_gas_station_old_standard_info('45007760001303', '20140701', 800, 0, 450, 0))

    #田东锦盛化工有限公司
    station_old_standard_info.append(get_gas_station_old_standard_info('45007760004402', '20140701', 400, 0, 650, 0))
    #田东电厂
    station_old_standard_info.append(get_gas_station_old_standard_info('45007760001901', '20140701', 400, 0, 650, 0))

    #中国铝业股份有限公司广西分公司(4＃)
    station_old_standard_info.append(get_gas_station_old_standard_info('45007760002007', '20140701', 400, 0, 650, 0))
    #中国铝业股份有限公司广西分公司(5＃)
    station_old_standard_info.append(get_gas_station_old_standard_info('45007760002008', '20140701', 400, 0, 650, 0))

    #本地测试用
    #station_old_standard_info.append(get_water_station_old_standard_info('45007760002801', '20140701', 20, 0, 2, 0))

    return station_old_standard_info


#田东锦盛化工有限公司


def format_old_standard_info():
    """
    获取各种企业的旧标准信息
    """
    station_old_standard_info = []

    #2014年国控糖厂
    sugar_2014_nation_supervise = ['45007760000201',
                                   '45007760000801',
                                   '45007760001401',
                                   '45007760001601',
                                   '45007760001701',
                                   '45007760000401',
                                   '45007760005001',
    ]
    station_old_standard_info.extend(get_sugar_old_standard(sugar_2014_nation_supervise))

    #中铝678，华银铝12345
    power_plant_2014_nation_supervise = ['45007760002004',
                                         '45007760002005',
                                         '45007760002006',
                                         '45007760002501',
                                         '45007760002502',
                                         '45007760002503',
                                         '45007760002504',
                                         '45007760002505',
    ]
    station_old_standard_info.extend(get_power_plant_old_standard(power_plant_2014_nation_supervise))

    station_old_standard_info.extend(get_special_standard())

    #构造出标准的现实文本，比如 0-60
    for old_standard_info in station_old_standard_info:
        for param, standard_info in old_standard_info['old_standard'].iteritems():
            #key 'standard_change_date'也在old_standard字典下，但其没有standard_min和standard_max的item，记得跳过
            if param <> 'standard_change_date':
                standard_info['text'] = str(standard_info['standard_min']) + '-' + str(
                    standard_info['standard_max'])

    return station_old_standard_info


def get_old_standard(mn):
    """
    在旧标准列表中查找指定mn的监控点位的旧标准信息
    """
    all_station_old_standard_info = format_old_standard_info()
    for old_standard_info in all_station_old_standard_info:
        if old_standard_info.get('mn') == mn:
            return old_standard_info
