class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        buildings = sorted(buildings, key=lambda x: x[2], reverse=True)
        building_groups = [] # [ [Li,Ri], [Li,Ri], right_H ]
        result = []

        for building in buildings:
            group_in = []
            new_group_left = building[1] # set default as right of building
            new_group_right = building[1]
            new_group_right_H = building[2]
            for group in building_groups:
                if (building[1] < group[0]) or (building[0] > group[1]):  # out of group
                    pass
                else:
                    new_group_left = min(group[0], new_group_left)
                    if new_group_right <= group[1]:
                        new_group_right = group[1]
                        new_group_right_H = group[2]
                    group_in.append(group)
                    if building[0] <= group[1] < building[1] and group[2] > building[2] :
                        result.append([group[1], building[2]]) # add cross right

            if not group_in: # create group
                building_groups.append([building[0], building[1], building[2]])
                result.append([building[0], building[2]])
            else: # delete old and add new
                if building[0] < new_group_left:
                    result.append([building[0], building[2]])  # add left corner
                    new_group_left = building[0]
                building_groups = [x for x in building_groups if x not in group_in] # del old
                building_groups.append([new_group_left, new_group_right, new_group_right_H])

        # add group_right_base
        for group in building_groups:
            result.append([group[1], 0])

        # sort
        return sorted(result)
        
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
    

    
    