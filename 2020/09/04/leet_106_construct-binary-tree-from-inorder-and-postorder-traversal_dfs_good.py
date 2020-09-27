# 2020\09\04\leet_106_construct-binary-tree-from-inorder-and-postorder-traversal_dfs_good.py
# - _leet 
# - _dfs
# - _good
# - _dfs_good

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        if not inorder:
            return None
        
        aux = {val: idx for idx, val in enumerate(inorder)}
        
        
        def func(in_left_idx, in_right_idx, post_left_idx, post_right_idx) -> TreeNode:
            # print(in_left_idx, in_right_idx, post_left_idx ,post_right_idx)
            nonlocal inorder, postorder
            if in_right_idx-in_left_idx + 1 == 1:
                return TreeNode(inorder[in_right_idx])
            elif in_right_idx - in_left_idx + 1 <= 0:
                return None
            else:
                current_root = postorder[post_right_idx]
                # tidx = find(inorder, in_left_idx, in_right_idx, current_root)
                tidx = aux[current_root]
                left_subtree_size, right_subtree_size = tidx-1 - in_left_idx + 1,  in_right_idx - (tidx + 1) + 1                
                left_in_lidx, left_in_ridx = in_left_idx, tidx-1
                left_post_lidx, left_post_ridx = post_left_idx, post_left_idx + left_subtree_size -1
                right_in_lidx, right_in_ridx = tidx+1,  in_right_idx
                right_post_lidx, right_post_ridx = left_post_ridx + 1,  post_right_idx - 1                
                return TreeNode(current_root, func(left_in_lidx, left_in_ridx, left_post_lidx, left_post_ridx  )
                , func(right_in_lidx, right_in_ridx, right_post_lidx, right_post_ridx))                                                             
        
        # Time : O(N), SPACE : O(N)
        in_left_idx, in_right_idx, post_left_idx, post_right_idx = 0, len(inorder)-1, 0, len(inorder)-1
        return func(in_left_idx, in_right_idx, post_left_idx, post_right_idx)
                                                       
        

    '''

    202009272158 ~ 202009272238
    Runtime: 48 ms, faster than 99.00% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
    Memory Usage: 19.8 MB, less than 48.75% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.

    '''