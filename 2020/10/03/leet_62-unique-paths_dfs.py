# 2020\10\03\leet_62-unique-paths_dfs.py
# - _leet 
# - dfs
# 202010132200 202010132215



class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
            problem
            
               (0,0) 에서 (m,n) grid 간다고 할 때 총 가지수  
            
            
            idea
            
                # (0,0)부터 (r, c)까지 가는 경우 
                
                def validate(point):
                    nonlocal m, n
                    return point[0] >= 0 and point[0] < m and point[1] >= 0 and point[1] < n 
                
                cache = defaultdict(lambda : -1)
                def func(point) :
                    nonlocal m, n
                    if cache[point] != - 1 :
                        return cache[point]
                    else:
                        if point == (0, 0):
                            return 0
                        else:
                            ret = 0
                            for prev in [(m-1, n), (m, n-1)]:
                                if validate(prev):
                                    ret += func(prev)
                            cache[point] = ret
                            return cache[point]
                        
            
            
                func(m, n)
            
            
            well-formed
            
            
                def validate(point):
                    nonlocal m, n
                    return point[0] >= 0 and point[0] < m and point[1] >= 0 and point[1] < n 
                
                cache = defaultdict(lambda : -1)
                
                def func(point) :
                    nonlocal m, n
                    if cache[point] != - 1 :
                        return cache[point]
                    else:
                        if point == (0, 0):
                            return 0
                        else:
                            ret = 0
                            for prev in [(m-1, n), (m, n-1)]:
                                if validate(prev):
                                    ret += func(prev)
                            cache[point] = ret
                            return cache[point]
                return func((m, n))               
            
            
        
        
        
        
        '''
        
        
        def validate(point):
            nonlocal m, n
            return point[0] >= 0 and point[0] < m and point[1] >= 0 and point[1] < n 

        cache = defaultdict(lambda : -1)

        def func(point) :
            nonlocal m, n
            if cache[point] != -1 :
                return cache[point]
            else:
                if point == (0, 0):
                    return 1
                else:
                    ret = 0
                    for prev in [(point[0]-1, point[1]), (point[0], point[1]-1)]:
                        if validate(prev):
                            ret += func(prev)
                    cache[point] = ret
                    return cache[point]
        
        return func((m-1, n-1))               

        
'''
Runtime: 40 ms, faster than 19.54% of Python3 online submissions for Unique Paths.
Memory Usage: 14.4 MB, less than 99.96% of Python3 online submissions for Unique Paths.
'''
