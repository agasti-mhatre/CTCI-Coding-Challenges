'''
1 0 2 3
4 5 6 7
8 9 1 2

0 0 0 0
4 0 6 7
8 0 1 2
'''

'''
1 0 0 3
4 5 6 7
8 9 1 2

0 0 0 0
4 0 0 7
8 0 0 2
'''


def zero_out_matrix(matrix):
    zero_matrix = []
    lookup_table = dict()
    for i in range(0, len(matrix)):
        zero_matrix.append(list())
        for j in range(0, len(matrix[i])):
            if matrix[i][j] == 0:
                zero_matrix[i].append(matrix[i][j])
                if i in lookup_table.keys():
                    lookup_table[i].append(j)
                else:
                    lookup_table[i] = list()
                    lookup_table[i].append(j)
            else:
                zero_matrix[i].append(matrix[i][j])


    for row_index, column_index_list in lookup_table.items():
        for n in range(0, len(zero_matrix[row_index])):
            zero_matrix[row_index][n] = 0

        for row in zero_matrix:
            for n in column_index_list:
                row[n] = 0


    return zero_matrix


if __name__ == "__main__":
    matrix = [
                [1, 2, 4, 5],
                [4, 5, 6, 7],
                [8, 9, 1, 0] 
                                ]

    print(zero_out_matrix(matrix))