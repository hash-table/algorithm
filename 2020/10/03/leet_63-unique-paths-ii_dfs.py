# 2020\10\03\leet_63-unique-paths-ii_dfs.py
# - _leet 
# - dfs
# 202010132215 202010132230




class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        '''
        
            problem
            
                (0, 0) 에 로봇이 있어 그리고 출발 (m, n)에 도달 할거야
                down 이나 right로만 이동할 수 있어
                now consider if some obstacles are added the gread how many unique paths would there be?
                길중간에 장애물이 있다면 어쩔래? 
                obstacleGrid가 있는 좌표가 주어져 
                empty는 1, 뭐 있으면 0 
                m, n은 최대 100 
            
            
            
            idea
                def validate(point):
                    nonlocal m, n
                    return point[0] >= 0 and point[0] < m and point[1] >= 0 and point[1] < n
                    
                    
                queue = deque()
                
                queue.append((0,0,0))
                
                while queue:
                    target = queue.popleft()
                    # queue에는 grid 없는것만 들어감
                    if target[0] == m-1 and target[1] == n-1:
                        return target[-1]
                    
                    for i in [(0, 1), (1, 0)]:
                        candidate = (target[0] + i[0], target[1] + i[1])
                        if validate(candidate) and obstacleGrid[candidate[0]][candidate[1]] != 1:
                            queue.append((candidate[0], candidate[1], target[-1] + 1))
                    
                return 0
                
            
            
            
            well-formed
        
        
        '''
        m = len(obstacleGrid)
        if m < 1 : return 0
        n = len(obstacleGrid[0])
        if n < 1 : return 0
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        
        def validate(point):
            nonlocal m, n
            return point[0] >= 0 and point[0] < m and point[1] >= 0 and point[1] < n

        
        cache = defaultdict(lambda : -1)
        def func(point):
            if cache[point] != -1:
                return cache[point]
            else:
                if point == (0, 0):
                    return 1
                else:
                    ret = 0
                    r, c = point
                    for cand in [(r-1, c), (r, c-1)]:
                        if validate(cand) and obstacleGrid[cand[0]][cand[1]] != 1:
                            ret += func(cand)
                    cache[point] = ret
                    return ret
                
        
        return func((m-1, n-1))
        '''
        Runtime: 44 ms, faster than 58.08% of Python3 online submissions for Unique Paths II.
        Memory Usage: 14.4 MB, less than 100.00% of Python3 online submissions for Unique Paths II.
        '''
