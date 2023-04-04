import random 

## pythone 的列表 从 0 开始 顺序  然后 从 -1开始 从后往前 逆序
list_1 = [32, 12, 98,1]
print(list_1[-2])
print(list_1[1:3]) # 从1开始 到 3 不包含3 
list_2 = []
# 随机数 从0开始 到10 结束 包含 10
for x in range(0, 10) :
    list_2.append(x)
print(list_2)    
# 遍历
i = 0
while i<len(list_2) :
    print(list_2[i])
    i += 1

# 创建可以被5整除的列表
list_3 = [x for x in range(0, 100) if x % 5 == 0]
print(list_3)

list_4 = list_1 + list_2
print(list_4)

list_1.extend(list_2);
print(list_1)

for i in list_1:
    print(i)
# 判断 25是否在数列里
has = 25 in list_1
print(has)

# 从大到下排序
list_1.sort(reverse=True)
print(list_1)

# 从小到大
list_1.sort()
print(list_1)

