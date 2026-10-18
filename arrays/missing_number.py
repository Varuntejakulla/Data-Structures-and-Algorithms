def missing_numbers(nums:list):

    for i in range(len(nums)+1):
        if i not in nums:
            return i
    return 



nums = [1,3,2,0]
print(missing_numbers(nums=nums))



def missing_number_using_hashmap(nums:list):
    freq={}
    for i in range(0,len(nums)+1):

        freq[i]=0
    for num in nums:
        freq[num]=1

    for k,v in freq.items():
        if v==0:
            return k
    

def missing_number_using_opt(nums:list):
    return (len(nums)*(len(nums)+1)//2 -sum(nums))


print(missing_number_using_opt(nums=nums))


