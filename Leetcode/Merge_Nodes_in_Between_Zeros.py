from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None

def ltoln(nums):
    head = ListNode()
    cur = head
    for i in nums[1:]:
        cur.next = ListNode()
        cur = cur.next
        cur.val = i
        
        
    cur.next = None
    return head

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) ->Optional[ListNode]:
        temp = curr = head
        curr = curr.next
        s = 0
        while curr:
            if curr.val == 0:
                temp = temp.next
                temp.val = s
                s = 0
            else :
                s += curr.val
            curr = curr.next
        temp.next = None
        return head.next

test = Solution()

ans = test.mergeNodes(ltoln([0,3,1,0,4,5,2,0]))
while ans:
    print(ans.val, end = ' ')
    ans = ans.next