def ekub(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(ekub(36, 60))  # Natija: 12

