class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        mini = float('inf')

        for i in range(len(nums)):
            s = 0

            for j in str(nums[i]):
                s = s + int(j)

            if i == s:
                mini = min(mini, i)

        if mini == float('inf'):
            return -1
        else:
            return mini