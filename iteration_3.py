# iteration_3.py

class FoodOrderingSystem:
    def __init__(self):
        self.menu = {
            'Pizza': 10.0,
            'Burger': 5.0,
            'Pasta': 7.5,
            'Salad': 4.0,
        }
        self.cart = []

    def display_menu(self):
        print("Available Food Items:")
        for idx, (food, price) in enumerate(self.menu.items(), 1):
            print(f"{idx}. {food}: ${price}")

    def add_to_cart(self, food_item):
        if food_item in self.menu:
            self.cart.append(food_item)
            print(f"{food_item} added to cart!")
        else:
            print(f"{food_item} is not on the menu.")

    def remove_from_cart(self, food_item):
        if food_item in self.cart:
            self.cart.remove(food_item)
            print(f"{food_item} removed from cart!")
        else:
            print(f"{food_item} is not in your cart.")

    def show_cart(self):
        if self.cart:
            print("Items in your cart:")
            for item in self.cart:
                print(f"- {item}")
        else:
            print("Your cart is empty.")

    def place_order(self):
        if not self.cart:
            print("Your cart is empty. Cannot place an order.")
            return
        total = sum(self.menu[item] for item in self.cart)
        print("\nOrder Summary:")
        self.show_cart()
        print(f"Total amount: ${total}")

    def user_input(self):
        while True:
            print("\nWhat would you like to do?")
            print("1. View Menu")
            print("2. Add Item to Cart")
            print("3. Remove Item from Cart")
            print("4. View Cart")
            print("5. Place Order")
            print("6. Exit")

            choice = input("Enter your choice (1-6): ")

            if choice == '1':
                self.display_menu()
            elif choice == '2':
                food_item = input("Enter food item to add to cart: ")
                self.add_to_cart(food_item)
            elif choice == '3':
                food_item = input("Enter food item to remove from cart: ")
                self.remove_from_cart(food_item)
            elif choice == '4':
                self.show_cart()
            elif choice == '5':
                self.place_order()
                break
            elif choice == '6':
                print("Exiting system.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == '__main__':
    system = FoodOrderingSystem()
    system.user_input()
