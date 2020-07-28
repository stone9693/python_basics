# chapter2/变量和数据类型  
# 2.1 Python语法简介  
Python 的语法主要有三个特点：英文输入，单行执行，缩进模式。  
![2_1](https://github.com/stone9693/python_basics/blob/master/source/2_1.png)  
如上图的代码，以“#”开头的语句是注释；一行是一块代码；以冒号“:”结尾时，换行执行缩进模式，其后的语句组成一个整体的代码块。  
大小写敏感的。  
# 2.2 print()  
print()函数———打印函数，让计算机把你给它的参数，打印到终端上。  
print()函数由两部分构成 ：函数体，参数；  
以print( ‘negative‘ )为例，  
函数体：print()  
参数：print('negative’)  
其中，函数体不可或缺。  
# 2.3 数据类型  
## 2.3.1 字符串  
字符串的标识是引号开始引号结束。  
引号包括单引号‘ ’ ，双引号 “ ” 和 三引号 ‘’‘ ’‘’ ，比如 ‘abc’ ，“abc”，’’’abc’’’ 等等。  
![2_2](https://github.com/stone9693/python_basics/blob/master/source/2_2.png)  
转义符  
![2_3](https://github.com/stone9693/python_basics/blob/master/source/2_3.png)  
![2_4](https://github.com/stone9693/python_basics/blob/master/source/2_4.png)  
字符串运算  
![2_5](https://github.com/stone9693/python_basics/blob/master/source/2_5.png)  
![2_6](https://github.com/stone9693/python_basics/blob/master/source/2_6.png)  
格式化  
![2_7](https://github.com/stone9693/python_basics/blob/master/source/2_7.png)  
![2_8](https://github.com/stone9693/python_basics/blob/master/source/2_8.png)  
字符串函数  
![2_9](https://github.com/stone9693/python_basics/blob/master/source/2_9.png)  
## 2.3.2 数值  
Python 支持四种不同的数值类型：  
整型(Int) - 通常被称为是整型或整数，是正或负整数，不带小数点。  
浮点型(floating point real values) - 浮点型由整数部分与小数部分组成，浮点型也可以使用科学计数法表示（2.5e2 = 2.5 x 102 = 250）  
复数(complex numbers) - 复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型。  
![2_10](https://github.com/stone9693/python_basics/blob/master/source/2_10.png)  
![2_11](https://github.com/stone9693/python_basics/blob/master/source/2_11.png)  
## 2.3.3 布尔值  
Python中有True 、 False 两种值（请注意大小写），也可以通过布尔运算计算出来。  
布尔值可以用 and、or 和 not 运算。  
and 运算是与运算，只有所有都为 True，and 运算结果才是 True。  
or 运算是或运算，只要其中有一个为 True，or 运算结果就是 True。  
not 运算是非运算，它是一个单目运算符，把 True 变成 False，False 变成 True。  
## 2.3.4 空值  
在 Python 中，用 None 来表示。  
# 2.4 变量  
## 2.4.1 变量的创建和赋值  
在 Python 程序中，变量是用一个变量名表示，可以是任意数据类型，变量名必须是大小写英文、数字和下划线（_）的组合，且不能用数字开头；   
如下图a就是一个变量。Python 是不用声明数据类型的。在 Python中“=”是赋值语句，跟其他的编程语言也是一样的，因为 Python 定义变量时不需要声明数据类型，因此可以把任意的数据类型赋值给变量，且同一个变量可以反复赋值，而且可以是不同的数据类型。  
![2_12](https://github.com/stone9693/python_basics/blob/master/source/2_12.png)  
## 2.4.2 变量的指向问题  
我们来看下这段代码，发现最后打印出来的变量 b 是’python’。  
这主要是变量 a 一开始是指向了’python’，b=a 创建了变量 b ,变量 b 也指向了a 指向的字符串’python’，最后 a=‘hello python’，把 变量 a 重新指向了’hello python’，所以最后输出变量 b 是’python’。  
![2_13](https://github.com/stone9693/python_basics/blob/master/source/2_13.png)  
## 2.4.3多个变量赋值  
Python 允许同时为多个变量赋值。  
例如：a=b=c=1 ，以上实例，创建一个整型对象，值为 1，三个变量被分配到相同的内存空间上。  
也可以为多个对象指定多个变量。例如： a,b,c=1,2,"daihou"以上实例，两个整型对象 1 和 2 的分配给变量 a 和 b，字符串对象 “daihou" 分配给变量 c。  
![2_14](https://github.com/stone9693/python_basics/blob/master/source/2_14.png)  
