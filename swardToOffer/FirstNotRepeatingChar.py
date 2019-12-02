#-*- coding:utf-8 -*-
'''
@project: exuding-nlp-all
@author: taoxudong
@time: 2019-06-11 09:53:01 
'''
'''
在一个字符串(0<=字符串长度<=10000，全部由字母组成)
中找到第一个只出现一次的字符,
并返回它的位置, 如果没有则返回 -1（需要区分大小写）.

标准的书本解法，先在hash表中统计各字母出现次数，第二次扫描直接访问hash表获得次数
    int FirstNotRepeatingChar(string str) {
        if ( str.length() == 0)
            return -1;
         
        unsigned int hashTime[256] = {0};
        for(int i =0;i<str.length();++i)
            hashTime[str[i]]++;
         
        for(int i =0;i<str.length();++i)
        {
            if(hashTime[str[i]] == 1)
                return i;
        }
        return -1;
    }
'''
class Solution:
    def FirstNotRepeatingChar(self, s):
        if len(s)<=0:
            return -1
        list_s = list(s)
        for i in range(len(list_s)):
            if i<len(list_s) and list_s[i] not in list_s[i+1:] and list_s[i] not in list_s[0:i]:
                flag = i
                break
            else:
                flag = -1
        return flag