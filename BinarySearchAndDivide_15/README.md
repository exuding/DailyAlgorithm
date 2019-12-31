# 二分法和分治法
    1.分析二分查找的一个技巧是：不要出现 else，而是把所有情况用 else if 写清楚，这样可以清楚地展现所有细节
    2.见到一个二分查找的代码时，首先注意这几个地方：
        nums[mid] == targe之后
        left = ...
        right = ...
    3.计算 mid 时需要技巧防止溢出，即 mid=left+(right-left)/2 更进一步要mid = (left + right) >> 1
    4. 为什么 while 循环的条件中是 <=，而不是 < ？
    答：因为初始化 right 的赋值是 nums.length-1，即最后一个元素的索引，而不是 nums.length。
    二者可能出现在不同功能的二分查找中，区别是：前者相当于两端都闭区间 [left, right]，后者相当于左闭右开区间 [left, right)，因为索引大小为 nums.length 是越界的。
    5.while(left <= right) 的终止条件是 left == right + 1
    6.while(left < right) 的终止条件是 left == right
 
## 33. 搜索旋转排序数组
    描述：
        假设按照升序排序的数组在预先未知的某个点上进行了旋转。( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
        搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
        可以假设数组中不存在重复的元素，算法时间复杂度必须是 O(log n) 级别。
    例子：
        输入: nums = [4,5,6,7,0,1,2], target = 0
        输出: 4
    题解：BFS-注意用cur_level和next_level  其实就是用cur_level代替以前的pop()最后一个 list代替节点
        class Solution:
            def search(self, nums: List[int], target: int) -> int:
                if not nums:return -1
                left,right = 0,len(nums)-1
                mediumPlus = nums[0]
                mid = left + (right-left)//2
                while left<=right:#等号必须有
                    if target == nums[mid]:return mid
                    if mediumPlus<=nums[mid]:#左边生序 
                        if mediumPlus<=target <= nums[mid]:#不用找右边小的部分
                            right = mid - 1
                        else:
                            left = mid + 1
                    else:#mediumPlus>nums[mid]###右边生序
                        if nums[mid]<=target<=nums[right] :
                            left = mid + 1
                        else:
                            right = mid - 1
                    mid = left + (right-left)//2
                return -1
## 34.在排序数组中查找元素的第一个和最后一个位置
    描述：
        给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
        你的算法时间复杂度必须是 O(log n) 级别。
        如果数组中不存在目标值，返回 [-1, -1]。
    例子：
        输入: nums = [5,7,7,8,8,10], target = 8
        输出: [3,4]
    题解：
    class Solution:
        def searchRange(self, nums: List[int], target: int) -> List[int]:
            return [self.left_bound(nums,target), self.right_bound(nums,target)]
        def right_bound(self, nums, target):#可以找到左边界
            if len(nums) == 0:
                return -1
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
            if right >= 0 and nums[right] == target: return right # 注意
            else: return -1
        def left_bound(self, nums, target):#可以找到右边界
            if len(nums) == 0:
                return -1
            left, right = 0, len(nums) - 1
    
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
            if left <= len(nums)-1 and nums[left] == target: return left  # 注意
            else: return -1  
  
## 35.搜索插入的位置
    描述：
        给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
    例子：
        输入: [1,3,5,6], 5
        输出: 2
        输入: [1,3,5,6], 2
        输出: 1
        输入: [1,3,5,6], 0
        输出: 0
    题解：
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not List:return 0
        left,right = 0,len(nums)-1
        mid = left + (right-left)//2
        while left<=right:
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid -1
            elif nums[mid] < target:
                left = mid + 1
            mid = left + (right-left)//2
        return left
    比较理解吧
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 返回大于等于 target 的索引，有可能是最后一个
        size = len(nums)
        # 特判
        if size == 0:
            return 0

        left = 0
        # 如果 target 比 nums里所有的数都大，则最后一个数的索引 + 1 就是候选值，因此，右边界应该是数组的长度
        right = size
        # 二分的逻辑一定要写对，否则会出现死循环或者数组下标越界
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                assert nums[mid] >= target
                # [1,5,7] 2
                right = mid
        # 调试语句
        # print('left = {}, right = {}, mid = {}'.format(left, right, mid))
        return left

