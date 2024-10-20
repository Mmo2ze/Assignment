import math
def program1():
    while True:
        x = float(input("Enter the x-coordinate: "))
        y = float(input("Enter the y-coordinate: "))
        distance = math.sqrt(math.fabs(x)**2 + math.fabs(y)**2)
        print(f"The distance from the origin is {distance:.2f}")
        if input("Do you want to continue? (y/n): ") == "n":
            break


def program2():
    while True:
        item_price = float(input("Enter item Price: "))
        while item_price < 0.05:
            print("Price cannot be less than 0.05")
            item_price = float(input("Enter item Price: "))
        print(f"Item Price: {item_price:.2f}, after 20% discount: {item_price * 0.8:.2f}")
        if input("Do you want to continue? (y/n): ") == "n":
            break
while True:
    chosenProgram = int(input("Enter 1 for program 1 or 2 for program 2: "))
    if chosenProgram == 1:
        program1()
    elif chosenProgram == 2:
        program2()