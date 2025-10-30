
for i in range(100, 0, -1):
    count = 0

    for j in str(i):
        count += 1 if j in '3' else 0

    if count == 0:
        print(i)
        continue

    for j in range(count):
        print('짝', end="")

    print()