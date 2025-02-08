from heuristics import misplaced_tiles, manhattan_distance

def test_heuristic(name, heuristic_func, state, goal, n, expected):
    result = heuristic_func(state, goal, n)
    print(f"\n testing {name}:")
    print(f"state: {state}")
    print(f"goal: {goal}")
    print(f"result: {result}, expect: {expected}")
    assert result == expected, f"test failed"
    print("test sucess")

if __name__ == "__main__":
    # 3 by 3 test cases
    goal_3x3 = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    state_solved = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    state_misplaced = (1, 2, 3, 4, 5, 6, 0, 7, 8) #misplaced 7, 8
    state_manhattan = (1, 2, 3, 4, 5, 6, 7, 0, 8) #misplaced 8 with one move upwards

    #misplaced tiles testing
    test_heuristic("misplace_solved", misplaced_tiles, state_solved, goal_3x3, 3, 0)
    test_heuristic("mispace_problem", misplaced_tiles, state_misplaced, goal_3x3, 3, 2)

    #manhattan distance testing
    test_heuristic("manhattan_solved", manhattan_distance, state_solved, goal_3x3, 3, 0)
    test_heuristic("manhattan_problem", manhattan_distance, state_manhattan, goal_3x3, 3, 1)

