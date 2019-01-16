import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

list_temp = []
sorted_list = []
n = int(input()) 

for i in input().split():
    t = int(i)
    list_temp.append(t)
    
if list_temp:
    closest2zero = min(list_temp, key = abs)

    if (-1) * closest2zero in list_temp:
        closest2zero = abs(closest2zero)

    print(closest2zero)
    
else:
    print(0)
