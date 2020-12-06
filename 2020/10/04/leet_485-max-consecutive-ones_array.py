
# 2020\10\04\leet_485-max-consecutive-ones_array.py
# - leet 
# - array
# 202010231500 202010231515
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        '''
            problem
                - 0, 1로 이루어진 binary array가 주어졌음
                - find the maimum number of consecutive 1s in this array
                - 전체에서 가장 1이 긴것을 찾아라
                
            
            
            
            test
            
                [1,1,0,1,1,1]
                    2 .... 3     
                -> 3
                
                
            
            idea
                # 이 함수가 가질 수 있는 최소 , 최대 값 -> 0, len(nums)
                ret, left = 0, 0
                len_nums = len(nums)
                while left < len_nums:
                    if nums[left] == 1:
                        # 조건에 맞는 연속적인 [left ... right] 부분을 찾는다
                        right = left
                        while right < len_nums and nums[right] == 1:
                            right += 1
                        # [left : right) 가 나오게 된다, ret을 비교하여 update 
                        ret = max(ret, right - left)
                        # 다음 iteration을 진행할 수 있게 iterator들을 조정한다 
                        left = right
                    else:
                        left += 1
                return ret                        
                        
                
                
                
                [1,1,0,1,1,1]
                
                ret, left = 0, 0
                len_nums = 6
                while left = 0 < len_nums = 6:
                    - left = 0 
                        nums[left] = nums[0] = 1
                        right = 0 
                        while 0 < 6 and nus[0] == 1
                            -> right += 1 ... 
                        # right = 2
                        #[0 : 2]
                        ret = max(ret, 2)
                        left = 2
                    - left = 2
                        nums[left] = nums[2] = 0
                        left += 1 = 3
                    - left = 3
                        nums[left] = nums[3] = 1 
                        right = 3
                        while right = 3 < 6 and nums[3] == 1
                            right += 1
                        # right = 6
                        # [3 : 6](2, 3)
                        left = 6
                return 3
            
            well-formed

                ret, left = 0, 0
                len_nums = len(nums)
                while left < len_nums:
                    if nums[left] == 1:
                        right = left
                        while right < len_nums and nums[right] == 1:
                            right += 1
                        ret = max(ret, right - left)
                        left = right
                    else:
                        left += 1
                return ret               
        
        
        '''
        ret, left = 0, 0
        len_nums = len(nums)
        while left < len_nums:
            if nums[left] == 1:
                right = left
                while right < len_nums and nums[right] == 1:
                    right += 1
                ret = max(ret, right - left)
                left = right
            else:
                left += 1
        return ret               

    '''
    
Runtime: 328 ms, faster than 95.53% of Python3 online submissions for Max Consecutive Ones.
Memory Usage: 14.4 MB, less than 8.05% of Python3 online submissions for Max Consecutive Ones.    
    
    '''