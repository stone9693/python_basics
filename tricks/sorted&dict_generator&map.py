# sorted，对可迭代对象进行排序
dict1={'a': 24, 'g': 52, 'i': 12, 'k': 33}
# 返回一个可迭代对象的列表
sorted(dict1.items(),key=lambda x:x[1])
# 字典生成式
dict2={key:value for key,value in sorted(dict1.items(),key=lambda x:x[1])}
# 倒叙排列string
str1='abcde'
str2=str1[::-1]
# map
list1=[1, 2, 3]
list2=[4, 5, 6]
iter=map(lambda x1,x2:x1+x2,list1,list2)
