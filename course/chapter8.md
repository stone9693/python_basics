# chapter8/模块和包  
# 8.1. 模块  
## 8. 1.1 模块简介  
类、函数、变量等，都可重复使用。  
为了方便调用，我们通常把他们放到Python文件之中。  
单个文件的代码阅读和调用都比较混乱。  
代码最好分开存储，相似功能的代码放在一起。  
模块可以帮助我们实现这样的功能。  
后缀为py的文件都是python的模块。  
![8_1](https://github.com/stone9693/python_basics/blob/master/source/8_1.png)  
## 8.1.2. 模块导入
分开存储的代码，怎么相互调用呢？  
这就需要导入其他模块。  
导入模块需要使用关键字import。  
![8_2](https://github.com/stone9693/python_basics/blob/master/source/8_2.png)  
举例：  
![8_3](https://github.com/stone9693/python_basics/blob/master/source/8_3.png)  
# 8.2 包
## 8.2. 1. 包简介
来自于不同目录下的模块，怎么引用呢？  
带有__init__.py文件的目录是Python的包。  
exercise包举例：  
![8_4](https://github.com/stone9693/python_basics/blob/master/source/8_4.png)  
## 8.2. 2. 包导入
不同目录下的模块的导入，可以通过包来实现。  
![8_5](https://github.com/stone9693/python_basics/blob/master/source/8_5.png)  
导入包下面的模块，或导入相关模块下的变量和函数。  
导入包时注意设置Python的环境，本次导入设置了上级路径作为环境。  
在Windows系统中，Python环境的设置可以临时设置或永久设置。  
永久设置可以在系统环境变量中添加PYTHONPATH，临时设置可以引入sys.path。  
