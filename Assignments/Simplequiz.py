tally_score=0
question1=input("What is the oppisite color of blue on the color wheel\n|")
if question1 == ("orange"):
    print("Correct")
    tally_score += 1
else:
    print("Incorrect")

question2=input("What is the oppisite color of red on the color wheel\n|")
if question2 == ("green"):
    print("Correct")
    tally_score += 1
else:
    print("Incorrect")

question3=input("What is the oppisite color of purple on the color wheel\n|")
if question3 == ("yellow"):
    print("Correct")
    tally_score += 1
else:
    print("Incorrect")

question4=input("What is the oppisite color of green on the color wheel\n|")
if question4 == ("red"):
    print("Correct")
    tally_score += 1
else:
    print("Incorrect")

question5=input("What is the oppisite color of yellow on the color wheel\n|")
if question5 == ("purple"):
    print("Correct")
    tally_score += 1
else:
    print("Incorrect")

question6=input("What is the oppisite color of orange on the color wheel\n|")
if question6 == ("blue"):
    print("Correct")
    tally_score += 1
else:
    print("Incorrect")

print("you got ", +tally_score,("/6" ))