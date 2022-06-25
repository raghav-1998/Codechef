"""
There are 10 problems in a contest. You know that the score of each problem is 
either 1 or 100 points.

Chef came to know the total score of a participant and he is wondering how many 
problems were actually solved by that participant.

Given the total score P of the participant, determine the number of problems 
solved by the participant. Print −1 in case the score is invalid.

Input Format
- First line will contain T, number of test cases. Then the test cases follow.
- Each test case contains of a single line containing a single integer P - 
  denoting the number of points scored by the participant.

Output Format
- For each testcase, output the number of problems solved by the participant or −1 
  if the score is invalid.

Constraints
- 1≤T≤1000
- 0≤P≤1000

Sample Input 1 
5
103
0
6
142
1000

Sample Output 1 
4
0
6
-1
10

"""

if __name__=="__main__":
    t=int(input())

    while(t):
        p=int(input())

        if(p<=10):
            print(p)
        else:
            no_of_hund_score=p//100
            remain_val=p%100

            no_of_one_score=remain_val
            total=no_of_hund_score+no_of_one_score

            if(total>10):
                print("-1")
            else:
                print(total)
        
        t-=1

