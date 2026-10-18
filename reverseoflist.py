
def reverseoflist(nums:list,left,right):
    if left>=right:
        return 

    nums[left],nums[right]=nums[right],nums[left]
    reverseoflist(nums,left+1,right-1)
    return nums


nums=[1,2,3,4,5,6]

print(reverseoflist(nums,0,len(nums)-1))


def palindrome(name):
    lenghth = len(name)
    left =0
    right =lenghth-1
    while left <right:
        if name[left]!=name[right]:
            return False
        left+=1
        right-=1
    return True

print(palindrome("daD"))



def palindromewitthresurcion(name,left,right):
    if left>=right:
        return True
    if name[left] != name[right]:
        return False
    
    return palindromewitthresurcion(name,left+1,right-1)

print(palindromewitthresurcion("dad",0,len("dad")-1))
    


def recursion_of_factorial(total,start,number):
    total*=start
    if  start==number:
        return total
    return recursion_of_factorial(total,start+1,number)
    


print(recursion_of_factorial(1,1,5))


