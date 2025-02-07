import heapq
import math

def heuristic_manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def heuristic_euclidean(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def astar_single(maze, heuristic=heuristic_manhattan):
    start = maze.start
    goal = maze.waypoints[0]

    priority_queue = []
    heapq.heappush(priority_queue, (0, start, []))  # (f_score, current_position, path)
    cost_so_far = {start: 0}

    while priority_queue:
        _, current, path = heapq.heappop(priority_queue)

        # Goal test
        if current == goal:
            return path + [current]

        for neighbor in maze.neighbors(*current):
            new_cost = cost_so_far[current] + 1  # Each move has a cost of 1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal)
                heapq.heappush(priority_queue, (priority, neighbor, path + [current]))

    return None  # No solution found
