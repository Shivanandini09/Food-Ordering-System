# iteration_2.py

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
        for food, price in self.menu.items():
            print(f"{food}: ${price}")

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

if __name__ == '__main__':
    system = FoodOrderingSystem()

    # Display Menu
    system.display_menu()

    # Add Items to Cart
    system.add_to_cart('Pizza')
    system.add_to_cart('Burger')

    # Show Cart
    system.show_cart()

    # Remove Item from Cart
    system.remove_from_cart('Burger')

    # Show Cart again
    system.show_cart()

    # Place Order
    system.place_order()
