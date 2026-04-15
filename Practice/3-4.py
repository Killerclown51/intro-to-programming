def get_number():
    n =input("enter a number")
    try:
        n = int(n)
    except:
        print("you entered a word, please enter a number")
        get_number()
    return n

def divide(x):

        return 100/x


num = get_number()
print(divide(num))