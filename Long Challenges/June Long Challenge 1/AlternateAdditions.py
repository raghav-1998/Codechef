"""
Chef has 2 numbers A and B (A<B).

Chef will perform some operations on A.

In the ith operation:

Chef will add 1 to A if i is odd.
Chef will add 2 to A if i is even.
Chef can stop at any instant. Can Chef make A equal to B?

Input Format
- The first line contains a single integer T — the number of test cases. Then the test cases follow.
- The first and only line of each test case contains two space separated integers A and B

Output Format
- For each test case, output YES if Chef can make A and B equal, NO otherwise.

Note that the checker is case-insensitive. So, YES, Yes, yEs are all considered same.

Constraints
- 1≤T≤1000
- 1≤A<B≤10^9

Sample Input 1 
4
1 2
3 6
4 9
10 20

Sample Output 1 
YES
YES
NO
YES

"""

if __name__=="__main__":
    t=int(input())

    while(t):
        a,b=[int(i) for i in input().strip().split(' ')]
        
        diff=b-a

        if(diff%3==0 or diff%3==1):
            print("YES")
        else:
            print("NO")
        t-=1