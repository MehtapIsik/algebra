# Run example: python tmp.py 4 5

import sys
import algebra

print(sys.argv)

name = sys.argv[0]
num1 = float(sys.argv[1])
num2 = float(sys.argv[2])

print(algebra.operations.product(num1, num2))
