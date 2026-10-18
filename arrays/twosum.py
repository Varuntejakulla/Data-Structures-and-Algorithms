def twosum(nums,target):
    hash_map={}
    for i ,num in enumerate(nums):
        remaining = target-nums[i]
        if remaining in hash_map:
            return [hash_map[remaining],i]
        hash_map[nums[i]]=i
    return []


nums=[1,3,5,23,2]
print(twosum(nums=nums,target=25))