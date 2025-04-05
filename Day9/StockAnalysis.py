def stock_market_analysis(prices):
    print("📈 Stock Market Trend Analysis\n")
    for i in range(1, len(prices)):
        prev = prices[i - 1]
        curr = prices[i]
        change = ((curr - prev) / prev) * 100

        print(f"Day {i} → Day {i+1}: Price changed from {prev} to {curr} ({change:.2f}%)")

        if change <= -5:
            print("📉 Signal: BUY (Price dropped significantly!)")
        elif change >= 5:
            print("📈 Signal: SELL (Price surged!)")
        else:
            print("🔄 Signal: HOLD (Minor change)")

        print("-" * 40)

# Sample historical stock prices for 6 days
stock_prices = [100, 98, 92, 95, 101, 106]

stock_market_analysis(stock_prices)
