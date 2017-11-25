sample = ['GTA','GGG','CAC']

def read_dna(dna_file):
  dna_data = ''
  with open(dna_file, 'r') as f:
    for line in f:
      dna_data += line
  return dna_data

def dna_codons(dna):
  codons = []
  for i in range(0, len(dna), 3):
    codons.append(dna[i:i+3])
  return codons

def match_dna(dna):
  matches = 0
  for codon in dna:
    if codon in sample:
      matches += 1
  return matches

def is_criminal(suspects):
  for suspect in suspects:
    dna_data = read_dna(suspect)
    codons = dna_codons(dna_data)
    num_matches = match_dna(codons)
    if num_matches >= 3:
      print '%s is possibly guilty!' % (suspect)
    else:
      print 'Inconclusive.'
  
is_criminal(['suspect1.txt', 'suspect2.txt', 'suspect3.txt'])
