import ds
# 通过文件名使用模块
# 通过模块名使用其中的变量和函数等内容
# 当然, 引入一个模块也会执行其中的函数, 所以输出包含了ds中的所有print
print('------------')
print(ds.knights)
basket = ds.basket
print(basket)

# 变体, 可以只引入模块中的某个符号而非整个模块
from ds import tel
print(tel)

# 重命名引入模块
import ds as myDsModule
print(myDsModule.knights)