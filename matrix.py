def matrix_chain_multiplication(dimensions):
    n = len(dimensions) - 1  
    dp = [[float('inf')] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 0

    for chain_length in range(2, n + 1):
        for i in range(n - chain_length + 1):
            j = i + chain_length - 1
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + dimensions[i] * dimensions[k + 1] * dimensions[j + 1]
                if cost < dp[i][j]:
                    dp[i][j] = cost

    return dp[0][n - 1]


matrices = [(2, 3), (3, 4), (4, 2)]

min_scalar_multiplications = matrix_chain_multiplication(matrices)
print("Minimum Scalar Multiplications:", min_scalar_multiplications)