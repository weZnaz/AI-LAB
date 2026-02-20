import heapq 
import copy 
# Goal State 
GOAL_STATE = [ 
[1, 2, 3], 
[4, 5, 6], 
[7, 8, 0]   # 0 represents blank 
] 
 
# Manhattan Distance Heuristic 
def heuristic(state): 
    distance = 0 
    for i in range(3): 
        for j in range(3): 
            if state[i][j] != 0: 
                for x in range(3): 
                    for y in range(3): 
                        if GOAL_STATE[x][y] == state[i][j]: 
                            distance += abs(i - x) + abs(j - y) 
    return distance 
 
# Find blank position 
def find_blank(state): 
    for i in range(3): 
        for j in range(3): 
            if state[i][j] == 0: 
                return i, j 
 
# Generate all possible moves 
def get_neighbors(state): 
    neighbors = [] 
    x, y = find_blank(state) 
 
    directions = [(-1,0), (1,0), (0,-1), (0,1)]  # Up, Down, Left, Right 
 
    for dx, dy in directions: 
        nx, ny = x + dx, y + dy 
        if 0 <= nx < 3 and 0 <= ny < 3: 
            new_state = copy.deepcopy(state) 
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], 
new_state[x][y] 
            neighbors.append(new_state) 
 
    return neighbors 
 
# Convert list of lists to tuple (for hashing) 
def to_tuple(state): 
    return tuple(tuple(row) for row in state) 
 
# A* Algorithm 
def a_star(start): 
    open_list = [] 
    heapq.heappush(open_list, (heuristic(start), 0, start, [])) 
    closed_set = set() 
 
    while open_list: 
        f, g, current, path = heapq.heappop(open_list) 
 
        if current == GOAL_STATE: 
            return path + [current] 
 
        closed_set.add(to_tuple(current)) 
 
        for neighbor in get_neighbors(current): 
            if to_tuple(neighbor) not in closed_set: 
                heapq.heappush( 
                    open_list, 
                    (g + 1 + heuristic(neighbor), g + 1, neighbor, path + [current]) 
                ) 
    return None 
 
# Print puzzle state 
def print_state(state): 
    for row in state: 
        print(row) 
    print() 
 
# -------- Main -------- 
start_state = [ 
    [1, 2, 3], 
    [4, 0, 6], 
    [7, 5, 8] 
] 
 
solution = a_star(start_state) 
 
if solution: 
print("Solution Path:") 
for step in solution: 
print_state(step) 
print("Total Moves:", len(solution) - 1) 
else: 
print("No solution found") 
