import random as rm
import time as tm
import sys

# Setup game constants
animal_list = ("dog", "cat", "porcupine", "whale", "rat", "rabbit", "pig", "horse", "lion", "bat", "ibex", "penguin")
animal_food = {
    "dog": ("beef", "chicken", "rice"),
    "cat": ("mice", "eggs", "cereal"),
    "porcupine": ("worms", "beetles", "ants"),
    "whale": ("prawns", "fish", "seals"),
    "rat": ("corn", "fruit", "biscuits"),
    "rabbit": ("carrots", "lettuce", "nuts"),
    "pig": ("potatoes", "turnips", "cabbage"),
    "horse": ("hay", "sugar cubes", "vegetables"),
    "lion": ("deer", "buffalo", "zebra"),
    "penguin": ("kfc", "subway", "dominos"),
    "ibex": ("grass", "flowers", "herbs"),
    "bat": ("beetles", "beef", "cereal"),
    "seal": ("krills", "fish", "penguin")
}
animal_gender = ("girl", "boy")
HEALTH_BAR = 100
animal_images = {
    "dog": "🐕", "cat": "🐈", "porcupine": "🦔", "whale": "🐋", "rat": "🐀", "rabbit": "🐇", 
    "pig": "🐷", "horse": "🐎", "lion": "🦁", "penguin": "🐧", "ibex": "🐐", "bat": "🦇", "seal": "🦭"
}
available_foods = set()
count, rounds = 0, 0

# Functions
def death(animal_name: str) -> None:
    print(f"sorry {animal_name} is dead :( ")

def health_bar_code(random_health: int) -> None:
    sys.stdout.write("[%s]" % (" " * HEALTH_BAR))
    sys.stdout.flush()
    sys.stdout.write("\b" * (HEALTH_BAR + 1))
    
    # Display health bar
    for i in range(random_health):
        tm.sleep(0.1)
        sys.stdout.write("-")
        sys.stdout.flush()

    for i in range(HEALTH_BAR - random_health):
        tm.sleep(0.01)
        sys.stdout.write("0")
        sys.stdout.flush()

    sys.stdout.write("]\n")

def get_game_mode() -> int:
    while True:
        try:
            game_mode = int(input("Would you like to play infinite mode or limited mode? Type 1 for infinite and 2 for limited! "))
            if game_mode in {1, 2}:
                return game_mode
            print("Choose between 1 or 2\n")
        except ValueError:
            print("Invalid input, please choose 1 or 2.")

def update_available_foods(random_animal: str) -> None:
    global available_foods
    available_foods.update(food for animal, foods in animal_food.items() if animal != random_animal for food in foods)

def feed_animal(animal_name: str, random_animal: str, decoy_animal: str, random_health: int) -> int:
    mixed_list = set(animal_food[random_animal]).union(animal_food[decoy_animal])
    chosen_food = input(f"What would you like to feed {animal_name}, choose from {sorted(mixed_list)}? ").lower().replace(" ", "")
    
    if chosen_food not in mixed_list and chosen_food in available_foods:
        print(f"Sorry, {chosen_food} wasn't in the options!")
        random_health -= 5
    elif chosen_food in animal_food[random_animal]:
        random_health += 10
        print(f"{animal_name} enjoyed that. Their score is now {random_health}")
    elif chosen_food in animal_food[decoy_animal]:
        random_health -= 10
        print(f"{animal_name} didn't like that. Their score is now {random_health}")
    else:
        random_health -= 10 if rm.randint(1, 3) >= 2 else 20
        print(f"While trying to give {chosen_food} to {animal_name}, your animal got food poisoning :( Their score is now {random_health}")
    
    return random_health

def main() -> None:
    global count, rounds

    game_mode = get_game_mode()

    # Start the game by randomly selecting an animal, a health score and a gender
    random_animal = rm.choice(animal_list)
    random_health = rm.randint(1, 100)
    random_gender = rm.choice(animal_gender)

    print(f"Your animal is a {random_gender} {random_animal} {animal_images[random_animal]}. It has a health score of {random_health}")
    animal_name = input("Give your animal a name: ")

    update_available_foods(random_animal)

    while random_health > 0:
        if (game_mode == 2 and rounds >= 100) or (game_mode == 2 and random_health >= 300):
            print("100 rounds have passed or 300 health has been reached, limited gamemode doesn't allow more gaming!")
            break

        rounds += 1
        decoy_animal = rm.choice([animal for animal in animal_list if animal != random_animal])
        print(f"{animal_name} {animal_images[random_animal]} is currently fine")

        random_health = feed_animal(animal_name, random_animal, decoy_animal, random_health)
        health_bar_code(random_health)

        if random_health <= 0:
            death(animal_name)
            break
        
        # Handle invalid inputs
        if random_health <= 0 or count >= 5:
            print(f"Stop being a pain! Choose from the given options")
            count = 0
            continue

if __name__ == "__main__":
    main()
