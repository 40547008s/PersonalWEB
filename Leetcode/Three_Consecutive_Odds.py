from typing import List 

class Solution():
    def threeConsecutiveOdds(self, arr):
        
        for i in range(len(arr) - 2):
            if arr[i] % 2 != 0 and arr[i + 1] % 2 != 0 and arr[i + 2] % 2 != 0:
                return True
        return False

test = Solution()
print(test.threeConsecutiveOdds([1,2,34,3,4,5,7,23,12]))