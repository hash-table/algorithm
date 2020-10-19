
# 2020\10\03\leet_1296_maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold_binarysearch_good.py
# _leet
# _good
# _binarysearch
# _binarysearch_good
# 202010181515 202010181600
import bisect 
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        
        len_row, len_col = len(mat), len(mat[0])
        
        subsum = [ [0] * (len_col + 1) for _ in range(len_row + 1) ]
        
        # subsum[r][c] -> 범위에 해당하는 매트릭스의 bottom-right 는 mat[r-1][c-1]
        for row in range(1, len_row + 1):
            for col in range(1, len_col + 1):
                subsum[row][col] = subsum[row-1][col] + subsum[row][col-1] - subsum[row-1][col-1] + mat[row-1][col-1]
        
        def get_val(smaller, bigger):
            # smaller 는 closed, bigger은 opened 라고 하자 
            return subsum[bigger[0]][bigger[1]] - subsum[smaller[0]][bigger[1]] - subsum[bigger[0]][smaller[1]] + subsum[smaller[0]][smaller[1]]
        
        d = 0
        for row in range(len_row):
            for col in range(len_col):
                left_top = (row, col)
                max_d = min(len_row - row, len_col - col)
                # right_bottom_closed = (row + max_d, )
                lo, hi = 0, max_d
                while lo <= hi:
                    mid = lo + (hi - lo) // 2
                    right_bottom = (row + mid, col + mid)
                    tmp = get_val(left_top, right_bottom)
                    
                    if tmp > threshold:
                        hi = mid -1
                    else:
                        lo = mid + 1
                        
                d = max(d, hi)
        return d
                    
'''
    Runtime: 2100 ms, faster than 16.98% of Python3 online submissions for Maximum Side Length of a Square with Sum Less than or Equal to Threshold.
    Memory Usage: 19.2 MB, less than 91.36% of Python3 online submissions for Maximum Side Length of a Square with Sum Less than or Equal to Threshold
'''