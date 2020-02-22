# encoding:utf-8
# FileName: main
# Author:   xiaoyi | 小一
# email:    1010490079@qq.com
# Date:     2020/2/22 21:05
# Description: 分析疫情数据| 拐点来了吗？
import os

from plot_data import plot_map, plot_line_chart
from preprocess import summary_data
from read_data import read_latest_data, read_all_data

if __name__ == '__main__':
    # 读取数据
    df_data = read_all_data('province')
    # 汇总每天的全国成绩
    df_result_all = summary_data(df_data, 'all')
    df_result_excep_HB = summary_data(df_data, 'excep_HB')
    df_result_HB = summary_data(df_data, 'HB')

    line_chart_title = [
        '累计确诊人数 (by:『知秋小梦』)',
        '新增确诊人数 (by:『知秋小梦』)',
        '累计治愈人数 (by:『知秋小梦』)',
        '累计死亡人数 (by:『知秋小梦』)',
        '治愈率 (by:『知秋小梦』)',
        '死亡率 (by:『知秋小梦』)'
    ]

    # 绘制折线图
    plot_line_chart('全国数据', line_chart_title, df_result_all)
    plot_line_chart('全国数据（除湖北省）', line_chart_title, df_result_excep_HB)
    plot_line_chart('湖北省数据', line_chart_title, df_result_HB)

    # 获取最新日期的疫情数据
    latest_date, df_latest_province_data = read_latest_data('province')
    # 筛选绘图数据
    list_curr_data = df_latest_province_data.iloc[:, [1, 2]].values.tolist()
    list_all_data = df_latest_province_data.iloc[:, [1, 3]].values.tolist()

    path_dir = r'D:\note\data_source\ncp_data'
    plot_map(list_all_data, df_latest_province_data,
             '截止' + latest_date + '中国累计确诊人数分布地图  (by:『知秋小梦』)',
             os.path.join(path_dir, '累计确诊人数分布地图.png'))
    plot_map(list_curr_data, df_latest_province_data,
             '截止' + latest_date + '中国当前确诊人数分布地图  (by:『知秋小梦』)',
             os.path.join(path_dir, '当前确诊人数分布地图.png'))