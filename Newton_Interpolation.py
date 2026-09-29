import numpy as np

def finite_diff(x,y):
  n = len(x)
  table = np.zeros((n,n))

  table[:,0] = y

  for i in range(1,n):
    for j in range(n-i):
      table[j,i] = (table[j+1,i-1] - table[j,i-1])/(x[j+i] - x[j])

  return table


def Newton_interpolation(X,y, x):

  n = len(X)
  FD = finite_diff(X,y)
  coeff = FD[0]
  prod = 1
  result = coeff[0]

  for i in range(1,n):
    prod *= (x - X[i-1])
    result += coeff[i]*prod

  return result

x_data = np.linspace(0,1.5,10)
y_data = np.sin(x_data)

x = 0.5
ans = Newton_interpolation(x_data, y_data,x )
print(ans)

