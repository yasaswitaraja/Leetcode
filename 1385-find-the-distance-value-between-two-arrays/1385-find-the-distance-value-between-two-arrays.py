class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        res = 0

        for i in arr1:
            found = False

            for j in arr2:
                if abs(i - j) <= d:
                    found = True
                    break

            if not found:
                res += 1

        return res