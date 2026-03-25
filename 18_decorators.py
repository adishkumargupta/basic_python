#Decorators

#Decorators is a comman method which we use any method using pass atribute without any change orignal function

# def logtime(func):
#     def wrapper():
#         print("before")
#         func()
#         print("after")
#     return wrapper


# @logtime
# def hello():
#     print("Hello")

# hello()



#with variable decorators

def repeat(n):
    def decorator(func):
        def inner():
            print("Before")
            for i in range(3):
                print("number", i)
            print("after")
        return inner
    return decorator

@repeat(3)
def hello():
    print("Hello")

hello()