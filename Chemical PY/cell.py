from aminoAcid import aminoAcid
from protein import protein

class Cell:
    def __init__(self, name, proteins):
        self.name = name
        self.proteins = proteins

def create_cells_from_file(file_path, amino_acids, proteins):
    cells = []

    try:
        with open(file_path, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                name = data[0]
                protein_names = data[1:]
                cell_proteins = [protein for protein in proteins if protein.name in protein_names]
                cell = Cell(name, cell_proteins)
                cells.append(cell)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return cells

file_path = 'cells.csv'
cells = create_cells_from_file(file_path, amino_acids, proteins)

def calculate_cell_protein_mass(cell, amino_acids):
    total_mass = 0
    for protein in cell.proteins:
        total_mass += sum(amino_acid.molecular_weight for amino_acid in amino_acids if um amino_acid.name in protein.amino_acid_composition)
    return total_mass

