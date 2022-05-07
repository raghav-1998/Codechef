"""
Pushpa has entered Chefland and wants to establish Pushpa-Raj here too.

Chefland has N towers where the height of the ith tower is Hi. To establish Pushpa-Raj, Pushpa does the following:

Initially, Pushpa chooses any tower i (1≤i≤N) and lands on the roof of that tower.
Let X denote the height of the tower Pushpa is currently on, then, Pushpa can land on the roof of any tower j (1≤j≤N) such that the height of the jth tower is (X+1).
Let i denote the index of the tower on which Pushpa lands, then, the height of all towers except tower i increases by 1 after each jump including the initial jump.

To establish Pushpa-Raj, Pushpa wants to land at the maximum height possible. Determine the maximum height Pushpa can reach.

Input Format:
- The first line contains a single integer T - the number of test cases. Then the test cases follow.
- The first line of each test case contains an integer N - the number of towers
- The second line of each test case contains N space-separated integers H1,H2,…,HN denoting the initial heights of each of the towers from the ground.

Output Format:
For each test case, output in a single line the maximum height achieved by Pushpa

Sample Input 1:
2
4
1 2 1 3
1
2

Sample Output 1:
3
2
"""

t=int(input())
while(t):
    n=int(input())
    inp=[int(i) for i in input().strip().split(' ')]
    height={}

    if(n==1):
        print(inp[0])
    else:
        for i in inp:
            if(i not in height):
                height[i]=i
            else:
                height[i]+=1

        print(max(height.values()))

    t-=1

