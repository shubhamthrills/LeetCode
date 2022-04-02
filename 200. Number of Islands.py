'''
✔️ DFS Method

1. An island is surrounded by water(0's)
2. We count things apart of our island if it is horizontal or vertical connected

3. Start at the top left of the 2d array, and visit the first row, and all its columns, trying to find the start of the first island
5. Once we find a 1, we can increment the number of islands, but we want to know where the island ends. 
   So let’s look and follow any of the horizontal or vertical spots near the current position we are on.
6. First, let’s mark the current start/visited parts of the islands as visited by turning them into a 0,
7. Second, explore all the adjacent possibilities,
8. If one of them is a 1, recursively turn it into a 0 and check its children
9. Once we are done, we should have gotten rid of the island that we discovered and can move on to the next island, if it exists in the 2d array
'''

class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '0'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
        
'''
Time Complexity: O(N^2)

# --------- Please UPVOTE the solution if you like the approach ---------

For any help or query related to coding problem reach me at
Linkedin:  https://www.linkedin.com/in/shubhamsagar/
                                            OR
Follow me on github for other leetcode solutions : https://github.com/shubhamthrills/
'''
