
# leet_490_the-maze.py
# _leet
# _dfs


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        
        row_num, col_num = len(maze), len(maze[0])
        visited = set()
        
        def is_valid(point):
            return point[0] >= 0 and point[0] < row_num and point[1] >= 0 and point[1] < col_num and maze[point[0]][point[1]] == 0
        
        
        def get_last_point(point, d) -> List[int]:
            ret = [point[0], point[1]]
            # 처음에는 point 로 valid 걸어서 틀리고 is_valid 에 조건 맞출 때 어긋나게 해서 틀림 
            while is_valid([ret[0] + d[0], ret[1] + d[1]]):                
                ret[0] += d[0]
                ret[1] += d[1]
            return ret
        
        
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        def func(point):
            visited.add(tuple(point))
            if point[0] == destination[0] and point[1] == destination[1]:
                return True
            for dir in dirs:
                last_point = get_last_point(point, dir)
                if tuple(last_point) not in visited:
                    ret = func(last_point)
                    if ret : 
                        return True
            return False
        
        return func(start)

'''

Runtime: 344 ms, faster than 24.43% of Python3 online submissions for The Maze.
Memory Usage: 16.8 MB, less than 10.32% of Python3 online submissions for The Maze.


'''