from utils import get_successors

def print_successors(state, n):
    print("\ntesting: ", state)
    successors = get_successors(state, n)
    for s, d in successors:
        print(f"direction: {d}, new state: {s}")

if __name__ == "__main__":
    #3 by 3 test case
    state_center = (1, 2, 3, 4, 0, 5, 6, 7, 8) #blank tile in center
    state_corner = (0, 1, 2, 3, 4, 5, 6, 7, 8) #blank tile in upper-left corner
    state_edge = (1, 2, 3, 0, 4, 5, 6, 7, 8) #blank tile in left edge

    print("===== testing 3 by 3 cases =====")
    print_successors(state_center, 3)
    print_successors(state_corner, 3)
    print_successors(state_edge, 3)

    #4 by 4 cases
    state_FourByFour = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 15)
    print("===== testing 4 by 4 cases =====")
    print_successors(state_FourByFour, 4)