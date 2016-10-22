import heapq

grades = [32, 45, 3, 889, 35, 2234, 1241]

print(heapq.nlargest(3, grades))

stocks = [
    {'tickers': 'GOOG', 'price': 434},
    {'tickers': 'AAPL', 'price': 325},
    {'tickers': 'FB', 'price': 54},
    {'tickers': 'AMZN', 'price': 623},
    {'tickers': 'F', 'price': 32},
    {'tickers': 'MSFT', 'price': 549},
]

print(heapq.nsmallest(2, stocks, key=lambda stock: stock['price']))