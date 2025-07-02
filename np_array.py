import numpy as np

#================ Understanding of split() function =========================
arr = 'you are my no.1 wifey'

fname1 = arr.split()
fname2 = arr.split('.')
fname3 = arr.split('.')[0]

print(type(fname1))
print(fname1)
print(fname2)
print(fname3)
#==============================================================================
arr1 = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])

arr2 = np.array([[10, 20],[40, 50],[0, 1]])



print(np.shape(arr1))
print(np.shape(arr2))

last_row = arr1[-1]
first_row = arr1[0]
print(first_row)
print(last_row)

print('first colukmn :', arr1[:,0])
print('third or lst colukmn :', arr1[:,2])


print('The first two rows are: \n',arr1[[0,1]])
print('The second and last columns are: \n',arr1[:,[1,-1]])

arr1[:,1] = 1

print('The replaced arr is : \n',arr1)

mul_arr = arr1@arr2

print('The multiplied array arr1*arr2 is: \n',mul_arr,'\n')


B = np.array([[10, 20, 30],
              [40, 50, 60],
              [70, 80, 90]])
v = np.array([[10], [20], [30]])

sub = B - v[0]
print('The subtraction of the first column of B with the first row of v: \n',sub,'\n')


print('Multiplying all the elements of B by 2: \n',B*2,'\n')

 

#=================================================================================================================#

#====================#
#    Magic Matrix.   #
#====================#

'''The algorithm is given in Christian Hill page - 208'''

N=5

magic_square = np.zeros((N,N), dtype=float)

n=1

i =0
j= N//2

while n < N*N:
    magic_square[i,j] = n
    n+=1
    new_i, new_j = (i-1)%N, (j+1)%N
    
    if magic_square[new_i,new_j]:
        i+=1
    else:
        i, j = new_i, new_j

print(magic_square)


