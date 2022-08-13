"""
There are 2 trains A and B and N stations in a line from 1 to N in order. There 
is also an array P of length N−1 such that Pi (1≤i<N) denotes the 
amount of time any train takes to go from the i-th station to the (i+1)-th station.

Initially, both trains are at station 1. Train A departs from station 1 and stops 
directly at station N. For safety purposes, it is maintained that train B cannot 
depart from station i unless train A has already reached station (i+1) (1≤i<N).

Find the minimum time after which train B reaches station N, once train A 
departs from station 1

Input Format
- The first line of input will contain a single integer T, denoting the number of 
test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains an integer N, denoting number of 
      stations.
    - The next line contains N−1 space-separated integers, 
      P1,P2,…,PN−1.

Output Format
For each test case, output on a new line the minimum time after which train B 
reaches station N.

Constraints
- 1≤T≤100
- 2≤N≤10^5
- 1≤Pi≤10^3
- The sum of N over all test cases won't exceed 10^5.

Sample Input 1 
3
2
4
3
3 5
4
5 2 6

Sample Output 1 
8
13
19

"""

if __name__=="__main__":
    t=int(input())
    while(t):
        n=int(input())
        time=[int(i) for i in input().strip().split(' ')]
        ans_a=ans_b=0
        
        for i in range(n-1):
            ans_a+=time[i]
            if(ans_a>ans_b):
                ans_b=ans_a+time[i]
            
            else:
                ans_b+=time[i]
        
        print(ans_b)
        t-=1