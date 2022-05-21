'''
In mathematics, the degree of polynomials in one variable is the highest power of the variable in the algebraic expression with non-zero coefficient.

Chef has a polynomial in one variable x with N terms. The polynomial looks like A0⋅x0+A1⋅x1+…+AN−2⋅xN−2+AN−1⋅xN−1 where Ai−1 denotes the coefficient of the ith term xi−1 for all (1≤i≤N).

Find the degree of the polynomial.

Note: It is guaranteed that there exists at least one term with non-zero coefficient.In mathematics, the degree of polynomials in one variable is the highest power of the variable in the algebraic expression with non-zero coefficient.

Chef has a polynomial in one variable x with N terms. The polynomial looks like A0⋅x0+A1⋅x1+…+AN−2⋅xN−2+AN−1⋅xN−1 where Ai−1 denotes the coefficient of the ith term xi−1 for all (1≤i≤N).

Find the degree of the polynomial.

Note: It is guaranteed that there exists at least one term with non-zero coefficient.

Input Format
- First line will contain T, number of test cases. Then the test cases follow.
- First line of each test case contains of a single integer N - the number of terms in the polynomial.
- Second line of each test case contains of N space-separated integers - the ith integer Ai−1 corresponds to the coefficient of xi−1.

Output Format
For each test case, output in a single line, the degree of the polynomial.

Constraints
- 1≤T≤100
- 1≤N≤1000
- −1000≤Ai≤1000
- Ai≠0 for at least one (0≤i<N).

Sample Input 1 
4
1
5
2
-3 3
3
0 0 5
4
1 2 4 0

Sample Output 1 
0
1
2
2

'''

def degreeOfPolynomial(inp,n):
    for i in range(n-1,-1,-1):
        if(inp[i]!=0):
            return i

if __name__=="__main__":
    t=int(input())
    while(t):
        n=int(input())
        inp=[int(i) for i in input().strip().split(' ')]
        print(degreeOfPolynomial(inp,n))
        t-=1