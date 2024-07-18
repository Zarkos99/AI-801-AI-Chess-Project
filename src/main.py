"""Module providing the project entry point."""

from agent import Agent
from environment import Environment
#from rational_agent import RationalAgent

def main():
    """Function called as the project entry point."""

    environment = Environment()
    agent = Agent() #RationalAgent()

    while True:
        environment()
        agent(environment)

    print("Hello World")

if __name__ == '__main__':
    main()
