// Java code for linearly search x in arr[].  If x 
// is present  then return its  location,  otherwise
// return -1


import java.io.*;


class LinearSearch {

    // This function returns index of element x in arr[]
    int search(int arr[], int x) {
        for(int i = 0; i < arr.length; i++) {
            // Return the index of the element if the element
			// is found
            if(arr[i] == x)
                return i;
        }

        // return -1 if the element is not found
		return -1;
    }

    public static void main (String[] args) {
		
        // Setup
        int arr[] = {4, 6, 2, 7, 8, 12, 45, 3, 56, 67, 88, 23, 43};
        int res;

        // Test
        // Should print index of 12 i.e., 5
        LinearSearch linearSearch = new LinearSearch();
        res = linearSearch.search(arr, 12);

        System.out.println(res);
	}
}
