def bfs(maze):
    start = maze.start
    goal = maze.waypoints[0]

    queue = deque([(start, [])])  # (current_position, path_taken)
    visited = set()

    while queue:
        (current, path) = queue.popleft()

        if current in visited:
            continue
        visited.add(current)

        # Goal test
        if current == goal:
            return path + [current]

        # Add neighbors to the queue
        for neighbor in maze.neighbors(*current):
            if neighbor not in visited:
                queue.append((neighbor, path + [current]))

    return None  # No solution found
