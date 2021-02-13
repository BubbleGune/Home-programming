# find the value of expression 3x^3+4-2 where number x is an integer

print(3 * int(input("Enter integer: ")) ** 3 + 4 - 2)

# find expression value (5x - 8)^1\2
print((5 * int(input("Enter integer: ")) - 8) ** 1/2)

# solve quadratic equation ax^2+bx+c = 0. numbers are entered in such a way that the discriminant is always positive
# numbers are entered in such a way that the discriminant is always positive
a = int(input())
b = int(input())
c = int(input())
discriminant = b ** 2 + 4 * a * c
x_one = (-b + discriminant ** (1/2) / 2 * a)
x_two = (-b - discriminant ** (1/2) / 2 * a)
print(x_one, x_two)
