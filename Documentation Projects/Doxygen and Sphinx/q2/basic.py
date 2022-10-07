def binarySearch(arr, val):
    """Splits a array in half

    :param arr: Given array to split
    
    :type arr: Pointer
    :param val: Value to find
    :type val: integer
    :return: Returns m or -1
    :rtype: integer
    """
    l = 0
    r = len(arr) - 1
    while l < r:
        m = l + (r - l) // 2
        if arr[m] > val:
            r = m
        elif arr[m] < val:
            l = m
        else:
            return m
    return -1
