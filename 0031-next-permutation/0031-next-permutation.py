class Solution:
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

    def reverse(self, nums, start):
        k = len(nums) - 1

        while start < k:
            self.swap(nums, start, k)
            start += 1
            k -= 1

    def nextPermutation(self, nums):
        i = len(nums) - 2

        # STEP 1: Find the breakpoint
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            j = len(nums) - 1

            # STEP 2: Find the smallest number greater than nums[i]
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1

            # STEP 3: Swap
            self.swap(nums, i, j)

        # STEP 4: Reverse the suffix
        self.reverse(nums, i + 1)