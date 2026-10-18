def remove_duplicate_from_sorted_array(nums:list):
    hash_map ={}
    
    for num in nums:
        if num not in hash_map:
            hash_map[num]=0
    

    return list(hash_map.keys()) 

nums =[1,3,5,1,1,2,4,2]

print(remove_duplicate_from_sorted_array(nums=nums))            



def remove_duplicates_pointers(nums):

    if not nums:
        return 0

    k=1
    for i in range(1,len(nums)):
        if nums[i]!=nums[i-1]:
            nums[k]=nums[i]
            k+=1
    return k


nums = [1, 1, 2, 2, 3, 3, 4]

print(remove_duplicates_pointers(nums=nums))


