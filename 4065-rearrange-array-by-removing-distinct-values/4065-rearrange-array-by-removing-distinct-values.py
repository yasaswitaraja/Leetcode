class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        ans = []
        while nums:
            s = sorted(set(nums))

            for x in s:
                ans.append(x)
                nums.remove(x)

        return ans