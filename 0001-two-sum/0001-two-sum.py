class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = dict()
        for i in range(len(nums)):
            x = target - nums[i]
            if x in d:
                return [d[x],i]
            d[nums[i]] = i    