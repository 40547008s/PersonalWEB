from typing import List

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        if m == 2: return position[-1] - position[0]

        def check(dis: int) -> bool:
            cur = position[0]+dis
            cnt = 1
            for i in position[1:]:
                if cur <= i:
                    cur = i+dis
                    cnt += 1
            return cnt >= m

        l, r = 0, position[-1]-position[0]
        while l < r:
            dis = (l+r+1) >> 1
            if check(dis) : l = dis
            else : r = dis -1
        return l

test = Solution()
print(test.maxDistance([1,2,3,4,7], 3))