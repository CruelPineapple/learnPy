# 一个斐波那契数列的例子
a, b = 0, 1

# 这是多重赋值
while a < 10:
    print(a, end=',')
    a, b = b, a + b
# 上式等号右侧的表达式在赋值前就会被求值!

# 空格规则: 错误地使用空格不会产生运行时错误,但是会产生警告
# 操作符两侧空格,逗号后空格

# 通过缩进来控制循环体范围,结束标志的一个空行
# 关于print函数的参数,除了要被打印的东西,还接受一些用于格式化的内容
# 比如上面的第二个参数end,每次打印完打一个逗号

x = int(input("Please enter an integer: "))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

# else if 在这里是elif,注意冒号和while句用法类似
# 官方说法,if,elif结构可以看作其他语言中switch case的替代

words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

# 这不就是java的增强for循环吗,js好像也有类似的

for i in range(5, 10):
    print(i)

# range函数创建一个数字序列, 范围从第一个参数开始, 到第二个参数结束
# 也可以只传入结束参数,这时候从0开始, 还可以指定步长
for i in range(0, 10, 3):
    print(i)

# 步长和起止点也能是负的
print(range(10))
# 输出range(0, 10)
# 但是如下操作可以成功迭代
print(sum(range(10)))  # 0+1+...+9
# 这叫做可迭代对象

# 循环中的else
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')

# 这里, else属于for循环, 不属于if
# 因此, 运行顺序是在for循环迭代结束后再运行else部分,且break后跳过else
# 另, //表示除法后向下取整

# pass 当语法上需要语句但是逻辑上啥都不干, 使用pass

# def 定义一个函数的句法,函数的开头需要两个空行


def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

# in 关键字, 检测一个序列是否包含某个值


# 如果指定了参数的默认值,那么其值会在函数声明处计算
i = 5


def f(arg=i):
    print(arg)


i = 6
f() # 5
# 他妈的,函数和类的声明首尾都需要两个空行,指定默认参数的时候=两边不应有空格
# 重要! 默认值只会执行一次!考虑如下函数


def g(a, l=[]):
    l.append(a)
    return l


print(g(1))
print(g(2))
print(g(3))
# [1]
# [1, 2]
# [1, 2, 3]
# 存在警告!
