#Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def make_BTS(nums) -> TreeNode:
    root = TreeNode(val = nums[0])
    for i in range(1,len(nums)) :
        if isinstance(nums[i], int) :
            cur = root
            while cur :
                if cur.val < nums[i]:
                    if cur.right:
                        cur = cur.right
                    else :
                        cur.right = TreeNode(val=nums[i])
                        break
                else :
                    if cur.left:
                        cur = cur.left
                    else :
                        cur.left = TreeNode(val=nums[i])
                        break
    return root

def rvl(root: TreeNode):
    if root.right:
        rvl(root.right)
    print(root.val, end = ' ')
    if root.left:
        rvl(root.left)

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        tsum = 0
        cur = root
        while cur:
            if cur.right is None :
                tsum += cur.val
                cur.val = tsum
                cur = cur.left
            else:
                pre = cur.right
                while pre.left and pre.left != cur:
                    pre = pre.left
                if pre.left is None:
                    pre.left = cur
                    cur = cur.right
                else:
                    tsum += cur.val
                    cur.val = tsum
                    pre.left = None
                    cur = cur.left
        return root
root = make_BTS([4,1,6,0,2,5,7,None,None,None,3,None,None,None,8])
rvl(root)
print()
test = Solution()
root = test.bstToGst(root)
rvl(root)