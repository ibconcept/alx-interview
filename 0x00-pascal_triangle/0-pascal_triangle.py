def generate_pascal_triangle(n):
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
    x = 5  # Replace this with any positive integer to generate more rows
    pascal_triangle = generate_pascal_triangle(x)
    print_pascal_triangle(pascal_triangle)

