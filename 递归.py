#练习一：定义一个函数power来任意数据的幂运算n**i
def power(n,i):
    # 基本条件
    if i==1:
        return n
    # 递归条件
    return n*power(n,i-1)
print(power(3,3))

# 练习2：创建一个函数，用来检查一个任意的字符串是否是回文字符串，如果是返回true，否则返回false。

def huiwen(str):
    # 基本条件
    if len(str) == 1:
        return True
    elif str[0]!=str[-1]:
        return False
    # 递归条件
    return huiwen(str[1:-1])

print(huiwen("abf"))
