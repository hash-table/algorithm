

# leet_368_largest-divisible-subset_dp_good.py
# - _leet 
# - _dp
# - _good
# - _dp_good
# 202010021916 202010021941


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        '''
            
            problem
                distinct, postive integer set 이 있다. 
                
                어떠한 subset을 뽑을 꺼야
                
                p1, p2, p3, p4.. 이런 distinct + postive 인 리스트가 있음
                그리고 얘들로
                (pa, pb, pc, pd) 뭐 이런걸 만들었다고 하자
                
                그럼 이 subset의 모든 pair들에 대해 pa%pb == 0, pa % pc == 0 ... 이러한 조건을 만족해야해
                
                이때 가장 크기가 큰 subset을 찾아라!
                
            
            idea
            
                - postive 이고 distinct 인 수
                    => a, b 가 있다고 하자 a > b 일때
                    a % b == 0 이어야 한다 
                    
                    정답인 subset이 하나 있다고 하자
                    [s1, s2, s3, s4, s5] , 이렇게 오름차순으로 있다고 하자 
                    1 6 12 24 72 144 216 288 뭐 이렇게 있으면 .. 1 6 12 244 72 144 288 이게 답이 되겠지
                    
                    func(nums, idx) 이고 nums[idx] 까지 썼을 때 가장 긴 길이 가 되는 리스트를 반환하는 문제 
                    aux[idx] : nums[idx]를 가장 마지막에 썼을 때 가장 긴 길이를 가지는 list 라고 볼 수 있네 
                    aux[idx]에 뭐가 들어있든 상관은 없어 가장 긴거만 있으면 되는거야 nums[idx]에서 끝나는. 
                                        
                    nums.sort()
                    len_n = len(nums)
                    
                    aux = dict()
                    aux[0] = [nums[0]]
                    for i in range(1, len_n):
                        target = nums[i]
                        # target이 붙을 수 있는 공간을 aux에서 찾는다 
                        # 이 때 찾은 것들에 대해서 가장 길이가 큰 것들 찾고, 여기에 target을 연결한다 

                        pick_idx = -1
                        cmp_len = -float('inf')
                        for j in range(0, i-1):
                            if target % nums[j] == 0:
                                if len(aux[j]) > cmp_len:
                                    cmp_len = len(aux[j])
                                    pick_idx = j
                                
                    
                        if pick_idx == -1:
                            aux[i] = [target]
                        else:
                            aux[i] = aux[pick_idx] + [target]
                            
                        
                    tmp = -float('inf')
                    ret = []
                    for k in aux:
                        val = aux[k]
                        if len(val) > tmp:
                            tmp = len(val)
                            ret = val
                    return ret
                    
            well-formed
                    
                # O(N)
                
                nums.sort()
                len_n = len(nums)
                aux = dict()
                aux[0] = [nums[0]]
                # O(N) * O(N)
                for i in range(1, len_n):
                    target = nums[i]
                    pick_idx = -1
                    cmp_len = -float('inf')
                    for j in range(0, i):
                        if target % nums[j] == 0 and len(aux[j]) > cmp_len:
                                cmp_len = len(aux[j])
                                pick_idx = j
                    if pick_idx == -1:
                        aux[i] = [target]
                    else:
                        aux[i] = aux[pick_idx] + [target]

                # O(N)
                tmp = -float('inf')
                ret = []
                for k in aux:
                    val = aux[k]
                    if len(val) > tmp:
                        tmp = len(val)
                        ret = val
                return ret

                        
                    
            
            test
        
                [1,2,3,5,6,8,12,16]
                
                aux = {
                    0 : [1]
                    1 : [1, 2]
                    2 : [1, 3]
                    3 : [1, 5]
                    6 : [1, 3, 6]
                    8 : [1, 2, 8]
                    12 : [1, 3, 6, 12]
                    16 : [1, 2, 8, 16]
                    }
        
        
        
        '''
        
        if not nums : return []
        nums.sort()
        len_n = len(nums)
        aux = dict()
        aux[0] = [nums[0]]
        for i in range(1, len_n):
            target = nums[i]
            pick_idx = -1
            cmp_len = -float('inf')
            for j in range(0, i):
                if target % nums[j] == 0 and len(aux[j]) > cmp_len:
                    cmp_len = len(aux[j])
                    pick_idx = j

            if pick_idx == -1:
                aux[i] = [target]
            else:
                aux[i] = aux[pick_idx] + [target]

        tmp = -float('inf')
        ret = []
        for k in aux:
            val = aux[k]
            if len(val) > tmp:
                tmp = len(val)
                ret = val
        return ret
        

'''
# 202010021916 202010021941
Runtime: 396 ms, faster than 81.71% of Python3 online submissions for Largest Divisible Subset.
Memory Usage: 14.4 MB, less than 8.25% of Python3 online submissions for Largest Divisible Subset.

'''