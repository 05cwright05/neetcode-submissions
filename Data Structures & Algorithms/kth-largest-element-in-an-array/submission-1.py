class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        without sorting if i want the kth largetst than i should maintain a min heap of the k largest

        basically each time we see a number we compare to the top of the min heap

        if we are bigger than that number pop off the min and put us in
        also if the heap is not full put us in

        at the end our answer is whatever is the top of that heap

        """
        import heapq

        heap = []

        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            elif num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

        return heap[0]

        


