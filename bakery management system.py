#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from datetime import datetime

class BakeryOrderManagement:
    def __init__(self):
        self.orders = pd.DataFrame(columns=["Order ID", "Customer Name", "Item", "Quantity", "Order Date"])
        self.next_order_id = 1

    def add_order(self):
        print("\n=== Add New Order ===")
        customer_name = input("Enter customer name: ")
        item = input("Enter name of item ordered: ")
        while True:
            try:
                quantity = int(input("Enter item's quantity: "))
                if quantity <= 0:
                    print("Quantity must be a positive integer. Please try again.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid integer for quantity.")

        order_date = datetime.now().strftime("%Y-%m-%d")
        new_order = pd.DataFrame([[self.next_order_id, customer_name, item, quantity, order_date]], 
                                 columns=["Order ID", "Customer Name", "Item", "Quantity", "Order Date"])
        self.orders = pd.concat([self.orders, new_order], ignore_index=True)
        print("Order added successfully!")
        self.next_order_id += 1

    def view_orders(self):
        print("\n=== All Orders ===")
        if self.orders.empty:
            print("No orders available.")
        else:
            print(self.orders)

    def update_order(self):
        print("\n=== Update Order ===")
        if self.orders.empty:
            print("No orders available to update.")
            return
        
        try:
            order_id = int(input("Enter order ID to update: "))
            if order_id < 1 or order_id > len(self.orders):
                print("Invalid order ID. Please enter a valid order ID.")
                return
            
            print("Updating Order ID:", order_id)
            new_item = input("Enter new item: ")
            new_quantity = int(input("Enter new quantity: "))

            self.orders.at[order_id - 1, "Item"] = new_item
            self.orders.at[order_id - 1, "Quantity"] = new_quantity
            print("Order updated successfully!")
        except ValueError:
            print("Invalid input. Please enter a valid integer for order ID and quantity.")

    def save_to_excel(self):
        if self.orders.empty:
            print("No orders to save.")
        else:
            filename = input("Enter filename to save (e.g., 'bakery_orders.xlsx'): ")
            if not filename.strip():
                print("Invalid filename.")
            else:
                self.orders.to_excel(filename.strip(), index=False)
                print(f"Orders saved to '{filename.strip()}'.")
  
# Create an instance of BakeryOrderManagement
order_system = BakeryOrderManagement()

# Main menu loop
while True:
    print("\n=== Bakery Management System ===")
    print("1. Add Order")
    print("2. View Orders")
    print("3. Update Order")
    print("4. Save to Excel")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        order_system.add_order()
    elif choice == '2':
        order_system.view_orders()
    elif choice == '3':
        order_system.update_order()
    elif choice == '4':
        order_system.save_to_excel()
    elif choice == '5':
        print("Exiting Bakery Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")


# In[ ]:




