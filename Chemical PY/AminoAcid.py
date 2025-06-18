import elements

class AminoAcid:
    def __init__(self, name, formula, molecular_weight):
        self.name = name
        self.formula = formula
        self.molecular_weight = molecular_weight

def create_amino_acids_from_file(file_path):
    amino_acids = []

    with open(file_path, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            name = data[0]
            formula = data[1]
            molecular_weight = float(data[2])
            amino_acid = AminoAcid(name, formula, molecular_weight)
            amino_acids.append(amino_acid)

    return amino_acids

file_path = 'amino_acids.csv'
amino_acids = create_amino_acids_from_file(file_path)

def find_amino_acids_by_property(amino_acids, property_name, property_value):
    matching_amino_acids = [amino_acid for amino_acid in amino_acids if getattr(amino_acid, property_name) == property_value]
    return matching_amino_acids

def sort_amino_acids_by_weight(amino_acids):
    sorted_amino_acids = sorted(amino_acids, key=lambda x: x.molecular_weight)
    return sorted_amino_acids
                                