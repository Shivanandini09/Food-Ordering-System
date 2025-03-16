# iteration_1.py

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

    def show_cart(self):
        if self.cart:
            print("Items in your cart:")
            for item in self.cart:
                print(f"- {item}")
        else:
            print("Your cart is empty.")

if __name__ == '__main__':
    system = FoodOrderingSystem()

    # Display Menu
    system.display_menu()

    # Add Items to Cart
    system.add_to_cart('Pizza')
    system.add_to_cart('Burger')

    # Show Cart
    system.show_cart()
