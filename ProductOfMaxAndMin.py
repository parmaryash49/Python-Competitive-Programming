"""
Given two arrays of size N1 and N2 respectively, the task is to calculate the product of max element of first array and min element of second array.

Input:
The first line of the input contains a single integer T, denoting the number of test cases. Then T test case follows. Each testcase contains 4 lines:-
Size of the first array N1
Elements of the first array separated by spaces
Size of the second array N2
Elements of the second array separated by spaces

Output:
For each testcase, print the product of the max element of the first array and the minimum element of the second array.

Constraints:
1<=T<=107
1<=N1,N2<=1000
-1000<=A[i]<=1000

Example:
Input:
2
6
5 7 9 3 6 2
6
1 2 6 -1 0 9
6
1 4 2 3 10 2
6
4 2 6 5 2 9

Output:
-9
20

Explanation:
For testcase 1: The first array is 5 7 9 3 6 2. The max element among these elements is 9. The second array is 1 2 6 -1 0 9. The min element among these elements is -1. The product of 9 and -1 is 9*-1=-9.
"""

count = int(input())

while count>0:
    input()
    a1 = list(map(int,input().split()))
    input()
    a2 = list(map(int,input().split()))
    print(max(a1)*min(a2))
    count-=1
