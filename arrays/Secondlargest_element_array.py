def Second_largest_element(nums:list):
    nums.sort()
    return nums[-2]


nums =[1,2,-4,23,652763,-3]

print(Second_largest_element(nums=nums))


def Second_largest(nums:list):
    largest =float("-inf")
    second_largest =float("-inf")

    for i in range(0,len(nums)):
        largest = max(largest,nums[i])

    for i in range(0,len(nums)):
        if nums[i]>second_largest and nums[i]!=largest:
            second_largest=nums[i]

    return second_largest


print(Second_largest(nums=nums))



def second_largest_element(nums:list):
    largest =float("-inf")
    second_largest =float("-inf")

    for i in range(len(nums)):
        if nums[i]>largest:
            second_largest=largest
            largest=nums[i]
        elif nums[i]>second_largest and nums[i]!=largest:
            second_largest=nums[i]


    return second_largest


print(second_largest_element(nums=nums))