from urllib.request import urlopen, quote
import json
import numpy as np

from pyecharts import GeoLines, Style

#地图名称
map_name=['海军','空军','陆军','后勤']
#这里填路线名称，每个名称一行
cities_name_set=[['海军军士学校',
                 '海军军官学校',
                 '海军机械学校'],
                 ['中央航空学校',
                 '空军通信学校',
                 '中央航空机械学校',
                 '空军参谋学校',],
                 ['陆军军官学校',
                 '陆军装甲兵学校',
                 '陆军步兵学校',
                 '陆军炮兵学校',
                 '陆军大学',
                 '国防医学院'],
                 ['测绘学堂',
                 '兵工学校（兵工工程学院）',
                 '联勤经理学校 联勤财务学校',
                 '中央警官学校',
                 '宪兵学校',
                 '副官学校']]
#这里填路线，每个路线一行，用[]括起来，
location_sets=[[['南京', '高雄左营'],
               ['厦门','高雄左营'],
               ['上海','高雄左营']],
               [['杭州','高雄冈山'],
               ['成都','高雄冈山'],
               ['成都','高雄冈山'],
               ['南京','屏东东港']],
               [['成都','台北'],
               ['上海','台中'],
               ['贵州省','高雄县凤山镇'],
               ['沾益','高雄县凤山镇'],
               ['广州','桃园县'],
               ['上海江湾','台北水源区']],
               [['重庆','花莲'],
               ['吴淞','花莲'],
               ['漳州','台北'],
               ['南京','台北'],
               ['重庆','台北'],
               ['南京','台北']]]



def set_data(location_name_list):
    geo_cities_coords = {}
    for location in location_name_list:
        print(location)
        lat_long = get_location_coordinate(location)
        geo_cities_coords[location] = list(lat_long)

    plotting_data = []
    for i in range(len(location_name_list)):
        if i < len(location_name_list)-1:
            plotting_data.append((location_name_list[i], location_name_list[i+1]))
    return plotting_data, geo_cities_coords


def get_location_coordinate(location_name):

    api_url = 'http://api.map.baidu.com/geocoding/v3/?address='
    api_url = f'{api_url}{quote(location_name)}&output=json&ak=VUGV6qYafFslx9bgN3NybHSXh3U1Shgv'
    result = urlopen(api_url)
    result = json.loads(result.read().decode())['result']['location']
    return result['lng'], result['lat']


# 参考小文的
def plot_geolines(plot_set, coords_set, name_set, map_name):
    # 设置画布的格式
    style = Style(title_pos="center",
                  width=1000,
                  height=800)

    # 部分地理轨迹图的格式
    style_geolines = style.add(is_label_show=True,
                               line_curve=0.3,  # 轨迹线的弯曲度，0-1
                               line_opacity=0.6,  # 轨迹线的透明度，0-1
                               geo_effect_symbol='circle',  # 特效的图形，有circle,plane,pin等等
                               geo_effect_symbolsize=0,  # 特效图形的大小
                               geo_effect_color='#7FFFD4',  # 特效的颜色
                               geo_effect_traillength=0.1,  # 特效图形的拖尾效果，0-1
                               label_color=['#a6cee3','#1f78b4','#b2df8a','#33a02c','#fb9a99','#e31a1c','#fdbf6f','#ff7f00','#cab2d6','#6a3d9a','#ffff99'],
                                            #'#9933CC','#666699','#660066','#333366','#0066CC','#9900FF','#333399','#99CCFF','#9933FF','#330099','#6699FF','#9966CC','#3300CC','#003366','#330033','#3300FF'],
                               #label_color=['#FFA500', '#FFF68F'],  # 轨迹线的颜色，标签点的颜色，
                               border_color='#000000',  # 边界的颜色
                               geo_normal_color='#f6e8ce',  # 地图的颜色
                               label_formatter='{b}',  # 标签格式
                               legend_pos='left')

    # 作图
    geolines = GeoLines(map_name, **style.init_style)
    for plot, coord, name in zip(plot_set, coords_set, name_set):
        geolines.add(name,
                     plot,
                     maptype='china',  # 地图的类型，可以是省的地方，如'广东',也可以是地市，如'东莞'等等
                     geo_cities_coords=coord,
                     **style_geolines)


    # 发布，得到图形的html文件
    geolines.render('{}.html'.format(map_name))


if __name__ == '__main__':
    #location_sets=[['长沙', '广西', '洪江', '潼南', '徐州'],['重庆','上海','西屯','清泉岗','新竹']]
    plot_set=[]
    coord_set=[]
    #cities_name_set=['陆军交辎学校','装甲兵教导总队']
    #location_name_list_1 = ['长沙', '广西', '洪江', '潼南', '徐州']
    #location_name_list_2=['重庆','上海','西屯','清泉岗','新竹']
    #plot_data, cities_coords = set_data(location_name_list_1)
    # 绘制动态图
    #plot_geolines(plot_data, cities_coords, '陆军交辎学校')
    #plot_data_2, cities_coords_2 = set_data(location_name_list_2)
    for j in range(4):
        for i in location_sets[j]:
            plot_data, cities_coords = set_data(i)
            plot_set.append(plot_data)
            coord_set.append(cities_coords)

        plot_geolines(plot_set, coord_set, cities_name_set[j], map_name[j])
    print('ok，去浏览器看看吧')

