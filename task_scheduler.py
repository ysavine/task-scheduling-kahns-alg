from collections import deque
from typing import List


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # Initialize variables
        t = [0] * (n + 1)  # Holds the time taken for each task
        indegrees = [0] * (n + 1)  # Holds the number of incomplete dependencies for each task
        graph = [[] for _ in range(n + 1)]  # Represents the graph of tasks and their dependencies
        
        # Populate graph of dependencies and count the number of tasks that need to be completed before each task
        for edge in relations:
            node1, node2 = edge
            graph[node1].append(node2)
            indegrees[node2] += 1
        
        # Perform topological sort, looking for initial tasks that have no incomplete incoming dependencies
        q = deque()
        for i in range(1, n + 1):
            if indegrees[i] == 0:
                q.append(i)
                t[i] = time[i - 1]
        
        while q:
            top = q.popleft() # Take the top task from the queue
            print(top) # Print the task that is started
            topTime = t[top] # Get the time taken to complete the top task
            for depend_tasks in graph[top]: # Iterate through the tasks that depend on the top task
                t[depend_tasks] = max(t[depend_tasks], topTime + time[depend_tasks - 1]) # Update the time taken to complete the dependent task choosing the longest path
                indegrees[depend_tasks] -= 1 # Reduce the number of incomplete dependencies for the dependent tasks
                if indegrees[depend_tasks] == 0: # If all dependencies are completed, add the task to the queue
                    q.append(depend_tasks)
        
        # Return the maximum time taken to complete all tasks
        return max(t)
n = 9
time = [1.5, 4, 1, 1.25, 2, 2.5, 1, 2, 1.5]

# Define the dependencies between tasks
relations = [
    [1, 2], # read chapter 3 of textbook for Computer Architecture -> complete caching HW
    [1, 3], # read chapter 3 of textbook for Computer Architecture -> take a practice midterm
    [4, 5], # attend Psych 101 lecture -> write a blog post for Psych 101
    [6, 7], # do a literature review for History 112 essay -> outline the essay for History 112
    [6, 8], # do a literature review for History 112 essay -> write the essay for History 112
    [7, 8], # outline the essay for History 112 -> write the essay for History 112
    [5, 9], # write a blog post for Psych 101 -> go to the Writing Studio
    [8, 9]  # write the essay for History 112 -> go to the Writing Studio
]

solution = Solution()
result = solution.minimumTime(n, relations, time)

# Print the minimum time required to complete all tasks
print("You will complete all your tasks in", result, "hours!")