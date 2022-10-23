from queue import SimpleQueue


def wave(matrix, x, y):
    # matrix[x][y] = 2

    q = SimpleQueue()
    q.put((x, y, matrix[x][y]))

    while q.qsize() != 0:
        x, y, v = q.get()
        if matrix[x][y] == 1:
            matrix[x][y] = v + 1
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    if i >= 0 and j >= 0 and i < len(matrix) and j < len(matrix[0]):
                        q.put((i, j, matrix[x][y]))

    for row in matrix:
        print(row)
