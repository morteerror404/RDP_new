from elements import Elements
from sympy import Eq, symbols, solve

def calculate_molar_mass(formula, elements_dict):
    molar_mass = 0
    for element_symbol, count in formula.items():
        element = elements_dict[element_symbol]
        molar_mass += element.atomicWeight * count
    return molar_mass

def predict_bond_type(element1, element2):
    if abs(element1.atomicNumber - element2.atomicNumber) > 1:
        return 'iônica'
    elif abs(element1.atomicNumber - element2.atomicNumber) == 1:
        return 'covalente'
    else:
        return 'desconhecida'

def balance_equation(equation, reactants_dict, products_dict):
    reactants, products = equation.split('->')
    reactant_compounds = reactants.strip().split(' + ')
    product_compounds = products.strip().split(' + ')

    equation_symbols = symbols(' '.join(reactant_compounds + product_compounds))
    equations = []

    for compound in reactant_compounds:
        coeff_symbols = symbols(f'{compound}_coeff')
        equation = Eq(sum(coeff_symbols), reactants_dict[compound])
        equations.append(equation)

    for compound in product_compounds:
        coeff_symbols = symbols(f'{compound}_coeff')
        equation = Eq(sum(coeff_symbols), products_dict[compound])
        equations.append(equation)

    solution = solve(equations, equation_symbols)
    balanced_equation = ' + '.join([f'{solution[symbol]} {symbol}' for symbol in equation_symbols])
    return balanced_equation

def calculate_average_electronegativity(elements_list):
    total_electronegativity = sum([element.electronegativity for element in elements_list])
    average_electronegativity = total_electronegativity / len(elements_list)
    return average_electronegativity
