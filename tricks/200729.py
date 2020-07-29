# sorted，对可迭代对象进行排序
dict1={'a': 24, 'g': 52, 'i': 12, 'k': 33}
# 返回一个可迭代对象的列表
sorted(dict1.items(),key=lambda x:x[1])
# 字典生成式
dict2={key:value for key,value in sorted(dict1.items(),key=lambda x:x[1])}
