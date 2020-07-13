"""
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.
"""
from collections import deque
from collections import defaultdict


def courseOrder(numCourses, prerequisites):
    """Return a course schedule according to the prerequisites provided."""
    graph = defaultdict(list)
    indegree = defaultdict(int)
    for course in prerequisites:
        u, v = course[0], course[1]
        graph[v].append(u)
        indegree[u] += 1

    q = deque()
    for node in range(numCourses):
        if node not in indegree:
            q.append(node)

    res = []
    while q:
        node = q.popleft()
        res.append(node)
        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)
                del indegree[nei]
    return res if len(res) == numCourses else []


# Test Cases
courses1 = [[1, 0]]
assert courseOrder(2, courses1) == [0, 1]

courses2 = [[1, 0], [2, 0], [3, 1], [3, 2]]
possibleSchedules = [[0, 1, 2, 3], [0, 2, 1, 3]]
assert courseOrder(4, courses2) in possibleSchedules
