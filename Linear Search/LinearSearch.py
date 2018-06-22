# Python code for linearly search x in arr[].  If x
# is present then return its  location,  otherwise
# return -1


def search(arr, x):

    for i in range(len(arr)):

        if arr[i] == x:
            return i

    return -1


# Setup
arr = [4, 6, 2, 7, 8, 12, 45, 3, 56, 67, 88, 23, 43]

# Test
# Should print index of 12 i.e., 5
print search(arr, 12)
