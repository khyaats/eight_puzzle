import time
import copy
import heapq

GRID_SIDE_LENGTH = 3 # Change this to 4 to solve 15 puzzle problem

# This function take user input for the difficulty level input and returns the default puzzle state
# TODO: For problem size other than 8 add elif's for more default states
def generate_default_puzzle_state():
    if GRID_SIDE_LENGTH == 3:
        puzzle_states = [
            [[1,2,3],[4,5,6],[7,8,0]],
            [[1,2,3],[4,5,6],[0,7,8]],
            [[1,2,3],[5,0,6],[4,7,8]],
            [[1,3,6],[5,0,2],[4,7,8]],
            [[1,3,6],[5,0,7],[4,8,2]],
            [[1,6,7],[5,0,3],[4,8,2]],
            [[7,1,2],[4,8,5],[6,3,0]],
            [[0,7,2],[4,6,1],[3,5,8]],
        ]
        levelOfDifficulty = int(input("Enter the difficulty level in the range [0-7].\n"))
        if 0 <= levelOfDifficulty <= 7:
            return puzzle_states[levelOfDifficulty]
        else:
            raise Exception("You have entered an Invalid Input!!!") 
    else:
        raise Exception("There was no default puzzle states configured for {}.".format(GRID_SIDE_LENGTH*GRID_SIDE_LENGTH-1))

# This function takes defined puzzle state input from the user 
def get_puzzle_state():
    print("You have selected the option to provide your initial puzzle state.\nUse a zero to represent the blank.")
    print("\nEnter the numbers delimiting with a space.\nPress ENTER after completing a row")
    read_numbers = {}
    puzzle_state = []
    for i in range(GRID_SIDE_LENGTH):
        print("Enter row number {}".format(i+1))
        row = list(map(int, input().split()))

        # Each row is validated
        if len(row) != GRID_SIDE_LENGTH:
            raise Exception("Incorrect row length provided. A row should have length: {}.".format(GRID_SIDE_LENGTH))
        for num in row:
            if not 0 <= num < GRID_SIDE_LENGTH * GRID_SIDE_LENGTH:
                raise Exception("Out of range!!!\nNumbers should be in the range [{}, {}].".format(0, GRID_SIDE_LENGTH * GRID_SIDE_LENGTH - 1))
            if num in read_numbers:
                raise Exception("Number {} alreadir_y entered. Duplicates are not allowed".format(num))
            else:
                read_numbers[num] = True
        puzzle_state.append(row)
    return puzzle_state

# This function which checks whether the state is goal or not
def goal_test(puzzle_state):
    for i in range(GRID_SIDE_LENGTH):
        for j in range(GRID_SIDE_LENGTH):

            # Blank tile represented by zero should be at the last
            if i == GRID_SIDE_LENGTH - 1 and j == GRID_SIDE_LENGTH - 1:
                if puzzle_state[i][j] != 0:
                    return False
            
            # Other numbers should be present at the rest of the place
            else:
                if puzzle_state[i][j] != GRID_SIDE_LENGTH * i + j + 1:
                    return False
    return True

def expand_nodes(puzzle_state):
    # the variable is used to keep track of the increment and decrement of the row and column index
    directions = [  [0, 1],
                    [0, -1],
                    [1, 0],
                    [-1, 0]
                    ]
    
    for i in range(GRID_SIDE_LENGTH):
        for j in range(GRID_SIDE_LENGTH):
            if puzzle_state[i][j] == 0:
                empty_space_in_x = i
                empty_space_in_y = j
    
    all_expanded_nodes = []
    for dir_x, dir_y in directions:
        x = empty_space_in_x + dir_x
        y = empty_space_in_y + dir_y
        if 0 <= x < GRID_SIDE_LENGTH and 0 <= y < GRID_SIDE_LENGTH:
            # For each move, deep copy the state and exchange blank with the corresponding tile
            node = copy.deepcopy(puzzle_state)
            node[empty_space_in_x][empty_space_in_y], node[x][y] = node[x][y], node[empty_space_in_x][empty_space_in_y]
            all_expanded_nodes.append(node)
    return all_expanded_nodes

# This function converts a state to tuple so that we can easily check if it is visited or not
def node_to_tuple(node):
    arr = []
    for row in node:
        # All the numbers are added in the order and converted to a tuple
        arr.extend(row)
    return tuple(arr)

def compute_heuristic_search(node, algorithm):
      
    # Manhattan Heuristic
    if algorithm == 3:
        h = 0
        for i in range(GRID_SIDE_LENGTH):
            for j in range(GRID_SIDE_LENGTH):
                if node[i][j] != 0: # Not checking for the blank

                    # Computing the position of the tile in the goal state
                    goal_state_i = (node[i][j] - 1) // GRID_SIDE_LENGTH
                    goal_state_j = (node[i][j] - 1) % GRID_SIDE_LENGTH

                    # Incrementing the heuristic by the difference in indices
                    h += abs(goal_state_i - i)
                    h += abs(goal_state_j - j)
        return h
    
    # Misplaced Heuristic
    if algorithm == 2:
        h = 0
        for i in range(GRID_SIDE_LENGTH):
            for j in range(GRID_SIDE_LENGTH):
                if i != GRID_SIDE_LENGTH - 1 or j != GRID_SIDE_LENGTH - 1: # Not checking for the last position
                    if node[i][j] != i * GRID_SIDE_LENGTH + j + 1: # If the position does not have the corresponding tile
                        h += 1
        return h
    
    else:
        return 0

# This function prints the intermediate nodes
def print_intermediate_node(node):
    for i in range(GRID_SIDE_LENGTH):
        print("[", ", ".join(map(str, node[i])), "]")

# This is the Main Search Function
def main_search(inital_state, algorithm):
    
    all_nodes = [] # Empty queue is initialized
    visited_nodes = set() # To track the visited nodes
    nodes_expanded = 0 # To track the number of nodes expanded
    max_queue_size = 0 # To track the maximum queue size
    time_start = time.time() # Algorithm start time
    h = compute_heuristic_search(inital_state, algorithm) # Compute heuristic for the initial state
    heapq.heappush(all_nodes, (h, 0, inital_state)) # Push the initial state onto the queue
    while len(all_nodes): # Until the queue is empty
        max_queue_size = max(max_queue_size, len(all_nodes)) # Check the queue size
        f, g, node = heapq.heappop(all_nodes) # Pop f(n), g(n) and the node having least f(n) from the queue
        if goal_test(node): # Check if the node is goal node or not
            # Print all the results
            print("Success! Goal State Found!")
            elapsed_time = time.time() - time_start
            print("Solution Depth: {}".format(g))
            print("Running Time: {0:.2f} ms".format(elapsed_time*1000))
            print("Nodes Expanded: {}".format(nodes_expanded))
            print("Max Queue Size: {}".format(max_queue_size))
            return node
        
        node_tuple = node_to_tuple(node)
        # Expand the node if it not visited
        if node_tuple not in visited_nodes:
            nodes_expanded += 1 # Increment the count tracking the number of nodes expanded
            visited_nodes.add(node_tuple) # Add it to visited
            # Print the current node. Comment the next 3 lines if you dont need lengthy intermediate nodes
            print("The best state to expand with a g(n) = {} and h(n) = {} is ...".format(g, f-g))
            print_intermediate_node(node)
            print()

            # Expand the nodes
            all_expanded_nodes = expand_nodes(node)
            for expanded_node in all_expanded_nodes:
                if node_to_tuple(expanded_node) not in visited_nodes:
                    h = compute_heuristic_search(expanded_node, algorithm) # Computing the heuristics
                    heapq.heappush(all_nodes, (h + g + 1, g + 1, expanded_node)) # Pushing it to the queue
    
    # Print the results when the solution is not found
    print("Failure!")
    elapsed_time = time.time() - time_start
    print("Running Time: {0:.2f} ms".format(elapsed_time*1000))
    print("Nodes Expanded: {}".format(nodes_expanded))
    print("Max Queue Size: {}".format(max_queue_size))
        
def main():
    try:
        puzzle_mode = input("Welcome to my {}-Puzzle Solver.\nType '1' to input your own puzzle, or '2' to select a default puzzle based on difficulty (0-7).\n".format(GRID_SIDE_LENGTH * GRID_SIDE_LENGTH - 1))
        if puzzle_mode == '1':
            puzzle_state = get_puzzle_state()
        elif puzzle_mode == '2':
            puzzle_state = generate_default_puzzle_state()
        else:
            print("Invalid Input!")
            return

        print("\nChoose an algorithm to run:")
        print("1 - Uniform Cost Search")
        print("2 - A* with the misplaced tile heuristic")
        print("3 - A* with the Manhattan distance heuristic")

        algo_choice = input("Enter 1, 2, or 3: ")

        if algo_choice not in ['1', '2', '3']:
            print("Invalid algorithm choice!")
            return

        algo_choice = int(algo_choice)
        algo_names = {
            1: "Uniform Cost Search",
            2: "A* with the misplaced tile heuristic",
            3: "A* with the Manhattan distance heuristic"
        }

        print(f"\nRunning {algo_names[algo_choice]}...\n")
        main_search(puzzle_state, algo_choice)
            
    except Exception as e:
        print(e)
        return
    
if __name__ == "__main__":
    main()
