'''
You are given an array A of length N.
Determine the count of subarrays of A which contain their length as an element.
Formally, count the number of pairs (L,R) (1≤L≤R≤N) such that: (R-L+1)∈{AL,AL+1,…,AR}.

Input Format
- First line will contain T, number of test cases. Then the test cases follow.
- First line of each test case contains an integer N denoting the length of the array A.
- Second line of each test case contains N space-separated integers A1,A2,…,AN - denoting the array A.

Output Format
For each test case, output the count of subarrays containing their lengths.

Constraints
1≤T≤1000
1≤N≤2⋅105
1≤Ai≤N
Sum of N over all test cases does not exceed 5*10^5.

Sample Input 1 
3
3
1 2 1
5
2 3 1 3 5
10
10 7 4 4 2 9 2 1 9 3

Sample Output 1 
4
6
15

'''

if __name__=="__main__":
    t=int(input())
    while(t):
        n=int(input())
        m=n+1
        arr=[int(i) for i in input().strip().split(' ')]
        p=[[-1] for i in range(m)]
        
        for i in range(n):
            p[arr[i]]+=[i]
        
        ans=n*(m)//2
        
        for i in range(1,m):
            p[i]+=[n]
            ans-=sum(max(0,p[i][j+1]-p[i][j]-i) for j in range(len(p[i])-1))
        
        print(ans)
    
        t-=1
