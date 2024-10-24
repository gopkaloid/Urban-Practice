def generate_password(n):
    pairs = []
    for i in range(1, n):
        for j in range(i + 1, n):
            if n % (i + j) == 0:
                pairs.append((i, j))
    password = ''.join([str(a) + str(b) for a, b in pairs])
    return password
n = int(input("Введите число n: "))
result = generate_password(n)
print(f"Пароль для числа {n}: {result}")