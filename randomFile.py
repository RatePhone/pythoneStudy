import random

# 生成10个 0~30 的随机数
list_1 = [ random.randint(0, 30) for x in range(0, 10)]
print(list_1)

# 活动1：处理列表在这次活动中，我们首先生成一个随机数列表，然后基于第一个列表生成另一个只包含被3整除的数字的列表。
# 重复10次这个实验。然后，计算两个列表之间的平均长度差。完成这次活动的步骤如下：
# 1.创建一个包含100个随机数的列表。2.从这个随机列表中创建一个新列表，新列表中的数字可以被3整除。
# 3.计算这两个列表的长度，并将两个列表的长度差存储在一个新变量中。
# 4.使用循环，执行步骤2和步骤3，并计算差值变量10次。
# 5.求这10个长度差的算术平均值。

res_list = []


i = 0
while i < 10:
    list_2 = [random.randint(0, 100) for x in range(0, 100)]
    list_4 = [x for x in list_2 if x % 3 == 0]
    res_list.append(len(list_2) - len(list_4))
    i +=1


print(res_list)
avg = sum(res_list) / float(len(res_list))
print(avg)

