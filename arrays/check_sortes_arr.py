def checkis_sorted_arr(nums:list):
    
    # for i in range(0,len(nums)):
    #     if nums[i]<nums[i+1]:
    #         return True
    return sorted(nums)

# nums =[1,2,-4,23,652763,-3]
nums2=[1,2,3,4,5,67,88,99,100]

print(checkis_sorted_arr(nums=nums2))



