class Solution:
    def merging(self, intervals):
        start = None
        stop = None
        result = []
        endpoints = []
        for interval in intervals:
            endpoints.append((interval[0], True))
            endpoints.append((interval[1], False))
        endpoints.sort(key=lambda x: (x[0], not x[1]))

        intervals_at_endpoint = 0
        for endpoint in endpoints:
            if endpoint[1] == True:
                if intervals_at_endpoint == 0:
                    start = endpoint[0]
                intervals_at_endpoint += 1
            else:
                if intervals_at_endpoint == 1:
                    stop = endpoint[0]
                    result.append((start, stop))
                intervals_at_endpoint -= 1     
        return result


intervals= [[1,10],
            [4,5],
            [9,11],
            [15,18]]
print(Solution().merging(intervals))