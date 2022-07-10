"""
There are N children and Chef wants to give them 1 candy each. Chef already 
has X candies with him. To buy the rest, he visits a candy shop. In the shop, 
packets containing exactly 4 candies are available.

Determine the minimum number of candy packets Chef must buy so that he is 
able to give 1 candy to each of the N children

Input Format
- The first line of input will contain a single integer T, denoting the number of 
  test cases.
- The first and only line of each test case contains two integers N and X — the 
  number of children and the number of candies Chef already has.

Output Format
For each test case, output the minimum number of candy packets Chef must buy 
so that he is able to give 1 candy to each of the N children.

Constraints
- 1≤T≤1000 
- 1≤N,X≤100

Sample Input 1 
4
20 12
10 100
10 9
20 9

Sample Output 1 
2
0
1
3

"""

if __name__=="__main__":
    t=int(input())
    while(t):
        N,X=[int(i) for i in input().strip().split(' ')]

        #if N<=X, no need to buy extra packets
        if(N<=X):
            print("0")
        else:
            #if extra candies required are divisible by 4
            if((N-X)%4==0):
                print((N-X)//4)
            
            else:
                print(((N-X)//4)+1)

        t-=1