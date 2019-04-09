def max_list_iter(int_list):  # must use iteration not recursion
    if int_list == None:
        raise ValueError
    elif len(int_list) == 0:
        return None
    x = int_list[0]
    for i in int_list:
        if i > x:
            x = i
    return x

def reverse_rec(int_list):   # must use recursion
    if int_list == None:
        raise ValueError
    if len(int_list) == 0:
        return []
    return reverse_rec(int_list[1:len(int_list)]) + int_list[0:1]
    #"""recursively reverses a list of numbers and returns the reversed list
    #If list is None, raises ValueError"""

def bin_search(target, low, high, int_list):  # must use recursion
    mid = (low + high) // 2
    if int_list == None:
        raise ValueError
    elif target < int_list[low] or target > int_list[high]:
        return None
    if int_list[mid] == target:
        return mid
    if int_list[mid] > target:
        high = mid - 1
    elif int_list[mid] < target:
        low = mid + 1
    return bin_search(target, low, high, int_list)
    #"""searches for target in int_list[low..high] and returns index if found
    #If target is not found returns None. If list is None, raises ValueError """
