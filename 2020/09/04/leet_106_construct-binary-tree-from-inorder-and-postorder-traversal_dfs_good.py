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
        '''
        
            problem

                inorder list와 postorder list가 주어졌따
                이걸로 binary tree 만들기
                * duplicate는 없음

                inorder : 9 3 15 20 7
                postorder : 9 15 7 20 3

            idea

                inorder(node)
                    inorder(node.left)
                    node
                    inorder(node.right)

                inlist := (left subtree) node (right subtree)

                postorder(node)
                    postorder(node.left)
                    postorder(node.right)
                    node

                outlist := (left subtree) (right subtree) node



                lidx, ridx = 0, len_inlist-1

                [lidx .. ridx] 에서


                    1. outlist[lidx.. ridx] 에서 root를 찾는다.
                    root_val = outlist[-1]
                    2. inlist에서 root_val과 같은 값을 가진 곳을 찾는다 
                        이 때 root의 위치를 tidx라고 하자

                    => inlist[lidx .. tidx-1] 이 left subtree
                    => inlist[tidx + 1 .. ridx]가 rightsubtree 

                    3. 2에서 구한 정보를 이용해 postorder에서 대응되는 leftsubree, rightsubtree를 찾는다
                base case
                    -> ridx - lidx +1 이 1 인경우, return TreeNode(post_list[ridx])
                    -> rid - lidx + 1 < 1, return None


                -> inlist, outlist 각각에 대한 left 와 right를 관리 해야 할 거 같음 

                => 만약 balanced 형태라고 가정을 하자 

                ilist, plist := inorder list, postorder list
                ilidx, iridx, plidx, pridx := 0, n-1, 0, n-1
                loop:
                    1. find root in plist : O(1)
                    2. find tidx which have root_val in ilist : O(len(ILIST))
                    3. find left subtree range(ilist[tidx-1]]) in plist : O(len(PLIST))
                       find right subtree range(ilist[tidx+1]) in plist : O(len(PLIST))
                    * left, right range 존재 가능한거 고려
                    until range가 존재할때까지 

                    => LOOP당 O(range)
                    => O(N) = O(N/2) + O(N/2) = 2 * O(N/2) = 4 * O(N/4)
                        => Time complexity :  O(N)
                        => Space complexity : O(1)


                def func(ilidx, iridx, plidx, pridx) -> TreeNode
                    nonlocal ilist, plist
                    if iridx-ilidx + 1 == 1:
                        return TreeNode(ilist[iridx])
                    elif iridx - ilidx + 1 <= 0:
                        return None
                    else:
                        current_root = plist[pridx]
                        # ilist에서 current_root가 어디있는지 찾는다
                        tidx = find(ilist, ilidx, iridx, current_root)
                        left_subtree_size = tidx-1 - ilidx + 1
                        right_subtree_size = iridx - (tidx + 1) + 1
                        if left_subtree_size == 0:
                            # right만 있는 경우
                            return TreeNode(current_root, None , func(tidx + 1, iridx, plidx, pridx - 1))
                        elif right_subtree_size == 0:
                            return TreeNode(current_root, func(ilidx, tidx - 1, plidx, pridx - 1), None)
                        else:
                            #둘다 잇는 경우
                            # plist에서 ilist[tidx-1]
                            next_limit_pidx = find(plist, plidx, pridx, ilist[tidx-1])
                            return TreeNode(current_root, func(ilidx, tidx-1, plidx, next_limit_pidx), func(tidx+1, iridx, next_limit_pidx+1, pridx))

            test

                inorder : 9 3 15 20 7
                postorder : 9 15 7 20 3
                ilidx, iridx, plidx, pridx = 0, 4 , 0 , 4

                func(0, 4 , 0 , 4)
                    -> recursion case

                    current_root = 3 
                    tidx = inorder에서 3과 같은 값을 찾음 : 1
                    left_subtree_size = 0 - 0 + 1 = 1
                    right_subtree_size = 4 - 2 + 1 = 3
                    다음경계값 = inorder[tidx-1] = 9
                    post에서 9의 위치 -> 0 

                    return TreeNode(3, func(0, 0, 0, 0), func(2, 4, 1, 3))

        '''
        if not inorder:
            return None
        
        def find(li, lidx, ridx, val):
            for idx in range(lidx, ridx+1):
                if li[idx] == val:
                    return idx
            return None
        
        
        def func(ilidx, iridx, plidx, pridx) -> TreeNode:
            # print(ilidx, iridx, plidx ,pridx)
            nonlocal inorder, postorder
            if iridx-ilidx + 1 == 1:
                return TreeNode(inorder[iridx])
            elif iridx - ilidx + 1 <= 0:
                return None
            else:
                current_root = postorder[pridx]
                tidx = find(inorder, ilidx, iridx, current_root)
                # in : [ileft, iright] -> [ileft, tidx-1], [tidx+1, iright]
                # post : [pleft, pright] => [pleft, p_next], [p_next+1, pright-1]
                left_subtree_size = tidx-1 - ilidx + 1
                right_subtree_size = iridx - (tidx + 1) + 1
                if left_subtree_size == 0:
                    return TreeNode(current_root, None , func(tidx + 1, iridx, plidx, pridx - 1))
                elif right_subtree_size == 0:
                    return TreeNode(current_root, func(ilidx, tidx - 1, plidx, pridx - 1), None)
                else:
                    # 현재 루트는 3 
                    # next_limit 는 2
                    # next_limit_pidx = find(postorder, plidx, pridx, inorder[tidx-1])
                    # 길이로 치면 되네 
                    return TreeNode(current_root, func(ilidx, tidx-1, plidx, plidx + left_subtree_size -1  ), func(tidx+1, iridx, plidx + left_subtree_size, pridx - 1))                                                             
        ilidx, iridx, plidx, pridx = 0, len(inorder)-1, 0, len(inorder)-1
        return func(ilidx, iridx, plidx, pridx)
                                                       
        

'''

202009272158 ~ 202009272238
Runtime: 272 ms, faster than 17.67% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
Memory Usage: 19.3 MB, less than 49.79% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.

'''