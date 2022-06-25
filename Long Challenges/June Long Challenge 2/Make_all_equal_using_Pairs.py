"""
Chef has an array A of length N.

In one operation, Chef can choose any two distinct indices i,j 
(1≤i,j≤N,i≠j) and either change Ai to Aj or change Aj to Ai.

Find the minimum number of operations required to make all the elements of the 
array equal.

Input Format
- First line will contain T, number of test cases. Then the test cases follow.
- First line of each test case consists of an integer N - denoting the size of array 
  A.
- Second line of each test case consists of N space-separated integers 
  A1,A2,…,AN - denoting the array A.

Output Format
For each test case, output the minimum number of operations required to make all 
the elements equal.

Constraints
- 1≤T≤100
- 2≤N≤1000
- 1≤Ai≤1000

Sample Input 1 
4
3
1 2 3
4
5 5 5 5
4
2 2 1 1
3
1 1 2

Sample Output 1 
2
0
2
1

"""

if __name__=="__main__":
    t=int(input())

    while(t):
        n=int(input())
        inp=[int(i) for i in input().strip().split(' ')]

        occurance={}
        for num in inp:
            if(num not in occurance):
                occurance[num]=1
            else:
                occurance[num]+=1
        
        ans=n-max(occurance.values())
        print(ans)
        t-=1