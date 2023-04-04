str1 = "hi ni hao wo shi ji qi ren "

# 查询字符串是否 有 该值
res = str1.find("hi")

print(res)

base_text = "When I have a apply,But It is no goodoy in living comes from having fine emotions,trusting them,giving them the freedom of a bird in the open. Joy in living can never be assumed as a pose or put on from the outside as a mask. People who have this joy do not need to talk about it; they radiate it. They just live out their joy and let it splash its sunlight and glow into other lives as naturally as bird sings.Sing is World here some one to sing"
new_base = base_text.replace(" ", ",").replace(".",",").replace(",,",",").replace(";","")
print(new_base)

list_1 = new_base.split(",")
list_2 = [x.lower() for x in list_1 ]
print(list_2)
dict1 = {x: 0 for x in list_2} # 最开始的x 来自 列表的 后面 1 是值 可以指定为 与x相关的


for x in list_2:
    num = dict1[x]
    dict1[x] = num + 1

print(dict1)


#另一种解法

unique = dict.fromkeys(list_2)

for k in list_2 : 
    if unique[k] is None :
        unique[k] = 1
    else :
        unique[k] += 1   

print(unique)

# sorted函数
sort_word = sorted(unique.items(), key=lambda key_val_tuple: key_val_tuple[1], reverse=True)
print(sort_word)

new_sort_word = sort_word[:5]
print(new_sort_word)
