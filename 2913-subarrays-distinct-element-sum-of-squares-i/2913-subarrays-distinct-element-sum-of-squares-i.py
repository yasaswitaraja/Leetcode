
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            x = set()
            for j in range(i, n):
                x.add(nums[j])
                ans += len(x) ** 2

        return ans
