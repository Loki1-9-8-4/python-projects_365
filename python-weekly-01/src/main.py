import random # download library

target_number = random.randint(1, 100) # create a varibale and give them the a random integer between 1 and 100

while True: # Start a loop (start until we break it)
    try:
        user_input = int(input("Guess my number between 1 and 100: ")) # ask the user for input and convert to integer

    except ValueError: # catch error! Example, user give text instead of a Number.
        print("Invalid Input! Please enter a whole Number.") # inform the user about the mistake!
        continue # Stop THIS loop iteration immediately and jump 

    if not 1 <= user_input <= 100:
        print("Number must be between 1 and 100! ")
        continue
    if user_input > target_number:
        print("Too high! ")
    elif user_input < target_number:
        print("Too low!")
    else:
        print("Correct")
        break