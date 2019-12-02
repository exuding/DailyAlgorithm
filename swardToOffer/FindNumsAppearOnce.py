#-*- coding:utf-8 -*-
'''
@project: exuding-nlp-all
@author: taoxudong
@time: 2019-06-13 11:16:04 
'''
'''
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
'''
# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        #去重 复制 减去开始的
        s = list(set(array))
        ss = s[:]
        new_arr = s + ss
        for i in array:
            if i in new_arr:
                new_arr.remove(i)
        return new_arr
s = Solution()
a = s.FindNumsAppearOnce([1,3,5,3,1,6,7,6])
print(a)
