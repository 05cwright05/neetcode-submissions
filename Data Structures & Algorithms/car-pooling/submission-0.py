class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        #general solution is to create a "number line"
        #then go along that line and if a trip is from 1 -5. Mark the 
        # 1st index with a +passengers
        # go to (end index of interval + 1) and mark a -pasenger here
        # then once we have done this  for all n, we can do one pass
        # thru the array and maintain a cummulative total
        # if at any point it exceeds capacity then it will not work

        number_line = [0 for _ in range(0, 1000+1)]

        for trip in trips:
            num_passengers = trip[0]
            start_index = trip[1]
            end_index = trip[2]

            number_line[start_index]+=num_passengers
            number_line[end_index]-=num_passengers

        cum_sum = 0
        for value in number_line:
            cum_sum += value
            if cum_sum > capacity:
                return False
        return True