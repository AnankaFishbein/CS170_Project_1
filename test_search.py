from algorithms import search
from heuristics import manhattan_distance, misplaced_tiles
from utils import generate_goal_state

def test_algorithm(name, initial_state, n, expected_depth):
    goal = generate_goal_state(n)
    print(f"======= Testing {name} ======")
    print(f"Initial State: {initial_state}")
    print(f"Goal State: {goal}")

    print(f"\n testing Uniform Cost Search")
    result_ucs = search(initial_state, goal, n)
    print_result("UCS", result_ucs, expected_depth)

    print(f"\n testing A* with Misplaced Tiles")
    result_misplaced = search(initial_state, goal, n, misplaced_tiles)
    print_result("A* Misplaced", result_misplaced, expected_depth)

    print(f"\n testing A* with Manhattan Distance")
    result_manhattan = search(initial_state, goal, n, manhattan_distance)
    print_result("A* Manhattan", result_manhattan, expected_depth)

def print_result(algo_name, result, expected_depth):
    if result:
        print(f"{algo_name} found solution with depth {result['depth']}")
        print(f"Expanded Nodes: {result['expanded_nodes']}")
        print(f"Max Queue Size: {result['max_queue_size']}")
        print(f"Actual path length: {len(result['path'])}, Expected path length: {expected_depth}")
        print(f"Path: {result['path']}")
        assert len(result['path']) == expected_depth, "Path length is not correct"
    else:
        print(f"{algo_name} did not find solution")
    
if __name__ == "__main__":
    # 3 by 3 test cases
    goal_3x3 = generate_goal_state(3)
    test_cases = [
        {
            "name": "case_solved",
            "initial_state": goal_3x3,
            "n": 3,
            "expected_depth": 0
        },
        {
            "name": "case_simple(steps=1)",
            "initial_state": (1, 2, 3, 4, 5, 6, 7, 0, 8),
            "n": 3,
            "expected_depth": 1
        },
        {
            "name": "case_classic(steps=8)",
            "initial_state": (1, 0, 3, 4, 2, 5, 7, 8, 6),
            "n": 3,
            "expected_depth": 3
        },
        {
            "name": "case_hard(steps=6)",
            "initial_state": (1, 2, 3, 4, 5, 0, 6, 7, 8),
            "n": 3,
            "expected_depth": 13
        }
    ]

    for case in test_cases:
        test_algorithm(case["name"], case["initial_state"], case["n"], case["expected_depth"])
