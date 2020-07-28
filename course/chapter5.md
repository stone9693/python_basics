# chapter5/函数  
# 5.1 函数基础  
## 5.1.1 函数形式  
函数是可实现一个或多个功能的代码块；  
函数的特点：重用性、模块化；  
Python的内置函数，如print()、len()、min()、max()等；  
同时，我们也可以自定义函数；  
![5_1](https://github.com/stone9693/python_basics/blob/master/source/5_1.png)  
## 5.1.2 函数调用  
![5_2](https://github.com/stone9693/python_basics/blob/master/source/5_2.png)  
参数是函数重要组成部分，python的参数灵活多样；  
参数类型：默认参数，关键字参数，不定长参数；  
# 5.2 函数参数  
## 5.2.1 可变和不可变  
python包含两类对象，一类是可变，另一类是不可变；  
字符串、元组、数字是不可变的对象；而列表和字典是可变对象；  
不可变参数：只是传递了参数值，参数本身不受影响；  
可变参数：参数本身受到影响；  
![5_3](https://github.com/stone9693/python_basics/blob/master/source/5_3.png)  
## 5.2.2 默认参数  
调用时，未赋值的参数，即为默认值参数了；  
![5_4](https://github.com/stone9693/python_basics/blob/master/source/5_4.png)  
## 5.2.3 关键字参数
在函数中，参数名是其关键字；  
实值传参，必须按照顺序；  
赋值传参，无需按照顺序；  
![5_5](https://github.com/stone9693/python_basics/blob/master/source/5_5.png)  
## 5.2.4 不定长参数
参数的个数不确定；  
星号以元组形式存放所有未命名参数；  
![5_6](https://github.com/stone9693/python_basics/blob/master/source/5_6.png)  
![5_7](https://github.com/stone9693/python_basics/blob/master/source/5_7.png)  
不定长参数也可以字典的形式传入，既关键字形式；  
![5_8](https://github.com/stone9693/python_basics/blob/master/source/5_8.png)  
星号以后的参数，强制使用关键字；  
![5_9](https://github.com/stone9693/python_basics/blob/master/source/5_9.png)  
匿名函数以lambda开头；  
具体形式如下；  
![5_10](https://github.com/stone9693/python_basics/blob/master/source/5_10.png)  
匿名函数的特点：  
特别简单；  
效率跟普通函数一样；  
可表达的逻辑有限；  
![5_11](https://github.com/stone9693/python_basics/blob/master/source/5_11.png)  
