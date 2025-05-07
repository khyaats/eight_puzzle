import time
import copy
import heapq

GRID_SIDE_LENGTH = 3 # Change this to 4 to solve 15 puzzle problem

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
