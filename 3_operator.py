#operators

# 1+1 #2
# 2-1 #1
# 2*2 #4
# 4/2 #2
# 4%3 #1
# 4**2 #16
# 5//2 #2

#comparison operators
# a=1
# b=2
# a == b # False
# a != b #True
# a > b #False
# a < b # True
# a >=b #False
# a <= #True

#Boolean Operator
condition1 = True
condition2 = False

not condition1 #False
condition1 and condition2 #False
condition1 or condition2 #True

#Or boolean operator
#if first value False return 2nd value
print(0 or 1) # 1
print(False or 'hey') # hey
print('hi' or 'hey') # hi
#Note [] is always return False value
print([] or False) #False
print(False or []) # []

#And boolean operator
# print(0 and 1) # 0
# print(1 and 0) #0
# print(False and 'hey') # False
# print('hi' and 'hey') # hi
# #Note [] is always return False value
# print([] and False) #[]
# print(False and []) # False


#Bitwise operators
& performs binary And
| performs binary Or
^ performs binary XOR operation
~ performs a binary NOT operation
<< shift left operation
>> shift right operation


# is and in operator
#is check memory match then return True
# in check value are exist in list or not and return True and False


# Ternary Operator

# def is_adult(age):
#     if age > 18:
#         return True
#     else:
#         return False

def is_adult2(age):
    #Ternary operator
    return True if age >18 else False
    



