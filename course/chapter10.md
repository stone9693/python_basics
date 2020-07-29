# Chapter10/pandas  
# 10.1 dataframe简介  
dataframe是pandas中最基础的数据结构，当然它也是pandas中最常见的对象，它跟表格类似。  
dataframe的行和列是分别存储的数据集；这种存储方式，加快了列和行的操作效率。  

## 10.1.1 创建dataframe  
一般情况下，可以通过列表和字典这些类型的数据源来创建dataframe。当然pandas也做了很多接口，方便其他数据源来生成dataframe。
具体创建方式如下。  
![10_1](https://github.com/stone9693/python_basics/blob/master/source/10_1.png)  
## 10.1.2 dataframe重构
dataframe既可以作为pandas的数据来源，也可以作为输出。为了实现理想的dataframe输出结果，需要对其进行各种操作，重构只是其中之一。  
在此，我们只是把dataframe结构的变化，简单概括为重构。具体重构方法如下。  
![10_2](https://github.com/stone9693/python_basics/blob/master/source/10_2.png)  
# 10.2 行、列操作  
行和列是dataframe最常见的数据单元，pandas拥有很多对行列的操作方法。  
## 10.2.1 列操作  
列操作可以实现对列的重新索引。  
![10_3](https://github.com/stone9693/python_basics/blob/master/source/10_3.png)  
## 10.2.2 行操作  
行操可以实现对行的重新索引，还会具体对行数据集进行操作。  
![10_4](https://github.com/stone9693/python_basics/blob/master/source/10_4.png)  
# 10.3 dataframe汇总  
Dataframe的汇总一般使用groupby方法，该方法会返回一个groupby对象，然后使用该对象进行相关汇总操作。  
![10_5](https://github.com/stone9693/python_basics/blob/master/source/10_5.png)  
# 10.4 dataframe连接
在dataframe操作时，经常会遇到不同dataframe的横向或者纵向连接，pandas提供了merge和concat方法进行相关操作。  
具体实例如下。  
![10_6](https://github.com/stone9693/python_basics/blob/master/source/10_6.png)  
