# heavy help from Tina and Jesus

def make_matrix(r, c):
    matrix = list(range(0))
    for i in range(r):
        list_row = list()
        for j in range(c):
            list_row.append(0)
        matrix.append(list_row)
    return matrix


def markov_simulation(ini_matrix, t_matrix, sim_num):
    value = 0
    for i in range(sim_num):
        loop = True
        moves = 0
        temporary_m = matrixmult(ini_matrix, t_matrix)
        while loop is True:
            temporary_m = matrixmult(temporary_m, t_matrix)
            moves += 1
            if float(temp_matrix[0][11]) > 1:
                value += moves
                loop = False
    return int(value/sim_num)
