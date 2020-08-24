while True:
    print("Who are you?")
    name = input()
    if name == "Joe":
        print("Hello Joe. What is the pw? (It is a fish)")
        password = input()
        if password == "swordfish":
            print("Access granted.")
            break
