class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid == []:
            return 0

        size_x = len(grid[0])
        size_y = len(grid)
        visited = [[False for _ in range(size_x)] for _ in range(size_y)]
        x = 0
        y = 0
        queue = []
        islands = 0
        
        #while not all([all(x) for x in visited]):
        for x, y in [(x,y) for x in range(size_x) for y in range(size_y)]:
            if grid[y][x]=='1' and not visited[y][x]:
                queue.append([x, y])
                visited[y][x] = True
                while len(queue) != 0:
                    # check up
                    if y>0 and not visited[y-1][x] and grid[y-1][x]!='0':
                        queue.append([x, y-1])
                        visited[y-1][x] = True

                    # check down
                    if y<size_y-1 and not visited[y+1][x] and grid[y+1][x]!='0':
                        queue.append([x, y+1])
                        visited[y+1][x] = True

                    # check right
                    if x<size_x-1 and not visited[y][x+1] and grid[y][x+1]!='0':
                        queue.append([x+1, y])
                        visited[y][x+1] = True

                    # check left
                    if x>0 and not visited[y][x-1] and grid[y][x-1]!='0':
                        queue.append([x-1, y])
                        visited[y][x-1] = True

                    queue = queue[1:]
                    if len(queue)!=0:
                        x = queue[0][0]
                        y = queue[0][1]
                islands += 1   
            visited[y][x] = True
        return islands
        
        

solution = Solution()
grid = [["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]]
print(solution.numIslands(grid))