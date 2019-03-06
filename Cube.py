import numpy as np
import itertools

def is_configuration(a):
    b=np.sum(a, axis=0)
    c=np.sum(a, axis=1)
    
    b= b >= 1
    b= np.all(b)
    c= c >= 1
    c= np.all(c)
    return c and b

def generate_matrix_from_bin(b, mat_size, mat_shape):
    test_matrix=np.fromstring(b, dtype=np.uint8)
    test_matrix=test_matrix[2:]
    test_matrix=np.subtract(test_matrix, 48)
    test_matrix=np.concatenate((np.zeros(mat_size-len(test_matrix)), test_matrix),axis=None)
    test_matrix=test_matrix.reshape(mat_shape)
    return test_matrix
def generate_matrix_from_list(combo, mat_list, mat_shape):
    result= np.zeros(mat_shape)
    for i in combo:
        result = result + mat_list[i]
    return result

def get_configuration_number(mat, mat_shape):
    count = 0
    num_ones= int(np.sum(mat))
    ind = np.transpose(np.nonzero(mat))
    decomp=list()
    min_dim = min(mat_shape)
    
    for i in range(num_ones):
        temp = np.zeros(mat_shape)
        temp[tuple(ind[i])] = 1
        decomp.append(temp)
    
    
    for i in range(min_dim, num_ones+1):
        combos = itertools.combinations(range(num_ones), i)
        for combo in combos:
            test_mat = generate_matrix_from_list(combo, decomp, mat_shape)
            if(is_configuration(test_mat)):
                count = count + 1
    return count
def dist(couple):
    x = np.array(couple)
    return np.linalg.norm(x[0]-x[1])

def get_cube(dim):
    odds = list()
    evens = list()
    x = itertools.product([0,1], repeat = dim)
    for i in x:
        cup = np.array(i)
        if(sum(cup) % 2):
            odds.append(i)
        else:
            evens.append(i)
    x = itertools.product(odds, evens)

    mat = list()

    for couple in x:
        mat.append(dist(couple))
    mat = np.array(mat)
    mat = mat.reshape((pow(2,dim-1),pow(2,dim-1)))
    mat = mat == 1
    return mat



def main():
    for dim in range(1,5):
        print(dim)
        mat= get_cube(dim)
        config = get_configuration_number(mat,(pow(2,dim-1),pow(2,dim-1)))
        res = np.array([config])
        np.save(str(dim)+".npy", res)
    


if __name__ == "__main__": main()
