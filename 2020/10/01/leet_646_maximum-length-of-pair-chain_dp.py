# 2020\10\01\leet_646_maximum-length-of-pair-chain_dp.py
# - _leet 
# - _dp
# 202010021635 202010021705 


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        '''
        
            problem
            
                - n개의 pair 가 주어짐
                
                - [ [1, 2], [2, 3], [3, 4]]
               
               이 pair에서 몇개를 뽑을꺼야 
                그리고 나열을 해볼건데
                [a, b] [c,d] 에서 b < c 이런식으로 배열을 하는거야 
                
                -> 이 때 가장 길게 만들 수 있는 길이는 얼마인가? 
                
            idea
                
                -> 재귀적으로 생각을 보자
                
                p0, p1, p2, p3 ..  pi 있을 때
                
                pi를 마지막으로 둘 수 있는, 가장 긴 길이를 찾는 것 
                
                f(pairs, idx): 마지막을 idx 로 둘 때 가장 길이가 긴 것 
                    - 이전의 해에서 가장 긴 것을 찾는거네 
                    - pi[0] 보다 작은 끝점을 가진 것들에 대해서. 
                
                1. pairs 를 end 값 기준으로 오름 차순 정렬 
                2. 올 수 있는 것들에 대해 가장 긴 길이를 찾는다
                    -> 올 수 있는 것 : target_pair[1]보다 작은 것들 
                        -> 또 생각해야할 것 : 
                            target_pair[1]보다 작은 값을 가진, i, j가 있을 때 
                                i의 값이  j보다 작다면 굳이 볼 필요가 없다 
                                    -> 즉, target_pair[1]보다 작으면서, 순 증가인 것들만을 봐야한다.. 
                3. update 한다. 
                
                            
                pairs = [[1,2], [2,3], [3, 4]]
                pairs.sort(key = lambda x : x[1])
                aux = dict()
                    # aux[3] -> pairs[3]을 제일 마지막으로 놔둘 때 가질 수 있는 가장 긴 길이 
                
                len_p = len(pairs)
                aux[0] = 1
                
                # O(N * (LAST_PAIR_PICK + O(N)))
                aux2 = [_[1] for _ in pairs]                
                
                for idx in range(1, len_p):
                    last_pair = pairs[idx]
                    # last_pair보다 앞에 있고, pairs[idx][1] 보다 작은 값들을 가진 갈 수 있는 곳들에 대해, 
                    # 가장 길이가 큰것을 고른다 
                    limit = last_pair[0]
                    # 이전에 온 것중에 last_pair가 올 수 있는 것을 찾는다.
                    # limit보다 pair[1]의 값이 작은 idx들에 대해서 조회를 해야함  
                    # aux2를 일단 쓰자. bisect 따로 안짜기 위해  
                    target_idx = bisect.bisect_left(aux2, limit, 0, idx)                    
                    prev_max_val = max([aux[_] for _ in range(target_idx, -1, -1) ])
                    aux[idx] = prev_max_val + 1
                    
                return max(aux)
            
            well-formed
                [ [1, 2], [2, 3], [3, 4]]
                
                aux2 = [2, 3, 4]
                
                pairs.sort(key = lambda x : x[1])
                aux = dict()
                len_p = len(pairs)
                aux[0] = 1
                aux2 = [_[1] for _ in pairs]                
                
                for idx in range(1, len_p):
                    last_pair = pairs[idx]
                    limit = last_pair[0]
                    target_idx = bisect.bisect_left(aux2, limit, 0, idx)
                    search_range = [aux[_] for _ in range(target_idx-1, -1, -1) ]
                    prev_max_val = 0 if not search_range else max(search_range)
                    aux[idx] = prev_max_val + 1
                
                
                return max(aux)
            
            
            
            test
                
        
        '''
        
        pairs.sort(key = lambda x : x[1])
        aux = dict()
        len_p = len(pairs)
        aux[0] = 1
        aux2 = [_[1] for _ in pairs]                

        # [[1,2], [2,3], [2,3], [3,4]]
        
        
        for idx in range(1, len_p):
            last_pair = pairs[idx]
            limit = last_pair[0]
            target_idx = bisect.bisect_left(aux2, limit, 0, idx)
            search_range = [aux[_] for _ in range(target_idx-1, -1, -1) ]
            prev_max_val = 0 if not search_range else max(search_range)
            aux[idx] = prev_max_val + 1


        return max([aux[_] for _ in aux])
        

        '''
            #202010021635 202010021705 
            Runtime: 712 ms, faster than 45.58% of Python3 online submissions for Maximum Length of Pair Chain.
            Memory Usage: 15 MB, less than 5.10% of Python3 online submissions for Maximum Length of Pair Chain.

        '''