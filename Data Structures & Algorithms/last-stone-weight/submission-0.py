class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """

        Given array of integers stones where stones[i] is the weight of the ith stone

        Simulate:
            - at each step smash the 2 heaviest stones gother 
            - if weight 1 == weight 2 => destroy both
            - if x < y, the stone of weight x is destroyed adn the stone of weight y has new weight y - x

        """

        # we can heapify in O(n) time on average if we do all at once
        import heapq

        heapq.heapify_max(stones)

        while len(stones) > 1:
            biggest_stone = heapq.heappop_max(stones)
            second_biggest_stone = heapq.heappop_max(stones)

            if biggest_stone > second_biggest_stone:
                heapq.heappush_max(stones, biggest_stone - second_biggest_stone)
        
        if not stones:
            return 0
        return stones[0]