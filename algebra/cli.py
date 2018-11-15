import sys
import algebra

print(sys.argv)

def main():
    name = sys.argv[0]
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])

    result = algebra.operations.product(num1, num2)
    print("Product of {} and {} is: {}".format(num1, num2, result))
   
