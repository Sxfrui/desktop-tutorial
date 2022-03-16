name = input("What is your name? ")

if name == "ben" or name == "thomas":
    evil_status = input("Are you evil?\n")
    if evil_status == "Yes":
     print("You're not allowed here!")
    else: print("Welcome!")
    exit()


input("hello, " + name + ". Would you like to check out our menu? ")
print("Hello, welcome to our shop.") 

menu = "Latte, Cappacino, Barrista, Ice Coffee, and Regular coffee."
order = print(name + ". This is our menu, please choose an item of your liking " + menu)

menu = input("What would you like? ")

price = "8"
quantity = input("How many would you like? ")
total = int(price) * int(quantity)
print("your total is: $" + str(total))

if order == "Latte":
    price = "13"
else: 
    price = "8"

