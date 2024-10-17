def median_followers(nums):
    sorted_list = sorted(nums)

#return None if the list is empty
    if nums == []:
        return None
#finding the center of the list
    median_index = len(sorted_list) / 2
    
    median = 0
#if the list doesnt have a perfect center, we return average of the two closest elements
    if median_index % 2 == 1:
        median_index = int(median_index)
        median = (sorted_list[median_index] + sorted_list[median_index - 1]) / 2
        return median
    else:
        median_index = int(median_index)
        median = sorted_list[median_index]
        return median
    
