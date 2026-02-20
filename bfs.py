# copy is used to create deep copies of 2D lists
import copy


# Function to find the position of blank tile (0)
def find_zero(board):
    # Loop through rows
    for i in range(3):
        # Loop through columns
        for j in range(3):
            # If blank tile is found
            if board[i][j] == 0:
                # Return its row and column
                return i, j


# Function to generate all possible next states
def get_next_states(board):
    # List to store new boards
    states = []

    # Find blank tile position
    x, y = find_zero(board)

    # Possible movement directions: down, up, right, left
    moves = [(1,0), (-1,0), (0,1), (0,-1)]

    # Try each movement
    for dx, dy in moves:
        # New row and column after move
        nx, ny = x + dx, y + dy

        # Check if new position is inside the board
        if 0 <= nx < 3 and 0 <= ny < 3:
            # Create a deep copy of board (to avoid changing original)
            new_board = copy.deepcopy(board)

            # Swap blank tile with adjacent tile
            new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]

            # Add new board to list
            states.append(new_board)

    # Return all possible next states
    return states


# DFS function to solve 8-puzzle
def dfs(start, goal, max_depth=20):
    # Stack is used for DFS (LIFO)
    stack = []

    # Set to store visited states
    visited = set()

    # Push start state with depth 0
    stack.append((start, 0))

    # Mark start state as visited
    visited.add(tuple(map(tuple, start)))

    # Continue until stack is empty
    while stack:
        # Pop last inserted state (DFS behavior)
        board, depth = stack.pop()

        # If current state is goal
        if board == goal:
            # Print depth (not guaranteed minimum)
            print("Solved in", depth, "moves (DFS)")
            return

        # Limit depth to avoid infinite loop
        if depth >= max_depth:
            continue

        # Generate next possible states
        for next_board in get_next_states(board):
            # Convert board to tuple (hashable)
            key = tuple(map(tuple, next_board))

            # If state is not visited
            if key not in visited:
                # Mark state as visited
                visited.add(key)

                # Push state to stack with increased depth
                stack.append((next_board, depth + 1))

    # If solution not found
    print("No solution found within depth limit")


# Initial state
start = [
    [1, 2, 3],
    [4, 0, 5],
    [6, 7, 8]
]

# Goal state
goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Call DFS function
dfs(start, goal)
