
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
        res = 0
        for row in range(1, len_row+1):
            for col in range(1, len_col + 1):
                subsum[row][col] = subsum[row-1][col] + subsum[row][col-1] - subsum[row-1][col-1] + mat[row-1][col-1]
                k = res + 1
                # left_top, right_bottom = (row-k, col-k) , (row, col)
                if row >= k and col >= k and threshold >= subsum[row][col] - subsum[row-k][col] - subsum[row][col-k] + subsum[row-k][col-k] :
                    res = k
        return res
        
                    

'''
Runtime: 732 ms, faster than 93.83% of Python3 online submissions for Maximum Side Length of a Square with Sum Less than or Equal to Threshold.
Memory Usage: 19.1 MB, less than 91.36% of Python3 online submissions for Maximum Side Length of a Square with Sum Less than or Equal to Threshold.

'''