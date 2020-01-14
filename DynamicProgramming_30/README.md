# 动态规划专题

## 动态规划题的特点
    例1:计数题：
    --机器人走网格求有多少种方式走到右下角（最优一个值可以用动态规划）
    --机器人走网格输出所有走到右下角的路径（不是一个解不可以用动态规划 可用递归 BFS解
    --有多少种方法选出k个数使得和是sum
    例2：求最大值最小值
    --从左上角走到右下角路径的最大数字和
    --最长上升子序列长度
    例3：求存在性
    --取石子游戏，先手是否必胜
    --能不能选出k个数使得和是sum
## 动态规划的三个组成部分
    1.确定状态
    解动态规划必须开数组，确定开的一个数组f[i]或者f[i][j]代表什么？就是确定状态
    确定状态需要两个意识：
        -最后一步
            以最少硬币题为例，虽然不知道最优解是什么，但是最优策略肯定是k枚硬币a1,a2....ak加起来是27
            所以一定有最后的硬币：ak
            除掉这枚硬币，前面的硬币面值加起来是27-ak
                注意：不关心前面的k-1枚硬币是怎么拼出27-ak的
                     因为是最优策略，所以拼出27-ak的硬币数一定要最少，否则就不是最优策略了
        -子问题
            最少用多少枚硬币可以拼出27-ak的硬币数即是子问题了
            ak的状态又只可能是2，5，7
            f(27) = min{f(27-2)+1,f(27-5)+1,f(25-7)+1}
                --这里为啥不用递归做
                f(x):
                    if x==0 return 0
                    res = max_value
                    if x>=2:res = min(f(x-2)+1,res)
                    if x>=5:res = min(f(x-5)+1,res)
                    if x>=7:res = min(f(x-7)+1,res)
                    return res
                    ***树的执行图****
                    递归会超时 因为不同状态分支下可能又同一个子问题
    2.转移方程
        --f(x) = min{f(x-2)+1,f(x-5)+1,f(x-7)+1}   
    3.初始条件和边界情况
        两个问题：
            1.x-2,x-5,x-7小于0怎么办？
            2.什么时候停下来
        --例如f[-1],f[-2],,,=正无穷 拼不出-1块钱
        所以f[1] = min{f[-1]+1,f[-4]+1,f[-6]+1}=正无穷 拼不出1块钱
        初始条件:f[0] = 0     (用转移方程算不出来的，但是有意义，需要手工定义)
        边界条件：不要越界
    4.计算顺序
        从后往前还是从前往后算
            本例子从前往后算
            初始条件：f[0] = 0
            然后计算：f[1],f[2],.....f[27]
        当我们计算f[x]时，f[x-2],f[x-5],f[x-7]都已经得到结果了 此时从前往后
        
## 1.Coin Change
    最少的硬币组合（类型2）
    #时间复杂度分析 27*3，每一步尝试三种硬币，一共27步
    
    def coinChange(coins, amount):
        a = [amount + 1 for i in range(amount+1)]  # 数组开多大呢 子状态从0-n就开 n+1 子状态从0-n-1就开 n
        # a[amount] = a[amount-ak]+1
        # ak = coins[i]
        a[0] = 0
        for i in range(1, amount+1):
            a[i] = amount + 1  # 假设拼不出来
            for j in coins:
                if i >= j:
                    a[i] = min(a[i - j] + 1, a[i])
        if a[amount] == amount + 1:
            a[amount] = -1
## 53. 最大子序和
    描述：给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
    示例:输入: [-2,1,-3,4,-1,2,1,-5,4],
        输出: 6
        解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
    题解：
        1.确定状态
             dp[i] 定义为数组nums 中已num[i] 结尾的最大连续子串和
        2.转移方程
             则有dp[i] = max(dp[i-1] + nums[i], num[i]);
        3.初始条件和边界
        4.计算顺序
        class Solution:
            def maxSubArray(self, nums: List[int]) -> int:
                dp = [0 for i in range(len(nums))]
                dp[0] = nums[0]
                max_sum = dp[0]
                for i in range(1,len(nums)):
                    dp[i] = max(dp[i-1]+nums[i],nums[i])
                    if max_sum<dp[i]:
                        max_sum = dp[i]
                return max_sum
## 70. 爬楼梯
    描述：假设你正在爬楼梯。需要 n 阶你才能到达楼顶，每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
    题解：
        class Solution:
            def climbStairs(self, n: int) -> int:
                dp = [1 for i in range(n+1)]
                for i in range(2,n+1):
                    dp[i] = (dp[i-1]) + (dp[i-2])
                return dp[n]
## 121. 买卖股票的最佳时机
    描述：给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。如果你最多只允许完成一笔交易（即买入和卖出一支股票），
            设计一个算法来计算你所能获取的最大利润。注意你不能在买入股票前卖出股票。
    示例1:
        输入: [7,1,5,3,6,4]
        输出: 5
        解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
             注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
    示例 2:
        输入: [7,6,4,3,1]
        输出: 0
        解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
    题解:
        class Solution:
            def maxProfit(self, prices: List[int]) -> int:
                #利润最大问题
                #前i天的最大收益 = max{前i-1天的最大收益，第i天的价格-前i-1天中的最小价格}
                if not prices:return 0
                dp = [0 for i in range(len(prices))]
                min_price = prices[0]
                for i in range(1,len(prices)):
                    dp[i] = max(dp[i-1],prices[i]-min_price)
                    min_price = min(min_price,prices[i])
                return dp[-1]
## 62. 不同路径
    描述:一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
        机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
        问总共有多少条不同的路径？
    题解:注意二维数组的定义 边界条件一开始就定义了的方法
    class Solution:
        def uniquePaths(self, m: int, n: int) -> int:
            # if m ==0 and n ==0:无意义？
            #     return 0
            # if m==0 or n==0:无意义？
            #     return 1     
            #dp = [[0 for i in range(n)]for j in range(m)]#二维数组不会定义？？？
            dp = [[1]*n] + [[1]+[0] * (n-1) for _ in range(m-1)]#初始状态也定义了
            for i in range(1,m):#行
                for j in range(1,n):
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
            return dp[-1][-1]
## 63. 不同路径 II
    描述:一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
        机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
        现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
        网格中的障碍物和空位置分别用 1 和 0 来表示。
    题解:对状态方程来说：如果有障碍物，有障碍物的格子不提供增益而已
        对优化来说，初始矩阵可都设置为0
        对边界来说，行判断，列判断，从dp[1][1]开始扫描
    class Solution:
        def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
            m = len(obstacleGrid)
            if m < 1:
                return 0
            n = len(obstacleGrid[0])
            if n < 1:
                return 0
            if 1 == obstacleGrid[0][0]:
                return 0
            dp = [[0]*n for _ in range(m)]  # 外层不能使用*，否则会浅拷贝内层，赋值会带来问题，初始化为０，可以避免额外的赋值
            for i in range(0, m):
                for j in range(0, n):
                    if 0 == i and 0 == j:
                        dp[i][j] = 1
                    elif 0 == i and 0 != j:
                        if 0 == obstacleGrid[i][j]:
                            dp[i][j] = dp[i][j - 1]
                    elif 0 != i and 0 == j:
                        if 0 == obstacleGrid[i][j]:
                            dp[i][j] = dp[i - 1][j]
                    else:
                        if 0 == obstacleGrid[i][j]:
                            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
            return dp[-1][-1]
## 64. 最小路径和
    描述：
        给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。说明：每次只能向下或者向右移动一步。
    示例：
        输入:
            [
              [1,3,1],
              [1,5,1],
              [4,2,1]
            ]
        输出: 7
        解释: 因为路径 1→3→1→1→1 的总和最小
    题解：
    class Solution:
        def minPathSum(self, grid: List[List[int]]) -> int:
            m = len(grid)
            n = len(grid[0])
            dp = [[0 for i in range(n)] for j in range(m)]
            for i in range(0,m):
                for j in range(0,n):
                    if i==0 and j!=0:
                        dp[0][j] = dp[0][j-1]+grid[0][j]
                    elif i !=0 and j==0:
                        dp[i][0] = dp[i-1][0]+grid[i][0]
                    else:
                        dp[i][j] = min(dp[i][j-1],dp[i-1][j])+grid[i][j]
            return dp[-1][-1]
## 91. 解码方法
    描述:
        一条包含字母 A-Z 的消息通过以下方式进行了编码：
        'A' -> 1
        'B' -> 2
        ...
        'Z' -> 26
        给定一个只包含数字的非空字符串，请计算解码方法的总数
    示例: 
        示例 1:
            输入: "12"
            输出: 2  
            解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
        示例 2:
            输入: "226"
            输出: 3
            解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
    题解:
        class Solution:
            def numDecodings(self, s: str) -> int:
                n=len(s)
                if(not s or s[0]=="0"):
                    return 0
                dp=[0]*(n+1)
                dp[0]=1
                dp[1]=1
                for i in range(1,n):
                    if(s[i]=="0"):
                        if(s[i-1]=="1" or s[i-1]=="2"):
                            dp[i+1]=dp[i-1]
                        else:
                            return 0
                    else:
                        if(s[i-1]=="1" or (s[i-1]=="2" and "1"<=s[i]<="6")):
                            dp[i+1]=dp[i]+dp[i-1]
                        else:
                            dp[i+1]=dp[i]
                return dp[-1]
