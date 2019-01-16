import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

pi = []
diff = []
n = int(input())
diff_min = 10000000

for i in range(n):
    pi.append(int(input()))

pi.sort()
former_puissance = 0

for puissance in pi:
    diff.append(abs(puissance - former_puissance))
    former_puissance = puissance
    
diff_min = min(diff)
print(diff_min)
    
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
