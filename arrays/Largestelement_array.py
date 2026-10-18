def largest_element_array(nums:list):

    return max(nums)


nums =[1,2,-4,23,652763,-3]

print(largest_element_array(nums=nums))


def largest_using_loop(nums:list):

    n= len(nums)
    largest= float("-inf")
    i=0
    while i<n:
        largest=max(largest,nums[i])
        i+=1
    return largest


print(largest_using_loop(nums=nums))