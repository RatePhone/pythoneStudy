from sys import getsizeof
from itertools import repeat

big_list = [x for x in range(0,10000000)]

sizeNum = getsizeof(big_list)


# 使用迭代器 降低内存 利用率吧

print(sizeNum)

samll_list = repeat(1, times=10000000)

print(samll_list)

samllNum = getsizeof(samll_list)

print(samllNum)

# 这里的i 是通过 enumerate函数生成的
for i,x in enumerate(samll_list) :
    print(x)
    if (i > 10) :
        break

def my_push(s, value) :
    return s + [value]
  
def my_pop(s) :
    top = s[-1]
    del s[-1]
    return top

mytest = []

mytest = my_push(mytest, 1)

print(mytest)
