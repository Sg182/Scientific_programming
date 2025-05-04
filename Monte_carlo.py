## Estimation of Pi using Monte Carlo method
import random
import math

def estimate_pi(number_points):

    inside_circle = 0

    for i in range(1,number_points+1):
        x = random.uniform(0,1)  # returns a random number between 0 and 1
        y = random.uniform(0,1)# returns a random number between 0 and 1

        # Check if the points is within the quater circle

        if y <= math.sqrt(1-x**2):
            inside_circle+=1

    pi = (inside_circle/number_points)*4
    return pi 


pie = estimate_pi(1000000)
print(f"The estimate value of pi is {pie}")


