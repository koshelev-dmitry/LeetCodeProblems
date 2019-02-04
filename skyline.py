class Solution:
    def getSkyline(self, buildings):
        priority, ans = [], [] 
        i, side = 0, 0
        while i < len(buildings) or priority:
            # checks to see if nothing is on the heap (just starting), then checks bounds, 
            # then checks if next building has a left-side that is <= the right-side of the 
            # top of the heap. 
            if not priority or i < len(buildings) and buildings[i][0] <= -priority[0][1]:
                side = buildings[i][0]
                # checks to see if there are multiple buildings with same start-point
                while i < len(buildings) and buildings[i][0] == side:
                    # pushes height, right-side tuple to heap (which will sort by height)
                    heapq.heappush(priority, (-buildings[i][2], -buildings[i][1]))
                    i += 1
            else:
                side = -priority[0][1]
                while priority and -priority[0][1] <= side:
                    heapq.heappop(priority)
            height = 0
            # checks heap for height, if nothing on heap, you are at the end, height = 0
            if priority:
                height = -priority[0][0]
            # checks if height is the same as the current height
            if not ans or height != ans[-1][1]:
                ans.append([side, height])
        return ans
        
    # def _getSkyline(self, buildings):
        # My first solution of the problem
    #     from collections import defaultdict
    #     endpoints = defaultdict(list)
    #     for l,r,h in buildings:
    #         endpoints[l].append((1,h))
    #         endpoints[r].append((0,h))

    #     result = []
    #     height = [0]
    #     curent_height = 0
    #     for x in sorted(endpoints.keys()):
    #         # at each x we have at least one point
    #         # calculate how many start we have
    #         start_heights = [i[1] for i in endpoints[x] if i[0] == 1]
    #         end_heights = [i[1] for i in endpoints[x] if i[0] == 0]
            
    #         # remove all end points from height list 
    #         if end_heights:
    #             for h in end_heights:
    #                 height.remove(h)
            
    #         # add points to height list
    #         if start_heights:
    #             for h in start_heights:
    #                 height.append(h)
            
    #         # now decide if we write to the result, and what we write
    #         if max(height) != curent_height:
    #             curent_height = max(height)
    #             result.append((x, curent_height))

    #     return result


    
test = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
# test = [[0,5,10],[1,5,15],[2,5,12]]
print(Solution().getSkyline(test))
    

    
    