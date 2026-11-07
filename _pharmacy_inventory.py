# Topic 2: Loop Structures
# Task 2: Smart Pharmacy Inventory & Sales Management System
# Topic: for loop, range(), conditions inside loops, counters and accumulators.

# Real-World Scenario
# A pharmacy wants to manage its medicine inventory and calculate
# the daily sales revenue.
# The program follows these rules:
# - Ask how many different medicines need to be processed.
# - Use a for loop to process each medicine.
# - Collect the medicine name, available stock, price per unit,
#   and quantity sold.
# - If the requested quantity is more than the available stock,
#   the sale is not processed.
# - If the sale is successful, calculate the sales amount and the
#   remaining stock.
# - If the remaining stock is below 10 units, display a low-stock
#   warning and count the medicine for restocking.
# - Keep the total revenue using an accumulator.
# - Display a final report.

print("===== SMART PHARMACY SYSTEM =====")

total_medicines = int(input("How many medicines do you want to process? "))

total_revenue = 0
successful_sales = 0
restock_count = 0

if total_medicines <= 0:
    print("\nInvalid input: Number of medicines must be greater than 0.")
else:
    for i in range(1, total_medicines + 1):
        print(f"\n----- Medicine {i} -----")
        name = input("Enter medicine name: ")
        stock = int(input("Enter available stock: "))
        price = float(input("Enter price per unit (Rs.): "))
        quantity = int(input("Enter quantity sold: "))

        if name.strip() == "" or stock < 0 or price <= 0 or quantity <= 0:
            print("Invalid input. This medicine was skipped.")
            continue

        if quantity > stock:
            print(f"Sale failed: Only {stock} units of {name} are available.")
            remaining_stock = stock
        else:
            sales_amount = quantity * price
            remaining_stock = stock - quantity
            total_revenue = total_revenue + sales_amount
            successful_sales = successful_sales + 1

            print(f"Sales Amount: Rs. {sales_amount:.2f}")
            print(f"Remaining Stock: {remaining_stock}")

        if remaining_stock < 10:
            print(f"WARNING: Low stock for {name}! Restocking required.")
            restock_count = restock_count + 1

    print("\n===== FINAL REPORT =====")
    print(f"Total Medicines Processed: {total_medicines}")
    print(f"Successful Sales: {successful_sales}")
    print(f"Total Revenue: Rs. {total_revenue:.2f}")
    print(f"Medicines Requiring Restocking: {restock_count}")

