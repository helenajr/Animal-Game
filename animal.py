import random
import time
import sys


health_bar = 100
animal_list = ["dog", "cat", "porcupine", "whale", "rat", "rabbit", "pig"]
food_list = []
porcupine_prefernces = {"animal":"porcupine",
                        "food":["mouse", "grains", "chips"],
                        "activities": ["swimming", "knitting"]}
animal_food = {"dog":["beef","chicken","rice"], "cat":["mice","eggs","cereal"],
               "porcupine": ["worms","beetles","ants"] , 
               "whale":["prawns", "fish","seals"], 
               "rat":["corn","fruit","biscuits"],
               "rabbit":["carrots","lettuce","nuts"],
               "pig":["potatoes","turnips","cabbage"]}
random_animal = random.choice(animal_list)

random_health = random.randint(1,100)
print(f"Your animal is a {random_animal}. It has a health score of {random_health}")

animal_name = input("Give your animal a name : ")

while random_health > 0:
    decoy_animal = random.choice(animal_list)
    print(f"Your animal is currently fine")
    mixed_list = [item for pair in zip(animal_food[random_animal], animal_food[decoy_animal]) for item in pair]
    chosen_food = input(f"What would you like to feed your {animal_name}, choose from {mixed_list}?")
    #chosen_food = input(f"What would you like to feed your {animal_name}, choose from {animal_food[random_animal]} {animal_food[decoy_animal]}?")
    if chosen_food in animal_food[random_animal]:
        random_health += 10
        print(f"your pet enjoyed that score is now {random_health}")
    else:
        random_health -= 10
        print(f"your pet didn't like that {random_health}")

    sys.stdout.write("[%s]" % (" " * health_bar))
    sys.stdout.flush()
    sys.stdout.write("\b" * (health_bar+1)) # return to start of line, after '['
    Health_width = random_health
    for i in range(Health_width):
        time.sleep(0.1) # do real work here
        # update the bar
        sys.stdout.write("-")
        sys.stdout.flush()
    Sick_width = health_bar-Health_width
    for i in range(Sick_width):
        time.sleep(0.01) # do real work here
        # update the bar
        sys.stdout.write("0")
        sys.stdout.flush()
    sys.stdout.write("]\n") # this ends the health bar
    
random_health -= 1

print(f"sorry your {random_animal} needs attention")