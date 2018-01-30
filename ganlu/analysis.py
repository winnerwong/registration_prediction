import pandas as pd

# 读取数据集
data = pd.read_table('train_20171215.txt',delim_whitespace=True)
# 数据类型都是int
print(data.dtypes)
# 数据不存在缺失值
print(data.describe())
# 查看数据
print(data)
# 查看上牌量和星期几的关系
week_list = [1,2,3,4,5,6,7]
week_map = {}
for i in week_list:
    value = sum(data[data["day_of_week"] == i]['cnt'])
    week_map.update({i:value})
print(week_map)
# 查看上牌量和品牌的关系
brand_list = [1,2,3,4,5]
brand_map = {}
for i in brand_list:
    value = sum(data[data["brand"] == i]['cnt'])
    brand_map.update({i: value})
print(brand_map)
# 查看不同品牌的车的上牌量和星期的关系
brand_list = [1,2,3,4,5]
week_list = [1,2,3,4,5,6,7]
combine_map = {}
for i in brand_list:
    for j in week_list:
        value = sum(data[(data['brand'] == i) & (data['day_of_week'] == j)]['cnt'])
        combine_map.update({'week'+str(j)+'brand'+str(i): value})
print(combine_map)
