import heapq

# Goal State
goal = ((1,2,3),
        (4,5,6),
        (7,8,0))

# Manhattan Distance Heuristic
def manhattan(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_x = (value - 1) // 3
                goal_y = (value - 1) % 3
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance

# Find blank position
def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Generate next states
def neighbors(state):
    x, y = find_zero(state)
    moves = [(1,0), (-1,0), (0,1), (0,-1)]
    result = []

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [list(row) for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            result.append(tuple(tuple(row) for row in new_state))
    return result

# Greedy Best First Search
def greedy_best_first(start):
    pq = []
    heapq.heappush(pq, (manhattan(start), start, []))
    visited = set()

    while pq:
        h, state, path = heapq.heappop(pq)

        if state == goal:
            return path + [state]

        if state in visited:
            continue
        visited.add(state)

        for neighbor in neighbors(state):
            heapq.heappush(pq, (manhattan(neighbor),
                                neighbor,
                                path + [state]))
    return None

# Example Start State
start = ((1,2,3),
         (4,0,6),
         (7,5,8))

solution = greedy_best_first(start)

if solution:
    print("Solution found in", len(solution)-1, "moves\n")
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution found")
