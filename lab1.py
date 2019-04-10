def max_list_iter(int_list): # must use iteration not recursion
    if int_list == None:     # if int_list is none then raises value error
        raise ValueError
    elif len(int_list) == 0: # if the list is empty then return None
        return None
    x = int_list[0]          # sets the initial max value to be tested in the loop as the first value in the list
    for i in int_list:       # loops through all values in int_list and updates x when a larger value is found in the list
        if i > x:
            x = i
    return x

def reverse_rec(int_list):    # must use recursion
    if int_list == None:      # if int_list is none then raises value error
        raise ValueError
    if len(int_list) == 0:    # if int_list is empty, return an empty list
        return []
    return reverse_rec(int_list[1:len(int_list)]) + int_list[0:1] # recursive step: repeatedly adds lists of the numbers in reverse order 

    #"""recursively reverses a list of numbers and returns the reversed list
    #If list is None, raises ValueError"""

def bin_search(target, low, high, int_list):  # must use recursion
    mid = (low + high) // 2                   # sets mid to the middle index of the list
    if int_list == None:                      # if int_list is none then raise value error
        raise ValueError
    elif target < int_list[low] or target > int_list[high]:   #if the target is higher than or lower than all the values in the list, return None
        return None
    if int_list[mid] == target:               # if the value in the list at index mid is the target, returns mid
        return mid         
    if int_list[mid] > target:                # if the target is less than the value at index mid then change the high to one less than the mid
        high = mid - 1
    elif int_list[mid] < target:              # if the target is greater than the value at index mid then change the low to one more than the mid
        low = mid + 1
    return bin_search(target, low, high, int_list)    # recursive step: calls bin_search with the new values for low and high

    #"""searches for target in int_list[low..high] and returns index if found
    #If target is not found returns None. If list is None, raises ValueError """
