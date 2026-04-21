
def start_adventure():
    gamer_tag = input("Please enter your username\n[")
    print(f"Welcome,{gamer_tag}")
    print("How many teammates do you bring:")
    print("1.One teammate/with a decent loudout")
    print("2.Two teammates/with free kits")
    print("3.Solo/Great kit")
    choice = input(">")
    if choice == "1":
        one_teammate()
    elif choice =="2":
        two_teammate()
    elif choice =="3":
        solo()
    else:
        print("Invalid please put valid number.")
        start_adventure
def one_teammate():
    print("Now we must choose a map:")
    print("1.Dam/Closed security")
    print("2.Buried city/Bird city")
    print("3.Stella montis/Night raid")
    choice = input(">")
    if choice == "1":
        dam()
    elif choice =="2":
        buried_city()
    elif choice =="3":
        stella_montis()
    else:
        print("Invalid please put valid number.")
        one_teammate
def two_teammate():
    print("Now we must choose a map:")
    print("1.Dam/Closed security")
    print("2.Buried city/Bird city")
    print("3.Stella montis/Night raid")
    choice = input(">")
    if choice == "1":
        dam()
    elif choice =="2":
        buried_city()
    elif choice =="3":
        stella_montis()
    else:
        print("Invalid please put valid number.")
        two_teammate
def solo():
    print("Now we must choose a map:")
    print("1.Dam/Closed security")
    print("2.Buried city/Bird city")
    print("3.Stella montis/Night raid")
    choice = input(">")
    if choice == "1":
        dam()
    elif choice =="2":
        buried_city()
    elif choice =="3":
        stella_montis()
    else:
        print("Invalid please put valid number.")
        solo
def dam():
    print("So you have chosen Dam/Closed security with")
def buried_city():
    print("So you have choosen Buried city/Bird city")
def stella_montis():
    print("So you have choosen Stella montis/Night raid")
start_adventure()