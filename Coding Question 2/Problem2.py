
# Arrange the King’s Army

# Take input
N, R, end = map(int, input().split())

# dp[i][j] → number of ways to arrange i soldiers ending with j
dp = [[0] * (R + 1) for _ in range(N + 1)]

# Base case: first position must be 1
dp[1][1] = 1

# Fill DP table
for i in range(2, N + 1):
    
    # Total ways from previous row
    total = sum(dp[i - 1])
    
    for j in range(1, R + 1):
        # Remove same adjacent case
        dp[i][j] = total - dp[i - 1][j]

# Final answer: length N ending with 'end'
print(dp[N][end])






# Alternative function-based approach


# def count_arrangements(N, R, end):
#     # Create DP table
#     dp = [[0] * (R + 1) for _ in range(N + 1)]

#     # First position must be 1
#     dp[1][1] = 1

#     # Fill DP table
#     for i in range(2, N + 1):
#         for j in range(1, R + 1):
#             for k in range(1, R + 1):
#                 if j != k:   # no same adjacent
#                     dp[i][j] += dp[i - 1][k]

#     # Last must be 'end'
#     return dp[N][end]


# # 🔽 Taking user input
# N, R, end = map(int, input("Enter N R end: ").split())

# # 🔽 Calling function
# result = count_arrangements(N, R, end)

# # 🔽 Output
# print("Number of valid arrangements:", result)

