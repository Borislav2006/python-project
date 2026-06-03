class CoffeeShop:
    MENU = {
        "oolong tea": 5.20 ,
        "espresso": 2.50,
        "cappuccino": 3.80,
        "latte": 4.00,
        "americano": 3.00,
        "mocha": 4.50,
        "green tea": 3.20,
        "black tea": 2.80
    }

    def __init__(self, name):
        self.name = name
        self.orders = []

    def add_order(self, customer_name, items):
        total = sum(self.MENU[item.lower()] for item in items if item.lower() in self.MENU)
        order = {
            "customer": customer_name,
            "items": items,
            "total": total
        }
        self.orders.append(order)
        return f"Order added for {customer_name}! Total: €{total:.2f}"

    def list_orders(self):
        if not self.orders:
            return "No orders yet."
        return "\n".join(
            [f"{i+1}. Customer: {order['customer']}, Items: {', '.join(order['items'])}, Total: €{order['total']:.2f}"
             for i, order in enumerate(self.orders)]
        )

    def calculate_total_revenue(self):
        return sum(order["total"] for order in self.orders)

    def remove_order(self, order_index):
        if 0 <= order_index < len(self.orders):
            removed_order = self.orders.pop(order_index)
            return f"Order for {removed_order['customer']} removed!"
        return "Invalid order number."

    def add_items_to_order(self, order_index, new_items):
        if 0 <= order_index < len(self.orders):
            order = self.orders[order_index]
            additional_total = sum(self.MENU[item.lower()] for item in new_items if item.lower() in self.MENU)
            order["items"].extend(new_items)
            order["total"] += additional_total
            return f"Added {', '.join(new_items)} to {order['customer']}'s order. New total: €{order['total']:.2f}"
        return "Invalid order number."

    def show_menu(self):
        return "\n".join([f"{item}: €{price:.2f}" for item, price in self.MENU.items()])