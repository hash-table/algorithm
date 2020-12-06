
# leet_75_sort-colors.py
# _leet
# _two-pointer


# sort-colors/
# 202012062104 202012062130

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        '''
        
            problem
            
                nums : n obejct clored red, white or blue 
                
                sort them in-place so that objects of the same color are adjacent 
                with the colors in the order red white blue
                red : 0, while : 1, blue : 2
            
            idea
            
                0부터 채우기 시작
                
                left, right, val 3개로 한번 접근
                
                nums[left] == val 이면 left += 1
                nums[left] != val 인 경우, right가 가르키는 부분과 바꾸기 시작한다.
                    case 1. nums[right] == val 인경우,
                        left 와 right 를 swap 한다.
                        left += 1을 한다. 
                    case 2. nums[right] != val 인 경우,
                        right -= 1 을 한다. 
                    
                left와 right 가 같은 지점을 가르키면 종료한다. 
            
                # val 이 주어진 상황 
                
                left, right = start, len(nums)-1
            
                while left < right:
                    if nums[left] == val:
                        left += 1
                    else:
                        if nums[right] == val:
                            tmp = nums[left]
                            nums[left] = nums[right]
                            nums[right] = tmp
                            left += 1
                            right -= 1
                        else:
                            right -= 1
                            
                return left        
                
            
            
            well-formed
            
            
                [1, 1, 0, 2]
                    l, r = 0, 3 
                        n[l] = 1 , n[r] = 2
                    l, r = 0, 2
                        n[l] = 1, n[r] = 0 
                        swap
                        n[l] = 0, n[r] = 1
                        l += 1, r -= 1 =>
                    l , r = 1, 1 
                        
                def func(left_start, right_end, val):
                    left, right = left_start, right_end
                    while left < right:
                        if nums[left] == val:
                            left += 1
                        else:
                            if nums[right] == val:
                                tmp = nums[left]
                                nums[left] = nums[right]
                                nums[right] = tmp
                                left += 1
                                right -= 1
                            else:
                                right -= 1

                    return left        
                    left_start, right_end = 0, len(nums) - 1
                    for val in [0, 1, 2]:
                        left_start = func(left_start, right_end, val)
        
        
        '''
        
        def func(left_start, right_end, val):
            left, right = left_start, right_end
            while left <= right:
                if nums[left] == val:
                    # 여긴 계속 가야하지 
                    left += 1
                else:
                    if nums[right] == val:
                        tmp = nums[left]
                        nums[left] = nums[right]
                        nums[right] = tmp
                        left += 1
                        right -= 1
                    else:
                        right -= 1
            return left        

        left_start, right_end = 0, len(nums) - 1
        
        color_list = set(nums)
        for val in [0, 1, 2]:
            left_start = func(left_start, right_end, val)
            
            
'''

Runtime: 36 ms, faster than 28.21% of Python3 online submissions for Sort Colors.
Memory Usage: 14.3 MB, less than 14.45% of Python3 online submissions for Sort Colors.


'''
