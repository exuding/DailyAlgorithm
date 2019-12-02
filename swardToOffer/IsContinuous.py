#-*- coding:utf-8 -*-
'''
@project: exuding-nlp-all
@author: taoxudong
@time: 2019-06-13 15:18:17 
'''

'''
一副扑克牌,发现里面居然有2个大王,2个小王(一副牌原本是54张^_^)...
随机从中抽出了5张牌,想测测自己的手气,看看能不能抽到顺子
“红心A,黑桃3,小王,大王,方片5”,“Oh My God!”不是顺子.....
LL不高兴了,他想了想,决定大\小 王可以看成任何数字,并且A看作1,J为11,Q为12,K为13。
上面的5张牌就可以变成“1,2,3,4,5”(大小王分别看作2和4),“So Lucky!”。LL决定去买体育彩票啦。
现在,要求你使用这幅牌模拟上面的过程,然后告诉我们LL的运气如何， 如果牌能组成顺子就输出true，否则就输出false。
为了方便起见,你可以认为大小王是0。
'''

'''
    思路：
    0到13内的数，每个数有4张，共54张，其中抽取5张，判断能否组成连续的数 
    说明：0可以当作任意的数 
    先排序比较处理 
    重复数不是0，一定不可以组成连续数
'''
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if len(numbers) == 0:
            return False
        # 对数字进行排序
        numbers.sort()
        # 大小王个数
        numofking = numbers.count(0)
        numoflack = 0
        for i in range(numofking, len(numbers) - 1):
            if numbers[i] == numbers[i + 1]:
                return False
            if numbers[i + 1] == numbers[i] + 1:
                continue
            else:
                # 统计相邻数字之间的空缺数
                numoflack += (numbers[i + 1] - numbers[i] - 1)
        if numoflack <= numofking:
            return True
        else:
            return False

s = Solution()
a = s.IsContinuous()
print(a)