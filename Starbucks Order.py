#Greet and gather information

print("Welcome to Starbucks, what can I get started for you today?")

#Define menu function to take order, cost function to map order to price

def menu():
    print("\n$3 Black Coffee \n" + "$4 Espresso \n" + "$4.50 Latte \n" + "$4.50 Cappuccino")
    order = input("\nWhat would you like to order? \nEnter your order: ")
    return order

def cost(order):
    if order == "Black Coffee":    
        price = 3
    elif order == "Espresso":
        price = 4
    elif order == "Latte":
        price = 4.50
    elif order == "Cappuccino":
        price = 4.50
    return price
        
#Take initial order

order = menu()
price = cost(order)
total = []
drinks = []
drinks.append(order)
total.append(price)

    
#Define repeat order function for more drink orders

def order_more():
    more = input("\nWould you like to order anything else? \nY/N: ")
    if more == "Y":
        order = input("\nWhat would you like? \nEnter your order:")
        price = cost(order)
        drinks.append(order)
        total.append(price)
        order_more()
    else:
        return

#Give opportunity for repeat orders
order_more()
print(drinks)
print(total)

#Give order and total cost
print("\nHere is what I have:")
for x in drinks:
    print(x)

print("\nYour total today is going to be $" + str(sum(total)) + ".")

#Ask for name and give instruction to wait
name = input("\n May I have your name please? \nName:")
print("\nThank you " + name + ", we will have that ready for you shortly.")

        


