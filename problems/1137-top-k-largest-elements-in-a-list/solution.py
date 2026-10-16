import heapq
def top_three_largest(values):
    # values: list of numbers
    # return the three largest values in descending order
    heap = []
    for val in values:

        heapq.heappush(heap, val)

        if len(heap) > 3:
            heapq.heappop(heap)

    heap.sort(reverse = True)

    return heap
