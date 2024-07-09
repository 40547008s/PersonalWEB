from typing import List

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        cur = 0
        res = 0
        for cos in customers:
            if cur > cos[0]:
                res += cur - cos[0]
                cur += cos[1]
            else :
                cur = cos[0]+cos[1]
            res += cos[1]
        return res/len(customers)

test = Solution()
print(test.averageWaitingTime([[5,2],[5,4],[10,3],[20,1]]))