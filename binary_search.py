"""
In this code, we will write a binary search algorithm 
so that we can search a given value in a list in O(lgn) time
"""
list1 = [1,3,5,6,7,9]
value = 10
def binary_search(input_array, value):
    low = 0
    high = len(input_array)-1
    while low <= high:
        mid = (low + high) / 2
        if input_array[mid] == value:
            return mid
        elif input_array[mid] < value:
            low = mid +1
        else:
            high = mid -1
    return -1
print(binary_search(list1, value))


            
