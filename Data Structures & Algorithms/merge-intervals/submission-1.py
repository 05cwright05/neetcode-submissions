class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # merge overlapping intervals
        """
        Given a list like [1,3][3,5][6,7]
        return [1,5], 6,7


        Maintain a current end of interval, this starts as end of first interval
        Then we move forward if hte start <= that end
        Then we should update the end
        Once it is not smaller we add in hte previous interval of original_start, end

        orgiinal start is not updated while the end continuously moves forward

        """
        intervals.sort()

        curr_start = intervals[0][0]
        curr_end = intervals[0][1]
        result = []
        for i in range(1, len(intervals)):
            if intervals[i][0] > curr_end:
                result.append([curr_start, curr_end])
                curr_start = intervals[i][0]
                curr_end = intervals[i][1]
            else:
                curr_end = max(curr_end, intervals[i][1])

        result.append([curr_start, curr_end])
        return result

        # dont forget to add hte last interval since it wont have an event that triggers it
