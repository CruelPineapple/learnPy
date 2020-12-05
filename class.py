
# python 中类不一样的地方:
class MyClass:
    def __init__(self):
        self.data = 0
    # 这是构造函数


x = MyClass()
# 类定义结尾需要两个空行
print(x.data)
# 构造函数中的self参数是不会被访问的, 例如一个带参数的构造函数:


class MyClass2:
    def __init__(self, num):
        self.data = num


y = MyClass2(2)
print(y.data)


# 关于方法对象
class Hello:
    def f(self):
        print('hello')


z = Hello()
hello = z.f
# 什么都不会发生, 这时候只是让hello引用了这个方法对象
hello()
# 打印hello

# 定义派生类
class MyHello(Hello):
    str = 'myHello'


