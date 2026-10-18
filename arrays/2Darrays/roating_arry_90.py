 
def rotating_array(nums):

    rows = len(nums)
    cols =len(nums[0])

    zer0_matrix = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in  range(cols):
            zer0_matrix[j][rows-1-i] = nums[i][j]
    return zer0_matrix       


nums=[[1,2,3], [4,5,6], [7, 8, 9]]
# print(rotating_array(nums))

# print(rotating_array_opt(nums))

def rotating_array_opt(nums:list[int]):

    rows = len(nums)
    cols =len(nums[0])

    for i in range(rows):
        for j in  range(i+1,cols):
             nums[i][j],nums[j][i] =nums[j][i],nums[i][j]
    for i in range(rows):
        nums[i].reverse()


    


    return nums     

def roatating_array_ktimes(nums,k):
    for i in range(k):
        rotating_array_opt(nums)
    return nums


   


print(roatating_array_ktimes(nums=nums,k=4))
