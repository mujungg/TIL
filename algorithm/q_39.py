from typing import List
import collections


# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         for i in range(0,len(prerequisites)):
#             for j in range(i, len(prerequisites)):
#                 if (prerequisites[i][0] == prerequisites[j][1]) and (prerequisites[i][1] == prerequisites[j][0]):
#                     return False
#
#
#         taken = []
#         graph = {}
#
#         for i in range(numCourses):
#             graph[i] = []
#         for i in prerequisites:
#             graph[i[0]].append(i[1])
#
#         print(graph)
#
#         def dfs(n):
#             print(f'dfs({n})')
#             if graph[n]:
#                 for i in graph[n]:
#                     dfs(i)
#
#             if n in taken:
#                 return
#             else:
#                 taken.append(n)
#                 print(f'taken={taken}')
#                 return
#
#         for i in graph:
#             dfs(i)
#
#         return len(taken) == numCourses
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)

        traced = set()

        def dfs(i):
            if i in traced:
                return False

            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False

            return True

        for x in list(graph):
            if not dfs(x):
                return False

        return True





numCourse = 3
prerequisites = [[1,0],[0,2],[2,1]]

a = Solution1()
print(a.canFinish(numCourse, prerequisites))
