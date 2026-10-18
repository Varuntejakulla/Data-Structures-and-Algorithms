def creating_matrix(col,rows):
    result =[]
    for i in range(rows):
        row =[]
        for j in range(col):
            row.append((i,j))
        result.append(row)
    return result


print(creating_matrix(2,5))


def  building_2d_martix(nums:list):
        rows =len(nums)
        cols =len(nums[0])

        for i in range(rows):
             for j in range(cols):
                  print(nums[i][j],end=" ")
             print()
nums = [[1,2,3],[4,5,6],[7,8,9]]

building_2d_martix(nums=nums)
             

