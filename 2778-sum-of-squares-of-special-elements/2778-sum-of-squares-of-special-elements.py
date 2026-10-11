class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)

        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                ans += nums[i - 1] * nums[i - 1]

                if i * i != n:
                    ans += nums[n // i - 1] * nums[n // i - 1]

        return ans