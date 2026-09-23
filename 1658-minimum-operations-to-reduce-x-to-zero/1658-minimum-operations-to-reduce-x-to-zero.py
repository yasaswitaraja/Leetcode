class Solution:

    def minOperations(self, nums: List[int], x: int) -> int:

        min_operation = float('inf')

        size = len(nums)

        cur_sum = 0

        left = -1

        right = size

        while left < size - 1 and cur_sum < x:

            left += 1
            cur_sum += nums[left]

        if cur_sum == x:

            min_operation = min(min_operation, left + 1)

        while left >= 0:

            cur_sum -= nums[left]
            left -= 1

            while right > left + 1 and cur_sum < x:

                right -= 1
                cur_sum += nums[right]

            if cur_sum == x:

                min_operation = min(
                    min_operation,
                    (left + 1) + (size - right)
                )

        return -1 if min_operation == float('inf') else min_operation