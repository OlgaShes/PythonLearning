def pascal(num):
    pascal_triangle = []
    for i in range(num + 1):
        pascal_triangle.append([1] * (i + 1))
    if num > 1:
        for n in range(2, num + 1):
            for m in range(1, n // 2 + 1):
                pascal_triangle[n][m] = pascal_triangle[n][-(m + 1)] = pascal_triangle[n - 1][m - 1] + pascal_triangle[n - 1][m]
    return pascal_triangle

print(*pascal(7), sep='\n')