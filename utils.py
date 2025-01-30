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
