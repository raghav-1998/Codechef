"""
While Alice was drinking sugarcane juice, she started wondering about the following facts:

1.The juicer sells each glass of sugarcane juice for 50 coins.
2.He spends 20% of his total income on buying sugarcane.
3.He spends 20% of his total income on buying salt and mint leaves.
4.He spends 30% of his total income on shop rent.

Alice wonders, what is the juicer's profit (in coins) when he sells N glasses of sugarcane juice?

Input Format:
- The first line of input will contain an integer T — the number of test cases. The description of T test cases follows.
- The first and only line of each test case contains an integer N, as described in the problem statement.

Output Format:
For each test case, output on a new line the juicer's profit when he sells N glasses of juice.

Sample Input 1 : 
4
2
4
5
10

Sample Output 1 : 
30
60
75
150
"""

t=int(input())

while(t):
    n=int(input())

    tot=n*50
    cost_sugarcane=tot//5
    cost_sugar_mint=tot//5
    cost_rent=(tot*3)//10

    profit=tot-(cost_sugarcane+cost_sugar_mint+cost_rent)

    print(profit)
    t-=1
