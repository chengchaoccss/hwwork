# 将函数作为返回值返回
#
# def fn():
#     def inner():
#         print("我是inner")
#     return inner
# # r并不是全局函数，是内部定义的，所以这个函数总能访问到fn函数内的变量
#
# r = fn()
# r()
# 1.函数嵌套
# 2.将内部函数作为返回值返回
# 3.内部函数调用外部函数变量
# 闭包用作保护隐私数据使用
def make_average():
    nums = []

    def average(num):
        nums.append(num)
        return sum(nums)/len(nums)
    return average

average = make_average()
print(average(20))
print(average(30))