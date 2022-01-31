from typing import List


class Solution:
    def dfs(self, grid, i, j):
        if i < 0 or i > len(grid) or \
                j < 0 or j > len(grid[0]) or \
                grid[i][j] != 1:
            return

        grid[i][j] = 0

        self.dfs(grid, i, j + 1)  # 동
        self.dfs(grid, i, j - 1)  # 서
        self.dfs(grid, i + 1, j)  # 남
        self.dfs(grid, i - 1, j)  # 북

    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.dfs(grid, i, j)
                    cnt += 1

        return cnt
