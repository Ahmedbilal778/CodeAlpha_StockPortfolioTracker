
# Stock Portfolio Tracker

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 400,
    "AMZN": 190
}

portfolio = {}
total_investment = 0

print("================================")
print("     STOCK PORTFOLIO TRACKER")
print("================================")

while True:
    stock_name = input(
        "\nEnter stock name (or 'done' to finish): "
    ).upper().strip()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Stock not available!")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero!")
            continue

    except ValueError:
        print("Please enter a valid number!")
        continue

    portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

    print("Stock added successfully!")


# Calculate total investment
print("\n========== PORTFOLIO SUMMARY ==========")

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity

    total_investment += investment

    print(
        f"{stock} | Quantity: {quantity} | "
        f"Price: ${price} | Value: ${investment}"
    )

print("---------------------------------------")
print(f"Total Investment: ${total_investment}")

print("\nThank you for using Stock Portfolio Tracker!")
