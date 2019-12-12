#-*- coding:utf-8 -*-
'''
@project: DailyAlgorithm
@author: taoxudong
@time: 2019-12-11 10:55:49 
'''

def longestCommonPrefix(strs):
    if strs:
        max = strs[0]
    else:
        return ''
    def getSImStr(s1,s2):
        res = ''
        min_len = min(len(s1),len(s2))
        for i in range(min_len):
            if s1[i]==s2[i]:
                res+=s2[i]
            else:
                break
        return res

    for i in range(1,len(strs)):
        max = getSImStr(max,strs[i])
        if max=='':
            break
    return max
a=longestCommonPrefix(["abab","aba","a"])
print(a)