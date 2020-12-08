
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


# 关于类的私有变量, python中没有严格意义的私有类变量
# 然而重载时, 子类中可以随意使用父类的变量名而不会破坏其内部的调用

class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)

# 上面的示例即使在 MappingSubclass 引入了一个 __update 标识符的情况下也不会出错，
# 因为它会在 Mapping 类中被替换为 _Mapping__update 而在 MappingSubclass 类中被替换为 _MappingSubclass__update。