"""
Given a string A of length N consisting of lowercase English alphabet letters.

You are allowed to perform the following operation on the string A any number of times:

Select a non-empty subsequence S of the array [1,2,3,…,N] and any lowercase English alphabet α;

Change Ai to α for all i∈S.

Find the minimum number of operations required to convert A into a given string 
B of length N consisting of lowercase English alphabet letters.

Input Format
- The first line of input contains a single integer T, denoting the number of test cases. The description of T test cases follow.
- The first line of each test case contains an integer N - the length of the string A and B.
- The second line of each test case contains the string A.
- The third line of each test case contains the string B

Output Format
For each test case, output the minimum number of operations required to convert 
string A into string B.

Constraints
1≤T≤10^4
1≤N≤10^5
Sum of N over all test cases does not exceed 10^5.

Sample Input 1 
3
2
ab
cd
3
aaa
bab
4
abcd
aaab

Sample Output 1 
2
1
2

"""


if __name__=="__main__":
    t=int(input())

    while(t):
        n=int(input())
        a=input()
        b=input()

        s=set()

        for i in range(n):
            if(a[i]!=b[i]):
                s.add(b[i])
        
        print(len(s))

        t-=1
        
