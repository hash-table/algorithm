# 2020\10\03\leet_79-word-search_backtracking.py
# - _leet 
# - _backtracking
# 202010131906 202010131923

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
            problem
            
                - 2d board 랑 word 가 주어졌어. 이 때 이 word가 board에 있는지를 반환하는 함수를 만들어라
                

            idea
            
                
                def backtracking(point):
                    pass
                
                for row in len(row_num):
                    for col in len(col_num):
                        if backtracking((row, col)):
                            return True
                
                return False


            well-formed

                dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                def valid(point):
                    nonlocal row_num, col_num
                    return point[0] >= 0 and point[0] < row_num and point[1] >= 0 and point[1] < col_num
                    
                def backtracking(point, word, offset):
                    nonlocal visit, dirs
                    if len(word) == offset:
                        return True
                    else:
                        visit.add(point)
                        for dir in dirs:
                            next_point = (point[0] + dir[0], point[1] + dir[1])
                            if valid(next_point) and next_point not in visit and board[next_point[0]][next_point[1]] == word[offset]:
                                tmp = backtracking(next_point, word, offset + 1)
                                if tmp: return True
                        visit.remove(point)                       
                        return False
                
                for row in len(row_num):
                    for col in len(col_num):
                        visit = set()
                        if board[row][col] == word[0]:
                            if backtracking((row, col), word, 1):
                                return True
                
                return False



            test
        
        
        
        '''
        
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        row_num = len(board)
        if row_num < 1 : return False
        col_num = len(board[0])
        if col_num < 1 : return False
        
        def valid(point):
            nonlocal row_num, col_num
            return point[0] >= 0 and point[0] < row_num and point[1] >= 0 and point[1] < col_num

        def backtracking(point, offset):
            nonlocal visit, dirs, word
            if len(word) == offset:
                return True
            else:
                visit.add(point)
                for dir in dirs:
                    next_point = (point[0] + dir[0], point[1] + dir[1])
                    if valid(next_point) and next_point not in visit and board[next_point[0]][next_point[1]] == word[offset]:
                        tmp = backtracking(next_point, offset + 1)
                        if tmp: return True
                visit.remove(point)                       
                return False

        for row in range(row_num):
            for col in range(col_num):
                visit = set()
                if board[row][col] == word[0]:
                    if backtracking((row, col), 1):
                        return True

        return False


    
    '''
    
    Runtime: 356 ms, faster than 66.93% of Python3 online submissions for Word Search.
    Memory Usage: 15.5 MB, less than 5.38% of Python3 online submissions for Word Search.    
    
    
    '''