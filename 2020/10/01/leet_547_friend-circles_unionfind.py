# 2020\10\01\leet_547_friend-circles_unionfind.py
# - _leet 
# - _unionfind

# 202009262226 202009262250
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        '''
        
            problem
            
                N명이 있음
                이중엔 친구들도 있고, 친구 아닌 애들도 있음
                친구관계는 transitive이다
                a 와 b 가 친구다. b와 c가 친구다
                => a, b 는 다이렉트 친구, b c 도 다이렉트 친구
                a c 는 인다이렉트 친구
                
                그리고 friend circle을 정의.
                    direct, indirect 친구들의 집합이야
                    
                N * N 매트릭스인 M이 주어져. 
                그리고 m[i][j] = 1 이라면, i번째와 j번재 친구는 다이렉트 프렌드야. 아니면 x
                
                이 때 너가 해야할 거는 이러한 friend circle이 몇개인가 ?
            
            idea
            
                union-find로 접근할 수 있는 문제
                matrix의 1인 값들에 대해 
                    friend[a] = b 라는 관계를 만들어 
                    그리고 root는 하나로 보게 
                    
                    -> find_root 가 필요
                    -> 둘 다 root가 있을 때 병합하는 거도 필요 
                    -> 최종적으로 union 이 다 되었다고 하자
                    그럼 자신이 자신의 친구인 것을 구하면 된다.
            
                    
                n = len(M)
                
                
                friends = [ _ for _ in range(n)]
                
                
                def find_root(i):
                    nonlocal friends
                    if friends[i] == i:
                        return i
                    else:
                        friends[i] = find_root(friends[i])
                        return friends[i]
                
                construct_friend(), M을 iterating 하면서 친구관계를 다 만들어 본다 
                 
                    for i in range(n):
                        for j in range(n):
                            if i != j :
                                root_f1 = find_root(i)
                                root_f2 = find_root(j)
                                if root_f1 != root_f2:
                                    # 아니라면, 이제 더 작은 애를 골라야해
                                    tmp = [(root_f1, i), (root_f2, j)]
                                    tmp.sort(key = lambda x : x[0])
                                    # root가 더 작은게 pick, root 더 큰애는 작은애로 들어간다
                                    # tmp[0]이 작은애, tmp[1] 이 큰애, 큰애의 루트의 루트가 tmp[0][0]이 된다
                                    parent[tmp[1][0]] = tmp[0][0]
                    

                ret = 0
                for k in friends:
                    if k == friends[k]:
                        ret += 1
                return ret 
                



            
            test
                
                1 2
                2 3
                1 4
                0 1
        
        
               0 1 2 3 4 5
               0 1 2 3 4 5
               
               1 2
                -> 더 작은거는 1 
                   0 1 2 3 4 5
                   0 0 1 1 1 5
                => 2
        '''
            
            
        n = len(M)
        if n < 1:
            return 0
        
        friends = [ _ for _ in range(n)]
                
        def find_root(i):
            nonlocal friends
            if friends[i] == i:
                return i
            else:
                friends[i] = find_root(friends[i])
                return friends[i]

        # O(|E| * lg**|N|), O(|N|)
        for i in range(n):
            for j in range(n):
                if i != j and M[i][j] == 1:
                    root_f1 = find_root(i)
                    root_f2 = find_root(j)
                    if root_f1 != root_f2:
                        tmp = [(root_f1, i), (root_f2, j)]
                        tmp.sort(key = lambda x : x[0])
                        friends[tmp[1][0]] = tmp[0][0]
                        friends[tmp[1][1]] = tmp[0][0]


        ret = 0
        for k, val in enumerate(friends):
            if k == val:
                ret += 1
        return ret 
    '''
    # 202009262226 202009262250

    Runtime: 200 ms, faster than 68.38% of Python3 online submissions for Friend Circles.
    Memory Usage: 14.6 MB, less than 15.87% of Python3 online submissions for Friend Circles.
    '''
                
        