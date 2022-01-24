from functools import wraps

def hitest(name="yasooob"):
    print("aaaa")
    return "hi " + name
#print(hitest())

#在函数中定义函数
def hi(name="yasoob"):
    print("now you are inside the hi() function")

    def greet():
        return "now you are in the greet function"
    
    def welcome():
        return "now you are in the welcome function"
    print(greet())
    print(welcome())
#函数中返回函数
def hiReturn(name="yasoob"):
    def greet():
        return "now you are in the greet function"
    def welcome():
        return "now you are in the welcome() function"
    if name == "yasoob":
        return greet()
    else:
        return welcome()
#将函数作为参数传给另一个函数
def hiParamter():
    return "hi yasoob"
def doSomethingBeforeHi(func):
    print("I am doing something before executing hi()")
    print(func())
#装饰器
def a_new_decorator(a_func):
    def wrapTheFunction():
        print("l am doing some boring work befor executing a_func")

        a_func()

        print("l am doing some boring work after executing a_func")
    return wrapTheFunction
def a_function_requiring_decoration():
    print("l am the function which need some decoration to remove my foul smell")

#新装饰器
@a_new_decorator
def a_function_requiring_decoration_s():
    print(" l am the function which needs some decoration to remove my foul smell")

#正规写法
def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__+"was called")
        return func(*args, **kwargs)
    return with_logging
@logit
def addition_func(x):
    return x+x
if __name__ == "__main__":
    #print(hi())
    #print(greet())
    #print(hi())
    #hi()
    #a = hiReturn()
    #print(a)
    #doSomethingBeforeHi(hiParamter)

    #####装饰器
    # a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
    # a_function_requiring_decoration()
    #@way
    #a_function_requiring_decoration_s()

    #normalize way
    results = addition_func(4)
