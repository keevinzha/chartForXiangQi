from pyecharts.charts import Map, Geo
from pyecharts import options as opts
from pyecharts.globals import ChartType,SymbolType

provience_dis={
    "长沙":(112.979352787651,28.2134782308532),"广西":(108.92427442705878,23.552254688119405),"洪江":(110.087193420965,27.239105321481),
               "潼南":(	105.819678845163,30.1499329659585),"徐州":(117.188106623177,34.2715534310919)}
list_key=list(provience_dis.keys())
list_value=list(provience_dis.values())
# 利用zip()函数生成由 <元组> 组成的 <列表>,list(z)为一个个元组，最后注意要加上[]成为列表
data_pro=[list(z) for z in zip(list_key,list_value)]
print(data_pro)

china=(
    Geo(init_opts=opts.InitOpts(width="1500px",height='1200px',page_title="成都人口流向图"))  # 初始化配置
    # 基本框架设置 参考 pyecharts-document-Geo
    .add_schema(maptype="china",
                is_roam=True,  # 开启鼠标缩放
                zoom=1,  # 当前视角比例缩放
                center=[104.06,30.67],  # 当前视角的中心点 经纬度表示
                layout_size=500,
                itemstyle_opts=opts.ItemStyleOpts(color="#FFFFCC",border_color="#800000"))
    # 为地图添加配置
    # 标注散点
    .add(
        "",  # series name
        # 添加数据项（坐标点名称，坐标点值）
        # data_pro,
        [("长沙",(112.979352787651,28.2134782308532)),("广西",(108.92427442705878,23.552254688119405)),("洪江",(110.087193420965,27.239105321481)),
         ("潼南",(	105.819678845163,30.1499329659585)),("徐州",(117.188106623177,34.2715534310919))],
        type_=ChartType.EFFECT_SCATTER,  # 添加图类型
        color="black"
    )
    # 标记流向线条
    .add(
        'Geo',  # series_name
        [("长沙","广西"),("广西","洪江"),("洪江","潼南"),("潼南","徐州")],
        type_=ChartType.LINES,
        is_selected=True,  # 图例
        effect_opts=opts.EffectOpts(symbol=SymbolType.ARROW,symbol_size=6,color="blue"),  # 添加效果 箭头arrow
        linestyle_opts=opts.LineStyleOpts(curve=0.2)
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=True))  # 系列配置项
    .set_global_opts(title_opts=opts.TitleOpts(title="陆军交辎学校迁移图"))  # 全局配置项
    .render('china.html')
)