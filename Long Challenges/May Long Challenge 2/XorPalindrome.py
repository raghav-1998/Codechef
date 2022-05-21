'''
You are given a binary string A of length N.

You can perform the following type of operation on the string A:

Choose two different indices i and j (1≤i,j≤N);
Change Ai and Aj to Ai⊕Aj. Here ⊕ represents the bitwise XOR operation.
Find the minimum number of operations required to convert the given string into a palindrome.

Input Format
- First line of the input contains T, the number of test cases. Then the test cases follow.
- First line of each test case contains an integer N denoting the size of the string.
- Second line of each test case contains a binary string A of length N containing 0s and 1s only.

Output Format
For each test case, print the minimum number of operations required to make the string a palindrome.

Constraints
- 1≤T≤1000
- 1≤N≤2⋅105
- Sum of N over all test cases does not exceeds 2*10^5.

Sample Input 1 
2
5
11011
7
0111010

Sample Output 1 
0
1
'''

def calcMinOperation(inp,n):
    beg=0
    end=n-1
    count=0

    while(beg<end):
        if(inp[beg]!=inp[end]):
            count+=1
        beg+=1
        end-=1
    
    if(count%2==0):
        ans=count//2
    else:
        ans=count//2+1
    return ans

if __name__=="__main__":
    t=int(input())

    while(t):
        n=int(input())
        inp=input()

        print(calcMinOperation(inp,n))
        t-=1