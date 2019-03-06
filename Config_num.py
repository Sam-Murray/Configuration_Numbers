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
    return test_matr ix
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

def get_configs_of_shape(mat_shape, target_configs):
    mat_size = np.prod(mat_shape)
    for i in range(pow(2,mat_size)):
        mat = generate_matrix_from_bin(bin(i), mat_size, mat_shape)
        
        config=get_configuration_number(mat, mat_shape)
        
        if(config in target_configs):
            np.save(str(config)+".npy", mat)
    return



def main():
    target_figs=[ 57, 38, 703]
    x=itertools.combinations_with_replacement(range(1,7), 2)
    for i in x:
        get_configs_of_shape(i,target_figs)
    


if __name__ == "__main__": main()