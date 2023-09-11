# Author: Amin (Mavericane)
# Github Link: https://github.com/mavericane/
# Website Link: https://mavericane.ir
# Description: This file fetches jokes from JokeAPI(English), OneAPI(Persian), API_Ninjas(English)
# Note: You need to register on OneAPI and API_Ninjas website and receive an API Key to send a request for a joke
# Importing required modules
# requests module for fetching web contents into the program
import requests

# termcolor module for colorizing outputs
import termcolor

# abc module for using abstraction in classes
from abc import ABC, abstractmethod


# Defining main Joke class
class Joke(ABC):
    @abstractmethod
    def get_random_joke(self):
        pass


# Defining JokeAPI class
class JokeAPI(Joke):
    def __init__(self, **kwargs):
        self.type = kwargs.get("type")

    def get_random_joke(self):
        try:
            params = {"type": self.type}
            result = requests.get(
                "https://v2.jokeapi.dev/joke/Any", params=params, timeout=10
            )
        except:
            return termcolor.colored(
                f"An error occurred while sending web request to JokeAPI", "red"
            )
        result = result.json()
        if result["error"]:
            return termcolor.colored(
                f"An error occurred while receiving the joke!", "red"
            )
        if result["type"] == "single":
            return result["joke"]
        elif result["type"] == "twopart":
            return f"{result['setup']}\n{result['delivery']}"


# Defining OneAPI class
class OneAPI(Joke):
    def __init__(self, **kwargs):
        self.token = kwargs.get("token")

    def get_random_joke(self):
        try:
            params = {"token": self.token}
            result = requests.get("https://one-api.ir/joke/", params=params, timeout=10)
        except:
            return termcolor.colored(
                f"An error occurred while sending web request to OneAPI", "red"
            )
        result = result.json()
        if result["status"] == 200:
            return result["result"]
        elif result["status"] == 401:
            return termcolor.colored("Your API key is not valid!", "red", "on_black")
        else:
            return termcolor.colored(
                f"An error occurred while receiving the joke! Error code: {result['status']}",
                "red",
            )


# Defining API_Ninjas class
class API_Ninjas(Joke):
    def __init__(self, **kwargs):
        self.token = kwargs.get("token")

    def get_random_joke(self):
        try:
            headers = {"X-Api-Key": self.token}
            result = requests.get(
                "https://api.api-ninjas.com/v1/jokes", headers=headers, timeout=10
            )
        except:
            return termcolor.colored(
                f"An error occurred while sending web request to API_Ninjas", "red"
            )
        result = result.json()
        if "error" in result:
            return termcolor.colored(f"{result['error']}", "red")
        else:
            return result[0]["joke"]


# Asking if the user wants to receive a joke from JokeAPI
while True:
    user_input = input("Do you want to receive a joke from JokeAPI? (Y yes, N no): ")
    if user_input.casefold() == "yes" or user_input.casefold() == "y":
        while True:
            user_input = input(
                "What type of joke do you want to receive 1.Single 2.Twopart? (Type number or name): "
            )
            if user_input.casefold() == "single" or user_input.casefold() == "1":
                joke_type = "single"
            elif user_input.casefold() == "twopart" or user_input.casefold() == "2":
                joke_type = "twopart"
            else:
                print(termcolor.colored("Entered option is not valid!", "red"))
                continue
            break
        jokeapi_obj = JokeAPI(type=joke_type)
        print(jokeapi_obj.get_random_joke(), "\n")
    elif user_input.casefold() == "no" or user_input.casefold() == "n":
        pass
    else:
        print(termcolor.colored("Entered option is not valid!", "red"))
        continue
    break

# Asking if the user wants to receive a joke from OneAPI
while True:
    user_input = input("Do you want to receive a joke from OneAPI? (Y yes, N no): ")
    if user_input.casefold() == "yes" or user_input.casefold() == "y":
        api_key = input("Please enter your API key that you recieved from OneAPI: ")
        oneapi_obj = OneAPI(token=api_key)
        print(oneapi_obj.get_random_joke(), "\n")
    elif user_input.casefold() == "no" or user_input.casefold() == "n":
        pass
    else:
        print(termcolor.colored("Entered option is not valid!", "red"))
        continue
    break

# Asking if the user wants to receive a joke from API_Ninjas
while True:
    user_input = input("Do you want to receive a joke from API_Ninjas? (Y yes, N no): ")
    if user_input.casefold() == "yes" or user_input.casefold() == "y":
        api_key = input("Please enter your API key that you recieved from API_Ninjas: ")
        API_Ninjas_obj = API_Ninjas(token=api_key)
        print(API_Ninjas_obj.get_random_joke())
    elif user_input.casefold() == "no" or user_input.casefold() == "n":
        pass
    else:
        print(termcolor.colored("Entered option is not valid!", "red"))
        continue
    break
