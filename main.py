numbers = [1, 2, 3, 4, 5]
squares = []

for num in numbers:
    if (sqr := num ** 2) < 15:
        squares.append(sqr)

print(squares)
