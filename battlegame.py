# Nicole Torres
# 12/24/22


# Declare three variables with the following names:
import sys


wizard = "Wizard"
elf = "Elf"
human = "Human"
dragon = "Dragon"


# Declare three variables, set to Integer values that indicate the hp of each character. (hp stands for hitpoints, which means remaining health.)
hp_wizard = 70
hp_elf = 100
hp_human = 150
hp_dragon = 300

# Declare three more variables having Integer values that indicate the damage of each character (how hard they hit).
wizard_damage = 150
elf_damage = 160
human_damage = 20
dragon_damage = 50


# Prompt the player to choose from a list of options.
# Show the player a list of options to choose from, using the print() function. You can use more than one print() function.
print("Players to choose from: ")
print("1." + wizard)
print("2." + elf)
print("3." + human)


# Use the input() function to prompt the user with the String: "Choose your character: ".
# Assign the value returned from the input function to a variable named character.
while True:
    user_character = input("Please choose your character: ")
    if user_character == "1":
        print(
            f"You chose the {wizard} \n Health: {hp_wizard} \n Damage: {wizard_damage}")
        user_character = wizard
        my_hp = hp_wizard
        my_damage = wizard_damage
        # print(user_character) #test
        break
    elif user_character == "2":
        print(
            f"You chose the {elf}\n Health: {hp_elf} \n Damage: {elf_damage}")
        user_character = elf
        my_hp = hp_elf
        my_damage = elf_damage
        # print(user_character)  # test
        break
    elif user_character == "3":
        print(
            f"You chose the {human} \n Health: {hp_human} \n Damage: {human_damage}")
        user_character = human
        my_hp = hp_human
        my_damage = human_damage
        # print(user_character)  # test
        break
    else:
        print("Not a valid character")
        continue


# task 4: Battle with the dragon
while True:
    hp_dragon = hp_dragon - my_damage

    if hp_dragon <= 0:
        print("The Dragon has lost the battle.\n")
        break
    else:
        print(
            f"The {user_character} damaged the dragon \n The dragon's current hp is: {hp_dragon} \n")
    # now dragon's turn to attack
    my_hp = my_hp - dragon_damage

    if my_hp <= 0:
        print(
            f"The {user_character} has lost the battle. \n ")
        break
    print(f"The {user_character}'s Health is now:  {my_hp}\n")
    # else:  # extra credit prompt
    # exit_prompt = input("Do you wish to exit? (Yes or No) :  ")
    # if exit_prompt == "Yes":
    #     sys.exit()``
    # if exit_prompt == "No":
    #     continue
