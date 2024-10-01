# import necessary packages
import random
import time
import sys

# setup the game by storing animals in a list and their dietry habits in a dictionary
animal_list = ["dog", "cat", "porcupine", "whale", "rat", "rabbit", "pig"]
animal_food = {"dog":["beef","chicken","rice"], "cat":["mice","eggs","cereal"],
               "porcupine": ["worms","beetles","ants"] , 
               "whale":["prawns", "fish","seals"], 
               "rat":["corn","fruit","biscuits"],
               "rabbit":["carrots","lettuce","nuts"],
               "pig":["potatoes","turnips","cabbage"]}
health_bar = 100 # size of heath bar which is printed to console

# start the game by randomly selecting an animal and a health score
random_animal = random.choice(animal_list)
random_health = random.randint(1,100)

# tell the user what their animal is and ask to name the animal
print(f"Your animal is a {random_animal}. It has a health score of {random_health}")
animal_name = input("Give your animal a name : ")

# keeps asking the user to select a food and adjusts the health score and displays the health bar
while random_health > 0:
    decoy_animal = random.choice(animal_list)
    print(f"{animal_name} is currently fine")
    mixed_list = [item for pair in zip(animal_food[random_animal], animal_food[decoy_animal]) for item in pair]
    chosen_food = input(f"What would you like to feed {animal_name}, choose from {mixed_list}?")
    
    if chosen_food in animal_food[random_animal]:
        random_health += 10
        print(f"{animal_name} enjoyed that. Their score is now {random_health}")
    else:
        random_health -= 10
        print(f"{animal_name} didn't like that. Their score is now {random_health}")

# health bar code
    sys.stdout.write("[%s]" % (" " * health_bar))
    sys.stdout.flush()
    sys.stdout.write("\b" * (health_bar+1)) # return to start of line, after '['
    Health_width = random_health
    for i in range(Health_width):
        time.sleep(0.1) 
        sys.stdout.write("-")
        sys.stdout.flush()
    Sick_width = health_bar-Health_width
    for i in range(Sick_width):
        time.sleep(0.01)
        sys.stdout.write("0")
        sys.stdout.flush()
    sys.stdout.write("]\n") # this ends the health bar
    
# final messgae to game player
print(f"sorry {animal_name} is dead :( ")