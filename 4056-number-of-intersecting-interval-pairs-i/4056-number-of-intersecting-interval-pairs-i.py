class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        count = 0

        for i in range(len(intervals)):
            for j in range(i + 1, len(intervals)):

                start1 = intervals[i][0]
                end1 = intervals[i][1]

                start2 = intervals[j][0]
                end2 = intervals[j][1]

                if max(start1, start2) <= min(end1, end2):
                    count += 1

        return count