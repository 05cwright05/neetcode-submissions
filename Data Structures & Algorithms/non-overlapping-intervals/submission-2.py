class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # lets explore a greedy heuristic first, can we just delete the largest
        # obvs this doesnt work cuz liek if i have 1, 500 and then a bunch of clusters in 501-510 that would be pointless
        # ok so what if instead we sort by starting value and if our ending value is ever greater than the next start,
        # perhaps we could just remove the one with a later end point since everything earlier is already good

        num_deleted = 0
        intervals.sort()


        interval_index = 0
        prev_end = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prev_end: # non overlapping
                prev_end = end
            else:
                num_deleted+=1
                prev_end = min(end, prev_end)

        
        return num_deleted