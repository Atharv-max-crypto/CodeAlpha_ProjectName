# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 130
}

total_investment = 0
result_data = []

print("📈 Simple Stock Tracker")
print("-----------------------")

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))

        price = stock_prices[stock]
        investment = price * quantity
        total_investment += investment

        result_data.append(f"{stock} | Qty: {quantity} | Price: {price} | Total: {investment}")

        print(f"Added: {stock} → Investment = {investment}\n")

    else:
        print("Stock not found! Try again.\n")

print("-----------------------")
print("Total Investment Value:", total_investment)

# Optional file saving
save = input("Do you want to save result to file? (yes/no): ").lower()

if save == "yes":
    with open("stock_report.txt", "w") as file:
        file.write("Stock Investment Report\n")
        file.write("------------------------\n")
        for line in result_data:
            file.write(line + "\n")
        file.write("\nTotal Investment: " + str(total_investment))

    print("Result saved to stock_report.txt")

else:
    print("Result not saved.")

print("Thank you for using Stock Tracker!")