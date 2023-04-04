# 集合
import random

# 这一步 生成的20个随机数 有可能有重复的
list_1 = [random.randint(0,10) for x in range(0, 20)]
# 这一步 就是 可以去重 
list_2 = list(set(list_1))

print(list_2)

set1 = {"apple", "orange", "banana"}
set2 = {"pear", "peach", "mango", "banana"}

# 寻找两个集合的并集 
print(set1 | set2)

# 寻找两个集合的交集
print(set1 & set2)

#字典
dict_1 = {"key1": 34, "key2": [0,1,2], "key3": {"apply","banana"}}
print(dict_1)

#遍历 
for k,v in dict_1.items() :
    print("{} - {}jjj".format(k, v)) # 这里 {}代表占位符 对应后面的 值 按 顺序

# 删除
del dict_1["key2"]
print(dict_1)

# 创建 值为key的平方根的字典
list_3 = [x for x in range(0, 10)]
dict_2 = {x: x**2 for x in list_3}
print(dict_2)

# 注意 （”tom“, 300） 这种数据接口 称为 元组 是python 独有的
dict_3 =dict([("tome", 300),("tan", 200), ("hu", 100)])
print(dict_3)

dict_4 =dict(tom=300,tan=100,hu=200)
print(dict_4)

# 元组是Python中的另一种数据类型。它本质上是连续的，类似于列表。元组由用逗号分隔的值组成，如下所示：
tuple_1 = 24, 42, 2.345, "hello", "word"
print(tuple_1)

# 元组的特殊之处在于，它是不可更改的数据类型。因此，一旦创建它的值就不能更改。我们只能访问它
print(tuple_1[-1])

# 元祖拆包 其实类似于 es6 的结构 模式 比如 ab= {a: "1", b: "2"} 解构 const {a,b} = ab
# 注意 必须将元组每个值都写出来 否则 无法解构
tuple_2 = "hello", "world"
hello, world = tuple_2
print(hello)
