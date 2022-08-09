'''
     0   1   2 
0    a   b   c
1    d   e   f
2    g   h   i

0    g   d   a
1    h   e   b
2    i   f   c
                             

a matrix[0][0] --> rotated_matrix[0][2]
b matrix[0][1] --> rotated_matrix[1][2]
c matrix[0][2] --> rotated_matrix[2][2] 

d matrix[1][0] --> rotated_matrix[0][1]
e matrix[1][1] --> rotated_matrix[1][1]
f matrix[1][2] --> rotated_matrix[2][1]

g matrix[2][0] --> rotated_matrix[0][0]
h matrix[2][1] --> rotated_matrix[1][0]
i matrix[2][2] --> rotated_matrix[2][0]
'''


'''
a   b   c   d           
e   f   g   h
i   j   k   l 
m   n   o   p

m   i   e   a           
n   j   f   b
o   k   g   c 
p   l   h   d
'''

'''
a   b   c   d   e           
f   g   h   i   j
k   l   m   n   o   
p   q   r   s   t
u   v   w   x   y

u   p   k   f   a           
v   q   l   g   b
w   r   m   h   c   
x   s   n   i   d
y   t   o   j   e

'''


def rotate90deg(matrix):
    rotated_matrix = list()
    n = len(matrix)
    for each_list in range(0, n):
        rotated_matrix.append(list())
        for each_num in range(0, n):
            rotated_matrix[each_list].append(None)

    for i in range(0, n):
        for j in range(0, n):
            rotated_matrix[j][n - 1 - i] = matrix[i][j]

    return rotated_matrix


if __name__ == "__main__":
    matrix = [
                ["a", "b", "c", "d"],
                ["e", "f", "g", "h"],
                ["i", "j", "k", "l"],
                ["m", "n", "o", "p"]
                                ]

print(rotate90deg(matrix))