#Day 0: Mean, Median and Mode
###Objective 
In this challenge, we practice calculating the mean, median, and mode. Check out the Tutorial tab for learning materials and an instructional video!

####Task 
Given an array, _X_, of _N_ integers, calculate and print the the respective mean, median, and mode on separate lines. If your array contains more than one modal value, choose the numerically smallest one.

Note: Other than the modal value (which will always be an integer), your answers should be in decimal form, rounded to a scale of _1_ decimal place (i.e.,_12.3_ , _7.0_ format).

###Input Format

The first line contains an integer, _N_, denoting the number of elements in the array. 
The second line contains _N_ space-separated integers describing the array's elements.

###Constraints

- _10 <= N <= 2500_
- _0<= xi <= 10^5, where _xi_ is _i^th_ the  element of the array.

###Output Format

Print **3** lines of output in the following order:

Print the _mean_ on a new line, to a scale of **1** decimal place (i.e., _12.3_ , _7.0_).
Print the _median_ on a new line, to a scale of **1** decimal place (i.e., _12.3_ , _7.0_).
Print the _mode_ on a new line; if more than one such value exists, print the numerically smallest one.

###Sample Input

```
10
64630 11735 14216 99233 14470 4978 73429 38120 51135 67060
```

###Sample Output

```
43900.6
44627.5
4978
Explanation
```

**Mean:** 
We sum all _N_ elements in the array, divide the sum by _N_, and print our result on a new line.

```
 Mean = (x0 + x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9) / 10 = 439006 / 10 = 43900.6
```

**Median:** 
To calculate the median, we need the elements of the array to be sorted in either non-increasing or non-decreasing order. The sorted array _X = {4978, 11735, 14216, 14470, 38120, 51135, 64630, 67060, 73429, 99233}_. We then average the two middle elements:
```
- Median = (x4 + x5) / 2 = 89255 / 2 = 44627.5
```
and print our result on a new line.
**Mode:** 
We can find the number of occurrences of all the elements in the array:
```
 4978 : 1
11735 : 1
14216 : 1
14470 : 1
38120 : 1
51135 : 1
64630 : 1
67060 : 1
73429 : 1
99233 : 1
```
Every number occurs once, making _1_ the maximum number of occurrences for any number in _X_. Because we have multiple values to choose from, we want to select the smallest one, _4978_, and print it on a new line.