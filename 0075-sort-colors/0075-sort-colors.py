
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        l = 0
        mid = 0
        r = len(nums) - 1

        while mid <= r:
            if nums[mid] == 0:
                nums[l], nums[mid] = nums[mid], nums[l]
                l += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[r], nums[mid] = nums[mid], nums[r]
                r -= 1
