#_*_coding:utf-8_*_
'''
@project: DailyAlgorithm
@author: exudingtao
@time: 2020/3/3 9:59 下午
'''
from collections import deque

class Sort(object):
    def __init__(self, array):
        self.array = array
        pass
    @staticmethod
    #冒泡排序是交换排序的一种，稳定，最好情况O(n),最坏O(n^2)
    def bubble_sort(array):
        if not array:
            return []
        for i in range(len(array)):
            for j in range(i+1,len(array)):
                if array[i] > array[j]:
                    temp = array[j]
                    array[j] = array[i]
                    array[i] = temp
        return array
    @staticmethod
    #选择排序，时间复杂度永远是O(n2)，不稳定
    #每一趟找到最小的索引
    def selection_sort(array):
        for i in range(len(array)):
            min_index = i
            for j in range(i+1, len(array)):
                if array[min_index] > array[j]:
                    min_index = j
            temp = array[min_index]
            array[min_index] = array[i]
            array[i] = temp
        return array
    @staticmethod
    #插入排序 时间复杂度O(n2)，想象成整理扑克牌
    def insert_sort(array):
        for i in range(len(array)-1):
            curent = array[i+1]
            pre_index = i
            while pre_index >= 0 and curent < array[pre_index]:
                #前半部分有序 后面第一个无序的找到  然后就是 后移和插入
                array[pre_index+1] = array[pre_index]
                pre_index -= 1
            array[pre_index+1] = curent
        return array

    #归并排序 始终都是O(n log n）的时间复杂度。代价是需要额外的内存空间。
    #该算法是采用分治法（Divide and Conquer）的一个非常典型的应用
    def merge_sort(self, array):
        if len(array) < 2:
            return array
        mid = len(array)/2
        left = self.merge_sort(array[:mid])
        right = self.merge_sort(array[mid:])
        return self.merge(left, right)

    # 归并排序——将两段排序好的数组结合成一个排序数组 [1,2,3][4,5]
    def merge(self,left, right):
        result = left + right
        result_num = len(left) + len(right)
        i = 0
        j = 0
        print(left,right)
        for index in range(result_num):
            if i >= len(left):
                result[index] = right[j]
                j = j + 1
            elif j >= len(right):
                result[index] = left[i]
                i = i + 1
            elif left[i] < right[j]:
                result[index] = left[i]
                i = i + 1
            else:
                result[index] = right[j]
                j = j + 1
        return result


    #快排
    # Quick Sort 分治法
    # 1.找基准
    # 2.基准定位 也叫分区 （比基准小的左移，比基准大的右移）
    # 3.递归的把左右分区子数列排序
    #最佳情况：T(n) = O(nlogn) 最差情况：T(n) = O(n2) 平均情况：T(n) = O(nlogn)
    def quick_sort(self, array,start,end):#end len(array)-1
        #分治 一分为2 递归结束条件
        if start >= end:
            return
        #定义双指针操作
        left = start
        right = end
        # 把0位置的数据，认为是中间值
        mid = array[left]
        while left < right:
            # 让右边游标往左移动，目的是找到小于mid的值，放到left游标位置
            while left < right and array[right] >= mid:
                right -= 1
            array[left] = array[right]
            # 让左边游标往右移动，目的是找到大于mid的值，放到right游标位置
            while left < right and array[left] < mid:
                left += 1
            array[right] = array[left]
        #mid 放入中间位置
        array[left] = mid
        #递归处理左边数据
        self.quick_sort(array, start, left-1)
        self.quick_sort(array, left+1, end)
        return array

    #堆排序
    #堆 1.满足完全二叉树（从上往下，从左往右）  2.跟节点值大于（小于）子节点值
    #无序的话从h-1层 做heapify 弄成堆
    #堆的性质：对于一个节点i 父节点是（i-1）/2 子节点是2i+1,2i+2
    #堆排序：1.如何把一个序列构造出一个大根堆
                    #调整大根堆，其实就是按照从右往左，从下到上的顺序，把每颗小树调整为一个大根堆,要找到第一个符合条件的调整节点
    #       2.输出堆顶元素后，如何使剩下的元素构造出一个大根堆

    #调用：a = [1,4,2,6,3,7,9,4]
    # array = deque(a)
    # array.appendleft(0)
    # res = sort.heap_sort(array)
    from collections import deque#链表结构deque可以直接在左添加辅助元素
    def swap_param(self, array, i, j):
        array[i], array[j] = array[j], array[i]
        return array
    #堆调整函数heap_adjust
    def heap_adjust(self, array, start, end):
        temp = array[start]
        i = start
        j = 2 * i #根的第一个左子树节点
        while j <= end:
            if (j < end) and (array[j] < array[j + 1]):#找到左右子树中最大的节点
                j += 1
            if temp < array[j]:#跟节点和子树中较大的节点交换
                array[i] = array[j]
                i = j
                j = 2 * i
            else:
                break
        array[i] = temp
    def heap_sort(self, array):#array为添加了辅助元素的deque
        arr_len = len(array) - 1
        first_sort_node = arr_len // 2 #找到 从右往左，从下到上的条件的第一个小树的跟节点
        for i in range(first_sort_node):
            self.heap_adjust(array, first_sort_node - i, arr_len)#例如根据4，3，2，1顺序节点，调整大根堆
        for i in range(arr_len-1):
            array = self.swap_param(array, 1, arr_len-i)#堆顶元素和最下边右边元素交换 且最后一个元素放最大
            self.heap_adjust(array, 1, arr_len-i-1)
        return [array[i] for i in range(1, arr_len)]




if __name__ == '__main__':
    sort = Sort([1,4,2,6,3,7,9,4])
    a = [1,4,2,6,3,7,9,4]
    array = deque(a)
    array.appendleft(0)
    res = sort.heap_sort(array)
    print(res)