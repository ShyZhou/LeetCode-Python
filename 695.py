# Max Area of Island

# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

# Example 1:

# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.

# Example 2:
# [[0,0,0,0,0,0,0,0]]
# Given the above grid, return 0.

# Note: The length of each dimension in the given grid does not exceed 50.

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited = set()
        def area(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0]) and (r, c) not in visited and grid[r][c]):
                return 0
            visited.add((r, c))
            return (1 + area(r + 1, c) + area(r - 1, c) + area(r, c + 1) + area(r, c - 1))


        return max(area(r, c)
            for r in range(len(grid))
            for c in range(len(grid[0]))
        )

sol = Solution()
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(sol.maxAreaOfIsland(grid))
