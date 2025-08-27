# Magic Square Generator using Siamese Method
# Author: Sayyed Amaan
# Timeline: Sep 2022 – Nov 2022

def generate_magic_square(n):
    if n % 2 == 0:
        raise ValueError("Only odd-order magic squares are supported using this method.")

    magic_square = [[0] * n for _ in range(n)]

    i, j = 0, n // 2  # Start position
    for num in range(1, n * n + 1):
        magic_square[i][j] = num
        new_i, new_j = (i - 1) % n, (j + 1) % n
        if magic_square[new_i][new_j]:
            i = (i + 1) % n
        else:
            i, j = new_i, new_j

    return magic_square


def display_square(square):
    n = len(square)
    print("\nMagic Square of size", n, "x", n)
    print("Magic Constant =", n * (n**2 + 1) // 2, "\n")
    for row in square:
        print(" ".join(f"{num:3d}" for num in row))


if __name__ == "__main__":
    try:
        n = int(input("Enter the size of the magic square (odd number): "))
        magic_square = generate_magic_square(n)
        display_square(magic_square)
    except ValueError as e:
        print("Error:", e)
