#Boat Trips
Alice owns a company that transports tour groups between two islands. She has _n_ trips booked, and each trip _i_ has _pi_ passengers. Alice has _m_ boats for transporting people, and each boat's maximum capacity is _c_ passengers.

Given the number of passengers going on each trip, determine whether or not Alice can perform all _n_ trips using no more than _m_ boats per individual trip. If this is possible, print Yes; otherwise, print No.

###Input Format

The first line contains three space-separated integers describing the respective values of _n_ (number of trips), _c_ (boat capacity), and _m_ (total number of boats). 
The second line contains _n_ space-separated integers describing the values of _po, p1, ..., pn-1_.

###Constraints
- 1 <= _n,c,m_ <= 100
- 1 <= _pi_ <= 100

###Output Format

Print Yes if Alice can perform all _n_ booked trips using no more than _m_ boats per trip; otherwise, print No.

###Sample Input 0

- 5 2 2
- 1 2 1 4 3

###Sample Output 0

- Yes

###Explanation 0

Alice has _m = 2_ boats and a maximum capacity of _c = 2_ passengers per boat. This means she can transport at most _m * c = 4_  passengers at a time.

There are _n = 5_ tour groups, and the largest tour group contains _p3 = 4_ passengers. Because Alice will be able to transport each group using _<= m_ boats per group, we print Yes.

###Sample Input 1

-5 1 2
-1 2 1 4 1

###Sample Output 1

-No

###Explanation 1

Alice has _m = 2_ boats and a maximum capacity of _c = 1_ passenger per boat. This means she can transport at most _m * c = 2_ passengers at a time.

There are _n = 5_ tour groups, and the largest tour group contains _p3 = 4_ passengers. Because Alice does not have enough boats to transport a group of four passengers, we print No.

