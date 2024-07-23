"""Module providing the project entry point."""

from agent import Agent
from environment import Environment
from problem_solving_agent import ProblemSolvingAgent
from rational_agent import RationalAgent

def main():
    """Function called as the project entry point."""

    RationalAgent()

    environment = Environment()
    agent = Agent(ProblemSolvingAgent())

    while True:
        environment()
        agent(environment)

if __name__ == '__main__':
    main()
