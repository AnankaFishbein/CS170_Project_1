from utils import parse_input

def test_parse_input(input_str, expected_n=None, expected_error=False):
    try:
        state, n = parse_input(input_str)
        print("\ntest input: ", input_str)
        print("result: ", state)
        print("puzzle size: n = ", n)
        if expected_n:
            assert n == expected_n, f"expecting n={expected_n}, getting n={n}"
        print("test sucess")
    except Exception as e:
        if expected_error:
            print(f"test sucessful (captured error: {str(e)}) ")
        else:
            print(f"test failed: {str(e)}")

if __name__ == "__main__":
    #vaild test cases
    test_parse_input("1 2 3 4 5 6 7 8 0", expected_n=3)#standred 3 by 3 case
    test_parse_input("1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 0", expected_n=4)#standred 4 by 4 case

    #invaild test cases
    test_parse_input("1 2 3 4 5", expected_error=True) # num of numbers not squared number
    test_parse_input("1 2 3 4 5 6 7 8 8", expected_error=True) # repetition of 8 and lack of 0
    test_parse_input("1 2 3 4 5 6 7 8 9", expected_error=True) #lack of 0
    test_parse_input("1 2 a 4 5 6 7 8 0", expected_error=True) #non-integer input
