# Day 1 of Pracitising AI/ML Foundation

a, b = 0, 1
while b <= 100:
    print(b, end="")
    a , b = b, a+b 

def is_prime(n):
    if n<2: return False
    for i in range(2, int(n)):
        if (n%i == 0):
            return False
    return True

print(is_prime(12))

s = "machine learning"
print(s[::-1])