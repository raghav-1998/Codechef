"""
JJ has an array A. He can perform the following operation on A:

- Divide A into two subsequences P and Q such that each Ai belongs to either 
  P or Q.
- Set A:=P concat Q
Here concat denotes the concatenation operation. For e.g. 
[2,1,5] concat [4,3]=[2,1,5,4,3].

Is it possible to make A sorted in non-decreasing order after applying the above 
operation at most once?

Note: An array X is a subsequence of an array Y if X can be obtained by deletion 
of several (possibly, zero or all) elements from Y.

Input Format
- The first line contains a single integer  T  — the number of test cases. Then the 
  test cases follow.
- The first line of each test case contains an integer N — the size of the array 
  A.
- The second line of each test case contains N space-separated integers 
  A1,A2,…,AN denoting the array A.

Output Format
For each test case, output YES if it is possible to make the array A sorted after 
applying the given operation at most once. Otherwise, output NO.

You may print each character of YES and NO in uppercase or lowercase (for 
example, yes, yEs, Yes will be considered identical).

Constraints
1≤T≤10^5
2≤N≤10^5
1≤Ai≤10^9
Sum of N over all test cases does not exceed 2⋅10^5

Sample Input 1 
3
6
4 5 6 1 2 3
5
1 3 5 2 4
5
5 10 7 11 9

Sample Output 1 
YES
NO
YES

"""

if __name__=="__main__":
    t=int(input())
    while(t):
        n=int(input())
        arr=[int(i) for i in input().strip().split(' ')]
        
        index=ele=-1
        for i in range(n-1):
            if(arr[i]>arr[i+1]):
                index=i+1 
                ele=arr[index]
                break
        
        if(index==-1 or index==n-1):
            print("Yes")
        else:
            for i in range(index):
                if(arr[i]>ele):
                    lmx=arr[i]
                    break
            
            rmx=arr[index-1]
            
            i=index+1 
            
            while(i<n):
                if(arr[i]>=rmx):
                    rmx=arr[i]
                elif(arr[i]<=lmx and arr[i]>=ele):
                    ele=arr[i]
                else:
                    print("No")
                    break 
                i+=1 
            
            if(i==n):
                print("Yes")
        t-=1