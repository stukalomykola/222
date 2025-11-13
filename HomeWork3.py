num = int(input("Enter a number: "))

n1 = num // 10000
n2 = num // 1000 % 10
n3 = num // 100 % 10
n4 = num // 10 % 10
n5 = num % 10

result = n5 * 10000 + n4 * 1000 + n3 * 100 + n2 * 10 + n1

print(result)