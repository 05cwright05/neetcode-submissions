class KthLargest:

    #what if we maintina a min heap of the k biggest
    # in teh example test case it would start with 2,3,3
    #Then  we compare the value we are adding to the root of the min heap
    #since 3 is bigger we pop 2 and add the 3. (then return 3)
    #etc.
    #yeah this is lit
    heap = []
    k = 0

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        nums= sorted(nums)
        if k > len(nums):
            self.heap = nums
        else:
            self.heap = nums[(len(nums)-k):len(nums)]
        heapq.heapify(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heappush(self.heap, val)
            heapq.heappop(self.heap)
        return self.heap[0]
