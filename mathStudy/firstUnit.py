from math import sqrt

# 计算平方根


def length(v):
    return sqrt(v[0]**2 + v[1]**2)


print(length((3, 4)))


def add(*vectors):
    return (sum([v[0] for v in vectors]), sum([v[1] for v in vectors]))


print(add((1, 2), (2, 4), (3, 6), (4, 8)))

