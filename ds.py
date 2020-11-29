# 列表的特性
# append(x), 在尾部添加元素
# extend(l), 在尾部添加一个可迭代对象来扩展列表
# insert(i,x), 在指定位置i插入元素x
# remove(x), 移除列表中第一个值为x的元素
# pop(i), 删除列表中位置i的元素并返回它, 若不指定参数则对最后一个元素进行操作
# clear() 删除所有元素
# index(x[,start[,end]]), 返回第一个为x的元素的索引, 可选参数用于限定范围
# count(x), 返回元素x在列表中出现的次数
# reverse(), 反转
# copy(), 返回列表的浅拷贝
# 列表做栈使用十分方便, 但是做队列性能会比较差因为在开头操作需要移动所有元素

# 列表推导式
# squares = []
# for x in range(10):
#     squares.append(x**2)
# 等效于:(下为列表推导式)
squares = [x**2 for x in range(10)]
print(squares)
# 列表推导式包含:
# 一个表达式, 后面跟一个for, 然后是一个或多个for或if:
test = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(test)
# 上例把两个列表中不同的元素结合起来
# 如果用正常的for语句写回比较麻烦:
test1 = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            test1.append((x, y))

print(test1)

del test1
# del用于删除某个元素, 某个切片, 或整个列表甚至这个变量

# 元组
# 一个元组由几个被逗号隔开的值组成:
t = 12345, 54321, 'hello'
print(t[2])
# 元组是不可变的, 不能给其中一个元素单独赋值, 元组一般包含不同类的元素
# 元组一般通过索引访问, 或是解包
# 解包:
x, y, z = t
print(x, y, z)

# 集合, 不重复元素组成的无序集
basket = {'apple', 'orange', 'apple', 'banana'}
# 用花括号创建非空集合, 重复元素会被自动移除
print(basket)
print('apple' in basket)
# 用set()创建集合
a = set('abcdefgabc')
print(a)

# 字典, 以关键字(任意不可变类型,如字符串或数字)为索引
# 可以将字典看作键值对的集合, 在一个字典中, 键必须是唯一的
tel = {'jack': 123, 'sape': 456}
# 花括号创建字典, 用逗号隔开键值对们
tel['tim'] = 789
# 像这样添加元素
print(tel)
print((tel['tim']))
# 访问字典或字典元素
list(tel)
print((list(tel)))
# 这将返回包含字典中所有键的列表, 按插入次序
print('tim' in tel)
# 检查是否存在键

myDict = dict([('a', 1), ('b', 2), ('c', 3)])
print(myDict)
# dict()函数直接从键值对创建字典

myDict = {x: x**2 for x in (2, 4, 6)}
print(myDict)
# 字典推导式创建字典

