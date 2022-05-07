"""
Chef has started developing interest in playing chess, and was learning how the Queen moves.

Chef has an empty N×N chessboard. He places a Queen at (X,Y) and wonders - What are the number of cells that are under attack by the Queen?

Notes:

- The top-left cell is (1,1), the top-right cell is (1,N), the bottom-left cell is (N,1) and the bottom-right cell is (N,N).
- The Queen can be moved any number of unoccupied cells in a straight line vertically, horizontally, or diagonally.
- The cell on which the Queen is present, is not said to be under attack by the Queen.

Input Format
- The first line contains a single integer T - the number of test cases. Then the test cases follow.
- The first and only line of each test case contains three integers N, X and Y, as described in the problem statement.

Output Format
For each test case, output in a single line, the total number of cells that are under attack by the Queen.

Sample Input 1 
5
1 1 1
3 2 2
3 2 1
2 2 2
150 62 41

Sample Output 1 
0
8
6
3
527

"""


t=int(input())
while(t):
   n,x,y=[int(i) for i in input().strip().split(' ')]
   if(x==1 or y==1 or x==n or y==n):
      ans=(n-1)*3
   else:
      ans=(n-1)*3
      if(x>n//2):
         x=(n+1)-x
      if(y>n//2):
         y=(n+1)-y
      a=min(x,y)
      if(n%2!=0 and x==y and x==(n//2)+1):
         ans+=(n-1)
      else:
         ans+=(a-1)*2
   
   print(ans)
   t-=1