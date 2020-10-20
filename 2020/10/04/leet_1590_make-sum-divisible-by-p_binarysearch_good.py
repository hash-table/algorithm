class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        
        '''


            need = sum(nums) % p

            # the in operation on a dict, or the dict_keys object you get back from calling keys() on it (in 3.x), 
            # is not O(N), it's O(1).
            # dict key 에 대한 membership check는 O(1)
            cur = 0
            dp = dict()
            # key : 나머지값, val : 해당 나머지값이 나온 제일 최근 인덱스 
            # 조회를 하면서 left 값을 저장해서 나아가면 O(n)만에 끝낼 수 있다         
            ret = float('inf')
            for idx, num in enumerate(nums):
                cur += num 
                cur %= p
                # cur이 right 가 되는거고 left는 dp에서 찾는 거라고 볼 수 있음
                target = cur - need
                if target in dp :
                    ret = min(ret, idx - dp[target] + 1 )
                dp[cur] = idx # cur이라는 값을 가지는 subsum의 인덱스를 계속해서 업데이트 한다 

            return ret if ret != float('inf') else -1

        
        
        
        
        
        '''
        
        need = sum(nums) % p
        cur = 0
        dp = {0 : -1}
        ret = len(nums)        
        for idx, num in enumerate(nums):
            cur = (cur + num) % p 
            dp[cur] = idx
            target = (cur - need) % p
            if target in dp :
                ret = min(ret, idx - dp[target] )
        
        return ret if ret < len(nums) else -1
    
    
'''

Runtime: 552 ms, faster than 76.13% of Python3 online submissions for Make Sum Divisible by P.
Memory Usage: 32.4 MB, less than 6.20% of Python3 online submissions for Make Sum Divisible by P.
'''
    
    