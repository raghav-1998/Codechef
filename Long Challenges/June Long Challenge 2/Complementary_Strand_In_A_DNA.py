"""
You are given the sequence of Nucleotides of one strand of DNA through a string 
S of length N. S contains the character A,T,C, and G only.

Chef knows that:

A is complementary to T.
T is complementary to A.
C is complementary to G.
G is complementary to C.
Using the string S, determine the sequence of the complementary strand of the DNA.

Input Format:
- First line will contain T, number of test cases. Then the test cases follow.
- First line of each test case contains an integer N - denoting the length of string S.
- Second line contains N characters denoting the string S.

Output Format:
For each test case, output the string containing N characters - sequence of 
nucleotides of the complementary strand.

Constraints
- 1≤T≤100
- 1≤N≤100
- S contains A, T, C, and G only

Sample Input 1 
4
4
ATCG
4
GTCC
5
AAAAA
3
TAC

Sample Output 1 
TAGC
CAGG
TTTTT
ATG

"""

if __name__=="__main__":
    t=int(input())

    while(t):
        n=int(input())
        s=input()

        ans=""
        for i in range(n):
            if(s[i]=='A'):
                ans+='T'
            elif(s[i]=='T'):
                ans+='A'
            elif(s[i]=='C'):
                ans+='G'
            else:
                ans+='C'
        
        print(ans)

        t-=1

