# Author: Amin (Mavericane)
# Github Link: https://github.com/mavericane/
# Website Link: https://mavericane.ir
# Description: Hangman game(guessing words with guessing letters) for multi-user playing with computer
# Importing required modules
# random module for selecting random choice
import random

# termcolor module for colorizing outputs
import termcolor


class Hangman_Game:
    player_list = []

    # list of words that the computer can randomly pick for the user to guess
    words = [
        "computer",
        "android",
        "linux",
        "motherboard",
        "object",
        "python",
        "skywalker",
        "love",
        "home",
        "dream",
        "earbuds",
    ]

    def __init__(self):
        self.name = input("Please enter your name: ")
        self.__random_word = random.choice(__class__.words)
        self.__chance_to_guess = 10
        self.__win_state = False
        self.player_list.append(self)
        self.guesses = ""

    def check_answer(self):
        def printer(win_state):
            for char in self.__random_word:
                if char != self.__random_word[-1]:
                    if char in self.guesses:
                        print(termcolor.colored(char, "green"), end="")
                    else:
                        print(termcolor.colored("_", "red"), end="")
                        win_state = False
                else:
                    if char in self.guesses:
                        print(termcolor.colored(char, "green"))
                    else:
                        print(termcolor.colored("_", "red"))
                        win_state = False
            if win_state:
                self.__win_state = True

        if self.has_chance_to_guess():
            win_state = True

            if (
                self.__chance_to_guess == 10
                and len(self.guesses) == 0
                or len(Hangman_Game.player_list) > 1
            ):
                printer(win_state)

            while True:
                guess = input(f"{self.name}, Please guess a character: ")

                if guess in self.guesses:
                    print(termcolor.colored(f"{self.name} try another guess", "yellow"))
                else:
                    break
            self.guesses += guess.lower()

            if guess not in self.__random_word:
                self.__minus_chance_to_guess()
                print(termcolor.colored(f"{self.name} guess is wrong!", "yellow"))
                if self.has_chance_to_guess():
                    print(
                        termcolor.colored(
                            f"{self.name} have {self.__chance_to_guess} more guesses",
                            "yellow",
                        )
                    )
                else:
                    return False
                if len(Hangman_Game.player_list) == 1:
                    printer(win_state)
            else:
                printer(win_state)
        else:
            return False

    def __minus_chance_to_guess(self):
        self.__chance_to_guess -= 1

    def has_chance_to_guess(self):
        if self.__chance_to_guess > 0:
            return True
        return False

    def has_won(self):
        return self.__win_state

    @classmethod
    def game_has_winner(cls):
        if any(player.has_won() is True for player in cls.player_list):
            return True
        return False


class Game_Controller:
    def __init__(self):
        while True:
            if len(Hangman_Game.player_list) >= 1:
                for player in Hangman_Game.player_list:
                    if not player.has_won():
                        if player.check_answer() == False:
                            print(
                                termcolor.colored(
                                    f"{player.name} has ran out of chance to guess",
                                    "red",
                                )
                            )
                            Hangman_Game.player_list.remove(player)
                    if Hangman_Game.game_has_winner():
                        for player in Hangman_Game.player_list:
                            if player.has_won():
                                print(
                                    termcolor.colored(f"{player.name} has won", "green")
                                )
                                exit()
            else:
                print(
                    termcolor.colored("There is no player left in player list", "red")
                )
                print(termcolor.colored("Exiting game...", "red"))
                exit()


if __name__ == "__main__":
    print("Hello welcome to multi user hangman game!")
    print(
        termcolor.colored(
            "Commands: add(for adding user), start(for starting game), exit(for exiting game)",
            "yellow",
            "on_black",
        )
    )
    while True:
        order = input("What do you want to do: ")
        if order == "add":
            Hangman_Game()
        elif order == "start":
            Game_Controller()
        elif order == "exit":
            exit()
