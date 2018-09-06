"""
Given an array Arr[] of N integers, write a program to find the sum of values of even and odd index positions separately.

Input: 
First line of input contains a single integer T which denotes the number of test cases. Then T test cases follows. First line of each test case contains a single integer N which denotes the number of elements in the array. Second line of each test case contains N space separated integer which denotes the elements of the array.
Output:
For each test case, in first line print the sum of elements of array present at even indexes and in the second line print the sum of elements at odd indexes.

Constraints:
1<=T<=100
1<=N<=1000
1<=Arr[i]<=105

Example:
Input:
2
6
1 2 3 4 5 6
7
10 20 30 40 50 60 70
Output:
9
12
160
120
"""

t = int(input())

while(t>0):
    n = int(input())
    arr = list(map(int,input().split()))
    sumo,sume = 0,0
    for i in range(0,n):
        if ((i+1)%2==0):
            sume+=arr[i]
        else:
            sumo+=arr[i]
    print(sumo)
    print(sume)
    t-=1
