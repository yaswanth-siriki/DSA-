def union_sorted_arrays(nums1, nums2):
    i, j = 0, 0
    union = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            if len(union) == 0 or union[-1] != nums1[i]:
                union.append(nums1[i])
            i += 1
        else:
            if len(union) == 0 or union[-1] != nums2[j]:
                union.append(nums2[j])
            j += 1
    while i < len(nums1):
        if union[-1] != nums1[i]:
            union.append(nums1[i])
        i += 1
    while j < len(nums2):
        if union[-1] != nums2[j]:
            union.append(nums2[j])
        j += 1
    return union
nums1 = [1, 2, 2, 3, 4]
nums2 = [2, 3, 5]
print(union_sorted_arrays(nums1, nums2))