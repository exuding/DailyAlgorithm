# 哈希表法
    
 
## 36. 有效的数独
    描述：
        判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。
        数字 1-9 在每一行只能出现一次。
        数字 1-9 在每一列只能出现一次。
        数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次
    题解：
    一个简单的解决方案是遍历该 9 x 9 数独 三 次，以确保：
    行中没有重复的数字。
    列中没有重复的数字。
    3 x 3 子数独内没有重复的数字。
    实际上，所有这一切都可以在一次迭代中完成。
    两个问题
    1.如何枚举子数独？
        可以使用 box_index = (row / 3) * 3 + columns / 3，其中 / 是整数除法
    2.如何确保行 / 列 / 子数独中没有重复项？
        可以利用 value -> count 哈希映射来跟踪所有已经遇到的值。
    class Solution:
        def isValidSudoku(self, board):
            """
            :type board: List[List[str]]
            :rtype: bool
            """
            # init data
            rows = [{} for i in range(9)]
            columns = [{} for i in range(9)]
            boxes = [{} for i in range(9)]
    
            # validate a board
            for i in range(9):
                for j in range(9):
                    num = board[i][j]
                    if num != '.':
                        num = int(num)
                        box_index = (i // 3 ) * 3 + j // 3
                        
                        # keep the current cell value
                        rows[i][num] = rows[i].get(num, 0) + 1
                        columns[j][num] = columns[j].get(num, 0) + 1
                        boxes[box_index][num] = boxes[box_index].get(num, 0) + 1
                        
                        # check if this value has been already seen before
                        if rows[i][num] > 1 or columns[j][num] > 1 or boxes[box_index][num] > 1:
                            return False         
            return True

