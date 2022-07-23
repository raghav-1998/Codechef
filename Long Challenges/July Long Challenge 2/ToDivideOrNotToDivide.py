"""
Alice likes all the numbers which are divisible by A. Bob does not like the numbers 
which are divisible by B and likes all the remaining numbers. Determine the smallest 
number greater than or equal to N which is liked by both Alice and Bob. Output −1 if 
no such number exists.

Input Format
- The first line contains a single integer T — the number of test cases. Then the test 
  cases follow.
- The first and only line of each test case contains three space-separated integers A, B 
  and N — the parameters mentioned in the problem statment

Output Format
For each test case, output the smallest number ≥ N which is divisible by A and is not 
divisible by B. Output −1 if no such number exists.

Constraints
1≤T≤1000
1≤A,B,N≤10^9

Sample Input 1 
3
5 2 11
4 3 24
7 7 100

Sample Output 1 
15
28
-1

"""

if __name__=="__main__":
    t=int(input())
    while(t):
        a,b,n=[int(i) for i in input().strip().split(' ')]
        if(a%b==0):
            print("-1")
        else:
            if(n%a!=0):
                n+=a-(n%a)
            
            while(not(n%a==0 and n%b!=0)):
                n+=a
            
            print(n)
            
        t-=1 