#_*_coding:utf-8_*_
'''
@project: Exuding
@author: exudingtao
@time: 2019/12/28 9:13 下午
'''


def coinChange(coins, amount):
    a = [amount + 1 for i in range(amount+1)]  # 数组开多大呢 子状态从0-n就开 n+1 子状态从0-n-1就开 n
    # a[amount] = a[amount-ak]+1
    # ak = coins[i]
    a[0] = 0
    for i in range(1, amount+1):
        a[i] = amount + 1  # 假设拼不出来
        for j in coins:
            if i >= j:
                a[i] = min(a[i - j] + 1, a[i])
    if a[amount] == amount + 1:
        a[amount] = -1
    return a[amount]
print(coinChange([1,2,5],11))
