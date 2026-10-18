def set_matrix_zeros(nums,rows,cols):


    for i in range(rows):

        if nums[i][cols] !=0:
            nums[i][cols]=float("-inf")


    for j in range(0,cols):
        if nums[rows][j] !=0:
            nums[rows][j]=float("-inf")


def set_zeros(nums:list):
    rows= len(nums)
    cols =len(nums[0])

    for i in range(rows):
        for j in range(cols):
            if nums[i][j]==0:
                set_matrix_zeros(nums,i,j)
    
   
    for i in range(rows):
        for j in range(cols):
            if nums[i][j]==float("-inf"):
                nums[i][j]=0
    return nums 

nums =[[1, 0, 7,1], [1,0, 5, 6], [2,3, 0, 9]]

print(set_zeros(nums=nums))


def set_zeros_optimization(nums):
    row_track =[0 for _ in range(len(nums))]
    cols_track =[0 for _ in range(len(nums[0]))]

    for i in range(0,len(nums)):
        for j in range(0,len(nums[0])):
            if nums[i][j]==0:
                row_track[i]= -1
                cols_track[j]= -1

    for i in range(0,len(nums)):
        for j in range(0,len(nums[0])):
            if row_track[i] or cols_track[j] ==-1:
                nums[i][j]=0

    return nums

nums =[[1, 0, 7,1], [1,0, 5, 6], [2,3, 0, 9]]
print(set_zeros_optimization(nums=nums))

        



