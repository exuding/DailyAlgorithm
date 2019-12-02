#-*- coding:utf-8 -*-
'''
@project: exuding-nlp-all
@author: taoxudong
@time: 2019-07-01 14:42:16 
'''
##全排列算法
'''
简单来说，它的思想即为，确定第1位，对n-1位进行全排列，确定第二位，对n-2位进行全排列
当指针指向第一个元素a时，它可以是其本身a(即和自己进行交换)，还可以和b，c进行交换，故有3种可能，
当第一个元素a确定以后，指针移向第二位置，第二个位置可以和其本身b及其后的元素c进行交换，又可以形成两种排列，
当指针指向第三个元素c的时候，这个时候其后没有元素了，此时，则确定了一组排列，输出。
但是每次输出后要把数组恢复为原来的样子。
'''
#1. 利用递归实现全排列
def permutations(arr,position,end):
    if position == end:
        print(arr)
    else:
        for index in range(position,end):
            arr[index],arr[position] = arr[position],arr[index]
            permutations(arr,position+1,end)
            arr[index],arr[position] = arr[position],arr[index]
arr=['a','b','c']
permutations(arr,0,len(arr))
#2.利用深度优先算法实现全排列
'''
深度搜索，返回时回溯
'''

