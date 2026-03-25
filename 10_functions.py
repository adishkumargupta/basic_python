# def hello():
#     print("Hello")

# hello()

# def hello(name): # perameters
#     print("Hello " + name)

# hello("adish") # arguments
# hello("kumar")

#default perameter
# def hello(name = "kumar"): # default perameter
#     print("Hello " + name)

# hello()


#Variable Scope
# age = 8 # global scope
# def test():
#     print(age) # 8
# print(age) #8
# test()

#local variable
# def test():
#     age =8
#     print(age)
# print(age) # age not define
# test()


#nested function
# def talk(phrase):
#     def say(word):
#         print(word)

#     words = phrase.split(" ")
#     for word in  words:
#         say(word)

# talk("I am going to by the milk")


#nonlocal variable
# def count():
#     count = 1

#     def increment():
#         nonlocal count
#         count = count + 1
#         print(count)

#     increment()
# count()


#closures Function
"""
A function inside another function
Then inner function remembers variables from the outer function
Even remembers after the outer function has finished
"""

# def outer():
#     x = 10

#     def inner():
#         print(x)
#     return inner
# func = outer()
# func()
