#-*- coding:utf-8 -*-
'''
@project: exuding-nlp-all
@author: taoxudong
@time: 2019-06-13 15:00:42 
'''
'''
例如，“student. a am I”。后来才意识到，这家伙原来把句子单词的顺序翻转了，正确的句子应该是“I am a student.”。
Cat对一一的翻转这些单词顺序可不在行，你能帮助他么？


    算法思想：先翻转整个句子，然后，依次翻转每个单词。
    依据空格来确定单词的起始和终止位置
    
'''
class Solution:
    def ReverseSentence(self, s):
        #字符串按空格分开
        s = s.split(' ')
        s = s[::-1]
        s = ' '.join(s)
        return s
s = Solution()
a = s.ReverseSentence('student. a am I')
print(a)