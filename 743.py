# Network Delay Time

# There are N network nodes, labelled 1 to N.

# Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

# Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.

# Example 1:

#     1
# 1 <- - 2
#        | 1
#        ^
# 4 <- - 3
#     1

# Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
# Output: 2

# Note:

# N will be in the range [1, 100].
# K will be in the range [1, N].
# The length of times will be in the range [1, 6000].
# All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100.

# Dijkstra, Time complexity O(N^2+E), space O(N+E)
# limitation: edge weight >= 0
class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        K -= 1
        nodes = collections.defaultdict(list)
        for u, v, w in times:
            nodes[u - 1].append((v - 1, w))
        dist = [float('inf')] * N
        dist[K] = 0
        done = set()
        for _ in range(N):
            smallest = min((d, i) for (i, d) in enumerate(dist) if i not in done)[1]
            for v, w in nodes[smallest]:
                if v not in done and dist[smallest] + w < dist[v]:
                    dist[v] = dist[smallest] + w
            done.add(smallest)
        return -1 if float('inf') in dist else max(dist)

# Floyd-Warshall, Time complexity O(N^3), space O(N^2)
class Solution(object):
    def networkDelayTime(self, times, N, K):
        d = [[float('inf') * N] for _ in range(N)]
        for time in times:
            u, v, w = time[0] - 1, time[1] - 1, time[2]
            d[u][v] = w
        for i in range(N):
            d[i][i] = 0
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])
        return -1 if float('inf') in d[K - 1] else max(d[K -1])

# Bellman-Ford, Time complexity O(N*E), space O(N)
class Solution(object):
    def networkDelayTime(self, times, N, K):
        dist = [float('inf')] * N
        dist[K - 1] = 0
        for i in range(N):
            for time in times:
                u, v, w = time[0] - 1, time[1] - 1, time[2]
                dist[v] = min(dist[v], dist[u] + w)
        return -1 if float('inf') in dist else max(dist)
