#_*_coding:utf-8_*_
'''
@project: Exuding
@author: exudingtao
@time: 2019/12/23 10:51 下午
'''
#双指针法
def removeElement(nums, val):
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1

    return i
#方法二
'''
方法二：双指针 —— 当要删除的元素很少时
思路
    现在考虑数组包含很少的要删除的元素的情况。
    如，num=[1，2，3，5，4]，Val=4num=[1，2，3，5，4]，Val=4。之前的算法会对前四个元素做不必要的复制操作。
    另一个例子是 num=[4，1，2，3，5]，Val=4num=[4，1，2，3，5]，Val=4。
    似乎没有必要将 [1，2，3，5][1，2，3，5] 这几个元素左移一步，因为问题描述中提到元素的顺序可以更改。
    
算法
    当我们遇到 nums[i] = valnums[i]=val 时，我们可以将当前元素与最后一个元素进行交换，并释放最后一个元素。这实际上使数组的大小减少了 1。
    请注意，被交换的最后一个元素可能是您想要移除的值。但是不要担心，在下一次迭代中，我们仍然会检查这个元素。
'''
def removeElement(nums, val):
    i,n =0,len(nums)
    while i<n:
        if nums[i]==val:
            nums[i] = nums[n-1]
            n-=1
        else:
            i+=1
    return n