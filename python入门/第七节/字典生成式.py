items = ['fruits', 'books', 'others']
prices = [96, 78, 85]
# for i in zip(items,prices):
#     print(i)

d = {item.upper(): price for item, price in zip(items, prices)}
print(d)
