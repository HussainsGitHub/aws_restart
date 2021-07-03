  
#Print prime numbers between the intervals 1 and 250 
for num in range(1,250 + 1): 
    if num > 1: 
        for i in range(2,num): 
            if (num % i) == 0: 
                break 
        else:
            print(num) 
