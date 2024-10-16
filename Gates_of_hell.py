def door():
    print("The castle is collapsing, ruuun!")
    print("ops There are two doors, Do you take the door on the left or the right?")
    answer = input(("Type left or right and hit 'Enter'.").lower())
    if answer == "left" or answer == "l":
        print("This is the Room of the dragon!!!!, you just died!  :( ")
    elif answer == "right" or answer == "r":
        print("Great, but almost done, there another two door!")
        answer = input(("Type left or right and hit 'Enter'.").lower())
        if answer == "left" or answer == "l":
            print("It is the exit, you are lucky!")
        elif answer == "right" or answer == "r":
            print("Oh noo, the giant two headed dog, you died!!! :( ")
        else:
            print("Too slow, you die!!!! ")
    else:
        print("You didn't pick left or right! Try again.")
        door()

door()