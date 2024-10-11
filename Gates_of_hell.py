def door():
    print("You've just entered in the castle!")
    print("Do you take the door on the left or the right?")
    answer = input(("Type left or right and hit 'Enter'.").lower())
    if answer == "left" or answer == "l":
        print("This is the Room of the hell, you just died!")
    elif answer == "right" or answer == "r":
        print("It is the exit, you are lucky!")
    else:
        print("You didn't pick left or right! Try again.")
        door()

door()