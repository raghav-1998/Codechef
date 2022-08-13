"""
You are given a positive integer X. Your task is to tell whether there exist two 
positive integers a and b (a>0,b>0) such that
                                2⋅a+2⋅b+a⋅b=X
If there exist positive integers a and b satisfying the above condition print YES, 
otherwise print NO.

Input Format
- The first line of input will contain a single integer T, denoting the number of 
  test cases.
- Each test case consists of single line containing a positive integer X

Output Format
For each test case, output on a new line YES or NO.

You may print each character of the string in either uppercase or lowercase (for 
example, the strings yes, YES, Yes, and yeS will all be treated as identical).

Constraints
- 1≤T≤100 
- 1≤X≤10^9

Sample Input 1 
4
2
5
6
12

Sample Output 1 
NO
YES
NO
YES

"""

if __name__=="__main__":
    t=int(input())
    while(t):
        X=int(input())

        i=1
        flag=0

        while(i*i<=X):
            if((X-(2*i))%(i+2)==0 and X!=(2*i)):
                flag=1
                break
            i+=1
        
        if(flag==1):
            print("YES")
        else:
            print("NO")
        
        t-=1