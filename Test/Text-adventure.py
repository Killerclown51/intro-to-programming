import random
def start_adventure():
    gamer_tag = input("Please enter your username\n[")
    print(f"Welcome,{gamer_tag}")
    print("How many teammates do you bring:")
    print("1.One teammate/with a decent loudout")
    print("2.Two teammates/with free kits")
    print("3.Solo/Great kit")
    choice = input(">")
    if choice == "1":
        one_teammate(gamer_tag)
    elif choice =="2":
        two_teammate(gamer_tag)
    elif choice =="3":
        solo(gamer_tag)
    else:
        print("Invalid please put valid number.")
        start_adventure()
def one_teammate(gamer_tag):
    print("Now we must choose a map:")
    print("1.Dam/Closed security")
    print("2.Buried city/Bird city")
    print("3.Stella montis/Night raid")
    choice = input(">")
    if choice == "1":
        dam1(gamer_tag)
    elif choice =="2":
        buried_city1(gamer_tag)
    elif choice =="3":
        stella_montis1(gamer_tag)
    else:
        print("Invalid please put valid number.")
        one_teammate(gamer_tag)
def two_teammate(gamer_tag):
    print("Now we must choose a map:")
    print("1.Dam/Closed security")
    print("2.Buried city/Bird city")
    print("3.Stella montis/Night raid")
    choice = input(">")
    if choice == "1":
        dam2(gamer_tag)
    elif choice =="2":
        buried_city2(gamer_tag)
    elif choice =="3":
        stella_montis2(gamer_tag)
    else:
        print("Invalid please put valid number.")
        two_teammate(gamer_tag)
def solo(gamer_tag):
    print("Now we must choose a map:")
    print("1.Dam/Closed security")
    print("2.Buried city/Bird city")
    print("3.Stella montis/Night raid")
    choice = input(">")
    if choice == "1":
        dam0(gamer_tag)
    elif choice =="2":
        buried_city0(gamer_tag)
    elif choice =="3":
        stella_montis0(gamer_tag)
    else:
        print("Invalid please put valid number.")
        solo(gamer_tag)
def dam1(gamer_tag):
    print(f"{gamer_tag} has chosen Dam/Closed security with one teammate")
    print("Loading...")
    spawn=[
        "You spawned in Power Generation Complex",
        "You spawned in Hydrophobic Dome Complex",
        "You spawned in Water Treatment",
        "You spawned in Testing Annex",
        "You spawned in Research & Administration",
    ]
    selected_spawn = random.choice(spawn)
    print(selected_spawn)
    e1=[
        "You hear footsteps and gunshots coming from the Power Generation Complex",
        "You hear footsteps and gunshots coming from the Hydrophobic Dome Complex",
        "You hear footsteps and gunshots coming from the Water Treatment",
        "You hear footsteps and gunshots coming from the Testing Annex",
        "You hear footsteps and gunshots coming from the Research & Administration",
        "You hear a CLANKER fighting a player in the Power Generation Complex",
        "You hear a CLANKER fighting a player in the Hydrophobic Dome Complex",
        "You hear a CLANKER fighting a player in the Water Treatment",
        "You hear a CLANKER fighting a player in the Testing Annex",
        "You hear a CLANKER fighting a player in the Research & Administration",
        "Your teammate ran into a fight in the Power Generation Complex",
        "Your teammate ran into a fight in the Hydrophobic Dome Complex",
        "Your teammate ran into a fight in the Water Treatment",
        "Your teammate ran into a fight in the Testing Annex",
        "Your teammate ran into a fight in the Research & Administration",
        "you hear a CLANKER nearby"
    ]
    event1= random.choice(e1)
    print(event1)
    print("What do you do?")
    print("1.Go towards it")
    print("2.Focus on looting")
    event1_choice = input(">")
    if event1_choice == "1": 
        out1=[
            "You went towards the noise and got killed by a player camping in the corner",
            "You went towards the noise and got killed by a CLANKER",
            "You went towards the noise and killed a player camping in the corner",
            "You went towards the noise and killed a CLANKER",
            "You went towards the noise and your teammate killed a player camping in the corner",
            "You went towards the noise and your teammate killed a CLANKER",
            "You see a downed player"
        ]
        print(random.choice(out1))
        if out1== "You see a downed player":
            print("What do you do?")
            print("1.Revive them")
            print("2.Kill them")
            print("3.Leave them")
            downed_choice = input(">")
            if downed_choice == "1":
                a=["You revived the player and they are now your teammate","You revived the player but they are a traitor and killed you but got killed by your teammate","You revived the player but they are a traitor and killed you and your teammate"]
                print(random.choice(a))
                if a == "You revived the player but they are a traitor and killed you but got killed by your teammate"or a == "You revived the player but they are a traitor and killed you and your teammate":
                    print("[GAME OVER]\n[{gamer_tag} has died to Jello_lover36]")
                elif a == "You revived the player and they are now your teammate":
                    print("You revived the player and they are now your teammate")
                    print("What should you do?")
                    print("1.Continue looting")
                    print("2.Go towards exstraction")
                    loot_choice = input(">")
                    if loot_choice == "1":
                        b=["You continued looting and die to a clanker","You run into a room and hear a click as you walk in.......Kaboom!"]
                        print(random.choice(b))
                        if b == "You continued looting and die to a clanker":
                            print("[GAME OVER]\n[{gamer_tag} has died to a CLANKER]")
                        elif b == "You run into a room and hear a click as you walk in.......Kaboom!":
                            print("[GAME OVER]\n[{gamer_tag} has died to a Drunk_Demoman]")
                    elif loot_choice == "2":
                        c=["You went towards exstraction and got killed by a player camping in the corner","You went towards exstraction and got killed by a CLANKER","You went towards exstraction and killed a player camping in the corner","You went towards exstraction and killed a CLANKER","You went towards exstraction and your teammate killed a player camping in the corner","You went towards exstraction and your teammate killed a CLANKER"]
                        print(random.choice(c))
                        if c == "You went towards exstraction and got killed by a player camping in the corner":
                            print("[GAME OVER]\n[{gamer_tag} has died to Jello_lover36]")
                        elif c == "You went towards exstraction and got killed by a CLANKER":
                            print("[GAME OVER]\n[{gamer_tag} has died to a CLANKER]")
                        elif c == "You went towards exstraction and killed a player camping in the corner"or c == "You went towards exstraction and your teammate killed a player camping in the corner":
                            print("You went towards exstraction and killed a player camping in the corner and escaped with your teammate")
                        elif c == "You went towards exstraction and killed a CLANKER"or c == "You went towards exstraction and your teammate killed a CLANKER":
                            print("You went towards exstraction and killed a CLANKER and escaped with your teammate")
            elif downed_choice == "2":
                a=["You killed the player and got some loot","As you loot you see a light and before you relize it.......kaboom!","It was a trap but you killed the player and got some loot"]
                print(random.choice(a))
                if a == "As you loot you see a light and before you relize it.......kaboom!":
                    print("[GAME OVER]\n[{gamer_tag} has died to Drunk_Demoman]")
                elif a == "It was a trap but you killed the player and got some loot"or a == "You killed the player and got some loot":
                    print("You got some loot and continued looting")
                    print("What should you do?")
                    print("1.Continue looting")
                    print("2.Go towards exstraction")
                    loot_choice = input(">")
                    if loot_choice == "1":
                        b=["You continued looting and die to a clanker","You run into a room and hear a click as you walk in.......Kaboom!"]
                        print(random.choice(b))
                        if b == "You continued looting and die to a clanker":
                            print("[GAME OVER]\n[{gamer_tag} has died to a CLANKER]")
                        elif b == "You run into a room and hear a click as you walk in.......Kaboom!":
                            print("[GAME OVER]\n[{gamer_tag} has died to a Drunk_Demoman]")
                    elif loot_choice == "2":
                        c=["You went towards exstraction and got killed by a player camping in the corner","You went towards exstraction and got killed by a CLANKER","You went towards exstraction and killed a player camping in the corner","You went towards exstraction and killed a CLANKER","You went towards exstraction and your teammate killed a player camping in the corner","You went towards exstraction and your teammate killed a CLANKER"]
                        print(random.choice(c))
                        if c == "You went towards exstraction and got killed by a player camping in the corner":
                            print("[GAME OVER]\n[{gamer_tag} has died to Jello_lover36]")
                        elif c == "You went towards exstraction and got killed by a CLANKER":
                            print("[GAME OVER]\n[{gamer_tag} has died to a CLANKER]")
                        elif c == "You went towards exstraction and killed a player camping in the corner"or c == "You went towards exstraction and your teammate killed a player camping in the corner":
                            print("You went towards exstraction and killed a player camping in the corner and escaped with your teammate")
                        elif c == "You went towards exstraction and killed a CLANKER"or c == "You went towards exstraction and your teammate killed a CLANKER":
                            print("You went towards exstraction and killed a CLANKER and escaped with your teammate")
            elif downed_choice == "3":
                print("You left the player and continued looting")
                print("What should you do?")
                print("1.Continue looting")
                print("2.Go towards exstraction")
                loot_choice = input(">")
                if loot_choice == "1":
                    b=["You continued looting and die to a clanker","You run into a room and hear a click as you walk in.......Kaboom!"]
                    print(random.choice(b))
                    if b == "You continued looting and die to a clanker":
                        print("[GAME OVER]\n[{gamer_tag} has died to a CLANKER]")
                    elif b == "You run into a room and hear a click as you walk in.......Kaboom!":
                        print("[GAME OVER]\n[{gamer_tag} has died to a Drunk_Demoman]")
                elif loot_choice == "2":
                    c=["You went towards exstraction and got killed by a player camping in the corner","You went towards exstraction and got killed by a CLANKER","You went towards exstraction and killed a player camping in the corner","You went towards exstraction and killed a CLANKER","You went towards exstraction and your teammate killed a player camping in the corner","You went towards exstraction and your teammate killed a CLANKER"]
                    print(random.choice(c))
                    if c == "You went towards exstraction and got killed by a player camping in the corner":
                        print("[GAME OVER]\n[{gamer_tag} has died to Jello_lover36]")
                    elif c == "You went towards exstraction and got killed by a CLANKER":
                        print("[GAME OVER]\n[{gamer_tag} has died to a CLANKER]")
                    elif c == "You went towards exstraction and killed a player camping in the corner"or c == "You went towards exstraction and your teammate killed a player camping in the corner":
                        print("You went towards exstraction and killed a player camping in the corner and escaped with your teammate")
                    elif c == "You went towards exstraction and killed a CLANKER"or c == "You went towards exstraction and your teammate killed a CLANKER":
                        print("You went towards extraction and killed a CLANKER and escaped with your teammate")
                else:                    print("Invalid please put valid number.")
        elif out1 == "You went towards the noise and got killed by a player camping in the corner":
            print("[GAME OVER]\n[{gamer_tag} has died to Jello_lover36]")
        elif out1 == "You went towards the noise and got killed by a CLANKER":
            print("[GAME OVER]\n[{gamer_tag} has died to a CLANKER]")
        else:
            
            print("What should you do?")
            print("1.Continue looting")
            print("2.Go towards exstraction")
            loot_choice = input(">")
            if loot_choice == "1":
                b=["You continued looting and die to a clanker","You run into a room and hear a click as you walk in.......Kaboom!"]
                print(random.choice(b))
                if b == "You continued looting and die to a clanker":
                    print("[GAME OVER]\n[{gamer_tag} has died to a CLANKER]")
                elif b == "You run into a room and hear a click as you walk in.......Kaboom!":
                    print("[GAME OVER]\n[{gamer_tag} has died to a Drunk_Demoman]")
            elif loot_choice == "2":
                c=["You went towards exstraction and got killed by a player camping in the corner","You went towards exstraction and got killed by a CLANKER","You went towards exstraction and killed a player camping in the corner","You went towards exstraction and killed a CLANKER","You went towards exstraction and your teammate killed a player camping in the corner","You went towards exstraction and your teammate killed a CLANKER"]
                print(random.choice(c))
                if c == "You went towards exstraction and got killed by a player camping in the corner":
                    print("[GAME OVER]\n[{gamer_tag} has died to Jello_lover36]")
                elif c == "You went towards exstraction and got killed by a CLANKER":
                    print("[GAME OVER]\n[{gamer_tag} has died to a CLANKER]")
                elif c == "You went towards exstraction and killed a player camping in the corner"or c == "You went towards exstraction and your teammate killed a player camping in the corner":
                    print("You went towards exstraction and killed a player camping in the corner and escaped with your teammate")
                elif c == "You went towards exstraction and killed a CLANKER"or c == "You went towards exstraction and your teammate killed a CLANKER":
                    print("You went towards extraction and killed a CLANKER and escaped with your teammate")
            else:
                print("Invalid please put valid number.")
    elif event1_choice == "2":
        print("You focused on looting and got killed by a CLANKER")
        print("[GAME OVER]\n[{gamer_tag} has died to a CLANKER]")
def buried_city1(gamer_tag):
    print(f"{gamer_tag} has chosen Buried city/Bird city with one teammate")
    print("Loading...")
    spawn=[
        "You spawned in Grandioso Appartments",
        "You spawned in Piazza Rosa",
        "You spawned in Library",
        "You spawned in Space Travel",
        "You spawned in Hospital"
    ]
    selected_spawn = random.choice(spawn)
    print(selected_spawn)
    e1=[
        "You hear footsteps and gunshots coming from the Grandioso Appartments",
        "You hear footsteps and gunshots coming from the Piazza Rosa",
        "You hear footsteps and gunshots coming from the Library",
        "You hear footsteps and gunshots coming from the Space Travel",
        "You hear footsteps and gunshots coming from the Hospital",
        "You hear a CLANKER fighting a player in the Grandioso Appartments",
        "You hear a CLANKER fighting a player in the Piazza Rosa",
        "You hear a CLANKER fighting a player in the Library",
        "You hear a CLANKER fighting a player in the Space Travel",
        "You hear a CLANKER fighting a player in the Hospital",
        "Your teammate ran into a fight in the Grandioso Appartments",
        "Your teammate ran into a fight in the Piazza Rosa",
        "Your teammate ran into a fight in the Library",
        "Your teammate ran into a fight in the Space Travel",
        "Your teammate ran into a fight in the Hospital",
        "you hear a CLANKER nearby",
    ]
    event1= random.choice(e1)
    print(event1)
    print("What do you do?")
    print("1.Go towards it")
    print("2.Focus on looting")
    event1_choice = input(">")
    if event1_choice == "1":
        out1=[
            "You went towards the noise and got killed by a player camping in the corner",
            "You went towards the noise and got killed by a CLANKER",
            "You went towards the noise and killed a player camping in the corner",
            "You went towards the noise and killed a CLANKER",
            "You went towards the noise and your teammate killed a player camping in the corner",
            "You went towards the noise and your teammate killed a CLANKER",
            "You see a downed player"
        ]
        a=random.choice(out1)
        print(a)
        if a== "You see a downed player":
            print("What do you do?")
            print("1.Revive them")
            print("2.Kill them")
            print("3.Leave them")
            downed_choice = input(">")
            if downed_choice == "1":
                a=["You revived the player and they are now your teammate","You revived the player but they are a traitor and killed you but got killed by your teammate","You revived the player but they are a traitor and killed you and your teammate"]
                print(random.choice(a))
                if a == "You revived the player but they are a traitor and killed you but got killed by your teammate"or a == "You revived the player but they are a traitor and killed you and your teammate":
                    print("[GAME OVER]\n[{gamer_tag} has died to Jello_lover36]")
                elif a == "You revived the player and they are now your teammate":
                    print("You revived the player and they are now your teammate")
                    print("What should you do?")
                    print("1.Continue looting")
                    print("2.Go towards exstraction")
                    loot_choice = input(">")
                    if loot_choice == "1":
                        b=["You continued looting and die to a clanker","You run into a room and hear a click as you walk in.......Kaboom!"]
                        print(random.choice(b))
                        if b == "You continued looting and die to a clanker":
                            print("[GAME OVER]\n[{gamer_tag} has died to a CLANKER]")
                        elif b == "You run into a room and hear a click as you walk in.......Kaboom!":
                            print("[GAME OVER]\n[{gamer_tag} has died to a Drunk_Demoman]")
                    elif loot_choice == "2":
                        c=["You went towards exstraction and got killed by a player camping in the corner","You went towards exstraction and got killed by a CLANKER","You went towards exstraction and killed a player camping in the corner","You went towards exstraction and killed a CLANKER","You went towards exstraction and your teammate killed a player camping in the corner","You went towards exstraction and your teammate killed a CLANKER"]
                        print(random.choice(c))
                        if c == "You went towards exstraction and got killed by a player camping in the corner":
                            print("[GAME OVER]\n[{gamer_tag} has died to Jello_lover36]")
                        elif c == "You went towards exstraction and got killed by a CLANKER":
                            print("[GAME OVER]\n[{gamer_tag} has died to a CLANKER]")
                        elif c == "You went towards exstraction and killed a player camping in the corner"or c == "You went towards exstraction and your teammate killed a player camping in the corner":
                            print("You went towards exstraction and killed a player camping in the corner and escaped with your teammate")
                        elif c == "You went towards exstraction and killed a CLANKER"or c == "You went towards exstraction and your teammate killed a CLANKER":
                            print("[GAME OVER]\n[{gamer_tag} has died to a CLANKER]")
            elif downed_choice == "2":
                a=["You killed the player and got some loot","As you loot you see a light and before you relize it.......kaboom!","It was a trap but you killed the player and got some loot"]
                print(random.choice(a))
                if a == "As you loot you see a light and before you relize it.......kaboom!":
                    print("[GAME OVER]\n[{gamer_tag} has died to Drunk_Demoman]")
                elif a == "It was a trap but you killed the player and got some loot"or a == "You killed the player and got some loot":
                    print("You got some loot and continued looting")
                    print("What should you do?")
                    print("1.Continue looting")
                    print("2.Go towards exstraction")
                    loot_choice = input(">")
                    if loot_choice == "1":
                        b=["You continued looting and die to a clanker","You run into a room and hear a click as you walk in.......Kaboom!"]
                        print(random.choice(b))
                        if b == "You continued looting and die to a clanker":
                            print("[GAME OVER]\n[{gamer_tag} has died to a CLANKER]")
                        elif b == "You run into a room and hear a click as you walk in.......Kaboom!":
                            print("[GAME OVER]\n[{gamer_tag} has died to a Drunk_Demoman]")
                    elif loot_choice == "2":
                        c=["You went towards exstraction and got killed by a player camping in the corner","You went towards exstraction and got killed by a CLANKER","You went towards exstraction and killed a player camping in the corner","You went towards exstraction and killed a CLANKER","You went towards exstraction and your teammate killed a player camping in the corner","You went towards exstraction and your teammate killed a CLANKER"]
                        print(random.choice(c))
                        if c == "You went towards exstraction and got killed by a player camping in the corner":
                            print("[GAME OVER]\n[{gamer_tag} has died to Jello_lover36]")
                        elif c == "You went towards exstraction and got killed by a CLANKER":
                            print("[GAME OVER]\n[{gamer_tag} has died to a CLANKER]")
                        elif c == "You went towards exstraction and killed a player camping in the corner"or c == "You went towards exstraction and your teammate killed a player camping in the corner":
                            print("You went towards exstraction and killed a player camping in the corner and escaped with your teammate")
            elif downed_choice == "3":
                print("You left the player and continued looting")
                print("What should you do?")
                print("1.Continue looting")
                print("2.Go towards exstraction")
                loot_choice = input(">")
                if loot_choice == "1":
                    b=["You continued looting and die to a clanker","You run into a room and hear a click as you walk in.......Kaboom!"]
                    print(random.choice(b))
                    if b == "You continued looting and die to a clanker":
                        print("[GAME OVER]\n[{gamer_tag} has died to a CLANKER]")
                    elif b == "You run into a room and hear a click as you walk in.......Kaboom!":
                        print("[GAME OVER]\n[{gamer_tag} has died to a Drunk_Demoman]")
                elif loot_choice == "2":
                    c=["You went towards exstraction and got killed by a player camping in the corner","You went towards exstraction and got killed by a CLANKER","You went towards exstraction and killed a player camping in the corner","You went towards exstraction and killed a CLANKER","You went towards exstraction and your teammate killed a player camping in the corner","You went towards exstraction and your teammate killed a CLANKER"]
                    print(random.choice(c))
                    if c == "You went towards exstraction and got killed by a player camping in the corner":
                        print("[GAME OVER]\n[{gamer_tag} has died to Jello_lover36]")
                    elif c == "You went towards exstraction and got killed by a CLANKER":
                        print("[GAME OVER]\n[{gamer_tag} has died to a CLANKER]")
                    elif c == "You went towards exstraction and killed a player camping in the corner"or c == "You went towards exstraction and your teammate killed a player camping in the corner":
                        print("You went towards exstraction and killed a player camping in the corner and escaped with your teammate")
                    elif c == "You went towards exstraction and killed a CLANKER"or c == "You went towards extraction and your teammate killed a CLANKER":
                        print("You went towards extraction and killed a CLANKER and escaped with your teammate")
                else:
                    print("Invalid please put valid number.")
        elif a == "You went towards the noise and got killed by a player camping in the corner":
            print("[GAME OVER]\n[{gamer_tag} has died to Jello_lover36]")
        elif a == "You went towards the noise and got killed by a CLANKER":
            print("[GAME OVER]\n[{gamer_tag} has died to a CLANKER]")
        elif a == "You went towards the noise and killed a player camping in the corner"or a == "You went towards the noise and your teammate killed a player camping in the corner":
            print("You went towards the noise and killed a player camping in the corner and escaped with your teammate")
        elif a == "You went towards the noise and killed a CLANKER"or a == "You went towards the noise and your teammate killed a CLANKER":
            print("You went towards the noise and killed a CLANKER and escaped with your teammate")
    elif event1_choice == "2":
        print("You focused on looting and got killed by a CLANKER")
        print("[GAME OVER]\n[{gamer_tag} has died to a CLANKER]")
def stella_montis1(gamer_tag):
    print(f"{gamer_tag} has chosen Stella montis/Night raid with one teammate")
    print("Loading...")
    spawn=[
        "You spawned in Lobby",
        "You spawned in Medical Research",
        "You spawned in Assembly",
        "You spawned in Cultural Archives",
        "You spawned in Loading Bay",
    ]
    selected_spawn = random.choice(spawn)
    print(selected_spawn)
    
def dam2(gamer_tag):
    print(f"{gamer_tag} has chosen Dam/Closed security with two teammates")
    print("Loading...")
    spawn=[
        "You spawned in Power Generation Complex",
        "You spawned in Hydrophobic Dome Complex",
        "You spawned in Water Treatment",
        "You spawned in Testing Annex",
        "You spawned in Research & Administration",
    ]
    selected_spawn = random.choice(spawn)
    print(selected_spawn)
def buried_city2(gamer_tag):
    print(f"{gamer_tag} has chosen Buried city/Bird city with two teammates")
    print("Loading...")
    spawn=[
        "You spawned in Grandioso Appartments",
        "You spawned in Piazza Rosa",
        "You spawned in Library",
        "You spawned in Space Travel",
        "You spawned in Hospital"
    ]
    selected_spawn = random.choice(spawn)
    print(selected_spawn)
def stella_montis2(gamer_tag):
    print(f"{gamer_tag} has chosen Stella montis/Night raid with two teammates")
    print("Loading...")
    spawn=[
        "You spawned in Lobby",
        "You spawned in Medical Research",
        "You spawned in Assembly",
        "You spawned in Cultural Archives",
        "You spawned in Loading Bay",
    ]
    selected_spawn = random.choice(spawn)
    print(selected_spawn)
def dam0(gamer_tag):
    print(f"{gamer_tag} has chosen Dam/Closed security solo")
    print("Loading...")
    spawn=[
        "You spawned in Power Generation Complex",
        "You spawned in Hydrophobic Dome Complex",
        "You spawned in Water Treatment",
        "You spawned in Testing Annex",
        "You spawned in Research & Administration",
    ]
    selected_spawn = random.choice(spawn)
    print(selected_spawn)
def buried_city0(gamer_tag):
    print(f"{gamer_tag} has chosen Buried city/Bird city solo")
    print("Loading...")
    spawn=[
        "You spawned in Grandioso Appartments",
        "You spawned in Piazza Rosa",
        "You spawned in Library",
        "You spawned in Space Travel",
        "You spawned in Hospital"
    ]
    selected_spawn = random.choice(spawn)
    print(selected_spawn)
def stella_montis0(gamer_tag):
    print(f"{gamer_tag} has chosen Stella montis/Night raid solo")
    print("Loading...")
    spawn=[
        "You spawned in Lobby",
        "You spawned in Medical Research",
        "You spawned in Assembly",
        "You spawned in Cultural Archives",
        "You spawned in Loading Bay",
    ]
    selected_spawn = random.choice(spawn)
    print(selected_spawn)
start_adventure()