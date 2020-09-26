# 2020\09\04\leet_1038-binary-search-tree-to-greater-sum-tree.py
# - _leet 
# - _bst
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 202009261303

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        '''
            problem

                bst있는데 이걸 greater tree로 바꿔
                bst의 원래 key 값들이 바뀜
                    key += sum of all keys greater than the original key in BST 


                => 모든 node 들에 대해 자기보다 큰 모든 값들을 += 하는 트리를 만들면 된다 

            idea
                => binary search tree 라는 것을 생각하자 
                    => 자신보다 오른쪽에 있는 값들만 생각하면 됨
                    => Right first 하고 그 합을 더하면 되지 않을까 
                    => Right, mid, left 로 순회하되 tracking 변수 하나 둬서 해결

                => node 에 대해, node key 값 및 tracking 같이 update


                accm = 0

                def func(node):

                    nonlocal accm
                    if node.right:
                        func(node.right)
                    accm += node.key
                    node.key = accm
                    if node.left:
                        func(node.left)

                if not node:
                    return node
                else:
                    func(root)
                    return root
            
                time : O(N), space : O(1)
            test
                edge
                    none -> none

                    


                        4 : 3 accm : 25->29, node = 29
                    1       10 : 2,accm : 15 -> 25, 25,  node : 25
                                15 : 1, accm: 0->15, node : 15 

                    a

        '''
        
        
        accm = 0

        def func(node):
            nonlocal accm
            if node.right:
                func(node.right)
            accm += node.val
            node.val = accm
            if node.left:
                func(node.left)
        if not root:
            return root
        else:
            func(root)
            return root

'''
202009261303 ~ 202009261317
Runtime: 32 ms, faster than 64.61% of Python3 online submissions for Binary Search Tree to Greater Sum Tree.
Memory Usage: 14.3 MB, less than 5.06% of Python3 online submissions for Binary Search Tree to Greater Sum Tree.

'''