from pyecharts.charts import Map
# 配置图表
from pyecharts import options as opts
#数据库？
from pyecharts.faker import Faker

c=(
    Map()
    .add("A",[list(i) for i in zip(Faker.country,Faker.values())])
    .render()
)