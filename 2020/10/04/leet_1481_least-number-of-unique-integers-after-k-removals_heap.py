

# leet_1481_least-number-of-unique-integers-after-k-removals_heap.py
# _leet
# _heap
# 202010201910 202010201921
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        arr_counter = Counter(arr)        
        aux = [0] * (len(arr)+ 1)   
        
        for num in arr_counter:
            aux[arr_counter[num]] += 1
        
        ret = len(arr_counter)
        
        for idx, val in enumerate(aux):
            if val == 0:
                continue
            else:
                tmp = (k // idx if (k // idx <= aux[idx]) else aux[idx]) 
                minus_val = tmp* idx
                if minus_val == 0:
                    break
                else:
                    k -= minus_val
                    ret -= tmp
                
                
            
        return ret
            
        
        


        
'''
O(N)
Runtime: 404 ms, faster than 97.67% of Python3 online submissions for Least Number of Unique Integers after K Removals.
Memory Usage: 30.8 MB, less than 5.70% of Python3 online submissions for Least Number of Unique Integers after K Removals.
'''