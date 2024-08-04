"""Module providing the project entry point."""

from agent import Agent
from environment import Environment

PUZZLE_PATH = "puzzles\\12-7-2016-variation-from-the-danish-gambit.txt"

def main():
    """Function called as the project entry point."""

    environment = Environment(PUZZLE_PATH)
    agent = Agent()
    run = True

    while run:
        run = environment()
        
        if run:
            agent(environment)

if __name__ == '__main__':
    main()
