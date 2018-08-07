# Course Schedule

"""
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. (https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs)
You may assume that there are no duplicate edges in the input prerequisites.

Hints:
This problem is equivalent to finding if a cycle exists in a directed graph. If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera explaining the basic concepts of Topological Sort (https://www.coursera.org/specializations/algorithms).
Topological sort could also be done via BFS.
"""

"""
Kahn's algorithm
https://en.wikipedia.org/wiki/Topological_sorting
Time Limit Exceeded
"""
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        matrix = [[0 for x in range(numCourses)] for y in range(numCourses)]
        for edge in prerequisites:
            matrix[edge[0]][edge[1]] = 1

        s = []
        l = []

        for j in range(numCourses):
            sum_tmp = 0
            for i in range(numCourses):
                sum_tmp += matrix[i][j]
            if sum_tmp == 0:
                s.append(j)

        while len(s):
            n = s.pop()
            l.append(n)

            for j in range(numCourses):
                if j not in l:
                    if matrix[n][j]:
                        matrix[n][j] = 0

                    sum_tmp = 0
                    for i in range(numCourses):
                        sum_tmp += matrix[i][j]
                    if sum_tmp == 0:
                        s.append(j)

        for i in range(numCourses):
            for j in range(numCourses):
                if matrix[i][j]:
                    return False
        return True

"""
BFS
"""
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        ind = [0 for x in range(numCourses)] # number of nodes connect to (->) each node
        m = [[] for x in range(numCourses)] # a list of nodes each node connect to (->)

        for p in prerequisites:
            ind[p[0]] += 1
            m[p[1]].append(p[0])

        st = [] # A list of nodes with no in-coming link
        for i in range(numCourses):
            if ind[i] == 0:
                st.append(i)

        count = 0
        while st:
            tmp = st.pop()
            count += 1
            for i in m[tmp]:
                ind[i] -= 1 # remove the link from node tmp to all its adjacent nodes
                # update st list
                if ind[i] == 0:
                    st.append(i)

        if count < numCourses:
            return False
        return True

"""
DFS
"""
class Solution(object):
    def dfs(self, v, visit, gr):
        if visit[v] == 1:
            return True

        visit[v] = -1 # set status to searching
        for i in gr[v]:
            if visit[i] == -1 or not self.dfs(i, visit, gr):
                # an adjacent node is also in searching (existence of cycle)
                return False
        visit[v] = 1 # set status to done
        return True


    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        visit = [0 for x in range(numCourses)] # status of each node, 0: unvisited; 1: visited; -1: dfs search on-going
        gr = [[] for x in range(numCourses)] # list of nodes each node connect to (->)

        for p in prerequisites:
            gr[p[1]].append(p[0])

        for n in range(numCourses):
            if visit[n] != 1:
                if not self.dfs(n, visit, gr):
                    return False
        return True
