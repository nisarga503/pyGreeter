def is_happy(n):
    seen = set()

    while n != 1:
        if n in seen:
            return False

        seen.add(n)

        total = 0
        while n > 0:
            digit = n % 10
            total += digit ** 2
            n //= 10

        n = total

    return True


num = int(input("Enter a number: "))

if is_happy(num):
    print(num, "is a Happy Number ")
else:
    print(num, "is not a Happy Number ")