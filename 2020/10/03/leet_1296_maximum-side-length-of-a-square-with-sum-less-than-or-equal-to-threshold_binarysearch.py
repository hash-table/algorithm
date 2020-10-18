
# 2020\10\03\leet_1296_maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold_binarysearch.py
# - _leet 
# - _binarysearch
# 202010181515 202010181600
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        '''
            problem
                - m * n 매트릭스 mat이 있다
                - threshold : int 가 있다
                - return the maximum side-length of a square with as um less than or equal to threshold 
                or return 0 if there is no such square
                => 매트릭스에서 어떤 square를 잡았어. 얘들의 합이 있지 이 때 합이 threshold 보다 작거나 같은 거라고 하자
                    -> 그럼 이건 조건에 맞는 sqaure야. 그럼 이런 square가 여러개 있을 때 가장 length 가 큰 게 있겠지
                    이거의 길이를 반환하는 문제 
                    -> 만약 없다면 0을 반환한다.
                => m, n <= 300
                => 매트릭스의 모든값은 0 ~ 10000 이다
                => threshold 는 100000 밑
                
            
            
            idea
                threshold : 10 
                1 1 2 3 4
                5 6 7 4 1
                1 1 2 4 1
                => subsum(p1, p2) 형태를 만들 수 있을까? 
                
                val((2, 4), ( 1, 2)) 
                
                1 1 2    3 4
                5 6 7    4 1
                
                
                1 1 2    
                         4 1
                
                4개영역에서 3개 영역을 빼는 것 
                -> val(r1, c1, r2, c2) 를 할 수 있는 걸 만든다고 하자 
                
                가로길이로 하면 
                
                모든 matrix를 순회하며, 걸린 위치가 left-top 일 때 모든 길이에 대해 조사를 다해본다 
                -> M N * MAX(M) * O(MN)
                => subsum을 하면 O(MN) => O(MAX(M, N)) 으로 줄일 수 있음 
            
                # 1차원 array에서의 생각
                -1, 2, 3, 4, 5 
                2, 5, 4, 0, 3 
                
                -> val(0, 5) -> 0 1 2 3 4 의 합
                -> val(1, 5) -> 2 4 5 0 3 의 합                 
                
                매 row에 대해 subsum을 만든다 
                
                a a a a a a  -> subsum[0]  0 ... 6
                a a a a a a  -> subsum[1]
                a a a a b b  -> subsum[2]
                a a a a b b  -> subsum[3]
                
                val(2, 4, 4, 6) 의 값을 구하는 것
                
                val(0, 0, 4, 6) 
                 - val(0, 0, 2, 6)
                 - val(0, 0, 4, 4)
                 + val(0, 0, 2, 4)
                가 되는 것
                subsum = []
                for r in range(row_num):
                    tmp = [0]
                    for c in range(col_num):
                        tmp.append(tmp[-1] + mat[r][c])
                    subsum.append(tmp)
                
                (0, 0) 
                        (sr, sc)

                                (er, ec)
                def get_val(sr, sc, er, ec):
                    nonlocal subsum
                    return subsum[er][ec] - subsum[sr][ec] - subsum[er][sc] + subsum[sr][sc]
                    

                ret = 0 
                for row in range(row_num):
                    for col in range(col_num):
                        # (row, col)에서 가질 수 있는 최고 길이 
                        limit_len = min(col_num - col , row_num - row)
                        sr, sc = row, col
                        for side_len in range(limit_len, 0, -1):
                            er, ec = row + side, col + side
                            #[(sr, sc) , (er, ec) )  가 되는 형태로 된다 
                            val = get_val(sr, sc, er, ec)
                            if val != -1:
                                ret = max(ret, side_len)
                                break
                return ret
            
            well-formed


                subsum = []
                for r in range(row_num):
                    tmp = [0]
                    for c in range(col_num):
                        tmp.append(tmp[-1] + mat[r][c])
                    subsum.append(tmp)

                def get_val(sr, sc, er, ec):
                    nonlocal subsum
                    return subsum[er][ec] - subsum[sr][ec] - subsum[er][sc] + subsum[sr][sc]
                
                

                ret = 0 
                for row in range(row_num):
                    for col in range(col_num):
                        limit_len = min(col_num - col , row_num - row)
                        sr, sc = row, col
                        for side_len in range(limit_len, 0, -1):
                            er, ec = row + side, col + side
                            val = get_val(sr, sc, er, ec)
                            if val <= threshold:
                                ret = max(ret, side_len)
                                break
                return ret
            
                O(M*N) + O(M*N*MIN(M, N)*O(1))
            test
        
        
        
        '''
        
        row_num, col_num = len(mat), len(mat[0])
        
        subsum = []
        subsum.append([0] * (col_num+1))
        for r in range(row_num):
            tmp = [0]
            for c in range(col_num):
                tmp.append(tmp[-1] + mat[r][c])
            subsum.append(tmp)

        for r in range(1, row_num+1):
            for c in range(1, col_num+1):
                subsum[r][c] += subsum[r-1][c]
                
        def get_val(sr, sc, er, ec):
            nonlocal subsum
            return subsum[er][ec] - subsum[sr][ec] - subsum[er][sc] + subsum[sr][sc]

        ret = 0 
        for row in range(row_num):
            for col in range(col_num):
                limit_len = min(col_num - col , row_num - row)
                sr, sc = row, col
                for side_len in range(limit_len, 0, -1):
                    er, ec = row + side_len, col + side_len
                    val = get_val(sr, sc, er, ec)
                    if val <= threshold:
                        ret = max(ret, side_len)
                        break
        return ret

    
    
'''
Runtime: 9472 ms, faster than 5.09% of Python3 online submissions for Maximum Side Length of a Square with Sum Less than or Equal to Threshold.
Memory Usage: 19.6 MB, less than 91.62% of Python3 online submissions for Maximum Side Length of a Square with Sum Less than or Equal to Threshold.
Next challenges:
'''    