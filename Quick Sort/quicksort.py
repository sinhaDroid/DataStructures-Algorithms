"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array, first, last):
    
    if first < last:
        pivot = partition(array, first, last)

        quicksort(array, first, pivot - 1)
        quicksort(array, pivot + 1, last)

    return array

def partition(array, first, last):
    pivotValue = array[first]

    left = right = first + 1

    while right <= last:
        if array[right] < pivotValue:
            array[left], array[right] = array[right], array[left]
            left += 1

        right += 1

    array[first], array[left - 1] = array[left - 1], array[first]
    return left - 1

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test, 0, len(test) - 1)
