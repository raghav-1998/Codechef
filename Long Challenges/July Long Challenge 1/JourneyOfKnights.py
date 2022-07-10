"""
Chef has an 8*8 chessboard. He placed a knight on the square (X1,Y1). Note 
that, the square at the intersection of the ith row and jth column is denoted by 
(i,j).

Chef wants to determine whether the knight can end up at the square (X2,Y2) in 
exactly 100 moves or not.

For reference, a knight can move to a square which is:

- One square horizontally and two squares vertically away from the current 
  square, or
- One square vertically and two squares horizontally away from the current 
  square
A visual description of this may be found here

Input Format
- The first line contains a single integer T — the number of test cases. Then the 
  test cases follow.
- The first and only line of each test case contains 4 integers X1,Y1,X2,Y2 — 
  where (X1,Y1) denotes the starting square of the knight and (X2,Y2) 
  denotes the ending square of the knight.

Output Format
For each test case, output YES if knight can move from (X1,Y1) to (X2,Y2) in 
exactly 100 moves. Otherwise, output NO.

You may print each character of YES and NO in uppercase or lowercase (for 
example, yes, yEs, Yes will be considered identical).

Constraints
1≤T≤1000
1≤X1,Y1,X2,Y2≤8

Sample Input 1 
3
1 1 1 1
8 8 7 6
8 8 8 6

Sample Output 1 
YES
NO
YES

"""

if __name__=="__main__":
    t=int(input())
    while(t):
        x1,y1,x2,y2=[int(i) for i in input().strip().split(' ')]

        if((abs((x1-x2)%2==0)and abs((y1-y2)%2==0)) or (abs((x1-x2)%2!=0)and abs((y1-y2)%2!=0))):
            print("YES")
        else:
            print("NO")

        t-=1