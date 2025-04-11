import numpy as np

def Matrix_input():

    matrix = []
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    print("Enter the elements row by row:\n")

    for i in range(1,rows+1):
        row = list(map(float, input(f"Enter for row {i}: ").split()))
        
        if len(row) != cols:
            print(" Rows doesn't have required number of elements. Try Again.")
            return Matrix_input()
        matrix.append(row)
        
    matrix = np.array(matrix)
    return matrix

def diagonalize(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)   # eigenvalues and eigenvectors are arrays 
    print("The eigenvalues are :", eigenvalues)
    D = np.diag(eigenvalues)
    return D

matrix = Matrix_input()
print(f"The diagonalized matrix is: ")
print(diagonalize(matrix))
