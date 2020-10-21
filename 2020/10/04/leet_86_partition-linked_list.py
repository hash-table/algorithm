# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# leet_86_partition-linked_list.py
# leet
# linked_list
# 202010220005 202010220040
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        '''
            problem
            
                linked list가 주어졌어
                value x가 주어졌어
                
                linked list를 재정렬을 할꺼야
                such tat all nodes less than x , come before nodes greater than or equal to x 
                
                정리하면, linkedlist가 있어. 그럼 값들이 있겠지
                x보다 작은것들은 다 앞에, x보다 크거나 같은 노드들은 뒤로, 이런식으로 링크드 리스트를 rearrange 해라
                
                
                
            idea
                1 4 3 2 5 2 , x = 3
                1 2 2 4 3 5 
                
                x = 3
                1 -> 4 -> 3 -> 2 -> 5 -> 2 -> None
                
                2개의 head를 둔다
                
                less_head, ge_head = Node(), Node()
                
                target = head
                less_target, ge_target = less_head, ge_head
                while target:
                    picked_li = less_target if target.val < x else ge_target
                    picked_li.next = target
                    tmp = target.next
                    target.next = None
                    target = tmp
                # iterating을 한번 더한다음에 less_target.next 에 ge_target을 붙인다
                if less_target and ge_target:
                    less_target.next = ge_target
                    return less_head.next
                elif less_target and not ge_target:
                    return less_head.next
                elif not less_target and ge_target:
                    return ge_target.next
                else:
                    return None
            
            
            well-formed

                less_head, ge_head = Node(), Node()                
                target = head
                less_target, ge_target = less_head, ge_head
                                
                while target:
                    picked_li = less_target if target.val < x else ge_target
                    picked_li.next = target
                    tmp = target.next
                    target.next = None
                    target = tmp
                
                if less_target and ge_target:
                    less_target.next = ge_head.next
                    return less_head.next
                elif less_target and not ge_target:
                    return less_head.next
                elif not less_target and ge_target:
                    return ge_head.next
                else:
                    return None



            test
        
        
        '''

        less_head, ge_head = ListNode(), ListNode()                
        target = head
        tmp = [less_head, ge_head]
        while target:
            idx = 0 if target.val < x else 1
            picked_li = tmp[idx]
            picked_li.next = target
            target = target.next
            tmp[idx] = picked_li.next
            tmp[idx].next = None
        
        
        if less_head.next and ge_head.next:
            tmp[0].next = ge_head.next
            return less_head.next
        elif less_head.next and not ge_head.next:
            return less_head.next
        elif not less_head.next and ge_head.next:
            return ge_head.next
        else:
            return None

        '''
        
Runtime: 32 ms, faster than 83.97% of Python3 online submissions for Partition List.
Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for Partition List.
        
        '''

