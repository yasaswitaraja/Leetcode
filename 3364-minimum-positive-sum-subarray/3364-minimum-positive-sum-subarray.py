class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        p = [0]
        t = 0

        for i in range(len(nums)):
            t = t + nums[i]
            p.append(t)       
        m = 10**18 
        for j in range(len(nums)):
            for k in range(j + 1, len(nums) + 1):
                if k - j > r:
                    break
                if l <= k - j <= r and p[k] - p[j] > 0:
                    s = p[k] - p[j]
                    if s < m:
                        m = s
        if m == 10**18:
            return -1
        else:
            return m