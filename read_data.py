# encoding:utf-8
# FileName: read_data
# Author:   xiaoyi | 小一
# email:    1010490079@qq.com
# Date:     2020/2/21 19:24
# Description: 从数据库中读取省份和地市数据
from datetime import datetime, timedelta

import pandas as pd
from sqlalchemy import create_engine


def read_all_data(tag='province'):
    """
    读取所有数据
    @param tag:
    @return:
    """
    # 连接数据库
    connect = create_engine('mysql+pymysql://username:password@localhost:3306/dbname?charset=utf8')

    if tag == 'province':
        sql = 'select * from t_ncp_province_info'
    else:
        sql = 'select * from t_ncp_city_info'

    df_data = pd.read_sql_query(sql, connect)

    return df_data


def read_latest_data(tag='province'):
    """
    读取最新的数据
    @param tag:
    @return:
    """
    # 连接数据库
    connect = create_engine('mysql+pymysql://username:password@localhost:3306/dbname?charset=utf8')

    # 获取数据库最新日期
    sql = 'select max(date) as date from t_ncp_province_info'
    latest_date = pd.read_sql_query(sql, connect)['date'][0]

    if tag == 'province':
        sql = 'select * from t_ncp_province_info where date="{0}"'.format(latest_date)
    else:
        sql = 'select * from t_ncp_city_info where date="{0}"'.format(latest_date)

    df_data = pd.read_sql_query(sql, connect)

    return latest_date, df_data


if __name__ == '__main__':
    pass