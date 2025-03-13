existing_car = input("Is there an existing car? Y/N\n")

if existing_car.upper() == "Y":
    print("What was the timing? \n1 - You were first\n2 - Someone else was first\n3 - You tied")
    timing = int(input(""))
    if timing == 1:
        print("You can go")
    elif timing == 2:
        print("Wait for them to go, then you can go")
    else:
        print("Is anyone crossing traffic?\n1 - You\n2 - Them\n3 - Both of you\n4 - Neither")
        crosser = int(input(""))
        if crosser == 1:
            print("Wait for them to go, then you can go")
        if crosser == 2:
            print("You can go")
        else:
            print("Who is farther to the right?\n1 - You\n2 - Them")
            rightest = int(input(""))
            if rightest == 2:
                print("Wait for them to go, then you can go")
            else:
                print("You can go")
else:
    print("You can go")