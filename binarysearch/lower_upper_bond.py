def lower_bond_array(nums:list,target):


    nums.sort()

    low =0
    high  = len(nums)
    lower_bond = -1

    while low < high:
        mid = low +high //2

        if nums[mid]>=target:
            lower_bond = mid
            high  =  mid-1
        else:
            low=mid+1
        

    return lower_bond



nums =[1,34,3,4,3,3,3,4,44,3,3,43]

print(lower_bond_array(nums,3))


def uppderbond(nums:list,target):
    nums.sort()
    print(nums)
    low =0 
    high = len(nums)
    higher_bond =len(nums)

    while low<=high:

        mid = (low+high)//2

        if nums[mid]>=target:
            
            higher_bond =mid
            high = mid-1

        else :
            low = mid+1


    return higher_bond


nums =[1,34,3,4,3,3,3,4,44,3,3,43]


print(uppderbond(nums=nums,target=3))



