# chapter4/条件和循环  
# 4.1 条件  
## 4.1.1 基本形式  
条件语句是通过一条或多条语句的执行结果（True 或者False）来决定执行的子程序；  
每个条件后面要使用冒号”:”，表示满足条件后执行子程序。  
缩进来划分子程序范围，相同缩进的语句组成一个整体子程序。  
如果“condition”为True，将执行"sub_program"语句；  
![4_1](https://github.com/stone9693/python_basics/blob/master/source/4_1.png)  
![4_2](https://github.com/stone9693/python_basics/blob/master/source/4_2.png)  
任何数据类型、数据结构、逻辑运算都可以作为条件；  
非 0 、非空值或者逻辑True为True；  
0 、空值或者逻辑False为 False；  
![4_3](https://github.com/stone9693/python_basics/blob/master/source/4_3.png)  
## 4.1.2 逻辑运算  
逻辑运算的返回值是False或者True；  
![4_4](https://github.com/stone9693/python_basics/blob/master/source/4_4.png)  
![4_5](https://github.com/stone9693/python_basics/blob/master/source/4_5.png)  
![4_6](https://github.com/stone9693/python_basics/blob/master/source/4_6.png)  
## 4.1.3 多个条件  
涉及到多个条件的判断，具体类型如下；  
![4_7](https://github.com/stone9693/python_basics/blob/master/source/4_7.png)  
![4_8](https://github.com/stone9693/python_basics/blob/master/source/4_8.png)  
## 4.1.4 条件嵌套  
条件语句中可以嵌套条件语句，具体如下；  
![4_9](https://github.com/stone9693/python_basics/blob/master/source/4_9.png)  
![4_10](https://github.com/stone9693/python_basics/blob/master/source/4_10.png)  
循环是在条件内多次执行子程序；  
循环包含while循环和for循环；  
循环的程序结构如下图；  
![4_11](https://github.com/stone9693/python_basics/blob/master/source/4_11.png)  
# 4.2 循环  
## 4.2.1 while循环  
while循环的伪代码如下图；  
循环的程序结构如下图；  
![4_12](https://github.com/stone9693/python_basics/blob/master/source/4_12.png)  
![4_13](https://github.com/stone9693/python_basics/blob/master/source/4_13.png)  
计算1-100的整数的和；  
条件是label=20的循环；  
![4_14](https://github.com/stone9693/python_basics/blob/master/source/4_14.png)  
![4_15](https://github.com/stone9693/python_basics/blob/master/source/4_15.png)  
## 4.2.2 for循环  
for循环可以遍历任何序列；  
for循环的程序结构和伪代码如下；  
![4_16](https://github.com/stone9693/python_basics/blob/master/source/4_16.png)  
![4_17](https://github.com/stone9693/python_basics/blob/master/source/4_17.png)  
我们公司都有哪些部门；  
用range函数来表达公司的这些部门：  
![4_18](https://github.com/stone9693/python_basics/blob/master/source/4_18.png)  
![4_19](https://github.com/stone9693/python_basics/blob/master/source/4_19.png)  
## 4.2.3 break、continue、pass  
break用于跳出整个循环，不再执行以后的循环；  
continue用于跳过当前循环，直接执行下一轮循环；  
pass代表空语句，一般用于站位；  
![4_20](https://github.com/stone9693/python_basics/blob/master/source/4_20.png)  
# 4.3 综合  
## 4.3.1 嵌套  
判断8-30之间的质数与合数；  
循环外的if好像有点麻烦，能简化点吗？  
![4_21](https://github.com/stone9693/python_basics/blob/master/source/4_21.png)  
## 4.3.2 赋值运算  
![4_22](https://github.com/stone9693/python_basics/blob/master/source/4_22.png)  
![4_23](https://github.com/stone9693/python_basics/blob/master/source/4_23.png)  
