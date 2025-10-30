
for i in range(1, 101):
    if (i % 2 == 0):
        print('2의 배수입니다.')
        continue
    if (i % 5 == 0):
        print('5의 배수입니다.')
        continue
    print(i)