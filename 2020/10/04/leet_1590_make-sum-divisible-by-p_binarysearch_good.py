
# 2020\10\04\leet_1590_make-sum-divisible-by-p_binarysearch_good.py
# _leet
# _good
# _binarysearch
# _binarysearch_good
# 202010192200 202010192300


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        '''
            problem
            
            - postive integers nums가 있음
            - remove the smallest subarray (empty도 가능) 
                -> such that the sum of the remaining elements is divisible by p
            - it is not allowed to remove the whole array
            
            - return the length of the smallest subarray that you eed to remove or - 1 
            - nums length 는 100 000 
            
            -> 정리를 하면
            nums는 양의정수인 List[int]
            그리고 p : int 가 주어져 
            
            nums에서 어떤 subarrray를 제거한다고 하자 
            남은 부분의 합이  p로 나눈 나머지가 0이 되게 하는 최소 subarray의 길이를 찾아야 한다 
            
            
            idea
            
            
                nums : [ 2 4 1 5, 6, 13] p = 3 
                
                nums => [2 1 1 2 0 1]
                subsum = [0, 2, 3, 4, 6, 0, 7]
                
                
                => subarray : [left ... right] 라고 하자
                이 부분을 제거하면 남는 부분은
                nums[0 ... left - 1]
                nums[right+1 ... len(nums)-1]
                
                이 때 저 남은 부분의 합이 p가 되는 가장 작은 지점 
                < = > left..right 길이가 최소가 되어야 한다 
                
                만약 전체 sum을 p로 나눈게 k라고 하자
                
                1. k == 0 -> return 0
                2. k != 0 
                    -> subsum의 합의 나머지가 k 가 되는 지점을 찾으면 된다 
                    이 지점이 없다면 -1을 반환한다 
                
                => 1. nums에 대해서 subsum을 만든다
                => 2. 합 k를 구한다, 여기서 mod 에 대한 연산을 고민
                => 3. 모든 idx에 대해 남은부분에서 최초로 존재하는 것을 찾는다 
                
                nums = [ _ % p for _ in nums]
                subsum = [0]
                for i in nums:
                    subsum.append(subsum[-1] + i)
                # 만들어야할 target 나머지 값을 구해야 한다 
                target = subsum[-1] % p
                # 이제 해야할 것은 subsum[idx+1] ( idx : 0 ... len(nums)-1) 들에 대해 
                (subsum[idx+1] + alpha ) % p == target인 지점들을 찾는 것 
                
                for curridx in range(0, len(nums)-1):
                    current = subsum[curridx+1]
                    # idx보다 크거나 같은 idx 중에서 
                    # limit보다 값들에 대해 current + target + p * iterating_numbe 가 되는 값을 찾아야한다 
                    # 그러면 여기서 이거는 O(|N| * log|N| * |max(subsum)//p|) , 이걸 개선해야한다
                    
                    current_mod = current % p
                    # 이제 해야할 거는 (current_mod + k) % p 인 것을 찾아야해 
                    # 그러면 모든 subsum의 나머지에 대해서, 각 나머지들의 idx를 저장하는 aux를 하나 만든다
                    # (current_mod + k) % p 를 키로 하는거는 나머지가 저 값인 것들의 idx가 되고 
                    # 여기서 curridx보다 같거나 큰 것을 찾고 이 길이를 반환한다 
                    # space를 쓰게 되지만, O(N)만큼 쓴다. 찾는 거는 O(N* log(N//P))
                    
                    
            
            well-formed

                ret = -1
                nums = [ _ % p for _ in nums]
                subsum = [0]
                for i in nums:
                    subsum.append(subsum[-1] + i)

                aux = defaultdict(lambda : [])
                for idx in range(1, len(subsum)):
                    modval = subsum[idx] % p 
                    aux[modval].append(idx - 1)
                    
                for strt_idx in range(1, len(subsum)):
                    # current[strt_idx] : 0 .... strt_idx -1 까지의 합
                    curr_modval= current[strt_idx] % p
                    counter_part = p - current[strt_idx] % p
                    
                    target_idx_list = aux[counter_part]
                    nearest_idx = bisect.bisect_left(target_idx_list, strt_idx)
                    if nearest_idx == len(target_idx_list):
                        pass
                    else:
                        ret = max(ret, target_idx_list[nearest_idx]- strt_idx + 1)
                return ret
            test
        
        
        
        '''
        ret = float('inf')
        nums = [ _ % p for _ in nums]
        subsum = [0]
        for i in nums:
            subsum.append(subsum[-1] + i)
        
        all_sum_mod = subsum[-1] % p
        aux = defaultdict(lambda : [])
        
        for idx in range(0, len(subsum)):
            modval = subsum[idx] % p 
            aux[modval].append(idx)
        
        for strt_idx in range(0, len(subsum)):
            # curr_modval= subsum[strt_idx+1] % p *** 여기서 틀렸다 
            # [0 : strt_idx] [strt_idx : x] [x : len(subsum)]
            curr_modval= subsum[strt_idx] % p
            counter_part = (curr_modval + all_sum_mod ) % p
            target_idx_list = aux[counter_part]
            # print(curr_modval, counter_part, target_idx_list)
            
            if target_idx_list:
                nearest_idx = bisect.bisect_left(target_idx_list, strt_idx)
                if nearest_idx == len(target_idx_list):
                    pass
                else:
                    ret = min(ret, target_idx_list[nearest_idx]- strt_idx)

        
        return ret if ret != float('inf') and ret != len(nums) else -1
    
    
    
'''
Runtime: 800 ms, faster than 12.31% of Python3 online submissions for Make Sum Divisible by P.
Memory Usage: 67.3 MB, less than 6.25% of Python3 online submissions for Make Sum Divisible by P.
'''
