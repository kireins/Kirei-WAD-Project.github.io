print("\n𓆝 𓆟 𓆞 𓆝 WELCOME TO KIREI'S DINER 𓆝 𓆟 𓆞 𓆝")
print("Categories: Food, Drink")

category = input("Choose a category (Food/Drink): ")

if category.lower() == "food":
    print("\nFood Menu:")
    print("1. Cheese Burger - Rp. 50,000.00")
    print("2. Brisket Plater - Rp. 75,000.00")
    print("3. Steak - Rp. 100,000.00")
    print("4. Bone Marrow - Rp. 120,000.00")
    print("5. New York Sliced Pizza - Rp. 90,000.00")

    food_choice = int(input("Choose a food item (1-5): "))
    quantity = int(input("Enter the quantity: "))
    food_prices = [50000, 75000, 100000, 120000, 90000]
    total_price = quantity * food_prices[food_choice - 1]

elif category.lower() == "drink":
    print("\nDrink Menu:")
    print("1. Pina Colada - Rp. 30,000.00")
    print("2. Cappuccino - Rp. 25,000.00")
    print("3. Ice Lemon Americano - Rp. 20,000.00")
    print("4. Equil Mineral - Rp. 15,000.00")
    print("5. Fresh Juice - Rp. 35,000.00")

    drink_choice = int(input("Choose a drink item (1-5): "))
    quantity = int(input("Enter the quantity: "))
    drink_prices = [30000, 25000, 20000, 15000, 35000]
    total_price = quantity * drink_prices[drink_choice - 1]

else:
    print("Invalid category. Please choose either Food or Drink.")

print(f"\n--------- Customer's Order ---------")
print(f"Category: {category}")
print(f"Quantity: {quantity}")
if category.lower() == "food":
    print(f"Menu: {'Cheese Burger' if food_choice == 1 else 'Brisket Plater' if food_choice == 2 else 'Steak' if food_choice == 3 else 'Bone Marrow' if food_choice == 4 else 'New York Sliced Pizza'}")
else:
    print(f"Menu: {'Pina Colada' if drink_choice == 1 else 'Cappuccino' if drink_choice == 2 else 'Ice Lemon Americano' if drink_choice == 3 else 'Equil Mineral' if drink_choice == 4 else 'Fresh Juice'}")
print(f"\nPrice: Rp. {total_price:,.2f}")

total_order = total_price

if total_order > 500000:
    discount = 0.25
elif total_order > 250000:
    discount = 0.15
elif total_order > 100000:
    discount = 0.10
else:
    discount = 0

discounted_amount = total_order * discount
total_order -= discounted_amount

print(f"\nTotal Order Amount after Discount: Rp. {total_order:,.2f}")

name = input("Enter your name: ")
phone_number = input("Enter your phone number: ")

provided_money = float(input("Enter the amount of money you are providing: "))

change = provided_money - total_order

print("\n--------- Receipt ---------")
print(f"Customer Name: {name}")
print(f"Phone Number: {phone_number}")
print(f"Order Summary: {category}, {quantity} {('Cheese Burger' if food_choice == 1 else 'Brisket Plater' if food_choice == 2 else 'Steak' if food_choice == 3 else 'Bone Marrow' if food_choice == 4 else 'New York Sliced Pizza') if category.lower() == 'food' else ('Pina Colada' if drink_choice == 1 else 'Cappuccino' if drink_choice == 2 else 'Ice Lemon Americano' if drink_choice == 3 else 'Equil Mineral' if drink_choice == 4 else 'Fresh Juice')}")
print(f"Total Amount: Rp. {total_order:,.2f}")
print(f"Provided Money: Rp. {provided_money:,.2f}")
print(f"Change: Rp. {change:,.2f}")

print("\n𓆝 𓆟 𓆞 𓆝 Thank you for ordering, and enjoy your meal! 𓆝 𓆟 𓆞 𓆝")
