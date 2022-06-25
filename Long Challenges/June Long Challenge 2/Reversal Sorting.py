"""
Chef is deriving weird ways to sort his array. Currently he is trying to sort his arrays 
in increasing order by reversing some of his subarrays.

To make it more challenging for himself, Chef decides that he can reverse only 
those subarrays that have sum of its elements at most X. Soon he notices that it 
might not be always possible to sort the array with this condition.

Can you help the Chef by telling him if the given array can be sorted by reversing 
subarrays with sum at most X.

More formally, for a given array A and an integer X, check whether the array can be 
sorted in increasing order by reversing some (possibly none) of the subarrays 
such that the sum of all elements of the subarray is at most X.

Input Format
- First line will contain T, number of test cases. Then the test cases follow.
- The first line of each test case contains of two space-separated integers N 
  and X denoting the length of the array and the maximum sum of subarrays 
  that you can reverse.
- The second line contains N space-separated integers A1,A2,...,AN 
  representing the initial array.
  
Output Format
- For each test case, output YES if Chef can sort the array using a finite number of 
  operations, else output NO.

- You may print each character of the string in uppercase or lowercase (for example, 
  the strings YeS, yEs, yes and YES will all be treated as identical).

Constraints
- 1≤T≤5⋅10^4
- 1≤N≤10^5
- 1≤Ai≤2⋅10^9
- 1≤X≤2⋅10^9
- Sum of N over all test cases does not exceeds 3⋅10^5

Sample Input 1 
3
4 1
1 2 3 4
4 1
2 1 3 4
5 7
3 2 2 3 3

Sample Output 1 
YES
NO
YES

"""

if __name__=="__main__":
    t=int(input())

    while(t):
        n,x=[int(i) for i in input().strip().split(' ')]
        inp=[int(i) for i in input().strip().split(' ')]

        flag=1
        for i in range(n-1):
            if(inp[i]>inp[i+1]):
                if(inp[i]+inp[i+1]>x):
                    flag=0
                    break
                else:
                    inp[i],inp[i+1]=inp[i+1],inp[i]

        
        if(flag==0):
            print("NO")
        else:
            print("YES")
        
        t-=1