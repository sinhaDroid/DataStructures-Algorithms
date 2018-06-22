// Javascript code for linearly search x in arr[].  If x
// is present then return its  location,  otherwise
// return -1


function search(arr, x) {

    var i;

    for (i = 0; i < arr.length; i++) {

        if (arr[i] == x)
            return i;
    }

    return -1;
}

// Setup
var arr = [4, 6, 2, 7, 8, 12, 45, 3, 56, 67, 88, 23, 43];

// Test
// Should print index of 12 i.e., 5
console.log(search(arr, 12));
