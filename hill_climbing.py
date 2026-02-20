import copy 
GOAL_STATE = [ 
[1, 2, 3], 
[4, 5, 6], 
[7, 8, 0] 
] 
# Manhattan Distance Heuristic 
def heuristic(state): 
h = 0 
for i in range(3): 
for j in range(3): 
if state[i][j] != 0: 
for x in range(3): 
return h 
for y in range(3): 
if GOAL_STATE[x][y] == state[i][j]: 
h += abs(i - x) + abs(j - y) 
# Find blank position 
def find_blank(state): 
for i in range(3): 
for j in range(3): 
if state[i][j] == 0: 
return i, j 
# Generate neighboring states 
def get_neighbors(state): 
neighbors = [] 
x, y = find_blank(state) 
directions = [(-1,0), (1,0), (0,-1), (0,1)] 
for dx, dy in directions: 
nx, ny = x + dx, y + dy 
if 0 <= nx < 3 and 0 <= ny < 3: 
new_state = copy.deepcopy(state) 
new_state[x][y], new_state[nx][ny] = 
new_state[nx][ny], new_state[x][y] 
neighbors.append(new_state) 
return neighbors 
# Hill Climbing Algorithm 
def hill_climbing(start): 
current = start 
path = [current] 
while True: 
current_h = heuristic(current) 
neighbors = get_neighbors(current) 
best_neighbor = current 
best_h = current_h 
for neighbor in neighbors: 
h = heuristic(neighbor) 
if h < best_h: 
best_neighbor = neighbor 
best_h = h 
if best_h >= current_h: 
return path 
current = best_neighbor 
path.append(current) 
# Print state 
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
solution = hill_climbing(start_state) 
print("Solution Path:") 
for step in solution: 
print_state(step) 
print("Total Moves:", len(solution) - 1)
