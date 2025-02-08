def misplaced_tiles(state, goal, n):
    #sum up number of 1.misplaced 2.non-empty tiles
    count = 0
    for s, g in zip(state, goal):
        if s == 0:
            continue
        if s != g:
            count += 1
    return count

def manhattan_distance(state, goal, n):
    #sum of all non-empty tile's sum of hori and verti distance to their goal tile
    distance = 0
    for i in range(len(state)):
        tile = state[i]
        if tile == 0:
            continue #skip blank tiles
        goal_pos = goal.index(tile) #find pos of target tile in goal state 
        current_row = i // n
        current_col = i % n
        goal_row = goal_pos // n
        goal_col = goal_pos % n
        distance += abs(current_row - goal_row) + abs(current_col - goal_col)
    return distance