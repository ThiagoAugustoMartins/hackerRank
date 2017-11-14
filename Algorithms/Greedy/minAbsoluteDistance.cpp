/*
    First of all find the best local solution between the two first pair of elements
    and after that try to find a better one in a sorted array, because the previous solution
    could already have been the best, and since the array is sorted we have only to check the pairs
*/

#include <bits/stdc++.h>

using namespace std;

int minimumAbsoluteDifference(int n, vector <int> arr) {
    // Complete this function
    sort(arr.begin(), arr.end());
    int min = INT_MAX;
    for(int i = 0; i < n - 1; i++){
        if(abs(arr[i] - arr[i + 1]) < min)
            min = abs(arr[i] - arr[i + 1]);
    }
    return min;
}

int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for(int arr_i = 0; arr_i < n; arr_i++){
       cin >> arr[arr_i];
    }
    int result = minimumAbsoluteDifference(n, arr);
    cout << result << endl;
    return 0;
}