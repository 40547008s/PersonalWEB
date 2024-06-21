from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int :
        min_satisfied = 0
        max_satisfied = 0
        for i in range(minutes):
            max_satisfied += customers[i] if grumpy[i] else 0
            min_satisfied += customers[i] if not grumpy[i] else 0
        
        cur_satisfied = max_satisfied
        for i in range(minutes, len(grumpy)):
            min_satisfied += customers[i] if not grumpy[i] else 0
            cur_satisfied += customers[i] if grumpy[i] else 0
            cur_satisfied -= customers[i-minutes] if grumpy[i-minutes] else 0
            max_satisfied = max(cur_satisfied, max_satisfied)
        return max_satisfied + min_satisfied

test = Solution()
print(test.maxSatisfied([1,0,1,2,1,1,7,5], [0,1,0,1,0,1,0,1], 3))