"""
Write a Python Program to remove the nth index character from a non-empty string.
Input & Output Format:
Input consists of a string and one integer.
The first input consists of a string.
The second input refers to the index position.
The output consists of a string.
Sample Input:
cyfuno
4
Sample Output:
cyfuo


ANS:
d={}
n=int(input())
sum=0
for i in range(0,n):
    key=i+1
    value=int(input())
    d[key]=value
    sum+=value
print(sum)

"""
