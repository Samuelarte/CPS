from collections import deque

def dfs(maze):
    start = maze.start
    goal = maze.waypoints[0]

    stack = [(start, [])]  # (current_position, path_taken)
    visited = set()

    while stack:
        (current, path) = stack.pop()

        if current in visited:
            continue
        visited.add(current)

        # Goal test
        if current == goal:
            return path + [current]

        # Add neighbors to the stack
        for neighbor in maze.neighbors(*current):
            if neighbor not in visited:
                stack.append((neighbor, path + [current]))

    return None  # No solution found
