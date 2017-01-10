#Day 6: Let's Review

###Objective 
Today we're expanding our knowledge of Strings and combining it with what we've already learned about loops. Check out the Tutorial tab for learning materials and an instructional video!

###Task 
Given a string, _S_, of length _N_ that is indexed from _0_ to _N - 1_, print its even-indexed and odd-indexed characters as _2_ space-separated strings on a single line (see the Sample below for more detail).

**Note:** _0_ is considered to be an even index.

###Input Format

The first line contains an integer, _T_ (the number of test cases). 
Each line _i_ of the _T_ subsequent lines contain a String, _S_.

###Constraints

- 1 <= T <= 10
- 2 <= length of S <= 10000

###Output Format

For each String _Sj_ (where _0 <= j <= T - 1_), print _Sj's_ even-indexed characters, followed by a space, followed by _Sj's_ odd-indexed characters.

###Sample Input

```
2
Hacker
Rank
```

###Sample Output

```
Hce akr
Rn ak
```

###Explanation

**Test Case 0:**  
 
```
S = "Hacker"
S[0] = "H"
S[1] = "a"
S[2] = "c"
S[3] = "k"
S[4] = "e"
S[5] = "r"
``` 

The even indices are 0, 2, and 4, and the odd indices are 1, 3, and 5. We then print a single line of 2 space-separated strings; the first string contains the ordered characters from S's even indices (_Hce_), and the second string contains the ordered characters from S's odd indices (_akr_).

**Test Case 1:**  

```
S = "Rank"
S[0] = "R"
S[1] = "a"
S[2] = "n"
S[3] = "k"
``` 

The even indices are 0 and 2, and the odd indices are 1 and 3. We then print a single line of 2 space-separated strings; the first string contains the ordered characters from S's even indices (Rn), and the second string contains the ordered characters from S's odd indices (ak).