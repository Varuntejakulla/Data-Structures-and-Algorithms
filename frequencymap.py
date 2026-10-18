def frequencymap(nums:list):
    freq_map ={}
    for num in nums:
        if num in freq_map:
            freq_map[num]+=1
        else:
            freq_map[num]=1
    return freq_map

#here we use the dictory.get(num,0)+1 if  find same it count to 2 
def frequency_map_optimization(nums:list):
    freq_map={}
    for num in nums:
        freq_map[num]= freq_map.get(num,0)+1
    return freq_map


def frequency_charatcter(word:str):
    hash_list ={}

    for ch in word:
        hash_list[ch] =hash_list.get(ch,0)+1

    repeated_count =0
    for ch in hash_list:
        if hash_list[ch]>1:
            repeated_count+=1
    return repeated_count





    
    



list1=[7,2,6,5,8,2,3,3]
list2= [3,5,6,7,8,9]


print(frequencymap(list1))
print(frequency_map_optimization(list1))

print(frequency_charatcter("hello"))       # 1

