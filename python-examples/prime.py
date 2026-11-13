def is_prime(number):
    if number < 2:
        return False
    return all(number % divisor for divisor in range(2, int(number ** 0.5) + 1))


if __name__ == "__main__":
    print([number for number in range(20) if is_prime(number)])
