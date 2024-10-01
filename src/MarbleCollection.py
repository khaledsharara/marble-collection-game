import random


class Agent:
    def __init__(self, name):
        self.name = name
        self.marbles = []

    def getAction(self, gameState: "MarbleGame"):
        """
        Decide the agent's move depending on the game's state

        :param gameState: The current game state
        """
        if gameState.marbles == 1:
            # The agent has no other choice than to move the last marble
            return 1
        elif gameState.marbles == 2:
            # The agent takes the last marble, winning the game
            return 1
        elif gameState.marbles == 3:
            # The agent takes the last two marble, winning the game
            return 2

        pass


class MarbleGame:
    def __init__(self):
        self.agents: list[Agent] = []
        self.marbles : int = 11

    def play_game(self, agent1: Agent, agent2: Agent):
        """
        Play a game between two agents. The game is played by taking turns between the two
        agents until there are no more marbles left. The game is played by calling the 
        getAction method on each agent in turn. First player is selected at random.

        :param agent1: The first agent
        :param agent2: The second agent
        """

        current_agent = random.choice([agent1, agent2])
        while self.marbles > 0:
            marble = current_agent.getAction(self)
            current_agent = agent1 if current_agent == agent2 else agent2

        pass
