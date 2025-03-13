# 1. Name:
#      Isaac Oliphant
# 2. Assignment Name:
#      Lab 04: Monopoly
# 3. Assignment Description:
#      This assigment finds the cheapest (if possible) method to putting a hotel onto Pennsylvania Ave.  If it is not possible, the program will tell you so.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was figuring out how many if/else statements to use.  I understand that by splitting up the program, I might be doing this slightly different than intended, but I figured that if there was one Master Clause, I could just figure out if that was true or not and put everything else conditional upon it while still allowing multiple paths to reach the desired ending.
# 5. How long did it take for you to complete the assignment?
#      About 5-6 hours

overruled = False
houses_owned = []
property_cost = 0
property_needed_text = ""
pac_text = ""
nc_text = ""
pen_text = ""

penn_owned = input("Do you own Pennsylvania Ave? Y/N\n")
if penn_owned.upper() == "Y":
    property_cost = 0
else:
    purchasable = input("Is Pennsylvania Ave available for your purchase? Y/N\n")
    if purchasable.upper() == "Y":
        property_cost = 320
        property_needed_text = "Pennsylvania Ave (320),"
    else:
        print("You need to own Pennsylvania Ave in order first.")
        overruled = True

all_greens = input("Do you have all three green properties? Y/N\n")
if all_greens.upper() == "Y":
    overruled = False
else:
    print("There is no official way to purchase three properties on one turn and you must own all three green properties.")
    overruled = True
        
if not overruled:     
    houses_owned.append(int(input("What is on Pacific Ave:\n0:zero houses\n1:one house\n2:two houses\n3:three houses\n4:four houses\n5:a hotel\n")))
    houses_owned.append(int(input("What is on North Carolina Ave:\n0:zero houses\n1:one house\n2:two houses\n3:three houses\n4:four houses\n5:a hotel\n")))
    houses_owned.append(int(input("What is on Pennsylvania Ave:\n0:zero houses\n1:one house\n2:two houses\n3:three houses\n4:four houses\n5:a hotel\n")))

    total_houses_needed = 12 - sum(houses_owned)
    pac_houses = 4 - houses_owned[0]
    if pac_houses > 0:
        pac_text = f"{pac_houses} house(s) on Pacific Ave ({pac_houses * 200}),"
    nc_houses = 4 - houses_owned[1]
    if nc_houses > 0:
        nc_text = f"{nc_houses} house(s) on North Carolina Ave ({nc_houses * 200}),"
    pen_houses = 4 - houses_owned[2]
    if pen_houses > 0:
        pen_text = f"{pen_houses} house(s) on Pennsylvania Ave ({pen_houses * 200}),"

    if sum(houses_owned) <= 12:
            bank_account = int(input("How much cash do you have?\n"))
            money_needed = total_houses_needed * 200 + 200 + property_cost
            house_count = int(input("How many houses are available to purchase?"))
            hotel_count = int(input("How many hotels are available to purchase?"))
            if bank_account >= money_needed:    
                
                if hotel_count > 0:
                    if house_count >= total_houses_needed:    
                        print(f"You can build a hotel on Pennsylvania Ave.\nIt will cost ${money_needed}:\n{property_needed_text} {pac_text} {nc_text} {pen_text} 1 hotel on Pennsylvania Ave (200)\nYou will have ${bank_account-money_needed} left.".strip())
                    else:
                        if house_count - 4 >= total_houses_needed:
                            print(f"You can build a hotel on Pennsylvania Ave but you have to build it all at once because there are not enough houses to place on Pennsylvania Ave.\nIt will cost ${money_needed}:\n{property_needed_text} {pac_text} {nc_text} {pen_text} 1 hotel on Pennsylvania Ave (200)\nYou will have ${bank_account-money_needed} left.".strip())
                        else:
                            print("There are not enough houses to build evenly accross your property.  You cannot build a hotel right now.")
                else:
                    print("There are not enough hotels to build a new one right now.")
            else:
                print(f"You do not have enough money; You need ${money_needed-bank_account} to build {pac_houses} house(s) on Pacific Ave, {nc_houses} house(s) on North Carolina Ave, {pen_houses} house() and 1 hotel on Pennsylvania Ave.")
    else:
        cheater_count = houses_owned.count(5)
        if cheater_count == 1:    
            hotel_index = houses_owned.index(5)
            if hotel_index == 0:
                hotel_location = "Pacific Ave"
                print("Move the hotel on Pacific Ave onto Pennsylvania Ave.")
            elif hotel_index == 1:
                hotel_location = "North Carolina Ave"
                print("Move the hotel on North Carolina Ave onto Pennsylvania Ave.")
            else:
                print("You already have a hotel on Pennsylvania Ave!  You can't build another one there!")
        elif cheater_count == 2:
            if houses_owned[2] != 5:
                print("Move the hotel on Pacific Ave or North Carolina Ave over to Pennsylvania.")
            else:
                print("You already have a hotel on Pennsylvania Ave!  You can't build another one there!")
        elif cheater_count == 3:
            print("You already have a hotel on Pennsylvania Ave!  You can't build another one there!")
        else:
            print("Someone is cheating.  Play right.")
else:
    print("You cannot build a hotel right now.")