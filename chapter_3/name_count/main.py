def count_names(list_of_lists, target_name):
    
    count = 0

    for i in list_of_lists:
        #iterates though each element in the nested list and counts each occurance of the target name
        for j in i:
            if target_name in j:
                count += 1
    
    return count

 #time complexity is O(n), but O(mn) if we consider m to be the number of lists and n the average lenght of a list