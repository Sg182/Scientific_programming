import numpy as np

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
                    y_val = float((y_val))
                except ValueError:
                    print(f"Warning!: Skipping the troublesome datas on line number:{line_no}")

              