# encoding:utf-8
# FileName: plot_data
# Author:   xiaoyi | 小一
# email:    1010490079@qq.com
# Date:     2020/2/22 11:12
# Description: 通过数据绘制各种图表
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot

# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)


def sns_set():
    """
    sns 相关设置
    @return:
    """
    # 声明使用 Seaborn 样式
    sns.set()
    # 有五种seaborn的绘图风格，它们分别是：darkgrid, whitegrid, dark, white, ticks。默认的主题是darkgrid。
    sns.set_style("whitegrid")
    # 有四个预置的环境，按大小从小到大排列分别为：paper, notebook, talk, poster。其中，notebook是默认的。
    sns.set_context('talk')
    # 中文字体设置-黑体
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 解决保存图像是负号'-'显示为方块的问题
    plt.rcParams['axes.unicode_minus'] = False
    # 解决Seaborn中文显示问题并调整字体大小
    sns.set(font='SimHei')

    return sns


def plot_line_chart(title, subtitles, df_data):
    """
    绘制折线图
    @param title:总标题
    @param subtitles:子图的子标题
    @param df_data:
    @return:
    """
    # 声明使用 Seaborn 样式
    sns = sns_set()
    # 对日期进行处理
    df_data['date'] = df_data['date'].apply(lambda x: x[-4:])
    # 设置x、y轴数据
    axis_x = df_data['date'].values.tolist()

    print(df_data)
    """画图"""
    figure, axes = plt.subplots(nrows=3, ncols=2, figsize=(6, 20))
    plt.suptitle(title)
    sns.lineplot(x='date', y='sum_diagnose', data=df_data, ax=axes[0, 0])
    sns.lineplot(x='date', y='curr_new', data=df_data, ax=axes[0, 1])
    sns.lineplot(x='date', y='cure', data=df_data, ax=axes[1, 0])
    sns.lineplot(x='date', y='death', data=df_data, ax=axes[1, 1])
    sns.lineplot(x='date', y='cure_per', data=df_data, ax=axes[2, 0])
    sns.lineplot(x='date', y='death_per', data=df_data, ax=axes[2, 1])

    # 设置每个图形的显示参数
    count = 0
    for i in range(3):
        for j in range(2):
            # Seaborn 需要通过 ax.set_title() 来添加 title
            axes[i, j].set_title(subtitles[count])
            # 设置 x/y 轴标签的字体大小和字体颜色
            axes[i, j].set_xlabel('', fontsize=10)
            if count>3:
                axes[i, j].set_ylabel('百分比', fontsize=10)
            else:
                axes[i, j].set_ylabel('人数', fontsize=10)

            # 设置坐标轴刻度旋转角度
            axes[i, j].set_xticklabels(axis_x, rotation=-60)
            # 设置坐标轴刻度的字体大小
            axes[i, j].tick_params(axis='x', labelsize=8)
            count += 1

    plt.show()


def plot_map(list_data, df_data, title, filepath_save):
    """
    绘制地图
    @param list_data:
    @param df_data:
    @param title:
    @param filepath_save:
    @return:
    """
    # 绘制地图
    ncp_map = (
        Map(init_opts=opts.InitOpts('1000px', '600px'))
        .add('', list_data, 'china')
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title=title,
                pos_left='center'
            ),
            visualmap_opts=opts.VisualMapOpts(
                # 设置为分段形数据显示
                is_piecewise=True,
                # 设置拖拽用的手柄
                is_calculable=True,
                # 设置数据最大值
                max_=df_data['sum_diagnose'].max(),
                # 自定义的每一段的范围，以及每一段的文字，以及每一段的特别的样式。
                pieces=[
                    {'min': 10001, 'label': '>10000', 'color': '#4F040A'},
                    {'min': 1000, 'max': 10000, 'label': '1000 - 10000', 'color': '#811C24'},
                    {'min': 500, 'max': 999, 'label': '500 - 999', 'color': '#CB2A2F'},
                    {'min': 100, 'max': 499, 'label': '100 - 499', 'color': '#E55A4E'},
                    {'min': 10, 'max': 99, 'label': '10 - 99', 'color': '#F59E83'},
                    {'min': 1, 'max': 9, 'label': '1 - 9', 'color': '#FDEBCF'},
                    {'min': 0, 'max': 0, 'label': '0', 'color': '#F7F7F7'}
                ]
            ),
        )
    )
    # 保存图片到本地
    make_snapshot(snapshot, ncp_map.render(), filepath_save)


if __name__ == '__main__':
    pass