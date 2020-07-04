#_*_coding:utf-8_*_
'''
@project: Exuding
@author: exudingtao
@time: 2019/12/23 11:26 下午
'''


def strStr(haystack, needle):
    len_n = len(needle)
    len_h = len(haystack)
    if len_h == 0 and len_n == 0:
        return 0
    if haystack == needle:
        return 0
    for i in range(len_h - len_n+1):
        print(haystack[i:i + len_n])
        if haystack[i:i + len_n] == needle:
            return i
        else:
            continue
    return -1
print(strStr("mississippi","pi"))