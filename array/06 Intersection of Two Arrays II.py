def intersect(nums1, nums2):
    nums1 = sorted(nums1)
    nums2 = sorted(nums2)
    intersect = []
    i, j = 0, 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            intersect.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
    
    return intersect

        
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(intersect(nums1, nums2))
