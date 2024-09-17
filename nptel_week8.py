def max_marks_with_drops(N, K, marks):
    # Initialize DP array
    Best = [[-float('inf')] * (K + 1) for _ in range(N)]
    
    # Base case for the first mark
    for j in range(K + 1):
        Best[0][j] = 0 if j > 0 else marks[0]  # Drop 0th mark or not
    
    # Fill the DP table
    for i in range(1, N):
        for j in range(K + 1):
            # Case 1: We don't drop the i-th test
            Best[i][j] = max(Best[i-1][j] + marks[i], marks[i])
            # Case 2: We drop the i-th test (only if j > 0)
            if j > 0:
                Best[i][j] = max(Best[i][j], Best[i-1][j-1])
    
    # Return the maximum value from the last row of the DP table
    return max(max(Best[i]) for i in range(N))

# Reading input
N, K = map(int, input().split())
marks = [int(input()) for _ in range(N)]

# Compute and print the result
print(max_marks_with_drops(N, K, marks))
