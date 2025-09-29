n_terms = int(input("Enter how many iterations you desire: "))

n1 = int(input("Enter first Integer in which the starting point of the sequence: "))
n2 = int(input("Enter second Integer in which where the first integer to be add of: "))
count = 0

print("Fibonaci Sequence upto: ", n_terms)

while(count < n_terms):
    print(n1, end=' ')
    nth = n1 + n2

    n1 = n2
    n2 = nth
    count += 1

print()