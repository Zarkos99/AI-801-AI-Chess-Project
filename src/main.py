"""Module providing the project entry point."""

from agent import Agent
from environment import Environment
from problem_solving_agent import ProblemSolvingAgent
from rational_agent import RationalAgent

def main():
    """Function called as the project entry point."""

    #RationalAgent(ProblemSolvingAgent())

    environment = Environment()
    agent = Agent(ProblemSolvingAgent())

    run = True
    while run:
        run = environment()
        #agent(environment)

if __name__ == '__main__':
    main()
