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
