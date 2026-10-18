def inseting_value(nums:list,insert_value):

    low = 0
    high = len(nums)
    value_index=-1
    while low<=high:

        mid = (low+ high) //2  

        if nums[mid] >=insert_value:
            value_index = mid
            high =mid-1

            

        else:
            low = mid+1
        
    return value_index

nums =[1,2,3,5,6]


print(inseting_value(nums=nums,insert_value=4))

    


