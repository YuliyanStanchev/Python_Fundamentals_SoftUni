def calculate_power(num, p):
    result = pow(num, p)
    return result


if __name__ == "__main__":
    number = float(input())
    power = int(input())
    print(calculate_power(number, power))
