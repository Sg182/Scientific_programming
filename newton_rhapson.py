def newton_rhapson(x0,f,df,tol = 1.0e-12,max_iter= 50):

    ''' Newton-Rhapsonmethod o find the root of f(x)=0.
    
    Parameters: x0 --> intitial guess
                 f --> function
                 df --> first drivative '''
    
    x = x0

    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if dfx ==0:
            raise ValueError(f"Derivative goes to 0 at iteration {i}, x ={x}")
        
        print(f"iteration:{i+1}     x: {x}")
        x_new = x - fx/dfx

        if abs(x_new - x) <= tol:
            print(f"Calculation Converged in {i+1} iterations!")
            break
        x = x_new

    return x_new



# Let us try an example

f = lambda x: x**3 - 2*x - 5
df = lambda x : 3*(x**2) -2 

root = newton_rhapson(2.0,f,df)
print(f"The root is : {root}")