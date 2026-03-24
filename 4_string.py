#String in python

#concat

#multi line string print
# print(""" This is
# multiple line 
# print
# """)

#string method
# str.upper()
# str.lower()
# str.title() #capatlize each first char
# str.islower() # True or False
# str.isupper() # True or False


"""
 isalpha check is string contains only characters then 
 return True but when we pass blank space with string its 
 return False and when we pass any number and empty or 
 white space only then return False

"""
# str = "three" # true
# str = "three " # False
# str = "4"  # False
# str = "4 "  # False
# str = " "  # False
# print(str.isalpha()) 

#isalnum
"""
isalnum check is string contains characters or digit then 
return True but when we pass blank space with string its 
return False and when we pass any number with blank space and empty or 
white space only then return False
"""
# str = "three" # true
# str = "4" # true
# str = "three " # False
# str = "4 "  # False
# str = " "  # False
# str = ""  # False
# print(str.isalnum())


#isdecimal 
# print(str.isdecimal()) # to check string contain only digits and is not empty 

#str.startswith()
#string.startswith(value, start, end)
# Parameters:
# value → text (or tuple of texts) you want to check
# start (optional) → starting position
# end (optional) → ending position

# str = "JAVA"
# print(str.startswith(("PY","JA"))) #tuple
# ''' "PY" not in str so get False 
# and "JA" is available in string so get True 
# so True False -> Ture (one condition true so final result True)
# '''

#endwith()

#replace()
# str.replace(old, new, count)
# str = "apple apple apple mango"
# print(str.replace("apple","orange", 2))
# # orange orange apple mango


#split
# str.split(separator, maxsplit)
# str = "one two three four"
# print(str.split(" ",2))
# # ["one","two","three four"]


# #strip
# str = "#####Python####"
# print(str.strip("#"))
# # Python


#join()

# data = ["apple","banana","mango"]
# print(",".join(data))
# # apple,banana,mango

#find()
# str = "hello world"
# # str.find(string, startIndex, endIndex)
# print(str.find("e", 3,6)) 
# # if not found return -1 


#slicing
# str = "adish"
# print(str[1:]) #dish
# print(str[:]) #adish
# print(str[:1]) # it means 0:1 # a
# print(str[-1:]) #h

#number data type
