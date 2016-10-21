# answer = lambda x: x * 7
# print(answer(5))
stocks = {
    'GOOG': 520.56,
    'FB': 76.45,
    'YHOO': 39.28,
    'AMZN': 309.45,
    'AAPL': 99.76
}

minval = sorted(zip(stocks.values(), stocks.keys()))

print(minval)