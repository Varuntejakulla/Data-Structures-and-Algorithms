
def longest_qequence(nums:list):
    my_set=set()
    for i in range(len(nums)):
        my_set.add(nums[i])

    longest = 0
    for num in my_set:
        
        if num-1 not in my_set:
            x=num

            count=1
            seq=[num]
            while x+1 in my_set:
                seq.append(x)
                count+=1
                x+=1
                
        
            longest =max(longest,count)

    return longest,seq


nums =[1,3,2,4,5,2,10]
print(longest_qequence(nums=nums))



