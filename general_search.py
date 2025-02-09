from utils import get_successors

class Problem:
    def __init__(self, initial_state, goal_state, n, operators):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.n = n
        self.operators = operators

def make_node(state, parent=None, operator=None, depth=0, cost=0):
    return {
        "state": state,
        "parent": parent,
        "operator": operator,
        "depth": depth,
        "cost": cost
    }

def make_queue(node):
    return [node]

def remove_front(queue):
    return queue.pop(0)

def expand(node, operators, n):
    successors = []
    for next_state, operator in get_successors(node['state'], n):
        successors.append(make_node(
            next_state,
            node,
            operator,
            node["depth"] + 1, #UCS only 1 cost
            node["cost"] + 1
        ))
    return successors

def goal_test(state, goal_state):
    return (state == goal_state)

def general_search(problem, queueing_func):
    #init
    nodes = make_queue(make_node(problem.initial_state))
    expanded_nodes = 0
    max_queue_size = 1
    #general search algorithm required by teacher
    while True:
        if not nodes:
            return None #no solution
        node = remove_front(nodes)
        expanded_nodes += 1
        if goal_test(node['state'], problem.goal_state):
            path = []
            current = node
            while current['parent'] is not None:
                path.append(current['operator'])
                current = current['parent']
            path.reverse()
            return {
                "path": path,
                "expanded_nodes": expanded_nodes,
                "max_queue_size": max_queue_size,
                "depth": node['depth']
            }
        nodes = queueing_func(nodes, expand(node, problem.operators, problem.n))
        max_queue_size = max(max_queue_size, len(nodes))

def uniform_cost_search(problem):
    def queueing_func(nodes, successors):
        return sorted(nodes + successors, key=lambda x: x['cost'])
    return general_search(problem, queueing_func)

def a_star_search(problem, heuristic):
    def queueing_func(nodes, successors):
        for successor in successors:
            successor['cost'] += heuristic(successor['state'], problem.goal_state, problem.n)
        return sorted(nodes + successors, key=lambda x: x['cost'])
    return general_search(problem, queueing_func)

def search(initial_state, goal_state, n, heuristic=None):
    problem = Problem(initial_state, goal_state, n, get_successors)
    if heuristic:
        return a_star_search(problem, heuristic)
    else:
        return uniform_cost_search(problem)