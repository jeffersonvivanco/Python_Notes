import heapq

nums = [1, -3, 20, 23, 4, 100, 22, -1, 0, 34, 45, -45, 89, 22]
print("smallest numbers: ",heapq.nsmallest(3, nums))

# used with more complex structures
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
print("The most expensive shares are => ", heapq.nlargest(3, portfolio, key=lambda s: s['price']))
