'''
You are given an array A of length N.

You can perform the following operation on the array any number of times:

Choose any subsequence S of the array A and a positive integer X such that X is a power of 2 and subtract X from all the elements of the subsequence S.
Find the minimum number of operations required to make all the elements of the array equal to 0.

Input Format
- First line will contain T, number of test cases. Then the test cases follow.
- First line of each test case contains an integer N denoting the length of the array A.
- Second line contains N space-separated integers A1,A2,…,AN - denoting the elements of array A.

Output Format
For each test case, output in a single line, the minimum number of moves required to make all the elements of the array A equal to 0.

Constraints
- 1≤T≤1000
- 1≤N≤105
- 0≤Ai≤109
- Sum of N over all test cases do not exceed 2*10^5

Sample Input 1 
4
3
2 2 2
4
2 2 2 4
2
0 0
3
1 2 3

Sample Output 1 
1
2
0
2

'''

import math as m

def minOperation(inp,n):
    unique=list(set(inp))

    count=0

    powOfTwo=set()
    for num in unique:
        if(num!=0):
            if m.floor(m.log2(num))==m.ceil(m.log2(num)):
                if(num not in powOfTwo):
                    powOfTwo.add(num)
                    count+=1
            else:
                while(num!=0):
                    nearPowOfTwo=pow(2,m.floor(m.log2(num)))
                    if(nearPowOfTwo not in powOfTwo):
                        powOfTwo.add(nearPowOfTwo)
                        count+=1
                    num-=nearPowOfTwo
    
    return count



if __name__=="__main__":
    t=int(input())

    while(t):
        n=int(input())
        inp=[int(i) for i in input().strip().split(' ')]

        print(minOperation(inp,n))

        t-=1