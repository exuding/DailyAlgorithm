#-*- coding:utf-8 -*-
'''
@project: Exuding
@author: taoxudong
@time: 2019-08-02 09:27:43 
'''
'''
请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        if s:
            list_s = list(s)
            for i in range(len(list_s)):
                if list_s[i] ==' ':
                    list_s[i] = '%20'
                res = ''.join(list_s)
            return res
        else:
            return  s
s = Solution()
a = s.replaceSpace('We Are Happy.')
print(a)
