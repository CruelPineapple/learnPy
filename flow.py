#一个斐波那契数列的例子
a,b=0,1
# 这是多重赋值
while a<10:
    print(a,end=',')
    a,b=b,a+b
# 上式等号右侧的表达式在赋值前就会被求值!

# 通过缩进来控制循环体范围,结束标志的一个空行
# 关于print函数的参数,除了要被打印的东西,还接受一些用于格式化的内容
# 比如上面的第二个参数end,每次打印完打一个逗号
