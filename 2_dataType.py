name = "adish"
print(type(name)) # str
print(isinstance(name, str)) # True
print(isinstance(name, int)) # False

# age = 1
# print(isinstance(age,int)) #True

# age = 1.1
# print(isinstance(age,int)) #False
# print(isinstance(age,float)) #True

#data type conversion

age = "34"
print(isinstance(age,int)) #False

age = int("34")
print(isinstance(age,int)) #True

number = "20"
age = int(number)
print(isinstance(age, int)) #True

number = "test"
age = int(number)
print(isinstance(age,int)) # Value Error


