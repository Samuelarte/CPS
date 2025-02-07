# submitted.py
# ---------------
# Licensing Information:
# This HW is inspired by previous work by University of Illinois at Urbana-Champaign


"""
This is the main entry point for MP5. You should only modify code
within this file -- the unrevised staff files will be used for all other
files and classes when code is run, so be careful to not modify anything else.
"""
# submitted should return the path.
# The path should be a list of tuples in the form (row, col) that correspond
# to the positions of the path taken by your search algorithm.
# maze is a Maze object based on the maze from the file specified by input filename
# searchMethod is the search method specified by --method flag (bfs,dfs,astar,astar_multi)

from collections import deque
import heapq

# =====================
# Breadth-First Search
# =====================
def bfs(maze):
    """
    Breadth-First Search (BFS) for solving the maze.
    Uses a queue (FIFO) to explore the shortest path first.
    """
    start = maze.start
    goal = maze.waypoints[0]

    queue = deque([(start, [start])])  # (current_position, path_taken)
    visited = set()

    while queue:
        current, path = queue.popleft()

        if current in visited:
            continue
        visited.add(current)

        # Goal test
        if current == goal:
            return path  # Return the solution path

        # Explore neighbors
        for neighbor in maze.neighbors(*current):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return []  # No solution found


# =====================
# Depth-First Search
# =====================
def dfs(maze):
    """
    Depth-First Search (DFS) for solving the maze.
    Uses a stack (LIFO) to explore deeper paths first.
    """
    start = maze.start
    goal = maze.waypoints[0]

    stack = [(start, [start])]  # (current_position, path_taken)
    visited = set()

    while stack:
        current, path = stack.pop()

        if current in visited:
            continue
        visited.add(current)

        # Goal test
        if current == goal:
            return path  # Return the solution path

        # Explore neighbors
        for neighbor in maze.neighbors(*current):
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))

    return []  # No solution found


# =====================
# A* Search Algorithm
# =====================
def heuristic(a, b):
    """
    Manhattan Distance heuristic function.
    Used to estimate the cost from node 'a' to goal 'b'.
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar_single(maze):
    """
    A* Search Algorithm for solving the maze.
    Uses a priority queue to explore the most promising paths first.
    """
    start = maze.start
    goal = maze.waypoints[0]

    pq = [(0, start, [start])]  # (priority, node, path)
    visited = set()
    g_costs = {start: 0}  # Dictionary to track the actual cost from start

    while pq:
        _, current, path = heapq.heappop(pq)

        if current in visited:
            continue
        visited.add(current)

        # Goal test
        if current == goal:
            return path  # Return the solution path

        # Explore neighbors
        for neighbor in maze.neighbors(*current):
            new_cost = g_costs[current] + 1  # All moves cost 1

            if neighbor not in g_costs or new_cost < g_costs[neighbor]:
                g_costs[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal)
                heapq.heappush(pq, (priority, neighbor, path + [neighbor]))

    return []  # No solution found
