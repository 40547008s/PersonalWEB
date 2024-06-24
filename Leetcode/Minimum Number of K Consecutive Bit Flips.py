from typing import List

class Solution:
    def minKBitFlips(self, nums: List[int], k:int) -> int:
        n = len(nums)
        flips = [0] * (n+1)
        total_flips = 0
        flip_counter = 0
        for i, num in enumerate(nums):
            flip_counter += flips[i]
            if (num + flip_counter) % 2 == 0:
                if i + k > n:
                    return -1
                flips[i] += 1
                flips[i+k] -= 1
                flip_counter += 1
                total_flips += 1
        return total_flips

test = Solution()
print(test.minKBitFlips([0,1,0],1))