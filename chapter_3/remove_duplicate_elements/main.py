def remove_duplicates(nums):
    
    no_dupes = []

    #appending to the new list if the element is not contained already
    for i in nums:
        if i not in no_dupes:
            no_dupes.append(i)
    
    return no_dupes
