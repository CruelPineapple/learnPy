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
            test1.append((x,y))

print(test1)

del test1
# del用于删除某个元素, 某个切片, 或整个列表甚至这个变量

# 元组