from typing import List

class Solution(object):
    def numberOfSubarrays(self, nums, k):
        left = right = oddCnt = res = 0
        n = len(nums)
        while right < n:
            if (nums[right]%2) == 1 : oddCnt += 1
            right += 1
            if oddCnt == k:
                tmp = right
                while right < n and (nums[right]%2) == 0:
                    right += 1
                rightEvenCnt = right - tmp
                leftEvenCnt = 0
                while nums[left]%2 == 0:
                    leftEvenCnt += 1
                    left += 1
                res += (leftEvenCnt+1) * (rightEvenCnt+1)
                left += 1
                oddCnt -= 1
        return res

test = Solution()
print(test.numberOfSubarrays([1,1,2,1,1],3))