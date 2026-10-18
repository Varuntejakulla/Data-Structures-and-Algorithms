def transpo_matrix(nums):
    rows= len(nums)
    cols = len(nums[0])

    for i in range(rows):
        for j in range(1,cols):
            nums[i][j], nums[j][i] = nums[j][i], nums[i][j]
    return nums



nums =[[1,2,3],[4,5,6],[7,8,9]]
print(transpo_matrix(nums=nums))