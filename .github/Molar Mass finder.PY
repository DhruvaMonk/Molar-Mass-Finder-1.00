# Python dictionary of all elements with their molar masses in g/mol
molar_masses = {
    'H': 1.008, 'He': 4.003, 'Li': 6.941, 'Be': 9.012,
    'B': 10.811, 'C': 12.011, 'N': 14.007, 'O': 15.999,
    'F': 18.998, 'Ne': 20.180, 'Na': 22.990, 'Mg': 24.305,
    'Al': 26.982, 'Si': 28.086, 'P': 30.974, 'S': 32.066,
    'Cl': 35.453, 'Ar': 39.948, 'K': 39.098, 'Ca': 40.078,
    'Sc': 44.956, 'Ti': 47.867, 'V': 50.942, 'Cr': 51.996,
    'Mn': 54.938, 'Fe': 55.845, 'Co': 58.933, 'Ni': 58.693,
    'Cu': 63.546, 'Zn': 65.38, 'Ga': 69.723, 'Ge': 72.63,
    'As': 74.922, 'Se': 78.971, 'Br': 79.904, 'Kr': 83.798,
    'Rb': 85.468, 'Sr': 87.62, 'Y': 88.906, 'Zr': 91.224,
    'Nb': 92.906, 'Mo': 95.95, 'Tc': (98),
    'Ru': 101.07, 'Rh': 102.91, 'Pd': 106.42, 
}

n= int(input("how many elements are in your compound?  "))
k= 1
number = 1
elements = []

while n >= k: 
    if k == 1:
        Grammar = "first"
    else:
        Grammar = "next"
    number = int(input(f"how many of the {Grammar} element do you have in the compound?    "))
    elements.extend([input(f"what is the {Grammar} element in the compound?   ")]  * number)
    k += 1
    number += 1

print(elements)

molar_mass = [molar_masses.get(item, item) for item in elements]

print(sum(molar_mass))





