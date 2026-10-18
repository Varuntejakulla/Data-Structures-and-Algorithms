def upper_traingle(rows,col):
    nums =[[0 for _ in range(rows)] for _ in range(col)]

    for i in range(rows):
        for j in range(col):
            if j<=i:
                print(nums[i][j],end=" ")
            else:
                print("*",end =" ")
        print()


upper_traingle(3,3)

