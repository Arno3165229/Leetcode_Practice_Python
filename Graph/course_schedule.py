class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = {i: [] for i in range(numCourses)}
        for course, pre_course in prerequisites:
            pre_map[course].append(pre_course)

        visited = set()

        def dfs(course):
            if pre_map[course] == []:
                return True
            if course in visited:
                return False
            visited.add(course)
            for pre_course in pre_map[course]:
                if dfs(pre_course) == False:
                    return False
            visited.remove(course)
            pre_map[course] = []
            return True

        for course in range(numCourses):
            if dfs(course) == False: return False
        return True
            
