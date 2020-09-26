# 2020\09\04\leet#1382-balance-a-binary-search-tree#bst#good.py

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        '''
            problem
            
                # 202009261119        
                # 202009261150        

                binary search tree가 주어져있음
                balanced bst, with same node values 를 return
                - balanced 는 어떠한 노드에 대해서 left, right subtree의 height 차이가 1을 넘지 않는 거
                
                => bst 에 대해 balanced-bst로 변경 하기 
                
                input number
                    : 1 ~ 10^ 4
                value
                    : distince value로 구성
                    : 1 ~ 10^5
                
            idea
            
                if root == None:
                    # func(root) 에 대해 balanced binary인지, root의 height, root
                    return True, 0, root
                    
                else:
                    # some recursion, func(node)
                    
                    left_height, node.left = func(node.left)
                    right_height, node.right = func(node.right)                   
                    if abs(left_height - right_height) > 1:
                        # rearrange node
                        pass
                    
                    else:
                        return max(left_height, right_height) + 1, root
                    
                    
                    (3) 10 (30)
                
                => mid-order
                
                mid_order_list = get_mid_order(root) : O(N), O(N)
                
                def recursion(left, right) -> Node: O(N), O(N)
                    nonlocal mid_order_list
                    if right-left <= 0:
                        return None
                    if right-left == 1:
                        return TreeNode(mid_order_list[left])
                    else:
                        #O(N) : O(1 + 2 * O(N/2))

                        mid = left + (right - left) // 2                
                        # left_part = [left .. mid-1]
                        # right_part = [mid+1 .. right]
                        return TreeNode(mid_order_list[mid], recursion(left, mid-1), recursion(mid+1, right))
                => time : O(N) space : O(N)

            test            
                - None
                    -> base case     
                - 1
                    -> 
                - 1 2 
                    l = 0, r = 0
                        rursion(0, 1)                    
                            mid = 0
                                recursion(0, -1)
                                    return None
                                recusrion(1, 1)
                                    return (1)
                                return 1, None, (1)
                - 1 2 3 
                    l = 0 , r = 2
                        recusion(0, 2)
                            mid = 1 
                                recursion(0, 0)
                                recursion(2, 2)
                - 1 2 3 4 
                    l = 0 , r = 3 
                        recursion(0, 3)
                            mid = 1
                                recursion(0, 0)
                                recursion(2, 3)
                                    
        '''
        
        
        
        if not root:
            return None
        
        def get_mid_order_list(root) -> List[TreeNode]:
            if not root:
                return []
            else:
                return get_mid_order_list(root.left) + [root.val] + get_mid_order_list(root.right)
                
        mid_order_list = get_mid_order_list(root)
        
        len_li = len(mid_order_list)
        
        def recursion(left, right) -> TreeNode:
            nonlocal mid_order_list
            
            if right-left + 1 < 1:
                return None
            elif right-left + 1 == 1:
                return TreeNode(mid_order_list[left], None, None)
            else:
                mid = left + (right - left) // 2        
                return TreeNode(mid_order_list[mid], recursion(left, mid-1), recursion(mid+1, right))
        
                
        
        return recursion(0, len_li-1)
        
        
        '''
        Runtime: 356 ms, faster than 85.58% of Python3 online submissions for Balance a Binary Search Tree.
        Memory Usage: 20.7 MB, less than 5.19% of Python3 online submissions for Balance a Binary Search Tree.
        '''