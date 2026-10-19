class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        x=[]
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == target:
                x.append(i)
        return x
                
