#map
# map(function, iterable)
# function → what you want to apply
# iterable → list, tuple, etc.

# list1 = [1,2,3,4,5]

# def mul(x):
#     return x*x

# newList = map(mul, list1)
# print(list(newList)) #[1, 4, 9, 16, 25]

#filter

# list1 = [1,2,3,4]
# def isEven(n):
#     return n%2 ==0

# result = filter(isEven,list1)
# print(list(result)) # [2,4]


#reduce
from functools import reduce

expenses = [('Dinner', 80), ('Car repair', 130),('cloths',190)]

sum = reduce(lambda a,b: a[1]+b[1], expenses)
print(sum)

