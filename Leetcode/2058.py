from typing import Optional
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def ltoln(nums: list) -> ListNode:
    head = ListNode()
    res = head
    for i in nums:
        if head.next:
            head = head.next
        head.val = i
        head.next = ListNode()
    head.next = None
    return res

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        cur = head
        pre = None
        nxt = head.next
        index = 0
        cp = []
        while nxt:
            if cur and pre and nxt:
                if pre.val < cur.val > nxt.val or pre.val > cur.val < nxt.val:
                    cp.append(index)
            index += 1
            pre = cur
            cur = cur.next
            nxt = nxt.next
        if len(cp) < 2 : return [-1, -1]

        return [min(cp[i]-cp[i-1] for i in range(1,len(cp))), cp[-1]-cp[0]]
head = ltoln([1,3,2,2,3,2,2,2,7])

text = Solution()
print(text.nodesBetweenCriticalPoints(head))