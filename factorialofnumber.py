def factorials(num):
    diviables = []
    for i in range(1,num//2):
        if num %i ==0:
            diviables.append(i)
    diviables.append(num)
    return diviables



    


print(factorials(30))

