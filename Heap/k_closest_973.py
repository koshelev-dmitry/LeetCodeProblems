class Solution:
    def kClosest(self, points, K):
        import heapq
        max_heap = []
        for i in range(K):
            square = points[i][0]**2 + points[i][1]**2
            max_heap.append((-square, points[i][0], points[i][1]))
        heapq.heapify(max_heap)
        for point in points[K:]:
            square = point[0]**2 + point[1]**2
            if max_heap[0][0] < -square:
                heapq.heappushpop(max_heap, (-square, point[0], point[1]))
        res = []
        for val in max_heap:
            res.append([val[1], val[2]])
        return res
        