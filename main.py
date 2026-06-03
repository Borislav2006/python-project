from models import CoffeeShop

def get_valid_choice(prompt, min_choice, max_choice):
    """Helper function to get a valid menu choice."""
    while True:
        try:
            choice = int(input(prompt))
            if min_choice <= choice <= max_choice:
                return str(choice)
            else:
                print(f"Please enter a number between {min_choice} and {max_choice}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_valid_items(shop, prompt):
    """Helper function to get valid menu items."""
    while True:
        print("\nAvailable items:")
        print(shop.show_menu())
        items_input = input(prompt)
        items = [item.strip().lower() for item in items_input.split(",")]
        invalid_items = [item for item in items if item not in shop.MENU]
        if invalid_items:
            print(f"Invalid items: {', '.join(invalid_items)}. Please check the menu and try again.")
        else:
            return items

def get_valid_order_index(shop, prompt):
    """Helper function to get a valid order index."""
    while True:
        try:
            order_index = int(input(prompt)) - 1 
            if 0 <= order_index < len(shop.orders):
                return order_index
            else:
                print(f"Please enter a number between 1 and {len(shop.orders)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    shop = CoffeeShop("The Daily Pour")

    while True:
        print("\n--- The Daily Pour ---")
        print("1. Show Menu")
        print("2. Add Order")
        print("3. List Orders")
        print("4. Add Items to Order")
        print("5. Remove Order")
        print("6. Calculate Total Revenue")
        print("7. Exit")

        choice = get_valid_choice("Enter your choice: ", 1, 7)

        if choice == "1":
            print("\n--- Menu ---")
            print(shop.show_menu())

        elif choice == "2":
            customer = input("Enter customer name: ").strip()
            if not customer:
                print("Customer name cannot be empty. Using 'Guest'.")
                customer = "Guest"
            items = get_valid_items(shop, "Enter items (comma-separated, e.g., oolong tea, espresso): ")
            print(shop.add_order(customer, items))

        elif choice == "3":
            print("\n--- Current Orders ---")
            print(shop.list_orders())

        elif choice == "4":
            print("\n--- Current Orders ---")
            if shop.list_orders() == "No orders yet.":
                print("No orders to add items to.")
                continue
            print(shop.list_orders())
            order_index = get_valid_order_index(shop, "Enter the order number to add items to: ")
            items = get_valid_items(shop, "Enter items to add (comma-separated): ")
            print(shop.add_items_to_order(order_index, items))

        elif choice == "5":
            print("\n--- Current Orders ---")
            if shop.list_orders() == "No orders yet.":
                print("No orders to remove.")
                continue
            print(shop.list_orders())
            order_index = get_valid_order_index(shop, "Enter the order number to remove: ")
            print(shop.remove_order(order_index))

        elif choice == "6":
            print(f"Total Revenue: €{shop.calculate_total_revenue():.2f}")

        elif choice == "7":
            print("Exiting...")
            break

if __name__ == "__main__":
    main()