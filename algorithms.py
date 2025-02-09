import heapq
from utils import get_successors

class PuzzleSolver:
    def __init__(self, initial_state, goal_state, n, heuristic=None):
        self.initial = initial_state
        self.goal = goal_state
        self.n = n
        self.heuristic = heuristic #heuristic of choice
    
    def solve(self):
        #serach then return goal state
        open_heap = []
        visited = {} #for backtracking: record parent of least g(n)
        counter = 0 #for potential tie breaking

        #init
        initial_g = 0
        if self.heuristic is not None:
            #is using a heuristic
            initial_h = self.heuristic(
                 self.initial, 
                 self.goal, 
                 self.n
                )
        else:
            # no heuristic is used, h(n) set to 0
            initial_h = 0
        
        initial_priority = initial_g + initial_h
        #use a min heap to implement a priority queue
        heapq.heappush(open_heap, (initial_priority, counter, self.initial, initial_g))
        visited[self.initial] = (initial_g, None, None) #format: (g, parent, operator)
        counter += 1

        expanded_nodes = 0
        max_queue_size = 1

        while open_heap:
            #pop the current lowest h(n) node
            temp = heapq.heappop(open_heap)
            current_priority = temp[0]
            #skip temp[1], it's unused value
            current_state = temp[2]
            current_g = temp[3]
            expanded_nodes += 1

            #if found goal state already, backtrack:
            if current_state == self.goal:
                path = []
                state = current_state
                while True:
                    entry = visited.get(state)
                    if entry is None:
                        break
                    g, parent, operator = entry #consistent format
                    if operator is not None:
                        path.append(operator)
                    state = parent #go back up one level
                path.reverse() #reverse to correct sequence
                return {
                    "path": path,
                    "expanded_nodes": expanded_nodes,
                    "max_queue_size": max_queue_size,
                    "depth": len(path)
                }
            
            #if not goal yet. generator all sucessors
            successors = get_successors(current_state, self.n)
            for next_state, operator in successors:
                new_g = current_g + 1 #uniform cost of 1

                #if found lower cost path, update:
                if next_state in visited:
                    existing_g, _, _ = visited[next_state] # bad readability
                    if new_g >= existing_g:
                        continue #skip since find a better path
                
                #calculate priority (Uniform Cost=g, A*=g+h)
                if self.heuristic is not None:
                    next_h = self.heuristic(next_state, self.goal, self.n)
                else:
                    next_h = 0
                new_priority = new_g + next_h

                #add to the peiority queue
                heapq.heappush(open_heap, (new_priority, counter, next_state, new_g))
                counter += 1
                visited[next_state] = (new_g, current_state, operator) # consistent formatting
                max_queue_size = max(max_queue_size, len(open_heap))

        return None #no solution found

def search(initial_state, goal_state, n, heuristic=None):
    #abstracted method for solve()
    solver = PuzzleSolver(initial_state, goal_state, n, heuristic)
    return solver.solve()
          
