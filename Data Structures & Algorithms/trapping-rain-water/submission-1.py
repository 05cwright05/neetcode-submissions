class Solution:
    def trap(self, height: List[int]) -> int:
        # array of pos ints heigths
        # each valye represents the height of a bar that has a width of 1
        # find the max area of water that can be trapped between the bars

        # the gernal strat here is at each position we need to know
        # the tallest heights (the greatest integer to my left)
        # and the tallest height to my right

        # i almost want to have a map from value: num_occurences but keep those values in sorted order so
        # if we want to imagine ourself wasting space 


        # at each index it is min(max_left_height, max_right_height) - height[i] 
        max_left_height = 0
        total_volume = 0
        for i in range(0, len(height)):
            max_right_height = 0
            for j in range(i+1, len(height)):
                max_right_height = max(max_right_height, height[j])
            volume_to_add = min(max_left_height, max_right_height) - height[i]
            if volume_to_add > 0:
                total_volume += volume_to_add
            # after exploring
            max_left_height = max(max_left_height, height[i])

        return total_volume