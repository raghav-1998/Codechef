"""
For an array A of length N, let F(A) denote the sum of the product of all the subarrays of A. Formally,

F(A)=∑L=1N∑R=LN(∏i=LRAi)
For example, let A=[1,0,1], then there are 6 possible subarrays:

Subarray [1,1] has product =1
Subarray [1,2] has product =0
Subarray [1,3] has product =0
Subarray [2,2] has product =0
Subarray [2,3] has product =0
Subarray [3,3] has product =1
So F(A)=1+1=2.

Given a binary array A, determine the value of F(A)

Input Format
- The first line of input will contain a single integer T, denoting the number of 
  test cases.
- Each test case consists of multiple lines of input.
  - The first line of each test case contains a single integer N denoting the 
    length of the array.
  - The second line contains N space-separated integers denoting the array 
    A.

Output Format
For each test case, output on a new line the value of  F(A) 

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
2
0
3
4

"""

if __name__=="__main__":
    t=int(input())

    while(t):
        n=int(input())
        arr=[int(i) for i in input().strip().split(' ')]

        ans=c=0

        for i in range(n):
            if(arr[i]==0):
                c=0
            else:
                c+=1
            ans+=c
        
        print(ans)
        
        t-=1