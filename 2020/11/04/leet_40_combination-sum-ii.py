
import bisect

# leet_40_combination-sum-ii.py
# _leet
# _backtracking
# 202011271340 202011271420

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        counter = Counter(candidates)
        num_list = list(counter.keys())
        ret = []
        
        def func(eidx, remainder) -> List[List[int]]:
            nonlocal num_list, counter
            if eidx == 0:
                return 'no_answer'
            elif remainder == 0:
                return [[]]
            else:
                pos = bisect_right(num_list, eidx, remainder)
                pos -= 1 
                ret = []
                if pos == -1:
                    return []
                else:
                    
                    largest_val = num_list[pos]
                    count = counter[largest_val]
                    for idx in range(0, counter+1):                       
                        tmp = func(eidx-1, remainder - idx * largest_val)
                        if tmp != no_answer:
                            for j in tmp:
                                ret += ( j + [larest_val] * idx)
                return ret
                

        return func(len(num_list), target)


