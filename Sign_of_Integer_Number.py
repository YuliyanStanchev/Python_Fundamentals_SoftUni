def define_sign(num):
    if num == 0:
       return f"The number {num} is zero."
    elif num < 0:
       return f"The number {num} is negative."
    else:
       return f"The number {num} is positive."


if __name__ == "__main__":
    number = int(input())
    print(define_sign(number))