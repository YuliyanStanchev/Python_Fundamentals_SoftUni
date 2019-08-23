def triangle_area(base, height):
    area = base * height / 2
    return area


if __name__ == "__main__":
    base = float(input())
    height = float(input())
    print(f"{triangle_area(base, height):.12g}")

