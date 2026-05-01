import time
import random

# Function to print a message and pause
def print_pause(message, delay=2):
    print(message)
    time.sleep(delay)

# Function for the second floor
def second_floor(score, bag):
    while not score > 3:
        print_pause("You climb the stairs slowly, "
                    "hearing creaking under your feet.")
        print_pause("At the top, you find two doors.")
        print_pause("One room has a soft singing sound coming from it.")
        print_pause("The other has a chilling, scary sound.")
        print_pause("Enter 'a' to enter the soft singing room.")
        print_pause("Enter 'b' to enter the scary room.")

        choice = input()
        while choice not in ("a", "b"):
            print_pause("Please enter the correct answer: 'a' or 'b'")
            choice = input()

        if choice == "a":
            print_pause("You entered the room and saw a peaceful ghost "
                        "singing to herself.")
            print_pause("She tells you a riddle. Solve it to win a weapon.")

            puzzles = [
                {"Riddle": "Something that gets bigger the more you take "
                           "from it, what is it?", "Answer": "hole"},
                {"Riddle": "It has a face but no tongue. It tells people the time.",
                 "Answer": "clock"},
                {"Riddle": "What walks and stands but has no legs?",
                 "Answer": "clock"},
                {"Riddle": "What doesn't get cold if you put it in the refrigerator?",
                 "Answer": "hot pepper"},
                {"Riddle": "It has leaves but isn't a tree. It has skin but "
                           "isn't an animal. It has knowledge but isn't a "
                           "human. What is it?", "Answer": "book"},
                {"Riddle": "Where is the sea that has no water?",
                 "Answer": "map"}
            ]

            puzzle = random.choice(puzzles)
            print_pause(f"Riddle: {puzzle['Riddle']}")
            answer = input("Your answer: ")

            if answer.lower() == puzzle['Answer']:
                print_pause("Correct! You get a magical sword that can "
                            "harm the ghost.")
                bag.append("sword")
            else:
                print_pause("Wrong answer.")

            print_pause(f"Your current score is: {score}")

        else:
            print_pause("You entered the scary room... find a monster.")
            print_pause("You look around to find a flame and a sword.")
            print_pause("What will you use?")
            print_pause("Enter 'a' for the flame. Enter 'b' for the sword.")
            choice = input()

            while choice not in ("a", "b"):
                print_pause("Please enter the correct answer: 'a' or 'b'")
                choice = input()

            if choice == "a":
                print_pause("The monster is afraid of fire, you defeated him.")
                score += 2
                if score >= 3:
                    score, bag = mysterious_box(score, bag)
                    return score, bag
            elif choice == "b":
                print_pause("The monster managed to break the sword, "
                            "but unfortunately you lost.")
                score -= 1

        if score >= 3:
            score, bag = mysterious_box(score, bag)

    return score, bag

# Function for the small door path
def small_door(score, bag):
    while not score > 3:
        print_pause("You find a dark tunnel with a dim light inside.")
        print_pause("At the end, you find a magic wand.")
        bag.append("wand")
        score += 2
        print_pause("You gained 2 points.")
        print_pause(f"Your current score is: {score}")

        if score >= 5:
            score, bag = mysterious_box(score, bag)

        return score, bag

# Mysterious box puzzle
def mysterious_box(score, bag):
    while not score > 5:
        reward_points = {
            "healing spell": 3,
            "invisibility cloak": 2,
            "nothing": 0
        }
        rewards = list(reward_points.keys())
        reward_item = random.choice(rewards)

        print_pause("You see a mysterious box that only opens if you "
                    "solve a puzzle.")
        print_pause("What is born black, lives red, and dies white?")

        answer = input("Your answer: ").lower()
        if answer in ("coal", "charcoal"):
            print_pause("Correct! The box opens.")
            print_pause(f"You received: {reward_item.title()}")
            if reward_item != "nothing":
                bag.append(reward_item)
                score += reward_points[reward_item]
        else:
            print_pause("Wrong answer. Try again later.")
            score -= 2

        print_pause(f"Your updated score: {score}")
        if score >= 5:
            score, bag = blood_sucker(score, bag)
        return score, bag

# Vampire challenge
def blood_sucker(score, bag):
    while not score > 3:
        print_pause("Bats appear from everywhere and a vampire appears "
                    "among them.")
        print_pause("He starts attacking you.")
        print_pause("You look around to find garlic and a glow stick. "
                    "Which one will you use?")
        print_pause("Enter 'a' for glow stick, 'b' for garlic.")
        choice = input()
        while choice not in ("a", "b"):
            print_pause("Please enter the correct answer: 'a' or 'b'")
            choice = input()

        if choice == "a":
            print_pause("The stick was a trap.")
            print_pause("You lost.")
            score -= 2
        elif choice == "b":
            print_pause("He is afraid of garlic. You defeated him.")
            score += 3

        if score >= 5:
            score, bag = start_game(score, bag)

    return score, bag

# Main game loop
def play_game():
    score = 3
    bag = []

    print_pause("You wake up to find yourself in a huge castle.")
    print_pause("A book nearby says a ghost haunts this place.")
    print_pause("Enter 'a' to go upstairs, 'b' to go through the small door.")

    while True:
        choice = input("Your choice (a/b): ")
        if choice == "a":
            score, bag = second_floor(score, bag)
        elif choice == "b":
            score, bag = small_door(score, bag)
        else:
            print_pause("Invalid input. Try again.")
            continue

        print_pause(f"Current bag: {bag}")
        print_pause(f"Current score: {score}")

        if bag and score >=5:
            print_pause("Use the sword and expel the ghost effectively.!")
            print_pause("Congratulations, you won the game.!")
            break
        else:
            print_pause("You didn't have the sword or you didn't have enough points..")
            print_pause("You failed to exorcise the ghost and you lost the game..")
            break

# A loop that allows you to restart the game from the beginning.
def start_game(score=None, bag=None):
    bag = []
    while True:
        play_game()
        print_pause("Do you want to play again?")
        print_pause("Enter 'a' for yes, 'b' for no.")
        choice = input("Your choice (a/b): ")
        while choice not in ("a", "b"):
            print_pause("Please enter the correct answer: 'a' or 'b'")
            choice = input()
        if choice.lower() != "a":
            print("Goodbye!")
            break
        else:
            print_pause("Have a nice time!")

# Start the game
start_game()