#_*_coding:utf-8_*_
'''
@project: DailyAlgorithm
@author: exudingtao
@time: 2019/12/6 7:58 下午
'''

def isPalindrome(x):
    if x < 0:
        return False
    temp = x
    res = 0
    while temp > 0:
        reNum = temp % 10
        temp = temp // 10
        res = res * 10 + reNum
    if res == x:
        return True
    else:
        return False
print(isPalindrome(121))

