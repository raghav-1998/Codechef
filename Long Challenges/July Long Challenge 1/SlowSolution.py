"""
Chef is trying to solve a problem having T test cases, where, for each test case he 
is given a single integer N.

Chef has an algorithm which takes exactly N2 iterations for a test case with value 
N.

The constraints of the problem are as follows:

1≤T≤maxT
1≤N≤maxN
Sum of N over all test cases does not exceed sumN.

Given the values maxT,maxN, and sumN, determine the maximum number 
of iterations Chef's algorithm can take for any valid input file satisfying all the 
constraints.

Formally speaking, find the maximum value of N1^2+N2^2+⋯+Nt^2 for:

1≤T≤maxT
1≤Ni≤maxN
N1+N2+N3+⋯+NT≤sumN

Input Format
- The first line of input will contain a single integer T, denoting the number of 
  test cases.
- Each test case consists of single line consisting of three integers 
  maxT,maxN, and sumN.

Output Format
For each test case, output the the maximum number of iterations Chef's algorithm 
can take in any valid test file.

Constraints
1≤T≤1000
1≤maxT≤maxN≤sumN≤10^4

Sample Input 1 
4
10 100 200
3 10 100
1000 1000 2200
100 100 100

Sample Output 1 
20000
300
2040000
10000

"""

if __name__=="__main__":
    t=int(input())
    while(t):
        maxT,maxN,sumN=[int(i) for i in input().strip().split(' ')]

        quot=sumN//maxN
        rem=sumN%maxN

        if(quot+1<=maxT):
            ans=(quot*(maxN*maxN))+(rem*rem)
        else:
            ans=maxT*(maxN*maxN)
        
        print(ans)

        t-=1