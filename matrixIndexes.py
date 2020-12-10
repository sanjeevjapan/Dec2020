import tensorflow as tf

smnist = tf.keras.datasets.mnist

import sys

print(sys.executable)

matrix = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
    ]
print(matrix)
print("matrix[1]",matrix[1])
print("matrix[1][2]",matrix[1][2])
print("matrix[2][2]",matrix[2][2])

transpose = ([[row[i] for row in matrix] for i in range(3)])
print(transpose)

### added this comment from desktop on branch1 after branching of onlineBranch2
