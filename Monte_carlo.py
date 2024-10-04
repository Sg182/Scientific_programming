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


def generate_orbitals(max_n):
    orbitals = []
    for i in range(1,max_n+1):
        for l in range(i):
            orbitals.append((i,l))
    return sorted(orbitals, key=lambda x: (x[0]+x[1], x[0]))

def max_electron(l):
    return 2*(2*l +1)
def orbital(n,l):
    label = ['s','p','d','e','f']
    return f"{n}{label[l]}{max_electron(l)}"


x = orbital(2,1)
print(x)


def generate_orbitals(max_n):
    orbitals = []
    for n in range(1, max_n + 1):
        for l in range(n):
            orbitals.append((n, l))
    return sorted(orbitals, key=lambda x: (x[0] + x[1], x[0]))

def max_electrons(l):
    return 2 * (2 * l + 1)

def orbital_label(n, l):
    labels = ['s', 'p', 'd', 'f', 'g', 'h', 'i']  # Extend if needed
    return f"{n}{labels[l]}"

def electron_configuration(Z):
    orbitals = generate_orbitals(7)  # 7 should be sufficient for elements up to 104
    configuration = []
    remaining_electrons = Z

    for n, l in orbitals:
        electrons_in_orbital = min(remaining_electrons, max_electrons(l))
        if electrons_in_orbital > 0:
            configuration.append((orbital_label(n, l), electrons_in_orbital))
            remaining_electrons -= electrons_in_orbital
        if remaining_electrons <= 0:
            break

    return configuration

def format_configuration(config):
    return " ".join([f"{orbital}{electrons}" for orbital, electrons in config])

# Print configurations for elements up to Rutherfordium (N = 104)
for Z in range(1,10):
    config = electron_configuration(Z)
    print(f"Element {Z}: {format_configuration(config)}")
