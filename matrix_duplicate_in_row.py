def matric(matrix):
    for row in matrix:
        if len(row) == len(set(row)):
            continue
        else:
            return 'fail'
    return 'pass'

    
print(matric([[1,2,3], [4,5,6], [7,8,9]]))
