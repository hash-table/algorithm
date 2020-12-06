# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



# leet_314_binary-tree-vertical-order-traversal.py
# _leet
# _dfs

#202012061455 202012061527

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        '''
            problem
                - binary tree가 있다.
                - vertical order traversal 라는 것을 만들거야 
                - if two nodes are in the same row and column, the order should be from left to right
            
            idea
                - left, right, depth에 대한 정보를 node를 순회할 때 넣고 정렬하는 방식? 
                
                - left -> right 로 하면 l->r 순서는 보장이 된다. 
                
                - 경로를 내려오며 left 횟수와 right 횟수의 합이 vertical degree를 표현할 수 있다. 
                
                - aux : dict 를 만들고 vertical degree 를 key 값으로 하는 dict를 생성. 
                
                - aux[vertical_degree] = List[Tuple]
                
                - 이 때 tuple은 (node의 값, depth )
                
                aux를 다 채우고 나서, aux의 key 값에 대해 aux[key] 에 대해서 depth에 대해서 정렬 
                
                정렬된 aux 의 node 값들만을 읽어 들인다. 
                
                
                def func(root: TreeNode):
                
                
                    aux = defaultdict(lambda : [])
                    
                    def dfs(here, left, right, depth):
                        
                        # dag이니까 edge 정보를, visited 를 저장할 필요가 없다. 
                        
                        # here에 대한 정보를 먼저 저장해야함
                        vertical_key = left + right
                        aux[vertical_key].append(here.val, depth)
                        # 다음 2개에 대해서 진행
                        
                        if here.left:
                            dfs(here.left, left+1, right, depth + 1)
                        if here.right:
                            dfs(here.right, left, right + 1, depth + 1)
                
                
                    dfs(root, 0, 0, 0)
                    ret = [] 
                    for vertical_val in sorted(aux.keys()):
                        aux[vertical_val].sort(key = labmda x : x[1])
                        ret.append(aux[vertical_val])
                    
                    return ret
                    
                
                
             well-formed
        
        
        
                def func(root: TreeNode):
                
                    aux = defaultdict(lambda : [])                    
                    
                    def dfs(here, left, right, depth):
                        vertical_key = left + right
                        aux[vertical_key].append(here.val, depth)
                        if here.left:
                            dfs(here.left, left+1, right, depth + 1)
                        if here.right:
                            dfs(here.right, left, right + 1, depth + 1)
                
                
                    dfs(root, 0, 0, 0)
                    ret = [] 
                    for vertical_val in sorted(aux.keys()):
                        aux[vertical_val].sort(key = labmda x : x[1])
                        ret.append(aux[vertical_val])
                    
                    return ret
        
        
        
        '''
        # 극값 체크는 반드시 하자 
        if not root: return []
        aux = defaultdict(lambda : [])                    
        def dfs(here, left, right, depth):
            vertical_key = -left + right
            aux[vertical_key].append((here.val, depth))
            if here.left:
                dfs(here.left, left+1, right, depth + 1)
            if here.right:
                dfs(here.right, left, right + 1, depth + 1)
        dfs(root, 0, 0, 0)
        ret = [] 
        for vertical_val in sorted(aux.keys()):
            aux[vertical_val].sort(key = lambda x : x[1])
            ret.append([_[0] for _ in aux[vertical_val]])

        return ret

        
'''
Runtime: 36 ms, faster than 48.83% of Python3 online submissions for Binary Tree Vertical Order Traversal.
Memory Usage: 14.2 MB, less than 19.62% of Python3 online submissions for Binary Tree Vertical Order Traversal.
'''