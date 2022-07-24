"""
For an array A of length N, let F(A) denote the sum of the product of all the 
subarrays of A. Formally,

F(A)=∑L=1N∑R=LN(∏i=LRAi)
For example, let A=[1,0,1], then there are 6 possible subarrays:

Subarray [1,1] has product =1
Subarray [1,2] has product =0
Subarray [1,3] has product =0
Subarray [2,2] has product =0
Subarray [2,3] has product =0
Subarray [3,3] has product =1
So F(A)=1+1=2.

Given a binary array A, determine the sum of F(A) over all the N! orderings of 
A modulo 998244353.

Note that orderings here are defined in terms of indices, not elements; which is 
why every array of length N has N! orderings. For example, the 3!=6 
orderings of A=[1,0,1] are:

[1,0,1] corresponding to indices [1,2,3]
[1,1,0] corresponding to indices [1,3,2]
[0,1,1] corresponding to indices [2,1,3]
[0,1,1] corresponding to indices [2,3,1]
[1,1,0] corresponding to indices [3,1,2]
[1,0,1] corresponding to indices [3,2,1]

Input Format
- The first line of input will contain a single integer T, denoting the number of 
  test cases.
- Each test case consists of multiple lines of input.
  - The first line of each test case contains a single integer N denoting the le
  - The second line contains N space-separated integers denoting the array 
    A.

Output Format
For each test case, output the sum of F(A) over all the N! orderings of A, 
modulo 998244353

Constraints
1≤T≤1000
1≤N≤10^5
0≤Ai≤1
The sum of N over all test cases won't exceed 2⋅10^5

Sample Input 1 
4
3
1 0 1
1
0
2
1 1
4
1 1 0 1

Sample Output 1 
16
0
6
120

"""
global fac,inv,finv,Mod
fac=[0]*1000001
inv=[0]*1000001
finv=[0]*1000001
Mod=998244353

def C(x,y):
    if(x<0 or y>x):
        return 0
    
    return fac[x]*finv[y]%Mod*finv[x-y]%Mod

if __name__=="__main__":
    fac[0]=inv[0]=inv[1]=finv[0]=finv[1]=1
    for i in range(1,1000001):
        fac[i]=fac[i-1]*i%Mod
    
    for i in range(2,1000001):
        inv[i]=Mod-Mod//i*inv[Mod%i]%Mod
    
    for i in range(2,1000001):
        finv[i]=finv[i-1]*inv[i]%Mod

    
    t=int(input())
    while(t):
        c0=c1=a=0
        n=int(input())
        
        lis=[int(i) for i in input().strip().split(' ')]

        for i in range(n):
            if(lis[i]==0):
                c0+=1
            else:
                c1+=1

        for i in range(c1+1):
            a=(a+i*C(c1+c0-i,c0))%Mod
        
        ans=(((a*(c0+1)-C(c1+c0-2,c0-1))%Mod+Mod)%Mod+C(c1+c0-2,c0-1))*fac[c1]%Mod*fac[c0]%Mod

        print(ans)
        t-=1


