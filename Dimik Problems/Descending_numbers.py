count = 0

for i in range(1000, 0, -1):
    print(i, end=" ")
    count += 1

    if count % 5 == 0:
        print()
        count = 0

