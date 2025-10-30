
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

