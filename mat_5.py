#Print elements in sorted order using row-column wise sorted matrix

def sortedMatrix(self, N, Mat):
    # Step 1: Flatten the matrix into a single list
    flat_list = []
    for row in Mat:
        for element in row:
            flat_list.append(element)
    
    # Step 2: Sort the flattened list
    flat_list.sort()

    # Step 3: Reshape the sorted list back into the matrix
    k = 0  # To keep track of the index in the sorted list
    for i in range(N):
        for j in range(N):
            Mat[i][j] = flat_list[k]  # Assign the sorted element back to the matrix
            k += 1

    return Mat
