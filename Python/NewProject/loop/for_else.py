'''

'''
import math
for n in range(99,1,-1):
    root=math.sqrt(n)
    if root==int(root):
        print(n)
        break
else:
    print('Nothing')
