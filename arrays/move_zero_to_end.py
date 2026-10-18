def move_to_end(nums:list):
    new_list = []
    for num in nums:
        if num==0:
            new_list.append(0)
            nums.remove(num)
    return nums+new_list


nums  = [1,2,4,0,0,1,4,0]
print(move_to_end(nums))
