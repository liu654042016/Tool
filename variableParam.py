#https://www.sohu.com/a/318781800_571478
#https://blog.csdn.net/cadi2011/article/details/84871401
def test():
    print("hello world")


def printOne(*args):
    print(args)

def printStr(**anything):
    print(anything)


if __name__ =="__main__":
    #test()
    printStr(first = 5, second = 100, en = 3)
    temp = (1, 2, 3, 4, 5)
    printOne(temp)
    printOne(*temp)