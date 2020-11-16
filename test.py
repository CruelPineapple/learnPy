print('hello')
# no new line at end of file
# 意思就是提示在文件结束的时候没有一个新行,换一下行就可以了
print(4/2)
# =>2.0 python会把除法结果转换为浮点数
print(2**10)
# =>1024 python中幂是**表示的
print('C:\some\name')
# \n会被转义成换行且\s会产生警告:invalid escape sequence
print(r'C:\some\name')
# 在字符串前添加r来使用原始字符串模式
print("""\
    字符串
字面值
    跨行输入
""")
# 使用三重"""和一个\进行字符串字面值的跨行输入
print(2*"nmsl")
# 特性,可以用*重复字符串
word="python"
print(word[-1])
# 比其他语言更高级的是,负索引表示从后往前访问字符串,-1表示最后一个
print(word[0:3])
print(word[3:6])
# 字符串剪切,第一个参数为起点索引,第二个参数为终点下一个索引.剪切越界会被自动处理

# 字符串不能按索引修改
