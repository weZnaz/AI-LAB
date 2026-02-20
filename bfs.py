# deque is used for BFS queue (fast pop from front)
from collections import deque

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


# BFS function to solve 8-puzzle
def bfs(start, goal):
    # Create queue for BFS
    queue = deque()

    # Set to store visited states
    visited = set()

    # Add start state with depth 0
    queue.append((start, 0))

    # Convert 2D list to tuple so it can be stored in set
    visited.add(tuple(map(tuple, start)))

    # Continue until queue is empty
    while queue:
        # Remove front element from queue
        board, depth = queue.popleft()

        # If current state is goal state
        if board == goal:
            # Print minimum moves
            print("Solved in", depth, "moves")
            return

        # Generate all next possible states
        for next_board in get_next_states(board):
            # Convert board to tuple (hashable)
            key = tuple(map(tuple, next_board))

            # If state is not visited before
            if key not in visited:
                # Mark state as visited
                visited.add(key)

                # Add state to queue with increased depth
                queue.append((next_board, depth + 1))

    # If goal is not reachable
    print("No solution found")


# Initial state of 8-puzzle
start = [
    [1, 2, 3],
    [4, 0, 5],
    [6, 7, 8]
]

# Goal state of 8-puzzle
goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Call BFS function
bfs(start, goal)
