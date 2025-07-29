class BlockWorld:
    def _init_(self, initial_state, final_goal):
        self.initial_state = initial_state
        self.final_goal = final_goal
    
    def is_goal_state(self, state):
        return state == self.final_goal
    
    def getting_all_moves(self, state):
        moves = []
        for i, stack in enumerate(state):
            if stack:
                picking_up = stack[-1] 
                for j, target_stack in enumerate(state):
                    if i != j:
                        new_state = [list(s) for s in state]
                        new_state[i] = new_state[i][:-1]
                        new_state[j].append(picking_up)
                        moves.append(new_state)
        return moves
    
    def dfs(self):
        stack = [(self.initial_state, [self.initial_state])]
        visited = set()

        while stack:
            current_state, path = stack.pop()

            if self.is_goal_state(current_state):
                return path

            visited.add(tuple(tuple(s) for s in current_state))

            for move in self.getting_all_moves(current_state):
                if tuple(tuple(s) for s in move) not in visited:
                    stack.append((move, path + [move]))

        return None


initial_state = [["A"], ["B", "C"], []]
goal_state = [[], [], ["A", "B", "C"]]

block_world = BlockWorld(initial_state, goal_state)
solution = block_world.dfs()

if solution:
    print("Solution found:")
    for step in solution:
        print(step)
else:
    print("No solution found.")