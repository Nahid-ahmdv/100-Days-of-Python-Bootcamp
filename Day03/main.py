print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice = input('You\'re at a cross road. Where do you want to go? LEFT or RIGHT?[type L or R] \n')
if choice.upper() == "L":
    choice = input("You've come to a lake. There is an island in the middle of the lake. Do you want to WAIT for a boat or SWIM across? [type W or S] \n") 
    if choice.upper() == "W":
        choice = input("You arrive at the island unharmed. There is a house with 3 doors. One RED, one YELLOW and one BLUE. Which colour do you choose? [type R or Y or B] \n")
        if choice.upper() == "Y":
            print("You found the treasure! You Win!")
        elif choice.upper() == "R":
            print("It's a room full of fire. Game Over!")
        elif choice.upper() == "B":
            print("You enter a room of beasts. Game Over!")
        else:
            print("You chose a door that doesn't exit! Game Over!")
    else: 
        print("You get attacked by an angry trout. Game Over!")
else:
    print("You fell into a hole. Game Over!")