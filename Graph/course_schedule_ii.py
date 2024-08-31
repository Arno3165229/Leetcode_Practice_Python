## Compare to LC 207 Course Schedule
## We cannot use the same logic to assgin the premap value as 0. Since it will directly return and do not append to the list.
## However, if we append to the list, it might casue the output value duplicated in list.
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap = {i:[] for i in range(numCourses)}
        for course, precourse in prerequisites:
            premap[course].append(precourse)

        cycle = set()
        ## need visited set in case recursive goes again and causes the output value duplicated in list
        visited = set()
        output = []

        def dfs(course):
            if course in visited:
                return True
            if course in cycle:
                return False

            cycle.add(course)
            for c in premap[course]:
                if not dfs(c):
                    return False
            cycle.remove(course)
            visited.add(course)
            output.append(course)
            return True ## still need to return here, if no return, in Pyton 'None' will be considered as False

        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return output

