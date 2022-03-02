import collections
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        dic = {}
        itinerary = []
        tickets.sort()

        for ticket in tickets:
            if ticket[0] in dic:
                dic[ticket[0]].append(ticket[1])
            else:
                dic[ticket[0]] = [ticket[1]]

        print(dic)

        def dfs(depart):
            itinerary.append(depart)
            if not dic[depart]:
                return
            for destination in dic[depart]:
                dic[depart].pop(0)
                dfs(destination)
                return

        dfs('JFK')

        if len(itinerary) == len(tickets) + 1:
            return itinerary
        else:
            return []

class Solution1:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for a, b in sorted(tickets):
            graph[a].append(b)

        route = []
        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop(0))
            route.append(a)

        dfs('JFK')
        return route[::-1]


a = Solution1()
print(a.findItinerary(tickets=
[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
