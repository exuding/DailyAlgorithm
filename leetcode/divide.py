#_*_coding:utf-8_*_
'''
@project: Exuding
@author: exudingtao
@time: 2019/12/24 11:39 上午
'''

##左移一位 数扩大两倍 计算机基础呀
#1.0原始版本  会超时
def divide(self, dividend, divisor):
    sig = True if dividend * divisor > 0 else False  # 判断二者相除是正or负
    dividend, divisor = abs(dividend), abs(divisor)  # 将被除数和除数都变成正数
    count = 0  # 用来表示减去了多少个除数，也就是商为多少
    while divisor <= dividend:  # 当被除数小于除数的时候终止循环
        dividend -= divisor
        count += 1
    res = count if sig == True else -count  # 给结果加上符号
    return max(min(res, 2 ** 31 - 1), -2 ** 31)
#2.0 让被减数成倍增张，但是会有乘法
def divide(self, dividend, divisor):
    sig = True if dividend * divisor > 0 else False  # 判断二者相除是正or负
    dividend, divisor = abs(dividend), abs(divisor)  # 将被除数和除数都变成正数
    res = 0  # 用来表示减去了多少个除数，也就是商为多少
    while divisor <= dividend:  # 当被除数小于除数的时候终止循环
        tmp_divisor, count = divisor, 1  # 倍增除数初始化
        while tmp_divisor <= dividend:  # 当倍增后的除数大于被除数重新，变成最开始的除数
            dividend -= tmp_divisor
            res += count
            count += 1  # 更新除数扩大的倍数
            tmp_divisor = divisor * count  # 更新除数
    res_value = res if sig == True else -res  # 给结果加上符号
    return max(min(res_value, 2 ** 31 - 1), -2 ** 31)

#3.0通过左移消除乘法
def divide(dividend, divisor):
    sig = True if dividend * divisor > 0 else False  # 判断二者相除是正or负
    dividend, divisor = abs(dividend), abs(divisor)  # 将被除数和除数都变成正数
    res = 0  # 用来表示减去了多少个除数，也就是商为多少
    while divisor <= dividend:  # 当被除数小于除数的时候终止循环
        tmp_divisor, count = divisor, 1  # 倍增除数初始化
        while tmp_divisor <= dividend:  # 当倍增后的除数大于被除数重新，变成最开始的除数
            dividend -= tmp_divisor
            res += count
            count <<= 1  # 向左移动一位
            tmp_divisor <<= 1  # 更新除数(将除数扩大两倍)
    res_value = res if sig == True else -res  # 给结果加上符号
    return max(min(res_value, 2 ** 31 - 1), -2 ** 31)



print(divide(10,3))

