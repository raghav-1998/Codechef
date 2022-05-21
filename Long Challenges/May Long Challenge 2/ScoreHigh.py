'''
Chef is taking a tough examination. The question paper consists of N objective problems and each problem has 4 options A,B,C, and D, out of which, exactly one option is correct.

Since Chef did not study for the exam, he does not know the answer to any of the problems. Chef was looking nearby for help when his friend somehow communicated the following information:

Exactly NA problems have option A as the answer.
Exactly NB problems have option B as the answer.
Exactly NC problems have option C as the answer.
Exactly ND problems have option D as the answer.

Note that:
NA+NB+NC+ND=N.

Each problem is worth exactly 1 mark and there is no negative marking.
Even though Chef knows the number of correct options of each type, he does not know the correct answer to any problem.
Based on the given information, find the maximum marks Chef can guarantee if he marks the answers optimally.

Input Format
- First line will contain T, number of test cases. Then the test cases follow.
- First line of each test case contains an integer N denoting the number of problems.
- Second line of each test case contains 4 integers NA,NB,NC, and ND - as mentioned in the problem statement.

Output Format
For each test case, output the maximum marks Chef can guarantee if he marks the answers optimally.

Constraints
1≤T≤1000
1≤N≤105
0≤NA,NB,NC,ND≤N
NA+NB+NC+ND=N

Sample Input 1 
2
5
0 0 5 0
10
7 1 1 1

Sample Output 1 
5
7
'''


if __name__=="__main__":
    t=int(input())

    while(t):
        n=int(input())
        N1,N2,N3,N4=[int(i) for i in input().strip().split(' ')]

        print(max(N1,N2,N3,N4))
        t-=1