# leet_212_word-search-ii_backtracking_good.py
# - _leet 
# - _backtracking
# - _good
# - _backtracking_good
# 202010051930 202010052015


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        '''
            problem
                - 2d board가 있다.
                - words : List[str], 사전 
                - find all words in the board
                    - board에서 words에 들어있는 모든 word들을 찾아라 
                - 방향은 가로 세로만 봄
                - 한번만 방문 될 수 있다 
                - 순서에 대해 한번 생각해봐야 하네
                - 뭐 방향은 가로 세로, 시작이 어디든 상관 없어 그냥 word이기만 하면 됨 
                - words의 word들은 모두 distinct
            
            idea
                
                - row, col 에 대해 다 돌면서 word가 되는지를 본다. 
                
                row_num = len(words)
                col_num = len(words[0])
                
                # words를 alphabet 기준으로 정방향 역방향 두개의 그래프를 그릴 수 있다 
                
                # 반복이 느껴지는데, 어떻게 명확하게 와닿지는 않음 
                for r in range(row_num):
                    for c in range(col_num):
                        
                        # 해당 (r, c)에서 시작인 경우
                        # 해당 (r, c)가 끝인 경우 
                        # 위의 두가지에 대해서 진행을 한다
                        # 어떠한 경우가 발생을 할 수 있나 
                        # 중복이 너무 많이 발생할 거 같아 
                    
                        pass
            
                - 방향을 반대로 해보자. 각 word들에 대해 해당 word가 여기 안에 있는지를 보는거야 
                
                
                                
                row_num = len(board)
                if row_num < 1 : return []
                col_num = len(board[0])
                if col_nun < 1  : return []
                
                finished = set()
                
                -> 각 word 들을 만들 수 있는지를 본다
                for row in range(row_num):
                    for col in range(col_num):
                        start_char = board[row][col]
                        for target_word in aux[start_char] if target_word not in finished:

                            if func(row, col, target_word):
                                
                                finished.add(target_word)
                        
                return list(finished)                
                
                dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                used_point = set()
                def func(r, c, tsidx) -> (r, c)에서 시작해서 target_string 을 만들수 있는지 
                    nonlocal dir,row_num, col_unm, target_word
                    if (r,c)가 사용불가능한 점인 경우:
                        return False
                    else:
                        #(r,c)가 사용가능한 점인 경우
                        if board(r, c) == target_word[tsidx]:
                            if tsidx >= len_target_word-1:
                                return True
                            else:
                                tmp_ret = False
                                for dir in dirs:
                                    nextr = r + dir[0]
                                    nextc = c + dir[1]
                                    if (nextr, nextc) 가 사용가능하고, 아직 방문하지 않은 점이라면:
                                        used_point.add((nextr, nextc))
                                        if func(nextr, nextc, tsidx+1):
                                            return True
                                return False
                            
                        else:
                            return False
                        
                        
                
                    
                
            well-formed
            
                row_num = len(board)
                if row_num < 1 : return []
                col_num = len(board[0])
                if col_nun < 1  : return []
                
                dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                finished = set()
                aux = defaultdict(labmda : [])
                
                for word in words:
                    aux[word[0]].append(word)
                
                
                def is_valid(r, c):
                    nonlocal row_num, col_num
                    return (r >= 0 and r < row_num and c >= 0 and c < col_num)
                    
                def func(r, c, target_word, tsidx, used) -> bool 
                    nonlocal row_num, col_unm, target_word, dirs
                    if not is_valid(r, c)
                        return False
                    else:
                        if board[r][c] == target_word[tsidx]:
                            if tsidx >= len(target_word)-1:
                                return True
                            else:
                                default_ret = False
                                for dir in dirs:
                                    nextr, nextc = r + dir[0], c + dir[1]
                                    if is_valid(nextr, nextc) and (nextr, nextc) not in used:
                                        used.add((nextr, nextc))
                                        if func(nextr, nextc, target_word, tsidx+1, used):
                                            return True
                                        used.remove((nextr, nextc))
                                return False                            
                        else:
                            return False
                                
                for row in range(row_num):
                    for col in range(col_num):
                        start_char = board[row][col]
                        for target_word in aux[start_char] if target_word not in finished:
                            if func(row, col, target_word):
                                finished.add(target_word)
                return list(finished)                 
            
            test
        
        
        
        '''
        row_num = len(board)
        if row_num < 1 : return []
        col_num = len(board[0])
        if col_num < 1  : return []

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        finished = set()
        aux = defaultdict(lambda : [])

        for word in words:
            aux[word[0]].append(word)


        def is_valid(r, c):
            nonlocal row_num, col_num
            return (r >= 0 and r < row_num and c >= 0 and c < col_num)

        def func(r, c, target_word, tidx, used) -> bool :
            nonlocal dirs
            if not is_valid(r, c):
                return False
            else:
                if board[r][c] == target_word[tidx]:
                    if tidx >= len(target_word)-1:
                        return True
                    else:
                        # default_ret = False
                        for dir in dirs:
                            nextr, nextc = r + dir[0], c + dir[1]
                            if is_valid(nextr, nextc) and (nextr, nextc) not in used:
                                used.add((nextr, nextc))
                                if func(nextr, nextc, target_word, tidx+1, used):
                                    return True
                                used.remove((nextr, nextc))
                        return False                            
                else:
                    return False

        for row in range(row_num):
            for col in range(col_num):
                start_char = board[row][col]
                for target_word in aux[start_char]:
                    if target_word not in finished:
                        if func(row, col, target_word, 0, {(row, col)}):    
                            finished.add(target_word)
        return list(finished)                 

    '''
    
    
    Time Limit Exceeded

    
    '''