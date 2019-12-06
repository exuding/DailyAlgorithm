
# leetcode进阶之路，道阻且长

## 1.数组之和

### 解题之前需要先想好各种可能情况，比如[],[1],[3,3],[1,2,3,4,3]等特殊情况

    示例:
    给定 nums = [2, 7, 11, 15], target = 9
    因为 nums[0] + nums[1] = 2 + 7 = 9
    所以返回 [0, 1]
    '''
    #获取list中的值和索引的对应关系
    cc = [1, 2, 3, 2, 4]
    from collections import defaultdict
    dd = defaultdict(list)
    for k, va in [(v,i) for i, v in enumerate(cc)]:
        dd[k].append(va)
    print(dd)
    '''
    def twoSum(self, nums, target):
        res = []
        for index,i in enumerate(nums):#enumerate同时获取索引和值
            temp = []
            b = target - i
            if b in nums[index+1:]:#python切片是左闭右开的
                temp.append(index)
                c = nums[index + 1:]
                temp.append(c.index(b)+index+1)
            res.extend(temp)
        return res

## 2.两数相加
    
    给出两个非空的链表用来表示两个非负的整数。它们各自的位数是按照逆序的方式存储的，并且它们的每个节点只能存储一位数字。
    如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
    您可以假设除了数字0之外，这两个数都不会以0开头。
    示例：
    输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
    输出：7 -> 0 -> 8
    原因：342 + 465 = 807
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #为新链表插入做准备，要学习
        head = None  # 链表头
        tail = None  # 链表尾部，方便插入的时候不需要遍历
        carry = 0
        while l1 or l2:#这样不用判断谁最长，只考虑节点是否为空
            l1_v = l1.val if l1 else 0 #没了就赋值为0，否则取节点的值
            l2_v = l2.val if l2 else 0 #没了就赋值为0，否则取节点的值
            val = l1_v + l2_v + carry
            carry = val // 10#这种方式要学习 不需要if>10判断
            val = val % 10

            node = ListNode(val)#链表赋值和c不太一样
            ###根绝指针操作逐渐添加链表节点
            if not head:
                head = node
                tail = head
            else:
                tail.next = node
                tail = node
            #一直以节点有无作为判断，有就指向下一个节点
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        #考虑同长度最后进一位情况，容易忘
        if carry > 0:
            tail.next = ListNode(1)
        return head

## 3.无重复字符的最大子串
    
    给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
    示例 1:
        输入: "abcabcbb"
        输出: 3 
        解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
    示例 2:
        输入: "bbbbb"
        输出: 1
        解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
    示例 3:
        输入: "pwwkew"
        输出: 3
        解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
    class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_number = 0
        number = 0
        test = ''  # 维护一个最长子串
        for i in s:
            # 如果i不在test字符串里面，字符串test添加这个字符，number+1
            if i not in test:
                test += i
                number += 1
                global s1
                s1 = test
            else:  # i在test字符串里
                if number >= max_number:
                    max_number = number
                index = test.index(i)
                test = test[(index + 1):] + i
                print(test)
                number = len(test)
            if number > max_number:
                max_number = number
        # print(s1)
        # print(max_number)
        return max_number


## 4. 寻找两个有序数组的中位数

    给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
    请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
    示例 1:
    nums1 = [1, 3]
    nums2 = [2]
    则中位数是 2.0
    示例 2:
    nums1 = [1, 2]
    nums2 = [3, 4]
    则中位数是 (2 + 3)/2 = 2.5
    class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #奇数找中位数，偶数找中间两数平均
        #注意原数组是有序数组
        '''
            这个题目可以归结到寻找第k小(大)元素问题
            对于奇数的情况，直接找到最中间的数即可，偶数的话需要求最中间两个数的平均值。
            为了简化代码，不分情况讨论，我们使用一个小trick，我们分别找第 (m+n+1) / 2 个，和 (m+n+2) / 2 个，然后求其平均值即可，这对奇偶数均适用。
            思路可以总结如下：取两个数组中的第k/2个元素进行比较，
            如果数组1的元素小于数组2的元素，
            则说明数组1中的前k/2个元素不可能成为第k个元素的候选，
            所以将数组1中的前k/2个元素去掉，组成新数组和数组2求第k-k/2小的元素，
            因为我们把前k/2个元素去掉了，所以相应的k值也应该减小。
            另外就是注意处理一些边界条件问题，比如某一个数组可能为空或者k为1的情况。
        '''

        def findKthElement(arr1, arr2, k):
            len1, len2 = len(arr1), len(arr2)
            if len1 > len2:
                #数组长的作为参数2
                return findKthElement(arr2, arr1, k)
            if not arr1:
                #如果短的参数1为空 递归返回条件
                return arr2[k - 1]
            if k == 1:
                #递归返回条件
                return min(arr1[0], arr2[0])
            i, j = min(k // 2, len1) - 1, min(k // 2, len2) - 1
            if arr1[i] > arr2[j]:
                return findKthElement(arr1, arr2[j + 1:], k - j - 1)
            else:
                return findKthElement(arr1[i + 1:], arr2, k - i - 1)

        l1, l2 = len(nums1), len(nums2)
        left, right = (l1 + l2 + 1) // 2, (l1 + l2 + 2) // 2
        return (findKthElement(nums1, nums2, left) + findKthElement(nums1, nums2, right)) / 2
## 5. 最长回文子串
    
    '''
    解法1：暴力解法，找到所有的子串，如果找到的子串比当前所存的最大子串长就替换 很像选择排序
    '''
    def longestPalindrome1(s):
        s = list(s)
        sub = s[0:1]#存放最大子串变量
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                temp = s[i:j]
                tempRe = s[i:j][::-1]
                if (temp == tempRe and len(temp)>len(sub)):
                    sub = temp
    
        return ''.join(sub)
    
    '''
    解法2:动态规划  算法时间复杂度为O(n*n)，空间复杂度为O(n*n)
    动态规划讲解链接：http://hawstein.com/2013/03/26/dp-novice-to-advanced/
    动态规划三个元素：最优子结构，边界，状态转移公式
    #####本题####
    假设dp[i,j]=1表示str[i...j]是回文子串，那个必定存在dp[i+1,j-1]=1。
    这样最长回文子串就能分解成一系列子问题，可以利用动态规划求解了
    
    '''
    def longestPalindrome2(s):
        #当前算法，时间复杂度为O(n*n)，空间复杂度为O(n*n)
        k = len(s)# 计算字符串的长度
        matrix = [[0 for i in range(k)] for i in range(k)]# 初始化n*n的列表
        logestSubStr = ""# 存储最长回文子串
        logestLen = 0# 最长回文子串的长度
    
        for j in range(0, k):
            for i in range(0, j + 1):
                if j - i <= 1:
                    if s[i] == s[j]:
                        matrix[i][j] = 1# 此时f(i,j)置为true
                        if logestLen < j - i + 1:# 将s[i:j]的长度与当前的回文子串的最长长度相比 
                            logestSubStr = s[i:j + 1]  # 取当前的最长回文子串
                            logestLen = j - i + 1  # 当前最长回文子串的长度
                else:
                    if s[i] == s[j] and matrix[i + 1][j - 1]:# 判断
                        matrix[i][j] = 1
                        if logestLen < j - i + 1:
                            logestSubStr = s[i:j + 1]
                            logestLen = j - i + 1
        return logestSubStr
    
    '''
    解法三：解法二的优化 算法的空间复杂度就为O(2n)，即O(n)
    当j>1时，判断f(i,j)是否为回文子串的操作只与j-1时的的操作相关，
    即f(i,j) = g(f(i, j-1))，其中j>1，i in range(0, j+1)，所以接下来就变成求解g()函数了。    
    用nlist存储j情况下所有的子串是否为回文子串的标志
    用olist存储j-1情况下所有的子串是否为回文子串的标志
    那么olist与nlist的关系是什么呢？
    nlist[i] = g(olist[i+1])
    '''
    def longestPalindrome3(s):
        k = len(s)
        olist = [0] * k# 申请长度为n的列表，并初始化
        nList = [0] * k# 同上
        logestSubStr = ""
        logestLen = 0
    
        for j in range(0, k):
            for i in range(0, j + 1):
                if j - i <= 1:
                    if s[i] == s[j]:
                        nList[i] = 1# 当 j 时，第 i 个子串为回文子串
                        len_t = j - i + 1
                        if logestLen < len_t:# 判断长度
                            logestSubStr = s[i:j + 1]
                            logestLen = len_t
                else:
                    if s[i] == s[j] and olist[i + 1]:# 当j-i>1时，判断s[i]是否等于s[j]，并判断当j-1时，第i+1个子串是否为回文子串
                        nList[i] = 1# 当 j 时，第 i 个子串为回文子串
                        len_t = j - i + 1
                        if logestLen < len_t:
                            logestSubStr = s[i:j + 1]
                            logestLen = len_t
            olist = nList# 覆盖旧的列表
            nList = [0] * k# 新的列表清空
        return logestSubStr
## 6. Z 字形变换
    
    解法一：暴力解法
    def convert(s, numRows):
    if len(s)==1:
        return s
    if numRows ==1:
        return s
    s = list(s)
    n = 0
    temp = [[0 for i in range(len(s))] for j in range(numRows)]
    for j in range(0, len(s), numRows - 1):#numRows - 1 不能为0
            for i in range(0,numRows):
                if i<=numRows-1 and n<len(s):
                    temp[i][j] = s[n]
                    n = n+1
                else:
                    break
            for i in range(1,numRows-1):
                if i<=numRows-2 and n <len(s):
                    temp[numRows-i-1][j+i] = s[n]
                    n = n + 1
                else:
                    break
    res = []
    for row in range(len(temp)):
        for col in range(len(s)):
            if temp[row][col]!=0:
                res.append(temp[row][col])

    return ''.join(res)

## 7. 整数反转
     
    def reverse(x):
        max = math.pow(2, 31)-1
        min = math.pow(2,31)*-1
        if x>0:
            a = list(str(x))[::-1]
            for i in a:
                if i == 0:
                    a.pop(i)
                else:
                    break
            res = int(''.join(a))
            return res if min<res<max else 0

        else:
            a = list(str(x*-1))[::-1]
            for i in a:
                if i == 0:
                    a.pop(i)
                else:
                    break
            res = int(''.join(a))*-1
            return res if min<res<max else 0

## 8.字符串转换整数 (atoi)
    
    这题主要是给测试做的，各种案例过不去'0+-1'，'+-2'，'4  +5-8'等等
    正则表达式来做吧
    max min 来限制越界问题ß
    def myAtoi(self, s: str) -> int:
        return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2**31 - 1),-2**31)





          