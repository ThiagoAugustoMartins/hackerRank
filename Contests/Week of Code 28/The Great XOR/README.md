#The Great XOR

Given a long integer, _x_, count the number of values of _a_ satisfying the following conditions:

```
a ^ x > x
0 < a < x
```

where _a_ and _x_ are long integers and _^_ is the bitwise XOR operator.

You are given _q_ queries, and each query is in the form of a long integer denoting _x_. For each query, print the total number of values of _a_ satisfying the conditions above on a new line.

###Input Format

The first line contains an integer, _q_, denoting the number of queries. 
Each of the _q_ subsequent lines contains a long integer describing the value of _x_ for a query.

###Constraints

```
1 <= q <= 10^5
1 <= x <= 10^10
```

###Subtasks

For 50% of the maximum score:
```
1 <= q <= 10^3
1 <= x <= 10^4
```

###Output Format

For each query, print the number of values of _a_ satisfying the given conditions on a new line.

###Sample Input 0

```
2
2
10
```

###Sample Output 0

```
1
5
```

###Explanation 0

We perform the following _q = 2_ queries:

- For _x = 2_ the only value of _a_ satisfying _0 < a < x_ is _1_. This also satisfies our other condition, as _1 ^ 2 = 3_ and _3 > x_. Because we have one valid _a_ and there are no more values to check, we print _1_ on a new line.
- For _x = 10_, the following values of _a_ satisfy our conditions:

```
1 ^ 10 = 11
4 ^ 10 = 14 
5 ^ 10 = 15
6 ^ 10 = 12
7 ^ 10 = 13
```

Because there are five valid values of _a_, we print _5_ on a new line.