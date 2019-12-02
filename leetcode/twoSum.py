class Solution:
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

s = Solution()
res = s.twoSum([1,3,2,3],6)
print(res)
