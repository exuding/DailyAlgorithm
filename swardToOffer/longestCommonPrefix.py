#-*- coding:utf-8 -*-
'''
@project: Exuding
@author: taoxudong
@time: 2019-08-05 18:20:38 
'''
class Solution:
    def longestCommonPrefix(self, strs):
        res = []
        if len(strs)==0:
            return ''
        if len(strs) == 1:
            return strs[0]
        #j为列表中长度最小元素长度
        min_lenstr = min([len(i) for i in strs])
        for j in range(min_lenstr):
            i = 0
            while i < (len(strs)-1):
                if list(strs[i])[j] == list(strs[i+1])[j]:
                    i = i+1
                else:
                    return ''.join(res)
            res.append((strs[0])[j])
        return ''.join(res)

    def longestCommonPrefixotwo(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = []
        for x in zip(*strs):
            print(x)
            if len(set(x)) == 1:
                prefix.append(x[0])
            else:
                break
        return "".join(prefix)


s = Solution()
a = s.longestCommonPrefixotwo(["aca","acba","acdgf"])
print(a)