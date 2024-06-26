import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def LtoT(nodes: list) -> TreeNode:
    n = len(nodes)
    
    if n == 0:
        return None
    
    parentStack = collections.deque()
    root = TreeNode(nodes[0])
    curParent = root

    for i in range(1, n):
        if i % 2 == 1:
            if nodes[i] is not None:
                curParent.left = TreeNode(val=nodes[i])
                parentStack.append(curParent.left)
        else:
            if nodes[i] is not None:
                curParent.right = TreeNode(val=nodes[i])
                parentStack.append(curParent.right)
            curParent = parentStack.popleft()
    return root

def travelp(root: TreeNode) -> list:
    traversal = []
    queue = collections.deque()
    queue.append(root)

    while queue:
        size = len(queue)
        while size:
            node = queue.popleft()
            traversal.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
            size -= 1
    return traversal

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nums = []
        def travel(node: TreeNode):
            if node is None:
                return
            travel(node.left)
            nums.append(node.val)
            travel(node.right)
        travel(root)

        def build_bst(start: int, end: int) -> TreeNode:
            if start > end:
                return None
            mid = (start+end) // 2
            node = TreeNode(nums[mid])
            node.left = build_bst(start,mid-1)
            node.right = build_bst(mid+1,end)
            return node
        return build_bst(0, len(nums)-1)
nodes = [2,1,3] #[1,None,2,None,3,None,4]
root = LtoT(nodes)

test = Solution()
print(travelp(test.balanceBST(root)))
