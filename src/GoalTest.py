class StateChess:
    # Define the State class for chess here maybe using it from kostis? 
    pass

class ProblemChess:
    def __init__(self):
        pass

    def goal_test(self, state):
        assert False
        return False

# Usage
problem = ProblemChess()
state = StateChess()

# This will raise an assertion error
problem.goal_test(state)