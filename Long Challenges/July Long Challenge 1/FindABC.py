"""
Chef has 3 hidden numbers A,B, and C such that 0≤A,B,C≤N.

Let f be a function such that f(i)=(A⊕i)+(B⊕i)+(C⊕i). Here ⊕ 
denotes the bitwise XOR operation.

Given the values of f(0),f(1),…,f(N), determine the values of A,B, and C.

It is guaranteed that at least one tuple exists for the given input. If there are 
multiple valid tuples of A,B,C, print any one.

Input Format
- The first line of input will contain a single integer T, denoting the number of 
test cases.
- Each test case consists of multiple lines of input.
  - The first line of each test case contains a single integer N denoting the 
    upper bound on the values of A,B,C.
  - Next line contains N+1 space-separated integers denoting 
    f(0),f(1),…,f(N).

Output Format
For each test case, output on a new line, three space-separated integers, the 
values of A,B, and C. If there are multiple valid tuples of A,B,C, print any one.

Constraints
1≤T≤2⋅10^4
2≤N≤10^5
Sum of N over all test cases does not exceed  2⋅10^5

Sample Input 1 
3
2
0 3 6
2
4 7 2
5
9 6 11 8 13 10

Sample Output 1 
0 0 0
2 0 2
1 3 5

"""

def highestPowerOf2(n):
    res=0

    for i in range(n,0,-1):
        if((i & (i-1))==0):
            return i


if __name__=="__main__":
    t=int(input())
    while(t):
        n=int(input())
        lis=[int(i) for i in input().strip().split(' ')]

        ans=[0]*3
        i=highestPowerOf2(n)

        while(i>0):
            diff=lis[i]-lis[0]
            if(diff<0):
                diff*=-1
                count=diff//i
                if(count==1):
                    count=2
                    if((ans[0]^i)<=n):
                        ans[0]^=i
                        count-=1
                    if(count and (ans[1]^i)<=n):
                        ans[1]^=i
                        count-=1
                    if(count>0 and (ans[2]^i)<=n):
                        ans[2]^=i
                
                elif(count==3):
                    ans[0]^=i
                    ans[1]^=i
                    ans[2]^=i
                
            else:
                count=diff//i
                if(count==1):
                    if((ans[0]^i)<=n):
                        ans[0]^=i
                    elif((ans[1]^i)<=n):
                        ans[1]^=i
                    else:
                        ans[2]^=i
            
            ans.sort()

            i//=2
        
        print(ans[0],ans[1],ans[2])
        t-=1

