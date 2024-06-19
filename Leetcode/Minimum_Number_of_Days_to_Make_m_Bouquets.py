from typing import List
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay): return -1

        def make(day: int) -> bool:
            bouquet = 0
            flower = 0
            for d in bloomDay:
                if d <= day:
                    flower += 1
                    if flower == k:
                        bouquet += 1
                        flower = 0
                else : flower = 0
            return bouquet >= m
        l, r = min(bloomDay), max(bloomDay)
        while l < r:
            mid = (l+r)//2
            if make(mid):
                r = mid
            else :
                l = mid+1
        return l            

test = Solution()
print(test.minDays(bloomDay = [1,10,3,10,2],m = 3, k = 1))