def parse_input(input_str):
    #take 1-d array as input, transform input into n by n puzzle
    #return puzzle size n
    numbers = list(map(int, input_str.split()))
    n_squared = len(numbers)
    n = int(n_squared ** 0.5)
    if n * n != n_squared:
        #???
        raise ValueError("Invalid Input: number of inputs must match n squared")
    sorted_numbers = sorted(numbers)#???
    expected = list(range(n_squared))
    if sorted_numbers != expected:
        raise ValueError("Invalid Input: must include all numbers from 0 to n^2-1")
    return tuple(numbers), n #???

def generate_goal_state(n):
    #target goal state 
    goal = list(range(1, n*n)) + [0]
    return tuple(goal)

def is_solvable(state, goal_state, n):
    #detect if given test case is solvable
    #for now is always true
    return True #temp

def get_successors(state, n):
    #generate all possible successors based on given state
    zero_pos = state.index(0) #find where blank tile is
    row = zero_pos // n #current row
    col = zero_pos % n #current column

    moves = []
    #set boundries on where blank tile could move
    if row > 0:
        moves.append(('Up', -n)) #blank move up, aka tile above blank move down
    if row < n-1:
        moves.append(('Down', n)) #blank move down
    if col > 0:
        moves.append(('Left', -1)) #blank move left
    if col < n-1:
        moves.append(('Right', 1)) #blank move right
    
    successors = []
    for direction, delta in moves:
        #calculate new position
        new_pos = zero_pos + delta
        #generate new state
        new_state = list(state)
        new_state[zero_pos], new_state[new_pos] = new_state[new_pos], new_state[zero_pos]
        successors.append((tuple(new_state), direction))#store as new state

    return successors
