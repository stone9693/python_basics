# chapter6/迭代器和生成器  
# 6.1 迭代器  
## 6.1.1 迭代基础  
迭代是一种算法，其目的是收敛到一个值；  
本次迭代的终值是下次迭代的初始值；  
迭代是所有计算机语言的基本算法；  
可迭代对象都可以进行迭代；  
怎么去检验可迭代对象？  
![6_1](https://github.com/stone9693/python_basics/blob/master/source/6_1.png)  
## 6.1.2 迭代器  
迭代器可以进行迭代操作；  
迭代器只能往前不会后退；  
迭代器函数：iter()，next() ；  
字符串，列表、元组、集合等可用于创建迭代器；  
![6_2](https://github.com/stone9693/python_basics/blob/master/source/6_2.png)  
# 6.2 生成器  
## 6.2.1 生成基础  
通过一定的算法做迭代；  
![6_3](https://github.com/stone9693/python_basics/blob/master/source/6_3.png)  
## 6.2.2 创建生成器  
生成算法的对象就是生成器，生成器也是迭代器；  
生成器的创建方法：1. yield函数；2. ()；  
![6_4](https://github.com/stone9693/python_basics/blob/master/source/6_4.png)  
生成算法的对象就是生成器，生成器也是迭代器；  
生成器的创建方法：1. yield函数；2. ()；  
![6_5](https://github.com/stone9693/python_basics/blob/master/source/6_5.png)  
