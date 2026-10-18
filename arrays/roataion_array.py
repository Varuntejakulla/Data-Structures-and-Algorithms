def rotating_array(nums):
    nums[:] = [nums[-1]] + nums[:-1]
    return nums


nums = [1, 2, 3, 4, 5]

print(rotating_array(nums))



def rotating_array2(nums):
    n =len(nums)
    temp =nums[n-1]
    for i  in range(n-2,-1,-1):
        nums[i+1]=nums[i]

    nums[0]=temp

    return nums

print(rotating_array2(nums=nums))