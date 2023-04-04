list_1 = ["word","hi","here","hello"]

list_2 = ["hi", "word"]

# 检查list_1 的元素 是否 包含所有的 list_2 元素

isAll = all(w in list_1 for w in list_2)

print(isAll)
