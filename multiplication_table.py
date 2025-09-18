def multiplication_table(row, column):
    for row in range(1, row + 1):
        for column in range(1, column + 1):
            product = row * column
            print(f"{product:4}", end="")
        print()

r = int(input(""))
c = int(input(""))
multiplication_table(r, c)