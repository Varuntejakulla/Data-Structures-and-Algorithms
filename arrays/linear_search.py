def linear_serach_array(nums:list,target):

    for i in range(len(nums)):
        if nums[i]==target:
            return i
    return -1

nums =[1, 2, 4, 1, 4, 0, 0, 0]

print(linear_serach_array(nums=nums,target=5))
