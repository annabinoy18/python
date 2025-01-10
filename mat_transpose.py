#Write a program to find the transpose of a square matrix of size N*N. Transpose of a matrix is obtained by changing rows to columns and columns to rows.
 def transpose(self, mat, n):
        # Write Your code here
        
        for i in range(n):
            for j in range(i+1,n):
                mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
                
        return mat
