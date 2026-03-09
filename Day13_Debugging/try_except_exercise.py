
while True:
    try:
        age = int(input("How old are you?"))
        if age > 18:
            print(f"You can drive at age {age}.")
            break
    except ValueError:
        print("You have typed in a an invalid number. Please try again with numerical numbers.")
