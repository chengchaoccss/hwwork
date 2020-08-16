## 函数式编程
    ### 在python中函数是一等对象，python中所有对象都是一等对象
    ### 一等函数有如下特点：
        #### 对象在运行是创建
        #### 能赋值给变量或作为数据结构中的元素
        #### 能作为参数传递
        #### 能作为返回值返回
    ### 高阶函数
        #### 高阶函数至少要符合以下特点中的一个
        ### 1. 接受一个或多个函数作为参数
        ### 2. 将函数作为返回值返回


l = [1,2,3,4,5,6,7,8,9,10]
def fn(func,lst):
    newlist = []
    for i in lst:
        if func(i):
            newlist.append(i)
    return newlist

def func1(i):
    if i%3 == 0:
        return True
    return False

def func2(i):
    if i%2 == 0:
        return True
    return False

print(fn(func1,l))
print(fn(func2,l))

# filter函数有以上的类似功能，不会对原对象产生影响
a = filter(func1,l)
print(list(a))

# 匿名函数 lambda函数表达式，专门用来创建一些简单的函数，用一次便会从内存中消失
# 语法：lambda 参数列表：返回值
print((lambda a,b:a+b)(10,20))
# 匿名函数可以赋值给一个变量
fn = lambda a,b:a+b

a = filter(lambda i:i>5,l)
print(list(a))

# map()函数可以对可迭代对象中的所有元素做指定的操作，然后将其添加到一个新的对象中返回

r = map(lambda i:i+1,l)
print(list(r))
# 匿名函数一般是用作参数使用，其他地方一般不适用

# sort()
# 对列表排序
newl = ['b','asd','f','ddf']
newl.sort()
print(newl)
newl.sort(key=len)#用函数作为参数
print(newl)

#sorted(),不影响原来对象，返回一个新对象