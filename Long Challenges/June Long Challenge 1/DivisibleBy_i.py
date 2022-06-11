"""
You are given an integer N.

Construct a permutation P of length N such that

For all i (1≤i≤N−1), i divides abs(Pi+1−Pi).
Recall that a permutation of length N is an array where every integer from 1 to N occurs exactly once.

It can be proven that for the given constraints at least one such P always exists

Input Format
- The first line of input contains a single integer T, denoting the number of test 
  cases. The description of T test cases follow.
- The only line of each test case contains an integer N - the length of the array to be constructed.

Output Format
For each test case, output a single line containing N space-separated integers 
P1,P2,…,PN, denoting the elements of the array P.

If there exist multiple such arrays, print any.

Constraints
1≤T≤5⋅10^4 
2≤N≤10^5
The sum of N over all test cases does not exceed 10^5

Sample Input 1 
2
2
3

Sample Output 1 
1 2
2 1 3

"""


if __name__=="__main__":
    t=int(input())
    while(t):
        n=int(input())

        l=[0 for i in range(n)]
        l[n-1]=n
        k=n

        for i in range(1,n):
            if(i%2!=0):
                l[n-1-i]=k-(n-i)
                k=l[n-1-i]
            else:
                l[n-1-i]=k+(n-i)
                k=l[n-1-i]
        
        for i in range(n):
            print(l[i],end=' ')
        
        print()
        t-=1

