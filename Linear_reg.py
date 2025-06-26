import numpy as np
import glob

class Experiment:
    
    def __init__(self, filename):
         x , y= [], []

         with open(filename,'r') as f:
            for line_no, line in enumerate(f):
                line =line.strip()
                if not line or line.startswith('#'):
                    continue

                try:
                    x_val, y_val = line.split()
                    x_val = float(x_val)
                    y_val = float(y_val)
                except ValueError:
                    print(f"Warning!: Skipping the troublesome datas on line number: {line_no}")
                    continue

                x.append(x_val)
                y.append(y_val)

            if not x:
                raise RuntimeError(f"No valid x-values are available in the file {filename}")
            
         self.x = np.array(x)
         self.y = np.array(y)


    def transform(self, x_func=None, y_func=None):

        if x_func is not None:
            self.x = x_func(self.x)
        if y_func is not None:
            self.y = y_func(self.y)

    def Linear_Regression(self):

        '''Performs Linear Regression and returns the gradient m and intercept c of the best-fit line.
           Here, mean are calculated for x,y and all other quantities.'''

        x = self.x
        y = self.y
        x_mean = np.mean(x)
        y_mean = np.mean(y)
        xy_mean = np.mean(x*y)
        x2_mean = np.mean(x*x)
        m = (xy_mean - x_mean*y_mean)/(x2_mean-x_mean**2)
        c = y_mean - m*x_mean

        return m,c 
    


R = 8.314     # J K^-1 mol^-1
Temp =[]      #Temperatures
k_s = []      #Rate constants

#files = ['caa-40.txt','caa-50.txt','caa-60.txt','caa-70.txt','caa-80.txt']

for file in sorted(glob.glob('caa-*.txt')):               #=====exploited the glob function==========#
                                                               
    exp = Experiment(file)
    exp.transform(x_func=lambda t:t, y_func=lambda c:1/c)
    k, intercept = exp.Linear_Regression()
    Temp.append(float(file.split('-')[1].split('.')[0]))                 #   Warning: Here the Temp is string
    k_s.append(k)
    

print('===========================================================')
print("     Temperature(in celcius)     rate-constant (k)             ")
for T,i in zip(Temp,k_s):
    print(f"        {T:.3f}                 {i:.4e}")
 
print("============================================================")
Temp_inv = np.array(Temp, dtype=float) + 273.15         # This is Numpy Broadcasting addition
Temp_inv = 1/Temp_inv

log_k = np.array(k_s)
log_k = np.log(log_k)

slope, lnA = np.polyfit(Temp_inv, log_k,1)             # Using np.Polyfit function from numpy
Activ_E = -slope*R

print(f"|  The Activation Energy is {Activ_E:.6f} J mol-1         |")
print('============================================================')






        

              