# chapter9/numpy  
# 9.1. ndarray简介  
ndarray是numpy的一种基本的数据结构，numpy的运算都是基于其展开的。  
## 9.1.1 创建ndarray  
在numpy中通常使用array方法来创建ndarray对象。  
![9_1](https://github.com/stone9693/python_basics/blob/master/source/9_1.png)  
还可以通过其他方法创建吗？  
举例：  
1. 通过np.arange  
![9_2](https://github.com/stone9693/python_basics/blob/master/source/9_2.png)  
2. 通过np.linspace  
![9_3](https://github.com/stone9693/python_basics/blob/master/source/9_3.png)  
3. 通过np.ones，np.zeros  
![9_4](https://github.com/stone9693/python_basics/blob/master/source/9_4.png)  
总之，numpy中的ndarray的创建方式多种多样。  
## 9.1.2 ndarray的索引  
元素索引，行列分别索引，条件索引。  
![9_5](https://github.com/stone9693/python_basics/blob/master/source/9_5.png)  
## 9.1.2 ndarray的运算
标量、同shape的ndarray都可以进行运算。  
![9_6](https://github.com/stone9693/python_basics/blob/master/source/9_6.png)  
# 9.2 线性代数
numpy的linalg模块是可用于线性代数的相关运算。  
本节主要涉及：np.linalg.dot，np.linalg.solve，np.linalg.inv；  
![9_7](https://github.com/stone9693/python_basics/blob/master/source/9_7.png)  
# 9.4 随机数
numpy中的random模块提供了随机数生成器。  
本节主要涉及：rand，randint，randn，permutation，shuffle；  
![9_8](https://github.com/stone9693/python_basics/blob/master/source/9_8.png)  
