# Python Solver for Sliding Puzzle

This Python script provides a solver for the classic 8-puzzle problem. The 8-puzzle is a sliding puzzle that consists of a 3x3 grid with eight numbered tiles and one empty tile. The objective is to arrange the tiles in a specific order by sliding them into the empty space.

The solver uses the A* search algorithm with two heuristic functions to find the optimal solution. You can choose between the Manhattan distance heuristic or the misplaced tiles heuristic to guide the search.

## Features

- Solves the 8-puzzle problem using A* search with two heuristic options
- Provides clear and concise code for solving the problem
- Supports user input for the initial state of the puzzle
- Includes test cases for various solvable initial states
- Measures and displays performance metrics, including runtime, nodes expanded, and max queue size

## Getting Started

### Prerequisites

- Python 3.x

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/sliding-puzzle-solver.git

# Navigate to the project directory
cd sliding-puzzle-solver
```

## Usage

Run the script and follow the prompts:

```bash
python puzzle_solver.py
```

You'll be prompted to:
1. Choose the input type: test cases or user input
2. Select the search algorithm (A* with Manhattan distance, A* with misplaced tiles, or Uniform Cost Search)
3. Enter the initial state or choose a test case

### Input Format

If you choose to enter your own puzzle, input the initial state of the puzzle as a flattened 3x3 grid, using 0 to represent the empty space. For example, the following puzzle:

```
1 2 3
4 0 5
6 7 8
```

Would be entered as: `1 2 3 4 0 5 6 7 8`

## Algorithm Details

The solver implements the A* search algorithm with the following heuristics:

1. **Manhattan Distance**: The sum of the horizontal and vertical distances of each tile from its goal position
2. **Misplaced Tiles**: The number of tiles that are not in their goal position
3. **Uniform Cost Search**: No heuristic (equivalent to Dijkstra's algorithm)

## Example Output

```
Selected algorithm: A* with Manhattan Distance
Initial state: 
1 2 3
4 0 5
6 7 8

Solution found!
Number of moves: 4
Path: RIGHT, DOWN, LEFT, UP

Performance metrics:
Runtime: 0.023 seconds
Nodes expanded: 12
Maximum queue size: 18
```

## Contributing

Contributions are welcome and encouraged! If you would like to improve the code, fix issues, or add new features, please follow these guidelines:

1. Fork the repository
2. Create a new branch for your feature or fix: `git checkout -b feature/your-feature-name`
3. Make your changes and commit them: `git commit -m 'Add your feature'`
4. Push your changes to your fork: `git push origin feature/your-feature-name`
5. Create a pull request to the `main` branch of this repository

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project was inspired by the classic 8-puzzle problem in artificial intelligence
- Thanks to all contributors who have helped improve this solver
