def create_codon_dict(path="/content/data/codons.txt"):
    file = open(path)
    rows = file.readlines()
    
    codon_dict = {}
    for row in rows:
        parts = row.strip().split('\t')
        codon = parts[0]
        amino_acid = parts[2]
        codon_dict[codon] = amino_acid
    
    file.close()
    return codon_dict
