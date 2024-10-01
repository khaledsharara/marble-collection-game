import random


class Agent:
    def __init__(self, name: str):
        self.name = name
        self.marbles = []

    def getAction(self, gameState: "MarbleGame"):
        """
        Decide the agent's move depending on the game's state

        :param gameState: The current game state
        """
        marbles_left: int = gameState.marbles

        if marbles_left == 1:
            # The agent has no other choice than to take the last marble
            return 1
        elif marbles_left == 2:
            # The agent takes the two marble, winning the game
            return 2
        else:
            # The agent takes a random number of marbles
            return random.randint(1, 2)


class MarbleGame:
    def __init__(self):
        self.agents: list[Agent] = []
        self.marbles: int = 11

    def play_game(self, agent1: Agent, agent2: Agent):
        """
        Play a game between two agents. The game is played by taking turns between the two
        agents until there are no more marbles left. The game is played by calling the
        getAction method on each agent in turn. First to  First player is selected at random.

        :param agent1: The first agent
        :param agent2: The second agent
        """

        current_agent: Agent = random.choice([agent1, agent2])
        while self.marbles > 0:
            marble_to_take = current_agent.getAction(self)
            self.marbles -= marble_to_take
            print(
                f"{current_agent.name} took {marble_to_take} marbles. {self.marbles} marbles left"
            )
            if self.marbles == 0:
                print(f"{current_agent.name} won!")
            else:
                current_agent = agent1 if current_agent == agent2 else agent2


def main():
    """
    Game Premise:
    Start with 11 marbles on the table.
    Two players take turns.
    On each turn, a player can take 1 or 2 marbles.
    The player who takes the last marble wins the game.

    Objective:
    The goal is to take the last marble and win.
    """
    while True:
        agent1 = Agent("Khaled")
        agent2 = Agent("Abdelrahman")
        game = MarbleGame()
        game.play_game(agent1, agent2)

        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != "y":
            break


if __name__ == "__main__":
    main()
