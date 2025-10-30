<<<<<<< HEAD
for i in range(100, 0, -1):
    
    num_str = str(i)
    
    clap = 0
    for digit in num_str:
        if digit in ('3', '6', '9'):
            clap = clap + 1
            
    if clap > 0:
        print("짝" * clap)
    else:
        print(i)
=======

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
>>>>>>> 876531b8abf236b154a91ae36b4d83d90e60b840
