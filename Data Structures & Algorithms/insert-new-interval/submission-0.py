class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start, new_end = newInterval
        res = []
        i = 0
        n = len(intervals)

        # 1. add all intervals completely before newInterval
        while i < n and intervals[i][1] < new_start:
            res.append(intervals[i])
            i += 1

        # 2. merge overlapping intervals
        while i < n and intervals[i][0] <= new_end:
            new_start = min(new_start, intervals[i][0])
            new_end = max(new_end, intervals[i][1])
            i += 1

        res.append([new_start, new_end])

        # 3. add remaining intervals
        while i < n:
            res.append(intervals[i])
            i += 1

        return res