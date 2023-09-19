print(
    """
      .-''''''-.
    .'          '.
   /   O      O   /
  :                :
  |                |   
  : ',          ,' :
   \  '-......-'  /
    '.          .'
      '-......-'
"""
)
print("Welcome to my island!")
print("There are two doors in front of you.  🚪 a red door and  🚪 a blue door")
door_choice = input("Which door do you want to open? \n").lower()


# Check user's choice
if door_choice == "red":
    print("Great! now you entred a room.")
    print("You found three boxes: 🎁 white, 🎁 black, 🎁 green")
    box_choice = input("Which box do you open? \n").lower()
    # Check user's choice for the first case
    if box_choice == "white":
        print("Oops! You opned a box filled with snakes 🐍 🐍 🐍")
    elif box_choice == "green":
        print("Congratulations! You found the treasure! 🪙 🪙 🪙")
    elif box_choice == "black":
        print("Oops! You opned a box filled with spiders 🕷️ 🕷️ 🕷️")
    else:
        print("Invalid choice!")
elif door_choice == "blue":
    print("Oops! You choose the corocodile door.")
    print("Game over! 🐊 🐊 🐊")

else:
    print("Invalid choice!")
