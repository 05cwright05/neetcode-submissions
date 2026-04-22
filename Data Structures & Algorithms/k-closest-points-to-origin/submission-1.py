class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #Return the k closes points to origin i.e. k smallest
        """

        when we see n smallest we know that we want to maintain a max heap of size n 
        Then if the point we are trying to insert is less than the maximum, pop the maximum and add our value instead

        I dont remmeber the syntax for a max heap tbh but since we are working with distances (all positive)
        We can use a min heap (but negate all values before working with them)

        So now we only insert if our value is greater than the min of the min heap (since a greater negative value is in reality smaller)

        
        """

        heap = []

        #heappush(heap, value)
        #heappop

        def compute_distance(point: List) -> int:
            x = point[0]
            y = point[1]

            return (x  ** 2 + y**2) ** .5

        for point in points:
            dist = compute_distance(point)
            dist *=-1

            if len(heap) < k:
                heapq.heappush(heap, (dist, point))
            elif dist > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap,(dist, point))
        result =[]

        for value in heap:
            result.append(value[1])

        return result

