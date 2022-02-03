from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]):
        def dfs(i, j):
            # 해당 인덱스가 땅이 아닌 경우 종료.
            if i < 0 or j >= len(grid) or \
                    j < 0 or j >= len(grid[0]) or \
                    grid[i][j] != '1':
                return
            # 해당 위치가 육지인 경우 탐색 완료 표시 후 동서남북 검사
            grid[i][j] = 0

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                dfs(i, j)
                # 재귀 탈출하면 섬 하나 탐색한 것이므로 count++
                count += 1

        return count

# class Solution:
#     def dfs(self, grid, i, j):
#         if i < 0 or i > len(grid) or \
#                 j < 0 or j > len(grid[0]) or \
#                 grid[i][j] != 1:
#             return
#
#         grid[i][j] = 0
#
#         self.dfs(grid, i, j + 1)  # 동
#         self.dfs(grid, i, j - 1)  # 서
#         self.dfs(grid, i + 1, j)  # 남
#         self.dfs(grid, i - 1, j)  # 북
#
#     def numIslands(self, grid: List[List[str]]) -> int:
#         cnt = 0
#
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == 1:
#                     self.dfs(grid, i, j)
#                     cnt += 1
#
#         return cnt
