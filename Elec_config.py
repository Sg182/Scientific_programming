from ast import Raise
from logging import config
import math
from shlex import join
from xml.dom.minidom import Element

# List of all elements upto Z=104

ELEMENTS = [
    "", "H","He","Li","Be","B","C","N","O","F","Ne",
    "Na","Mg","Al","Si","P","S","Cl","Ar","K","Ca","Sc","Ti","V","Cr","Mn","Fe","Co","Ni","Cu","Zn",
    "Ga","Ge","As","Se","Br","Kr","Rb","Sr","Y","Zr","Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd","In","Sn",
    "Sb","Te","I","Xe","Cs","Ba","La","Ce","Pr","Nd",
    "Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb",
    "Lu","Hf","Ta","W","Re","Os","Ir","Pt","Au","Hg",
    "Tl","Pb","Bi","Po","At","Rn","Fr","Ra","Ac","Th",
    "Pa","U","Np","Pu","Am","Cm","Bk","Cf","Es","Fm",
    "Md","No","Lr","Rf"
]

orbitals = {0:'s', 1:'p', 2:'d', 3:'f'}

# now create a list which has tuples associated with (n,l) sorted according to Aufbau priciple

subshells = []

for n in range(1,9):
    for l in range(n):
        subshells.append((n,l))

# Sort the subshells according to Aufbau principle
subshells.sort(key=lambda x: (x[0] + x[1], x[0]))

def max_electron_l(l):
    return 2*(2*l +1)

def electronic_config(Z):
    remaining = Z
    config = [] # initializing empty list to store electronic configuration

    for n,l in subshells:
        if remaining !=0:
            occupied = min(max_electron_l(l),remaining)
            config.append(f"{n}{orbitals[l]}{occupied}")
            remaining = remaining- occupied
        else:
            break
    
    return '.'.join(config)

# The function below returns integer Z, whether the user passes a number or a symbol as argument
def resolve_to_atomic_number(user_input):
    try:
        Z = int(user_input)
        if 1<= Z <= (len(ELEMENTS)-1):
            return Z
        else:
            raise ValueError("The Z is out of range")
    except ValueError:
        symbol = user_input.strip().capitalize()
        if symbol in ELEMENTS:
            Z = ELEMENTS.index(symbol)
            return Z
        else:
            raise ValueError(f"Unknown element symbol:{symbol}")




if __name__ == '__main__':
    user_input = input("Enter the atomic number Z or the element Symbol:")
    try:
        Z = resolve_to_atomic_number(user_input)
        print(electronic_config(Z))
         
    except ValueError as e:
        print(e)