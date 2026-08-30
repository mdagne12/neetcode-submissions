class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Negate the values to create a max heap since python 
        # only has built-in support for a min heap
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            stone1 = -1 * heapq.heappop(max_heap)
            stone2 = -1 * heapq.heappop(max_heap)

            if stone1 != stone2:
                heapq.heappush(max_heap, stone2 - stone1)

        return 0 if len(max_heap) == 0 else -1 * max_heap[0]



            



        