year = 2020
event = 'President election'
print(f'Result of the {year} {event}')
# 格式化变量字面值

yes_votes = 42_572_654
no_votes = 43_132_495
persentage = yes_votes / (no_votes + yes_votes)
print('{:-9} YES voates {:2.3%}'.format(yes_votes, persentage))

# f格式化中, 变量名后使用:跟一个整数即可限制最小字符宽度
print(f'{year:10}')