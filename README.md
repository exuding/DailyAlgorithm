
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
## 9. 回文数
    
    可以用转化成字符串判断，也可以判断两个数 网站给的进阶是要求不用字符串
    def isPalindrome(x):
    if x < 0:
        return False
    temp = x
    res = 0
    while temp > 0:
        reNum = temp % 10
        temp = temp // 10
        res = res * 10 + reNum
    if res == x:
        return True
    else:
        return False
## 10.正则匹配
    
    此题可以空间换时间 动态规划解决 还可以回溯法解决 要从后往前找
    题解链接：https://hk029.gitbooks.io/leetbook/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92/010.%20Regular%20Expression%20Matching/010.%20Regular%20Expression%20Matching.html
    状态 
    首先状态 dp 一定能自己想出来。
    dp[i][j] 表示 s 的前 i个是否能被 p 的前 j 个匹配
    转移方程
    怎么想转移方程？首先想的时候从已经求出了 dp[i-1][j-1] 入手，再加上已知 s[i]、p[j]，要想的问题就是怎么去求 dp[i][j]。
    已知 dp[i-1][j-1] 意思就是前面子串都匹配上了，不知道新的一位的情况。
    那就分情况考虑，所以对于新的一位 p[j] s[i] 的值不同，要分情况讨论：
    考虑最简单的 p[j] == s[i] : dp[i][j] = dp[i-1][j-1]
    然后从 p[j] 可能的情况来考虑，让 p[j]=各种能等于的东西。
    p[j] == "." : dp[i][j] = dp[i-1][j-1]
    p[j] ==" * ":

    第一个难想出来的点：怎么区分 *∗ 的两种讨论情况
    首先给了 *，明白 * 的含义是 匹配零个或多个前面的那一个元素，所以要考虑他前面的元素 p[j-1]。* 跟着他前一个字符走，前一个能匹配上 s[i]，* 才能有用，前一个都不能匹配上 s[i]，* 也无能为力，只能让前一个字符消失，也就是匹配 00 次前一个字符。
    所以按照 p[j-1] 和 s[i] 是否相等，我们分为两种情况：
    3.1 p[j-1] != s[i] : dp[i][j] = dp[i][j-2]
    这就是刚才说的那种前一个字符匹配不上的情况。
    比如(ab, abc * )。遇到 * 往前看两个，发现前面 s[i] 的 ab 对 p[j-2] 的 ab 能匹配，虽然后面是 c*，但是可以看做匹配 00 次 c，相当于直接去掉 c *，所以也是 True。注意 (ab, abc**) 是 False。
    3.2 p[j-1] == s[i] or p[j-1] == "."：
    * 前面那个字符，能匹配 s[i]，或者 * 前面那个字符是万能的 .
    因为 . * 就相当于 . .，那就只要看前面可不可以匹配就行。
    比如 (##b , ###b *)，或者 ( ##b , ### . * ) 只看 ### 后面一定是能够匹配上的。
    所以要看 b 和 b * 前面那部分 ## 的地方匹不匹配。
    第二个难想出来的点：怎么判断前面是否匹配
        dp[i][j] = dp[i-1][j] // 多个字符匹配的情况	
        or dp[i][j] = dp[i][j-1] // 单个字符匹配的情况
        or dp[i][j] = dp[i][j-2] // 没有匹配的情况	
    看 ### 匹不匹配，不是直接只看 ### 匹不匹配，要综合后面的 b b* 来分析
    这三种情况是 oror 的关系，满足任意一种都可以匹配上，同时是最难以理解的地方：
        dp[i-1][j] 就是看 s 里 b 多不多， ### 和 ###b * 是否匹配，一旦匹配，s 后面再添个 b 也不影响，因为有 * 在，也就是 ###b 和 ###b *也会匹配。
        dp[i][j-1] 就是去掉 * 的那部分，###b 和 ###b 是否匹配，比如 qqb qqb
        dp[i][j-2] 就是 去掉多余的 b *，p 本身之前的能否匹配，###b 和 ### 是否匹配，比如 qqb qqbb* 之前的 qqb qqb 就可以匹配，那多了的 b * 也无所谓，因为 b * 可以是匹配 00 次 b，相当于 b * 可以直接去掉了。
        三种满足一种就能匹配上。
    为什么没有 dp[i-1][j-2] 的情况？ 就是 ### 和 ### 是否匹配？因为这种情况已经是 dp[i][j-1] 的子问题。也就是 s[i]==p[j-1]，则 dp[i-1][j-2]=dp[i][j-1]。
    最后来个归纳：
        如果 p.charAt(j) == s.charAt(i) : dp[i][j] = dp[i-1][j-1]；
        如果 p.charAt(j) == '.' : dp[i][j] = dp[i-1][j-1]；
        如果 p.charAt(j) == '*'：
        如果 p.charAt(j-1) != s.charAt(i) : dp[i][j] = dp[i][j-2] //in this case, a* only counts as empty
        如果 p.charAt(i-1) == s.charAt(i) or p.charAt(i-1) == '.'：
        dp[i][j] = dp[i-1][j] //in this case, a* counts as multiple a
        or dp[i][j] = dp[i][j-1] // in this case, a* counts as single a
        or dp[i][j] = dp[i][j-2] // in this case, a* counts as empty
    第二种题解 代码依据的题解：
    首先建立了一个全部为False的二维矩阵保存递归的结果,行数是(字符串长度+1),列数是(p的长度+1).这里为什么要多建一行一列呢?因为需要考虑到p和s为空的情况. 其中dp[i][j]表明字符串s[:i]与p[:j]的匹配结果.(其中s[:i]最后一个元素为s[i-1],p[:j]最后一个元素为p[j-1],搞懂这一点才看得懂代码的)
    首先处理i为0(s=='')或者j为0(p=='')的情况.当p==''时,只有s==''时二者才能匹配,所以首列中,只有首个元素为0,即dp[0][0]=0. 当s==''时,只有p==''或者p=='x*y*'(或类似形式)时,二者才能匹配. 所以有
    dp[0][j] ==( j >= 2) and (p[j-1]=='*') and (dp[0][j-2]). 
    有必要对上面这个式子解释: 首先j>=2,因为j=1时,p不为空,也不存在首个元素就为*的情况,所以此时p与s肯定无法匹配.dp[0][j]对应p的子串,最后一个元素为p[j-1],只有p[j-1]=='*'时才有可能匹配成功.同时需要dp[0][j-2]同样为True时,dp[0][j]才能为True.(这个地方好好理解一下,对下面的总代码理解很重要)
    下面就使用双重循环开始递归了.dp[i][j]对应s的子串,最后一个元素为s[i-1],对应p的子串,最后一个元素为p[j-1].
    一. 首先判断p[j-1]是否为'*'. 如果p[j-1] == '*',那么'*'前面肯定是有一个字母的(比如说b吧),那么需要同时考虑'b*',此时分两种情况:
    'b*'是无用的,比如s='aaaa',p='a*b*'.此时s与p的配对结果与s与'a*'配对的结果是一样的.所以有
    dp[i][j] = dp[i][j-2].
    'b*'是有用的,比如s='aabb',p='a*b*'.之前s='aab',p='a*b'时二者已经配对过了,所以s='aab',p='a*b*'时,二者同样能配对,同样需要判断s[i-1]是否与p[j-2]相同,或者p[j-2]=='.'(即可以代替任何字符),所以有
    dp[i][j] = dp[i-1][j] and (p[j-2] == s[i-1] or p[j-2] == '.')
    1与2两种情况有一种成立就行,即取或.
    if p[j-1] == '*':
                        dp[i][j] = dp[i][j-2] or (dp[i-1][j] and (p[j-2] == s[i-1] or p[j-2] == '.'))
    二. 如果p[j-1]不为'*'.,判断起来就相对简单了.首先要考虑之前的子串是否匹配成功了,即dp[i-1][j-1]的值,同时要考虑dp[i][j]对应的s的子串最后一位s[i-1],p的子串p[j-1]是否相等, p[j-1] == '.'时同样满足情况,毕竟'.'是万能匹配符. 所以就
    else:
                        dp[i][j] = dp[i-1][j-1] and(p[j-1] == s[i-1] or p[j-1] == '.')
    递归的过程中环环相扣,字符串s能否与p匹配取决于两个的子串能够逐渐匹配.真的是学到了很多,最后dp[len(s)][len(p)]位置上的布尔值(即二维矩阵右下角的值)就表明了s能够与p匹配,直接返回dp[len(s)][len(p)]就行了.下面是总代码
    希望能对大家有所帮助~~~
    
    class Solution:
        def isMatch(self, s, p):
            dp = [[False for i in range(len(p)+1)] for j in range(len(s)+1)]
            
            dp[0][0] = True
            for j in range(1, len(p) + 1):
                dp[0][j] ==( j >= 2) and (p[j-1]=='*') and (dp[0][j-2]). 
            
            for i in range(1, len(s)+1):
                for j in range(1, len(p)+1):
                    if p[j-1] == '*':
                        dp[i][j] = dp[i][j-2] or (dp[i-1][j] and (p[j-2] == s[i-1] or p[j-2] == '.'))
                    else:
                        dp[i][j] = dp[i-1][j-1] and(p[j-1] == s[i-1] or p[j-1] == '.')
            
            return dp[len(s)][len(p)]
            

## 12.整数转罗马数字

    #利用字符串
    def intToRoman(num):
        c = {0: ("", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"),
             1: ("", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"),
             2: ("", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"),
             3: ("", "M", "MM", "MMM")}
        res = ''
        str_num = str(num)
        for i in str(num):
            res += c[len(str(num)) - 1][int(i)]
            num = str_num[1:]
        return res
    #利用余数和整除 
    def intToRoman1(num):
        M = ("", "M", "MM", "MMM")
        C = ("", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM")
        X = ("", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC")
        I = ("", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX")
        return M[num // 1000] + C[(num % 1000) // 100] + X[((num % 100) // 10)] + I[num % 10]

## 13.罗马数字转整数

    #Python里有这个机制 负一索引对应的就是最后数组最后一个元素
    def romanToInt(s):
    #"IV""XL""CD"  4系列
    #"IX""XC""CM"  9系列
    c = {'M':1000,
         'C':100,
         'D':500,
         'X':10,
         'L':50,
         'I':1,
         'V':5}
    res = 0
    for i in s:
        temp = c[i]
        res +=temp
    s_list = list(s)
    for i in range(1,len(s_list)):#Python里有这个机制 负一索引对应的就是最后数组最后一个元素
        if s_list[i]=='V' and s_list[i-1]=='I':
            res -=2
        elif s_list[i]=='L' and s_list[i-1]=='X':
            res -=20
        elif s_list[i]=='D' and s_list[i-1]=='C':
            res -=200
        elif s_list[i]=='X' and s_list[i-1]=='I':
            res -=2
        elif s_list[i]=='C' and s_list[i-1]=='X':
            res -=20
        elif s_list[i]=='M' and s_list[i-1]=='C':
            res -=200
        else:
            res =res
    return res
## 14. 最长公共前缀
    
    def longestCommonPrefix(strs):
    if strs:
        max = strs[0]
    else:
        return ''
    def getSImStr(s1,s2):
        res = ''
        min_len = min(len(s1),len(s2))
        for i in range(min_len):
            if s1[i]==s2[i]:
                res=res+str(s2[i])
            else:
                break
        return res

    for i in range(1,len(strs)):
        max = getSImStr(max,strs[i])
        if max=='':
            break
    return max
## 15. 三数之和
    #时间效率
    def threeSum(nums):
        res = []
        #[0,0]
        if len(nums)<3:
            return []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                temp = 0 - (nums[i] + nums[j])
                if temp in nums[j+1:]:
                    temp_res = []
                    temp_res.append(nums[i])
                    temp_res.append(nums[j])
                    temp_res.append(temp)
                    temp_res.sort()
                    res.append(temp_res)
        lis2 = list()
        for li in res:
            if li not in lis2:
                lis2.append(li)
        return lis2

    def threeSum1(nums):
        '''
        1.特判，对于数组长度 nn，如果数组为 nullnull 或者数组长度小于 33，返回 [][]。
        2.对数组进行排序。
        3.遍历排序后数组：
            3.1若 nums[i]>0：因为已经排序好，所以后面不可能有三个数加和等于0，直接返回结果。
            3.2对于重复元素：跳过，避免出现重复解
            3.3令左指针 L=i+1，右指针 R=n-1，当 L<R 时，执行循环：
                3.3.1当 nums[i]+nums[L]+nums[R]==0，满足存储。在此基础上继续执行循环，如（-1 1 2 2 3）
                     判断左界和右界是否和下一位置重复，去除重复解。并同时将 L,R移到下一位置，寻找新的解
                3.3.2若和大于 0，说明 nums[R] 太大，R左移
                3.3.3若和小于 0，说明 nums[L] 太小，L右移
        '''
        # 对列表进行排序
        nums.sort()
        res, k = [], 0
        for k in range(len(nums) - 2):
            # 如果出现最小元素为正数，则不存在和为0的情况，直接返回
            if nums[k] > 0:
                break
            # 如果出现第一个元素重复的情况，为避免重复结果，跳过后续执行
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            # 定义接下来的两个元素的双指针
            i, j = k + 1, len(nums) - 1
            while i < j:
                s = nums[k] + nums[i] + nums[j]
                if s < 0:
                    i += 1
                    # 跳过重复元素
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                elif s > 0:
                    j -= 1
                    # 跳过重复元素
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                else:
                    # 当出现元素满足条件是，将结果加入到列表
                    res.append([nums[k], nums[i], nums[j]])
                    # 接着更新索引（注意跳过相同元素）
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
        return res
    
## 16. 最接近的三数之和
    
    双指针法的解题思路：
    1.先让数组有序，也就是需要先对数组进行排序
    2.然后每次固定一个元素，再去寻找另外两个元素，也就是双指针
    双指针法的代码实现：
    1.对数组进行排序
    2.初始化一个用于保存结果的值 result = nusm[0] + nums[1] + nums[2] （不要自己设初值，直接从数组中抽取三个元素，假设这是最接近的三数之和，然后再更新就是了）。
    3.利用下标 i 对数组进行遍历，此时就是在固定第一个元素，注意，下标 i 的边界为 i < nums.length-2，否则设置指针的时候会出现数组越界。
    4.每次遍历的过程中设置两个指针，分别是 left = i + 1、right = nums.length - 1。
    5.检查 sum = nums[i] + nums[left] + nums[right]与 target 的距离，如果该距离比之前保存的 result 与 target 的距离更小，就更新 result。
    6.然后就是移动双指针：
    如果 sum 的值比 target 大，那么我们让 right--，因为数组是有序的，right --会使得下一次的 sum 更小，也就更接近 target 的值
    同理，如果 sum 的值 target 小，那么我们让 left++。·
    left++ 和 right-- 的界限自然是 left != right，如果 left == right，说明我们已经将所有的元素都遍历过一遍了。
    重复上面的操作，直到i循环结束为止，返回 result。
    '''
    class Solution:
        def threeSumClosest(self, nums: List[int], target: int) -> int:
            if len(nums)<3:
                return ''
            nums.sort()
            min_num = nums[0]+nums[1]+nums[2]
            for i in range(len(nums)-2):
                first = i+1
                last = len(nums)-1
                while first != last:
                    temp = nums[first]+nums[last]+nums[i]
                    if temp == target:#相等
                        return target
                    if abs(temp - target) < abs(min_num - target):#更新结果
                        min_num = temp
                    if temp > target:#更新指针
                        last-=1
                        # 跳过重复元素
                        while first < last-1 and nums[last] == nums[last - 1]:
                            last -= 1
                    else:#更新指针
                        first += 1
                        #跳过重复元素
                        while first < last-1 and nums[first] == nums[first + 1]:
                            first += 1
            return min_num
    
    def threeSumClosest1(nums,target):
        if len(nums)<3:
            return ''
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            first = i + 1
            last = len(nums) - 1
            while first != last:
                sum = nums[first] + nums[last] + nums[i]
                if abs(sum - target) < abs(result - target):  # 更新结果
                    result = sum
                if sum > target:  # 更新指针
                    last -= 1
                else:  # 更新指针
                    first += 1
        return result
## 17.电话号码的字母组合

    #方法一 遍历上次的组合结果，逐个合并
    def letterCombinations(digits):
        KEY = {'2': ['a', 'b', 'c'],
               '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'],
               '9': ['w', 'x', 'y', 'z']}
        if not digits:
            return ''
        res = ['']#res就是一个逐渐添加的 又每一轮都遍历 完成了全排列
        for num in digits:
            temp =[]
            for char_item in KEY[num]:
                for r in res:
                    temp.append(char_item+r)
            res = temp
        return res
    
    #递归
    '''
    当没有数字的时候返回空
    当只有一个数字的时候，返回该数字对应的字母
    当有两个数字的时候，返回第一个数字对应的字母分别加上第二个数字所对应的字母，生成字符串列表
    当有三个数字的时候，返回第一个数字对应的字母分别加上后两个数字生成的字符串列表
    '''
    def letterCombinations1(digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        result = []
        tail = []
        len_d = len(digits)
        if len_d == 0:
            return tail
        if len_d == 1:
            return dic[digits]
    
        tail = letterCombinations(digits[1:])
    
        for i in dic[digits[0]]:
            for j in tail:
                result.append(i + j)
        return result
## 18.四数之和
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 4: return []
        nums.sort()
        res = []
        for i in range(n-3):
            # 防止重复 数组进入 res   关键
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # 当数组最小值和都大于target 跳出  关键
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            # 当数组最大值和都小于target,说明i这个数还是太小,遍历下一个   关键
            if nums[i] + nums[n-1] + nums[n-2] + nums[n-3] < target:
                continue
            for j in range(i+1,n-2):
                # 防止重复 数组进入 res
                if j - i > 1 and nums[j] == nums[j-1]:
                    continue
                # 同理
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                # 同理
                if nums[i] + nums[j] + nums[n-1] + nums[n-2] < target:
                    continue
                # 双指针
                left = j + 1
                right = n - 1
                while left < right:
                    tmp = nums[i] + nums[j] + nums[left] + nums[right]
                    if tmp == target:
                        res.append([nums[i],nums[j],nums[left],nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif tmp > target:
                        right -= 1
                    else:
                        left += 1
        return res
## 19. 删除链表的倒数第N个节点
    #两趟扫描
    def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
        p = head
        count = 1
        while p.next:
            p = p.next
            count += 1
        p = head
        if count <= 1 and n == 1:
            return None
        elif count <= 1 and n == 0:
            return head
        elif count == n:
            head = head.next
            return head
        else:
            for i in range(count - n - 1):
                p = p.next
            p.next = p.next.next
        return head
    # 优化 一趟扫描 双指针
    def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
        first,last = head,head
        for i in range(n):#搞一个n的窗口，后一个到末尾的时候，开始的就是倒数第n个
            last = last.next
        if last:
            while last.next:
                first = first.next
                last = last.next
            first.next = first.next.next
            return head
        else:
            head = first.next
            return head
## 20. 有效的括号
    #投机取巧法
    def isValid(self, s):
        while '{}' in s or '()' in s or '[]' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == ''
    #通过栈来实现
    def isValid1(s):
        if len(s)==0:
            return True
        if len(s)%2 != 0:
            return False
        res = []
        for i in s:
            if i in ['(','{','[']:
                res.append(i)
            else:
                if res:
                    if i==')' and res[-1] == '(' or i==']' and res[-1] == '[' or i=='}' and res[-1] == '{':
                        res.pop()#默认删除最后一个 也可指定索引
                    else:
                        return False
                else:
                    return False
        if res:
            return False
        else:
            return True
## 21. 合并两个有序链表
    方法 1：递归
    想法
    我们可以如下递归地定义在两个链表里的 merge 操作（忽略边界情况，比如空链表等）：
    { 
    list1[0]+merge(list1[1:],list2) ; list1[0]<list2[0]
    list2[0]+merge(list1,list2[1:]) ; otherwise
    ​}
    也就是说，两个链表头部较小的一个与剩下元素的 merge 操作结果合并。
    算法
    我们直接将以上递归过程建模，首先考虑边界情况。
    特殊的，如果 l1 或者 l2 一开始就是 null ，那么没有任何操作需要合并，所以我们只需要返回非空链表。
    否则，我们要判断 l1 和 l2 哪一个的头元素更小，然后递归地决定下一个添加到结果里的值。
    如果两个链表都是空的，那么过程终止，所以递归过程最终一定会终止。
    ##递归返回结果
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
    方法2. 迭代法
    def mergeTwoLists(l1, l2):
        l3 = ListNode(-1)
        temp = l3
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    temp.next = l1
                    l1 = l1.next
                else:
                    temp.next = l2
                    l2 = l2.next
                temp = temp.next
            elif l1:
                temp.next = l1
                temp = temp.next
                l1 = l1.next
            else:
                temp.next = l2
                temp = temp.next
                l2 = l2.next
        return l3.next#头节点是-1 不输出
    #改进一下
    def mergeTwoLists1(l1, l2):
        l3 = ListNode(-1)
        temp = l3
        while l1 and l2:
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        temp.next = l1 if l1 is not None else l2
        return l3.next
## 回溯法
### 22. 括号生成
    例如，给出 n = 3，生成结果为：["(()())","(())()","((()))","()(())","()()()"]
    
    #回溯法   又叫穷举法，就是把所有可能穷举出来
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append(S)
                return
            if left < n:#左括号的个数少于3个 从零开始的所以小于3
                backtrack(S+'(', left+1, right)
            if right < left:#只要右括号的个数少于左括号就可以塞右括号
                backtrack(S+')', left, right+1)

        backtrack()
        return ans
## 链表题
### 23. 合并K个排序链表
    示例：
    输入:
    [
      1->4->5,
      1->3->4,
      2->6
    ]
    输出: 1->1->2->3->4->4->5->6
    
    递归又归并 需要不断看 双指针改成了递归，看不懂可以先看下面的双指针
    class Solution:
    
        def mergeKLists(self, lists: List[ListNode]) -> ListNode:
            if not lists: return
            n = len(lists)
            return self.merge(lists, 0, n - 1)
    
        def merge(self, lists, left, right):
            if left == right:#递归停止
                return lists[left]
            mid = left + (right - left) // 2
            l1 = self.merge(lists, left, mid)
            l2 = self.merge(lists, mid + 1, right)
            return self.mergeTwoLists(l1, l2)
    
        def mergeTwoLists(self,l1, l2):
            l3 = ListNode(-1)
            temp = l3
            while l1 and l2:
                if l1.val < l2.val:
                    temp.next = l1
                    l1 = l1.next
                else:
                    temp.next = l2
                    l2 = l2.next
                temp = temp.next
            temp.next = l1 if l1 is not None else l2
            return l3.next
    #分治思想，两两合并 更好理解
    左右双指针，每次合并后结果放到left指针的位置，双指针中间碰头后，left指针归零，直至right指针到0
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        left,right = 0,len(lists)-1
        while right > 0:
            while left < right:
                lists[left] = mergeTwoLists(lists[left], lists[right]);
                left+=1
                right-=1  
            left = 0
        return lists[0]

    def mergeTwoLists(self,l1, l2):
        l3 = ListNode(-1)
        temp = l3
        while l1 and l2:
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        temp.next = l1 if l1 is not None else l2
        return l3.next 
 ### 24.两两交换链表中的节点
    示例：
    给定 1->2->3->4, 你应该返回 2->1->4->3.
    

   


          
          
          
          
      