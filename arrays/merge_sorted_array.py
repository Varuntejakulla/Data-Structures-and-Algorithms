def merge_sorted_array(nums1:list,nums2:list):
    merge_liist=set()
    i,j=0,0
    n,m=len(nums1),len(nums2)
    while i<n and j<m:
            merge_liist.add(nums1[i])
            merge_liist.add(nums2[j])
            i+=1
            j+=1
    while i < n:
        merge_liist.add(nums1[i])
        i += 1

    while j < m:
        merge_liist.add(nums2[j])

    return list(merge_liist)

nums1=[1, 2, 4, 1, 4, 0, 0, 0]
nums2=[1, 2, 4, 1, 4, 1,1,1]

print(merge_sorted_array(nums1=nums1,nums2=nums2))
