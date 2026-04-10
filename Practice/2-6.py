def hello():
    print("hello")
    print("jon")


print("not indented")
hello()

def add(x = 0,y = 0): #this funtions purpose is to add two numbers
    print(x+y)

add(2, 10)
add()
add(y=4)

def add(x, y):
    return x + y

print(add(2, 10))