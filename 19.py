def plus_one(x):
    return x+1

plus_one(10)
plus_one(20)

plus_one = lambda x: x+1
plus_one(10)
plus_one(20)

a = [1,2,3,4,5]
list(map(lambda x:x**2, a))
# [1,4,9,16,25]

b = [[1,2],[2,1],[0,3]]
b.sort(key=lambda x: x[0])
# [[0,3],[1,2],[2,1]]

b.sort(key=lambda x: x[1])
# [[2,1],[1,2],[0,3]]

a = [1,2,3,4,5]
list(filter(lambda x:x>2, a))
# [3,4,5]