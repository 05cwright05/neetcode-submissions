class Solution:
    def trap(self, height: List[int]) -> int:
        # array of pos ints heigths
        # each valye represents the height of a bar that has a width of 1
        # find the max area of water that can be trapped between the bars

        # the gernal strat here is at each position we need to know
        # the tallest heights (the greatest integer to my left)
        # and the tallest height to my right

       # suffix sum array so 
       # so we iterate backward 

        suffix_sum = [0 for _ in range(0, len(height))]
        max_value = 0
        for j in range(len(height) -1, -1, -1):
            max_value = max(max_value, height[j])
            suffix_sum[j] = max_value



        # at each index it is min(max_left_height, max_right_height) - height[i] 
        max_left_height = 0
        total_volume = 0
        for i in range(0, len(height)):
            volume_to_add = min(max_left_height, suffix_sum[i]) - height[i]
            if volume_to_add > 0:
                total_volume += volume_to_add
            # after exploring
            max_left_height = max(max_left_height, height[i])

        return total_volume