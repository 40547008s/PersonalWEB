from typing import List

class Solution(object):
    def longestSubarray(self, nums, limit):
        q_min = []
        q_max = []
        ans = 0
        begin = 0
        for i, num in enumerate(nums):
            while q_min and num < q_min[-1]:
                q_min.pop()
            q_min.append(num)
            while q_max and num > q_max[-1]:
                q_max.pop()
            q_max.append(num)

            while q_max[0] - q_min[0] > limit:
                if q_min[0] == nums[begin]:
                    q_min.pop(0)
                if q_max[0] == nums[begin]:
                    q_max.pop(0)
                begin += 1
            ans = max(ans, i - begin + 1)
        return ans

test = Solution()
print(test.longestSubarray([8,2,4,7], 4))