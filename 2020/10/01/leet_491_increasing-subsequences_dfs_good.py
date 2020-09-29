# leet_491_increasing-subsequences_dfs_good.py
# - _leet 
# - _dfs
# - _good
# - _dfs_good
# 202009300805 202009300840



class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        '''
            problem
                - 모든 증가 subsequences of the given arrray를 모두 구해라 길이는 최소 2 이상 
                
            idea
                nums[:i] 까지의 해를 func(nums, i)라고 하자                 
                nums[i]가 들어왔다. 
                -> [0 ... i-1] 중 nums[i]와 연결되는 것이 있다면 계속해서 추가해 나간다 
                이 때 기존에 나온 것이라면 넣지 않는다 
                
                최소길이는 2 이상. nums길이가 2보다 작다면 []
                
                4 7 6 6 7 
                
                aux = dict()
                # aux[10] : nums[10]에서 끝나는 모든 답, set()이다.  func(10)이 들어있다고 보면 된다 
                # aux에는 unique한 것만이 들어가야 한다 
                # aux[i] = [nums[i]] 이렇게 초기화를 하자 
                aux2 = set()
                
                - idx 가 0인 경우
                    -> return []
                - idx 가 1인 경우
                    -> [0 : idx] 중 nums[idx]보다 작은 것들을 찾는다. 그리고 답을 잇는다
    
                    for i in range(0, idx):
                        if nums[i] < nums[idx]:
                            # aux[i]에 대해 nums[idx]를 붙인다 이 때 답이 unique 해야 함을 잊지말자 
                            # nums[i]에서 끝난 것들의 모든 해에 대해 답을 넣는다 
                            for j in aux[i]:
                                check = tuple(j + [nums[idx]])
                                if check not in aux2:
                                    aux[idx].append(j + [nums[idx]])
                                    aux2.add(check)
                    # Time : O(|N| * 2 ** n )
                                            
                              
                              
                알고리즘을 정리하면 다음과 같다. 
                len_n = len(nums)     
                aux = dict() # aux[idx] := nums[idx]에서 끝나는 정답부분의 리스트 
                aux2 = set() # 중복을 check 하기 위한 것
                # o(|n|)
                for idx in range(len_n):
                    aux[idx] = [nums[idx]]
                                
                # 하나짜리를 aux2에 넣어야할까? 어차피 tuple로 체크하면 되니까 굳이 넣을 필요는 없어 보인다                               
                              
                              
                # O(N * N * (2 ** N) * O(N))                    
                for i in range(1, len_n):
                    for j in range(0, i-1)
                        # nums[i] 보다 작거나 같은 nums[j]들에 대해, nums[i]를 이어 붙일 때, 지금까지 나오지 않은 것만 넣는다 
                        if nums[j] <= nums[i]:
                            for k in aux[j]:
                                check = tuple(k + [nums[idx]])
                                if check not in aux2:
                                    aux[i].append(j + [nums[i]])
                                    aux2.add(check)
                # 지금까지 모은 AUX의 값들을 넣는다 
                ret = []
                for k in aux:
                    ret += aux[k]
        
                return ret
        
        '''

        len_n = len(nums)     
        aux = dict() # aux[idx] := nums[idx]에서 끝나는 정답부분의 리스트 
        aux2 = set() # 중복을 check 하기 위한 것
        # o(|n|)
        for idx in range(len_n):
            aux[idx] = [[nums[idx]]]
        
        for i in range(1, len_n):
            for j in range(0, i):
                # nums[i] 보다 작거나 같은 nums[j]들에 대해, nums[i]를 이어 붙일 때, 지금까지 나오지 않은 것만 넣는다 
                if nums[j] <= nums[i]:
                    for k in aux[j]:
                        check = tuple(k + [nums[i]])
                        if check not in aux2:
                            aux[i].append( k + [nums[i]])
                            aux2.add(check)
        # 지금까지 모은 AUX의 값들을 넣는다 
        ret = []
        for k in aux:
            ret += aux[k][1:]

        return ret


    '''
        Runtime: 212 ms, faster than 95.81% of Python3 online submissions for Increasing Subsequences.
        Memory Usage: 25.3 MB, less than 12.06% of Python3 online submissions for Increasing Subsequences.

    '''