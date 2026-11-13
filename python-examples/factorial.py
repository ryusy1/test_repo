def factorial(n):
    result = 1
    for number in range(2, n + 1):
        result *= number
    return result


if __name__ == "__main__":
    print(factorial(5))
