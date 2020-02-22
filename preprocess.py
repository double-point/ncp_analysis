# encoding:utf-8
# FileName: reshapa_data
# Author:   xiaoyi | 小一
# email:    1010490079@qq.com
# Date:     2020/2/22 14:59
# Description: 为画图准备数据


def summary_data(df_data, tag='all'):
    """
    汇总天粒度数据
    @param df_data:
    @param tag:
    @return:
    """
    """区分湖北省和非湖北省数据"""
    if tag == 'HB':
        df_data = df_data[df_data['province'] == '湖北']
    elif tag == 'excep_HB':
        df_data = df_data[~(df_data['province'] == '湖北')]

    # 对2月12号之前的当前确认人数用累计确诊人数填充
    df_data['curr_diagnose'][df_data['date'] < '2020-02-12'] = df_data['sum_diagnose'][df_data['date']<'2020-02-12']
    # 通过分组计算出每天全国的累计确诊人数、治愈人数、死亡人数
    df_result = df_data[['sum_diagnose', 'curr_diagnose', 'cure', 'death', 'date']].groupby('date', as_index=False).sum()
    # 计算百分比
    df_result['cure_per'] = df_result['cure']/df_result['sum_diagnose']*100
    df_result['death_per'] = df_result['death']/df_result['sum_diagnose']*100
    # 计算每日新增确诊人数（累计确诊人数的一阶差分）
    df_result['curr_new'] = df_result['sum_diagnose'].diff()[1:]
    # 填充上一步产生的空值
    df_result.fillna(0, inplace=True)

    return df_result


if __name__ == '__main__':
    pass