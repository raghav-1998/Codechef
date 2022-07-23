"""
Chef has two numbers N and M. He calls a pair of numbers (A,B) good if it 
satisfies the following conditions:

- 1≤A,B≤M
- gcd(A,B)≥N
Chef wants to find a good pair (A,B) such that the value of |A−B| is 
maximized. Can you help Chef? (Here |X| represents the absolute value of X).

If there are multiple good pairs for which the value of |A−B| is maximized, you 
can print any of them. It can be proved that under the given constraints, at least 
one good pair always exists.

Input Format
- The first line contains a single integer T — the number of test cases. Then the 
   test cases follow.
- The first line of each test case contains two integers N and M — the 
  parameters mentioned in the statment.

Output Format
For each test case, output two integers A and B such that (A,B) is a good pair 
and the value of |A−B| is maximized

Constraints
1≤T≤1000
1≤N≤10^5
N≤M≤10^9
Sum of N over all test cases does not exceed 2⋅10^5

Sample Input 1 
3
5 6
2 8
10 89

Sample Output 1 
6 6
8 2
11 88

"""

if __name__=="__main__":
    t=int(input())

    while(t):
        n,m=[int(i) for i in input().strip().split(' ')]
        if m<2*n:
            print(m,m)
        elif m%n==0:
            print(m,n)
        else:
            res=0
            res_1=0
            quot=m//2
            if m>=2*n:
                quot=2*n
            Min=0
            for i in range(n,quot):
                d=m//i
                c_min=(i*d)-i
                if(c_min>Min):
                    res=i
                    res_1=i*d
                    Min=c_min
            
            print(res,res_1)

        t-=1