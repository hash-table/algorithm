

# leet_1481_least-number-of-unique-integers-after-k-removals_heap.py
# _leet
# _heap
# 202010201910 202010201921
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        '''
        
        
            problem
                arr : 정수 배열 
                k : 정수
                찾아라 the least number of unique integers after removing exactly k elements
                
                배열이 있어 
                여기서 k개를 정확하게 지웠다고 하자. 이 때 지우는 방법은 여러개겠지? 이렇게 지웠어
                그럼 살아 남은 것들이 있겠지? 이 살아 남은거의 unique 숫자의 개수를 구해라 
                
                arr = [5 5 4] k = 1
                -> 4를 제거 했어 -> 5 1개
                arr = [4 3 1 1 3 3 2] k = 3 
                음 결국에 가장 개수가 작은 것들부터 지운다고 하자 
                arr  arr_
                    1 : 2
                    2 : 1
                    3 : 3
                    4 : 1
                저기서 나는 3개를 지울 거야 
                개수가 가장 작은거는 2 : 1개, 4 : 1개 잖아 저거 두개를 지운다고 하자 
                그럼 1, 3 남으니까 2개 
                arr의 길이는 10^5 이하 
                
                
                
            
            idea
            
            
                # [ ( 숫자, 그 개수) .... ] 가 있다고 하자. 이걸 개수에 대해서 정렬을 해 
                # 개수를 제거하는데 정확히 k가 되면 그만둬 
                
                aux = [] 
                heapify(aux)
                arr_counter = Counter(arr)
                for num in arr_counter:
                    heappush(aux, (arr_counter[num], num))
                
                accm = 0
                
                ret = len(aux)
                
                while aux:
                    top = heappop(aux)
                    if k >= top[0]:
                        k -= top[0]
                        ret -= 1  
                    else:
                        break
                return ret 

            
            
            
            well-formed
            
                aux = [] 
                heapify(aux)
                arr_counter = Counter(arr)
                for num in arr_counter:
                    heappush(aux, (arr_counter[num], num))

                ret = len(aux)               
                while aux:
                    top = heappop(aux)
                    if k >= top[0]:
                        k -= top[0]
                        ret -= 1  
                    else:
                        break
                return ret 
            
            test
        
        
        
        
        '''
        aux = [] 
        heapify(aux)
        arr_counter = Counter(arr)
        for num in arr_counter:
            heappush(aux, (arr_counter[num], num))

        ret = len(aux)               
        while aux:
            top = heappop(aux)
            if k >= top[0]:
                k -= top[0]
                ret -= 1  
            else:
                break
        
        return ret 

'''
Runtime: 580 ms, faster than 46.05% of Python3 online submissions for Least Number of Unique Integers after K Removals.
Memory Usage: 34.4 MB, less than 5.70% of Python3 online submissions for Least Number of Unique Integers after K Removals.
'''