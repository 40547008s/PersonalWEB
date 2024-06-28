from typing import List

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        city = [0]*n

        for x, y in roads:
            city[x] += 1
            city[y] += 1
        
        city.sort()

        res = 0
        for i in range(n):
            print(city[i], i+1)
            res += city[i]*(i+1)
        return res

test = Solution()
print(test.maximumImportance(5, [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]))