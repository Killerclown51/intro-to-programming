import random
print("I am bob i shall tell you what the future entelse or whatever")
q1=int(input("What is your lucky number\n|"))
q2=float(input("how many years into the future do you want to see\n|"))
q3=float(input("Now i need a magical multiplier\n|"))

def fortune_teller():
    fortune = [
        "you will hit the jackpot in the next 20 years",
        "Dont trust kyle",
        "Your sad",
        "your crush doesnt like you",
        "You will end up homeless",
        "your autistic",
    
    ]
    return random.choice(fortune)
fortune=fortune_teller()
print(f"{fortune}")