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
print("Your Mission is to Find the Treasure.")
choice1 = input("You're at a crossroad, where do you want to go?.\n Type 'left' or 'right'. \n").lower()
if choice1 == "left":
    choice2 = input("You've come to a lake.\n"
                    "In the middle of the lake, there's an island." 
                    "Type 'wait' to wait for a boat and 'swim' to swim across").lower()
    if choice2 == "wait":
        choice3 = input("There're 3 doors in front of you.\n"
                        "Type 'Blue' to go through the blue door, 'Red' to go through the red door and 'Yellow' to go through the yellow door").lower()
        if choice3 == "yellow":
            print("Congratulations! You found the treasure. You win!")
        elif choice3 == "red":
            print("You've been turned into stone by Medusa.\n Game Over")
        elif choice3 == "blue": 
            print("You've entered a burning room.\n Game Over")
        else:
            print("Game Over")
    else:
        print("You got attacked by a crocodile")
else:
    print("You got hit by a bus")                  
        