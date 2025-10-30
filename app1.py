for i in range(1, 101):

    if i % 2 == 0 or i % 5 == 0:

        multi = []
        
        if i % 2 == 0:
            multi.append("2")
            
        if i % 5 == 0:
            multi.append("5")

        print(f"{i}: {', '.join(multi)}의 배수입니다")
        
    else:
        print(i)