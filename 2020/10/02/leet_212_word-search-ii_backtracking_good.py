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
                2d board,words 들이 주어짐
                board에서 4방향으로 이동할 수 있을 때 찾을 수 있는 모든 단어들을 return 
                words는 distnct 이다
            
            idea
               
                => iteration과정에서 엄청 많이 중복이 발생함
                    -> o a a n 이라고 할 때, o에서 a - a - n 을 갔는데, a에서 또 a - n 을 가는 경우
                => iteration과정에서 중복이 많이 생기는 것은 자명한 것 같음. 그렇다면 어떻게 pruning을 효율적으로 할까?
                
                
                words_aux = defaultdict(lambda : [])
                # words 를 이용해서 trie 구조를 만들 수 있지 않을까? 
                for word in words:
                    words_aux[word[0]].append(words)
                # trie에 대해 잘 모른다 공부를 해야할듯. 
                
                found = set()
                
                
                dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                def validate_node(node):
                    nonlocal len_row, len_col
                    return node[0] >= 0 and node[0] < len_row and node[1] >= 0 and node[1] < len_col
                    
                # 정답 set이 엄청 narrow 함을 생각하자. 과정들도 모두 words내에 들어 있어야 한다 
                def dfs(node):
                    nonlocal trie
                    visit = set()
                    tree = trie[board[node[0]][node[1]]]     
                    # node 는 시작 문자, trie의 root 라는 거잖아 
                    def recur(node, accm, trie_node):
                        nonlocal visit, found
                        visit.add(node)
                        accm = accm + board[node[0]][node[1]]
                        # accm이 tree에 존재하는 path 인가? 
                        
                        if trie_node.end_flag :
                            words_set.remove(accm)
                            found.add(accm)
                        
                        candidates = tree[trie_node]
                        children = set(trie_node.children.keys())
                        for dir in dirs:
                            next_node = (node[0] + dir[0], node[1] + dir[1])
                            if validate_node(next_node) and next_node not in visit and :
                                # accm이 적어도 words 내에 존재하는 path 여야 한다 
                                # board[next_node[0]][next_node[1]] 이랑 같은 곳들에 대해 가야함 
                                board[next_node[0]][next_node[1]] in children_chr:
                                recur(next_node, accm )
                    recur(node, '')         
                    
                    
                    
                    
                    
                
                for r in range(row):
                    for c in range(col):
                        현재 남은 words 중에서 board[r][c]가 첫 글자일 때 
                        가질 수 있는 모든 단어들을 찾는다.
                        # (r, c)에서 갈 수 있는 모든 방식을 다 체크한다.
                        
                
            
            
            
            
            well-formed
            
            
            
            test
        
        
        '''
        def add_trie(root, word, offset):
            if offset < len(word):
                if root.children.get(word[offset], None) == None:
                    root.children[word[offset]] = Node(word[offset])
                add_trie(root.children[word[offset]], word, offset+1)
            else:
                root.end_flag = True
        
        trie_root = Node('<root>')
        
        for word in words:
            add_trie(trie_root, word, 0)

        word_set = set(words)
        found = set()
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))                

        def validate_node(node):
            nonlocal row_num, col_num
            return node[0] >= 0 and node[0] < row_num and node[1] >= 0 and node[1] < col_num    
        
        def dfs(point):
            nonlocal board, trie_root
            visit = set()
            char = board[point[0]][point[1]]
            tree = trie_root.children.get(char, None)
            if tree:
                recur(point, '', tree, visit)         
        
        
        def recur(point, accm, trie_node, visit):
            nonlocal dirs
            visit.add(point)
            accm = accm + board[point[0]][point[1]]
            
            if trie_node.end_flag :
                found.add(accm)

            candidates  = set(trie_node.children.keys())
            for dir in dirs:
                next_point = (point[0] + dir[0], point[1] + dir[1])
                if validate_node(next_point) and next_point not in visit and board[next_point[0]][next_point[1]] in candidates:
                    recur(next_point, accm, trie_node.children[board[next_point[0]][next_point[1]]], visit)
            
            visit.remove(point)


        row_num = len(board)
        if row_num < 1: return []
        col_num = len(board[0])
        if col_num < 1: return []
        
        for r in range(row_num):
            for c in range(col_num):
                dfs((r, c))
        return list(found)

'''
    Runtime: 480 ms, faster than 27.48% of Python3 online submissions for Word Search II.
    Memory Usage: 39.1 MB, less than 8.80% of Python3 online submissions for Word Search II.

'''