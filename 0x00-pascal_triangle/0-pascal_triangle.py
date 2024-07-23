#!/usr/bin/env python3
import sys

def pascal_triangle(n):
    assert isinstance(n, int) and n > 0, "n must be a positive integer"
    
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle

def print_pascal_triangle(triangle):
    for row in triangle:
        print(' '.join(map(str, row)).center(2 * len(triangle) - 1))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <number_of_rows>")
        sys.exit(1)
    
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("The argument must be an integer.")
        sys.exit(1)

    try:
        pascal_triangle = pascal_triangle(n)
        print_pascal_triangle(pascal_triangle)
    except AssertionError as e:
        print(e)
        sys.exit(1)

