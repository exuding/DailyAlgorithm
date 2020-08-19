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


## 分治

### 引文

MapReduce（分治算法的应用） 是 Google 大数据处理的三驾马车之一，另外两个是 GFS 和 Bigtable。它在倒排索引、PageRank 计算、网页分析等搜索引擎相关的技术中都有大量的应用。

尽管开发一个 MapReduce 看起来很高深，感觉遥不可及。实际上，万变不离其宗，它的本质就是分治算法思想，分治算法。如何理解分治算法？为什么说 MapRedue 的本质就是分治算法呢？

### 主要思想

分治算法的主要思想是将原问题**递归地分成**若干个子问题，直到子问题**满足边界条件**，停止递归。将子问题逐个击破(一般是同种方法)，将已经解决的子问题合并，最后，算法会**层层合并**得到原问题的答案。

### 分治算法的步骤

* 分：**递归地**将问题**分解**为各个的子**问题**(性质相同的、相互独立的子问题)；
* 治：将这些规模更小的子问题**逐个击破**；
* 合：将已解决的子问题**逐层合并**，最终得出原问题的解；

![](https://img-blog.csdnimg.cn/20200408204450701.png)

### 分治法适用的情况

* 原问题的**计算复杂度**随着问题的规模的增加而增加。
* 原问题**能够被分解**成更小的子问题。
* 子问题的**结构和性质**与原问题一样，并且**相互独立**，子问题之间**不包含**公共的子子问题。
* 原问题分解出的子问题的解**可以合并**为该问题的解。



### 伪代码

```python
def divide_conquer(problem, paraml, param2,...):
    # 不断切分的终止条件
    if problem is None:
        print_result
        return
    # 准备数据
    data=prepare_data(problem)
    # 将大问题拆分为小问题
    subproblems=split_problem(problem, data)
    # 处理小问题，得到子结果
    subresult1=self.divide_conquer(subproblems[0],p1,..…)
    subresult2=self.divide_conquer(subproblems[1],p1,...)
    subresult3=self.divide_conquer(subproblems[2],p1,.…)
    # 对子结果进行合并 得到最终结果
    result=process_result(subresult1, subresult2, subresult3,...)
```

### 举个栗子

​		通过应用举例分析理解分治算法的原理其实并不难，但是要想灵活应用并在编程中体现这种思想中却并不容易。所以，这里这里用分治算法应用在排序的时候的一个栗子，加深对分治算法的理解。

相关概念：

- **有序度**：表示一组数据的有序程度
- **逆序度**：表示一组数据的无序程度

一般通过**计算有序对或者逆序对的个数**，来表示数据的有序度或逆序度。

假设我们有 `n` 个数据，我们期望数据从小到大排列，那完全有序的数据的有序度就是 $n(n-1)/2$，逆序度等于 0；相反，倒序排列的数据的有序度就是 0，逆序度是 $n(n-1)/2$。

**Q：如何编程求出一组数据的有序对个数或者逆序对个数呢？**

因为有序对个数和逆序对个数的求解方式是类似的，所以这里可以只思考逆序对（常接触的）个数的求解方法。

- 方法1
  - 拿数组里的每个数字跟它后面的数字比较，看有几个比它小的。
  - 把比它小的数字个数记作 `k`，通过这样的方式，把每个数字都考察一遍之后，然后对每个数字对应的 `k` 值求和
  - 最后得到的总和就是逆序对个数。
  - 这样操作的时间复杂度是$O(n^2)$（需要两层循环过滤）。那有没有更加高效的处理方法呢？这里尝试套用分治的思想来求数组 A 的逆序对个数。
- 方法2
  - 首先将数组分成前后两半 A1 和 A2，分别计算 A1 和 A2 的逆序对个数 K1 和 K2
  - 然后再计算 A1 与 A2 之间的逆序对个数 K3。那数组 A 的逆序对个数就等于 K1+K2+K3。
  - 注意使用分治算法其中一个要求是，**子问题合并的代价不能太大**，否则就起不了降低时间复杂度的效果了。
  - **如何快速计算出两个子问题 A1 与 A2 之间的逆序对个数呢？这里就要借助归并排序算法了。（这里先回顾一下归并排序思想）**如何借助归并排序算法来解决呢？归并排序中有一个非常关键的操作，就是将两个有序的小数组，合并成一个有序的数组。实际上，在这个合并的过程中，可以计算这两个小数组的逆序对个数了。每次合并操作，我们都计算逆序对个数，把这些计算出来的逆序对个数求和，就是这个数组的逆序对个数了。

### 算法应用

#### [169. 多数元素](https://leetcode-cn.com/problems/majority-element/)

* 题目描述

  给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 [n/2] 的元素。

  你可以假设数组是非空的，并且给定的数组总是存在众数。

  示例 1:

  ```python
  输入: [3,2,3]
  输出: 3
  ```

  示例 2:

  ```python
  输入: [2,2,1,1,1,2,2]
  输出: 2
  ```

* 解题思路

  * 确定切分的终止条件
  
    直到所有的子问题都是长度为 1 的数组，停止切分。
  
  * 准备数据，将大问题切分为小问题
  
    递归地将原数组二分为左区间与右区间，直到最终的数组只剩下一个元素，将其返回
  
  * 处理子问题得到子结果，并合并
  
    - 长度为 1 的子数组中唯一的数显然是众数，直接返回即可。
  
    - 如果它们的众数相同，那么显然这一段区间的众数是它们相同的值。
  
    - 如果他们的众数不同，比较两个众数在整个区间内出现的次数来决定该区间的众数

* 代码

  ```python
  class Solution(object):
      def majorityElement2(self, nums):
          """
          :type nums: List[int]
          :rtype: int
          """
          # 【不断切分的终止条件】
          if not nums:
              return None
          if len(nums) == 1:
              return nums[0]
          # 【准备数据，并将大问题拆分为小问题】
          left = self.majorityElement(nums[:len(nums)//2])
          right = self.majorityElement(nums[len(nums)//2:])
          # 【处理子问题，得到子结果】
          # 【对子结果进行合并 得到最终结果】
          if left == right:
              return left
          if nums.count(left) > nums.count(right):
              return left
          else:
              return right    
  ```
  

#### [53. 最大子序和](https://leetcode-cn.com/problems/maximum-subarray/)

* 题目描述

  给定一个整数数组 `nums` ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

  示例:

  ```
  输入: [-2,1,-3,4,-1,2,1,-5,4],
  输出: 6
  解释: 连续子数组 [4,-1,2,1] 的和最大为6。
  ```

* 解题思路

  * 确定切分的终止条件

    直到所有的子问题都是长度为 1 的数组，停止切分。

  * 准备数据，将大问题切分为小问题

    递归地将原数组二分为左区间与右区间，直到最终的数组只剩下一个元素，将其返回

  * 处理子问题得到子结果，并合并

    - 将数组切分为左右区间
      - 对与左区间：从右到左计算左边的最大子序和
      - 对与右区间：从左到右计算右边的最大子序和

    - 由于左右区间计算累加和的方向不一致，因此，左右区间直接合并相加之后就是整个区间的和
    - 最终返回左区间的元素、右区间的元素、以及整个区间(相对子问题)和的最大值

* 代码

  ```python
  class Solution(object):
      def maxSubArray(self, nums):
          """
          :type nums: List[int]
          :rtype: int
          """
          # 【确定不断切分的终止条件】
          n = len(nums)
          if n == 1:
              return nums[0]
  
          # 【准备数据，并将大问题拆分为小的问题】
          left = self.maxSubArray(nums[:len(nums)//2])
          right = self.maxSubArray(nums[len(nums)//2:])
  
          # 【处理小问题，得到子结果】
          #　从右到左计算左边的最大子序和
          max_l = nums[len(nums)//2 -1] # max_l为该数组的最右边的元素
          tmp = 0 # tmp用来记录连续子数组的和
          
          for i in range( len(nums)//2-1 , -1 , -1 ):# 从右到左遍历数组的元素
              tmp += nums[i]
              max_l = max(tmp ,max_l)
              
          # 从左到右计算右边的最大子序和
          max_r = nums[len(nums)//2]
          tmp = 0
          for i in range(len(nums)//2,len(nums)):
              tmp += nums[i]
              max_r = max(tmp,max_r)
              
          # 【对子结果进行合并 得到最终结果】
          # 返回三个中的最大值
          return max(left,right,max_l+ max_r)
  ```

  

#### [50. Pow(x, n)](https://leetcode-cn.com/problems/powx-n/)

* 题目描述

  实现 `pow(x, n) `，即计算 `x` 的 `n` 次幂函数。

  示例 1:

  ```
  输入: 2.00000, 10
  输出: 1024.00000
  ```

  示例 2:

  ```
  输入: 2.10000, 3
  输出: 9.26100
  ```

  示例 3:

  ```
  输入: 2.00000, -2
  输出: 0.25000
  解释: 2-2 = 1/22 = 1/4 = 0.25
  ```

  说明:

  `-100.0 < x < 100.0`
  `n `是 32 位有符号整数，其数值范围是$[−2^{31}, 2^{31} − 1] $。

* 解题思路

  * 确定切分的终止条件

    对`n`不断除以2，并更新`n`，直到为0，终止切分

  * 准备数据，将大问题切分为小问题

    对`n`不断除以2，更新

  * 处理子问题得到子结果，并合并

    * `x`与自身相乘更新`x`
    * 如果`n%2 ==1`
      - 将`p`乘以`x`之后赋值给`p`(初始值为1)，返回`p`
  * 最终返回`p`

* 代码

  ```python
  class Solution(object):
      def myPow(self, x, n):
          """
          :type x: float
          :type n: int
          :rtype: float
          """
          # 处理n为负的情况
          if n < 0 :
              x = 1/x
              n = -n
          # 【确定不断切分的终止条件】
          if n == 0 :
              return 1
  
          # 【准备数据，并将大问题拆分为小的问题】
          if n%2 ==1:
            # 【处理小问题，得到子结果】
            p = x * self.myPow(x,n-1)# 【对子结果进行合并 得到最终结果】
            return p
          return self.myPow(x*x,n/2)  
  ```

