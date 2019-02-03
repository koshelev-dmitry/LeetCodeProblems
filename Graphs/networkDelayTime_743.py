class Solution:
    def networkDelayTime(self, times, N, K):
        """
        My first ever code on solving Graphs
        """
        graph_tree = {} # {node:(neigboors, time)}
        for edge in times:
            if edge[0] in graph_tree:
                graph_tree[edge[0]].append((edge[1], edge[2])) # neighboors
            else:
                graph_tree[edge[0]] = [(edge[1], edge[2])]
        # print("Starting graph tree:")
        # for key, value in graph_tree.items():
        #     print('key:', key)
        #     for val in value:
        #         print('      ->',val) 
        # print('')

        visited = {K:0} # {node:shortest_time_to_get_here}
        lvl = []
        nodes_in_lvl = [K]
        
        current_time = 0
        max_time = 0

        while nodes_in_lvl:
            # print(f"\ncurrent level contains {nodes_in_lvl}")
            next_nodes = []
            for node in nodes_in_lvl:
                # print(f"from node {node}")
                current_time = visited[node]
                if node in graph_tree: # check if this node has childrens
                    neighboors_of_current_node = graph_tree[node] #neighbors nodes
                    for neighboor in neighboors_of_current_node:
                        # neighboor node
                        # print(f"visit {neighboor[0]}")
                        if neighboor[0] in visited: # then update the time to get here
                            if visited[neighboor[0]] > current_time + neighboor[1]: # if we are faster  
                                # print(f"visit {neighboor[0]}, time is updated from {visited[neighboor[0]]} to {current_time + neighboor[1]}")
                                visited[neighboor[0]] = current_time + neighboor[1]
                                next_nodes.append(neighboor[0])
                        else: # if not visited
                            visited[neighboor[0]] = current_time + neighboor[1]
                            max_time = max(max_time, current_time + neighboor[1])
                            next_nodes.append(neighboor[0])
            nodes_in_lvl = next_nodes
        
        if len(visited) == N:
            return visited[max(visited, key=visited.get)]
        else:
            return -1

    def leetCode_solution(self, times, N, K):
        


# times = [[2,1,1],[2,3,1],[3,4,1]]
times = [[1,2,1],[2,3,2],[1,3,4]]
N = 3
K = 1
# print(Solution().networkDelayTime(times, N, k))