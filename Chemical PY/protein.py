from aminoAcid import aminoAcid, amino_acids

class Protein:
    def __init__(self, name, amino_acid_composition):
        self.name = name
        self.amino_acid_composition = amino_acid_composition

def create_proteins_from_file(file_path, amino_acids):
    proteins = []

    try:
        with open(file_path, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                name = data[0]
                amino_acid_composition = data[1]
                protein = Protein(name, amino_acid_composition)
                proteins.append(protein)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return proteins

file_path = 'proteins.csv'
proteins = create_proteins_from_file(file_path, amino_acids)

def calculate_protein_mass(protein, amino_acids):
    try:
        total_mass = sum(amino_acid.molecular_weight for amino_acid in amino_acids if amino_acid.name in protein.amino_acid_composition)
        return total_mass
    except KeyError:
        print(f"One or more amino acids in {protein.name}'s composition were not found in the amino acids list.")
    except Exception as e:
        print(f"An error occurred: {e}")

protein_to_calculate = proteins[0]  # Choose a protein to calculate the mass
protein_mass = calculate_protein_mass(protein_to_calculate, amino_acids)
if protein_mass is not None:
    print(f"Total Mass of Protein {protein_to_calculate.name}: {protein_mass}")
