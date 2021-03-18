from pyecharts.charts import Bar
#数据库？
from pyecharts.faker import Faker
#主题
from pyecharts.globals import ThemeType

c=(
    Bar({"theme":ThemeType.MACARONS})#主题
    .add_xaxis(Faker.choose())
    .add_yaxis("A",Faker.values())
    .add_yaxis ("B", Faker.values ())
    .render()
)