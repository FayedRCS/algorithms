def merge_sort(nums):
    
    if len(nums) < 2:
        return nums
    
    #finding a int value for the list median
    half = len(nums) // 2

    #splitting list into two "slices" then we use recursion to repeat the process --> we're left with each element in it's own list
    left_side = nums[:half]
    right_side = nums[half:]

    #recursion bit
    leftie_sort = merge_sort(left_side)
    rightie_sort = merge_sort(right_side)

    return merge(leftie_sort, rightie_sort)


def merge(first, second):
    
    final = []

    i = 0
    j = 0

    #"merging" both lists, incrementing our starter variables i,j respectively 
    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            final.append(first[i])
            i += 1
        else:
            final.append(second[j])
            j += 1
            
    #adding, or extending rather the final with the rememnants of list
    final.extend(first[i:])
    final.extend(second[j:])
    

    return final