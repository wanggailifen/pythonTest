# https://gallery.pyecharts.org/#/README

from pyecharts.charts import Line
from pyecharts.options import *

line = Line()

# 设置全局配置项
line.set_global_opts(
    title_opts=TitleOpts(title="测试GDP展示", pos_left="center", pos_bottom="10%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True)
)

line.add_xaxis(["中国", "美国", "英国"])
line.add_yaxis("GDP", [30, 20, 15])
path = line.render()
print(path)
