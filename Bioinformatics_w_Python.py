# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 13:22:33 2021

@author: Kim Hinz
"""

# %% Find the number of times a binding sequence exists in an ori
def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text) - len(Pattern) + 1):
        if Text[i:i + len(Pattern)] == Pattern:
            count = count + 1
    return count 

Text = "ATCAATGATCAACGTAAGCTTCTAAGCATGATCAAGGTGCTCACACAGTTTATCCACAACCTGAGTGGATGACATCAAGATAGGTCGTTGTATCTCCTTCCTCTCGTACTCTCATGACCACGGAAAGATGATCAAGAGAGGATGATTTCTTGGCCATATCGCAATGAATACTTGTGACTTGTGCTTCCAATTGACATCTTCAGCGCCATATTGCGCTGGCCAAGGTGACGGAGCGGGATTACGAAAGCATGATCATGGCTGTTGTTCTGTTTATCTTGTTTTGACTGAGACTTGTTAGGATAGACGGTTTTTCATCACTGACTAGCCAAAGCCTTACTCTGCCTGACATCGACCGTAAATTGATAATGAATTTACATGCTTCCGCGACGATTTACCTCTTGATCATCGATCCGATTGAAGATCTTCAATTGTTAATTCTCTTGCCTCGACTCATAGCCATGATGAGCTCTTGATCATGTTTCCTTAACCCTCTATTTTTTACGGAAGAATGATCAAGCTGCTGCTCTTGATCATCGTTTC"

Pattern = "TGATCA"

print("The number of times " + Pattern + 
      " exists in the ori of Vibrio is: " + 
      str(PatternCount(Text, Pattern)))

# %% Find the frequency of a k-mer in a sequence
# Sample Input:
# ACGTTGCATGTCGCATGATGCATGAGAGCT
# 4

# Sample Output:
# CATG GCAT
Text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
k = 4

def FrequencyMap(Text, k):                                                 # This func. keeps only the unique patterns
    freq = {}
    n = len(Text)
    for i in range(n - k + 1):
        Pattern = Text[i:i + k]
        freq[Pattern] = 0                                                  # This line adds the pattern as key and 0 as value
        for j in range(n - k + 1):                                         # We're going through the string AGAIN
            if Text[j:j + k] == Pattern:
                freq[Pattern] = freq[Pattern] + 1
    return freq

print(FrequencyMap(Text, k))

def FrequentWords(Text, k):
    words = [] # New list
    
    freq = FrequencyMap(Text, k)
    m = max(freq.values())
    
    for key in freq: # For every key in freq
        if freq[key] == m: # If the value of each key == m
            pattern = key # Grab that key
            words.append(pattern) # Keep it
    return words

print(FrequentWords(Text, k))

# %% Find the frequency of a k-mer in Vibrio cholerae

# Copy your updated FrequentWords function (along with all required subroutines) below this line
def FrequencyMap(Text, k):                                                 # This func. keeps only the unique patterns
    freq = {}
    n = len(Text)
    for i in range(n - k + 1):
        Pattern = Text[i:i + k]
        freq[Pattern] = 0                                                  # This line adds the pattern as key and 0 as value
        for j in range(n - k + 1):                                         # We're going through the string AGAIN
            if Text[j:j + k] == Pattern:
                freq[Pattern] = freq[Pattern] + 1
    return freq

def FrequentWords(Text, k):
    words = [] # New list
    
    freq = FrequencyMap(Text, k)
    m = max(freq.values())
    
    for key in freq: # For every key in freq
        if freq[key] == m: # If the value of each key == m
            pattern = key # Grab that key
            words.append(pattern) # Keep it
    return words

# Now set Text equal to the Vibrio cholerae oriC and k equal to 10
Text = "ATCAATGATCAACGTAAGCTTCTAAGCATGATCAAGGTGCTCACACAGTTTATCCACAACCTGAGTGGATGACATCAAGATAGGTCGTTGTATCTCCTTCCTCTCGTACTCTCATGACCACGGAAAGATGATCAAGAGAGGATGATTTCTTGGCCATATCGCAATGAATACTTGTGACTTGTGCTTCCAATTGACATCTTCAGCGCCATATTGCGCTGGCCAAGGTGACGGAGCGGGATTACGAAAGCATGATCATGGCTGTTGTTCTGTTTATCTTGTTTTGACTGAGACTTGTTAGGATAGACGGTTTTTCATCACTGACTAGCCAAAGCCTTACTCTGCCTGACATCGACCGTAAATTGATAATGAATTTACATGCTTCCGCGACGATTTACCTCTTGATCATCGATCCGATTGAAGATCTTCAATTGTTAATTCTCTTGCCTCGACTCATAGCCATGATGAGCTCTTGATCATGTTTCCTTAACCCTCTATTTTTTACGGAAGAATGATCAAGCTGCTGCTCTTGATCATCGTTTC"
k = 10
# Finally, print the result of calling FrequentWords on Text and k.
print(FrequentWords(Text, k))

# %% Finding the reverse complement of DNA
# Sample Input: AAAACCCGGT
# Sample Output: TGGCCCAAAA

def Reverse(Pattern):
    rev = ""
    
    for char in Pattern:
        rev = char + rev
    return rev
    
print(Reverse("AAAACCCGGT"))

def Complement(Pattern):
    comp = ""
    
    for char in Pattern:
        if char == "A":
            comp = comp + "T"
        elif char == "T":
            comp = comp + "A"
        elif char == "C":
            comp = comp + "G"
        elif char == "G":
            comp = comp + "C"
    return comp

print(Complement("AAAACCCGGT"))

def ReverseComplement(Pattern):
    rev_patt = Reverse(Pattern)
    rc_patt = Complement(rev_patt)
    return rc_patt

print(ReverseComplement("AAAACCCGGT"))

# %% Find patterns and return their positions
Pattern = "ATAT"
Genome = "GATATATGCATATACTT"

def PatternMatching(Pattern, Genome):
    position = []
    
    G_len = len(Genome)
    P_len = len(Pattern)
    
    for n in range(G_len - P_len + 1):
        if Genome[n:(n + P_len)] == Pattern:
            position.append(n)
    return position

print(PatternMatching(Pattern, Genome))

# %% Using the number of C in a half-strand to find ori
def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text) - len(Pattern) + 1):
        if Text[i:i + len(Pattern)] == Pattern:
            count = count + 1
    return count

def SymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    for i in range(n):
        array[i] = PatternCount(ExtendedGenome[i:i+(n//2)], symbol)
    return array

correct_output1 = {0: 4, 1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7: 3}
my_output1 = SymbolArray("AAAAGGGG", "A")
print(correct_output1 == my_output1)

correct_output2 = {0: 7, 1: 7, 2: 7, 3: 7, 4: 7, 5: 7, 6: 7, 7: 6, 8: 6, 9: 6, 10: 6, 11: 6, 12: 6, 13: 6, 14: 6, 15: 6, 16: 6, 17: 5, 18: 5, 19: 5, 20: 4, 21: 4, 22: 4, 23: 4, 24: 4, 25: 3, 26: 3, 27: 3, 28: 3, 29: 3, 30: 3, 31: 3, 32: 3, 33: 3, 34: 3, 35: 3, 36: 3, 37: 3, 38: 3, 39: 3, 40: 3, 41: 3, 42: 3, 43: 2, 44: 2, 45: 2, 46: 2, 47: 2, 48: 2, 49: 2, 50: 3, 51: 3, 52: 3, 53: 3, 54: 3, 55: 3, 56: 3, 57: 3, 58: 2, 59: 2, 60: 2, 61: 2, 62: 3, 63: 3, 64: 3, 65: 3, 66: 3, 67: 3, 68: 3, 69: 3, 70: 3, 71: 3, 72: 3, 73: 3, 74: 3, 75: 3, 76: 4, 77: 4, 78: 4, 79: 4, 80: 4, 81: 4, 82: 4, 83: 4, 84: 4, 85: 4, 86: 5, 87: 5, 88: 5, 89: 6, 90: 6, 91: 6, 92: 6, 93: 6, 94: 7, 95: 7, 96: 7, 97: 7, 98: 7, 99: 7, 100: 7, 101: 7, 102: 7, 103: 7, 104: 6, 105: 6, 106: 6, 107: 7, 108: 7, 109: 7, 110: 7, 111: 7, 112: 8, 113: 8, 114: 8, 115: 8, 116: 7, 117: 7, 118: 7, 119: 7, 120: 7, 121: 7, 122: 7, 123: 7, 124: 7, 125: 7, 126: 7, 127: 8, 128: 7, 129: 7, 130: 7, 131: 7, 132: 7, 133: 7, 134: 7}
my_output2 = SymbolArray("AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTGCATAGAGGAAGCGAGCAAAGGTGGTTTCTTTCGCTTTATCCAGCGCGTTAACCACGTTCTGTGCCGACTTT", 
                         "CC")
print(correct_output2 == my_output2)

# %% A more efficient algorithm for finding occurrences of C
def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text) - len(Pattern) + 1):
        if Text[i:i + len(Pattern)] == Pattern:
            count = count + 1
    return count

def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]

    # look at the first half of Genome to compute first array value
    array[0] = PatternCount(Genome[0:n//2], symbol)

    for i in range(1, n):
        # start by setting the current array value equal to the previous array value
        array[i] = array[i-1]

        # the current array value can differ from the previous array value by at most 1
        if ExtendedGenome[i-1] == symbol:
            array[i] = array[i]-1
        if ExtendedGenome[i+(n//2)-1] == symbol:
            array[i] = array[i]+1
    return array

print(FasterSymbolArray("AAAAGGGG", "A"))

# %% G and C skew to determine forward and reverse half-strands
Genome = "CATGGGCATCGGCCATACGCC"
Genome = "AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTGCATAGAGGAAGCGAGCAAAGGTGGTTTCTTTCGCTTTATCCAGCGCGTTAACCACGTTCTGTGCCGACTTT"

def SkewArray(Genome):
    Skew = {}
    n = len(Genome)
    Skew[0] = 0
    
    for i in range(n):
        if Genome[i] == "T" or Genome[i] == "A":
            Skew[i + 1] = Skew[i]
        elif Genome[i] == "G":
            Skew[i + 1] = Skew[i] + 1
        elif Genome[i] == "C":
            Skew[i + 1] = Skew[i] - 1
    return Skew.values()

print(SkewArray(Genome))

# %% Using the GC skew minimum to locate ori
Genome = "TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT"
Genome = "CATTCCAGTACTTCGATGATGGCGTGAAGA"

def SkewArray(Genome):
    Skew = {}
    n = len(Genome)
    Skew[0] = 0
    
    for i in range(n):
        if Genome[i] == "T" or Genome[i] == "A":
            Skew[i + 1] = Skew[i]
        elif Genome[i] == "G":
            Skew[i + 1] = Skew[i] + 1
        elif Genome[i] == "C":
            Skew[i + 1] = Skew[i] - 1
    return Skew

print(SkewArray(Genome))

def MinimumSkew(Genome):
    positions = []
    skew = SkewArray(Genome)
    skewmin = min(skew.values())
    
    for n in range(len(skew)):
        if skew[n] == skewmin:
            positions.append(n)
            
    return positions

print(MinimumSkew(Genome))

# %% Compute the Hamming distance
p = "GGGCCGTTGGT"
q = "GGACCGTTGAC"
p = "TGACCCGTTATGCTCGAGTTCGGTCAGAGCGTCATTGCGAGTAGTCGTTTGCTTTCTCAAACTCC"
q = "GAGCGATTAAGCGTGACAGCCCCAGGGAACCCACAAAACGTGATCGCAGTCCATCCGATCATACA"

def HammingDistance(p, q):
    Hamming = 0
    
    for n in range(len(p)):
        if p[n] == q[n]:
            Hamming += 0
        elif p[n] != q[n]:
            Hamming += 1
    return Hamming

print(HammingDistance(p, q))

# %% Find all approximate occurrences of a pattern
Pattern = "ATTCTGGA"
Genome = "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT"
d = 3

def HammingDistance(p, q):
    Hamming = 0
    
    for n in range(len(p)):
        if p[n] == q[n]:
            Hamming += 0
        elif p[n] != q[n]:
            Hamming += 1
    return Hamming

def ApproximatePatternMatching(Genome, Pattern, d):
    positions = []
    for n in range(len(Genome) - len(Pattern) + 1):
        subPattern = Genome[n:(n + len(Pattern))]
        if HammingDistance(Pattern, subPattern) <= d:
            positions.append(n)    
    return positions

print(ApproximatePatternMatching(Genome, Pattern, d))

# %% Count all approximate occurrences of a pattern
Pattern = "GAGG"
Genome = "TTTAGAGCCTTCAGAGG"
d = 2

def HammingDistance(p, q):
    Hamming = 0
    
    for n in range(len(p)):
        if p[n] == q[n]:
            Hamming += 0
        elif p[n] != q[n]:
            Hamming += 1
    return Hamming

def ApproximatePatternCount(Genome, Pattern, d):
    count = 0
    for n in range(len(Genome) - len(Pattern) + 1):
        subPattern = Genome[n:(n + len(Pattern))]
        if HammingDistance(Pattern, subPattern) <= d:
            count += 1    
    return count

print(ApproximatePatternCount(Genome, Pattern, d))

# %% Find the most common nucleotides in motifs
Motifs = ["AACGTA", "CCCGTT", "CACCTT", "GGATTA", "TTCCGG"]
Motifs2 = ["GTACAACTGT", "CAACTATGAA", "TCCTACAGGA", "AAGCAAGGGT", "GCGTACGACC", "TCGTCAGCGT", "AACAAGGTCA", "CTCAGGCGTC", "GGATCCAGGT", "GGCAAGTACC"]

def Count(Motifs):
    count = {}
    k = len(Motifs[0])
    for symbol in "ACGT":
    	count[symbol] = []
    	for j in range(k):
    		count[symbol].append(0)
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count

print(Count(Motifs))

def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}
    counts = Count(Motifs)
    for symbol in "ACGT":
    	profile[symbol] = []
    	for j in range(k):
    		profile[symbol].append(counts[symbol][j] / t)
    return profile

print(Profile(Motifs))

def Consensus(Motifs):
    k = len(Motifs[0])
    counts = Count(Motifs)
    consensus = ""
    
    for j in range(k):
        max_num = max(counts["A"][j], counts["C"][j], counts["G"][j], counts["T"][j]) - 1
        for symbol in "ACGT":
            if counts[symbol][j] > max_num:
                max_num = counts[symbol][j]
                consensus += symbol
    return consensus # Note, if 2 nucleotides have the same freq, it won't pick it by random. It'll be alphabetical according to the for loop

print(Consensus(Motifs)) # Should be CACCTA
print(Consensus(Motifs2)) # Should be GACTAAGGGT
        
def Score(Motifs):
    con_seq = Consensus(Motifs)
    counts = Count(Motifs)
    score = 0
    
    for x in range(len(Motifs[0])):
        for symbol in "ACGT":
            if symbol == con_seq[x]:
                col_score = len(Motifs) - counts[symbol][x]
                score += col_score
    return score

print(Score(Motifs))

# %% Calculating the probability of a string
Text = "ACGGGGATTACC"
Profile = {"A": [0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.9, 0.1, 0.1, 0.1, 0.3, 0.0],
           "C": [0.1, 0.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.4, 0.1, 0.2, 0.4, 0.6],
           "G": [0.0, 0.0, 1.0, 1.0, 0.9, 0.9, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0],
           "T": [0.7, 0.2, 0.0, 0.0, 0.1, 0.1, 0.0, 0.5, 0.8, 0.7, 0.3, 0.4]}

def Pr(Text, Profile):
    probability = 1
    for n in range(len(Text)):
        char = Text[n]
        for symbol in "ACGT":
            if char == symbol:
                prob = Profile[symbol][n]
                probability = probability * prob
    return probability

print(Pr(Text, Profile)) # Should be 0.0008398080000000002

# %% Returning the most probable k-mer of all possible k-mers
Text = "ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT"
k = 5
Profile = {"A": [0.2, 0.2, 0.3, 0.2, 0.3],
           "C": [0.4, 0.3, 0.1, 0.5, 0.1],
           "G": [0.3, 0.3, 0.5, 0.2, 0.4],
           "T": [0.1, 0.2, 0.1, 0.1, 0.2]}

def FrequencyMap(Text, k):                                                 # This func. keeps only the unique patterns
    freq = {}
    n = len(Text)
    for i in range(n - k + 1):
        Pattern = Text[i:i + k]
        freq[Pattern] = 0                                                  # This line adds the pattern as key and 0 as value
        for j in range(n - k + 1):                                         # We're going through the string AGAIN
            if Text[j:j + k] == Pattern:
                freq[Pattern] = freq[Pattern] + 1
    return freq

def Pr(Text, Profile):
    probability = 1
    for n in range(len(Text)):
        char = Text[n]
        for symbol in "ACGT":
            if char == symbol:
                prob = Profile[symbol][n]
                probability = probability * prob
    return probability

def ProfileMostProbableKmer(Text, k, Profile):
    kmers_freq = FrequencyMap(Text, k)
    kmers_prob = {}
    for key in kmers_freq:
        prob = Pr(key, Profile)
        kmers_prob[key] = prob
    max_prob = max(kmers_prob.values())
    return list(kmers_prob.keys())[list(kmers_prob.values()).index(max_prob)] # This part returns the key when given the value

print(ProfileMostProbableKmer(Text, k, Profile)) # Should be CCGAG

# %% The greedy motif search algorithm
k = 3
t = 5
Dna = ["GGCGTTCAGGCA", "AAGAATCAGTCA", "CAAGGAGTTCGC", "CACGTCAATCAC", "CAATAATATTCG"]

def Count(Motifs):
    count = {}
    k = len(Motifs[0])
    for symbol in "ACGT":
    	count[symbol] = []
    	for j in range(k):
    		count[symbol].append(0)
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count

def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}
    counts = Count(Motifs)
    for symbol in "ACGT":
    	profile[symbol] = []
    	for j in range(k):
    		profile[symbol].append(counts[symbol][j] / t)
    return profile

def Consensus(Motifs):
    k = len(Motifs[0])
    counts = Count(Motifs)
    consensus = ""
    
    for j in range(k):
        max_num = max(counts["A"][j], counts["C"][j], counts["G"][j], counts["T"][j]) - 1
        for symbol in "ACGT":
            if counts[symbol][j] > max_num:
                max_num = counts[symbol][j]
                consensus += symbol
    return consensus

def Score(Motifs):
    con_seq = Consensus(Motifs)
    counts = Count(Motifs)
    score = 0
    
    for x in range(len(Motifs[0])):
        for symbol in "ACGT":
            if symbol == con_seq[x]:
                col_score = len(Motifs) - counts[symbol][x]
                score += col_score
    return score

def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n - k + 1):
        Pattern = Text[i:i + k]
        freq[Pattern] = 0
        for j in range(n - k + 1):
            if Text[j:j + k] == Pattern:
                freq[Pattern] = freq[Pattern] + 1
    return freq

def Pr(Text, Profile):
    probability = 1
    for n in range(len(Text)):
        char = Text[n]
        for symbol in "ACGT":
            if char == symbol:
                prob = Profile[symbol][n]
                probability = probability * prob
    return probability

def ProfileMostProbableKmer(Text, k, Profile):
    kmers_freq = FrequencyMap(Text, k)
    kmers_prob = {}
    for key in kmers_freq:
        prob = Pr(key, Profile)
        kmers_prob[key] = prob
    max_prob = max(kmers_prob.values())
    return list(kmers_prob.keys())[list(kmers_prob.values()).index(max_prob)] # This part returns the key when given the value

def GreedyMotifSearch(Dna, k, t):
    best_motifs = []
    for x in range(t):
        best_motifs.append(Dna[x][0:k]) # The first k-mers from the DNA sequences
    for rnd in range(0, len(Dna[0]) - k + 1): # Will iterate through all possible k-mers in the first sequence
        Motifs = []
        Motifs.append(Dna[0][rnd:rnd + k]) # Grabs the next k-mer in the first sequence and adds it to a list
        for strng in range(1, t): # Iterates through the rest of the sequences
            prof = Profile(Motifs[0:strng]) # Creates a frequency profile from the k-mers from the first sequence
            Motifs.append(ProfileMostProbableKmer(Dna[strng], k, prof)) # Adds most prob k-mer from Dna[strng] according to the current profile
        if Score(Motifs) < Score(best_motifs):
            best_motifs = Motifs
    return best_motifs

print(GreedyMotifSearch(Dna, k, t)) # Output should be CAG / CAG / CAA / CAA / CAA

# %% Find the DosR binding site in M. tuberculosis
k = 15
t = 10
Dna = ["GCGCCCCGCCCGGACAGCCATGCGCTAACCCTGGCTTCGATGGCGCCGGCTCAGTTAGGGCCGGAAGTCCCCAATGTGGCAGACCTTTCGCCCCTGGCGGACGAATGACCCCAGTGGCCGGGACTTCAGGCCCTATCGGAGGGCTCCGGCGCGGTGGTCGGATTTGTCTGTGGAGGTTACACCCCAATCGCAAGGATGCATTATGACCAGCGAGCTGAGCCTGGTCGCCACTGGAAAGGGGAGCAACATC",
       "CCGATCGGCATCACTATCGGTCCTGCGGCCGCCCATAGCGCTATATCCGGCTGGTGAAATCAATTGACAACCTTCGACTTTGAGGTGGCCTACGGCGAGGACAAGCCAGGCAAGCCAGCTGCCTCAACGCGCGCCAGTACGGGTCCATCGACCCGCGGCCCACGGGTCAAACGACCCTAGTGTTCGCTACGACGTGGTCGTACCTTCGGCAGCAGATCAGCAATAGCACCCCGACTCGAGGAGGATCCCG",
       "ACCGTCGATGTGCCCGGTCGCGCCGCGTCCACCTCGGTCATCGACCCCACGATGAGGACGCCATCGGCCGCGACCAAGCCCCGTGAAACTCTGACGGCGTGCTGGCCGGGCTGCGGCACCTGATCACCTTAGGGCACTTGGGCCACCACAACGGGCCGCCGGTCTCGACAGTGGCCACCACCACACAGGTGACTTCCGGCGGGACGTAAGTCCCTAACGCGTCGTTCCGCACGCGGTTAGCTTTGCTGCC",
       "GGGTCAGGTATATTTATCGCACACTTGGGCACATGACACACAAGCGCCAGAATCCCGGACCGAACCGAGCACCGTGGGTGGGCAGCCTCCATACAGCGATGACCTGATCGATCATCGGCCAGGGCGCCGGGCTTCCAACCGTGGCCGTCTCAGTACCCAGCCTCATTGACCCTTCGACGCATCCACTGCGCGTAAGTCGGCTCAACCCTTTCAAACCGCTGGATTACCGACCGCAGAAAGGGGGCAGGAC",
       "GTAGGTCAAACCGGGTGTACATACCCGCTCAATCGCCCAGCACTTCGGGCAGATCACCGGGTTTCCCCGGTATCACCAATACTGCCACCAAACACAGCAGGCGGGAAGGGGCGAAAGTCCCTTATCCGACAATAAAACTTCGCTTGTTCGACGCCCGGTTCACCCGATATGCACGGCGCCCAGCCATTCGTGACCGACGTCCCCAGCCCCAAGGCCGAACGACCCTAGGAGCCACGAGCAATTCACAGCG",
       "CCGCTGGCGACGCTGTTCGCCGGCAGCGTGCGTGACGACTTCGAGCTGCCCGACTACACCTGGTGACCACCGCCGACGGGCACCTCTCCGCCAGGTAGGCACGGTTTGTCGCCGGCAATGTGACCTTTGGGCGCGGTCTTGAGGACCTTCGGCCCCACCCACGAGGCCGCCGCCGGCCGATCGTATGACGTGCAATGTACGCCATAGGGTGCGTGTTACGGCGATTACCTGAAGGCGGCGGTGGTCCGGA",
       "GGCCAACTGCACCGCGCTCTTGATGACATCGGTGGTCACCATGGTGTCCGGCATGATCAACCTCCGCTGTTCGATATCACCCCGATCTTTCTGAACGGCGGTTGGCAGACAACAGGGTCAATGGTCCCCAAGTGGATCACCGACGGGCGCGGACAAATGGCCCGCGCTTCGGGGACTTCTGTCCCTAGCCCTGGCCACGATGGGCTGGTCGGATCAAAGGCATCCGTTTCCATCGATTAGGAGGCATCAA",
       "GTACATGTCCAGAGCGAGCCTCAGCTTCTGCGCAGCGACGGAAACTGCCACACTCAAAGCCTACTGGGCGCACGTGTGGCAACGAGTCGATCCACACGAAATGCCGCCGTTGGGCCGCGGACTAGCCGAATTTTCCGGGTGGTGACACAGCCCACATTTGGCATGGGACTTTCGGCCCTGTCCGCGTCCGTGTCGGCCAGACAAGCTTTGGGCATTGGCCACAATCGGGCCACAATCGAAAGCCGAGCAG",
       "GGCAGCTGTCGGCAACTGTAAGCCATTTCTGGGACTTTGCTGTGAAAAGCTGGGCGATGGTTGTGGACCTGGACGAGCCACCCGTGCGATAGGTGAGATTCATTCTCGCCCTGACGGGTTGCGTCTGTCATCGGTCGATAAGGACTAACGGCCCTCAGGTGGGGACCAACGCCCCTGGGAGATAGCGGTCCCCGCCAGTAACGTACCGCTGAACCGACGGGATGTATCCGCCCCAGCGAAGGAGACGGCG",
       "TCAGCACCATGACCGCCTGGCCACCAATCGCCCGTAACAAGCGGGACGTCCGCGACGACGCGTGCGCTAGCGCCGTGGCGGTGACAACGACCAGATATGGTCCGAGCACGCGGGCGAACCTCGTGTTCTGGCCTCGGCCAGTTGTGTAGAGCTCATCGCTGTCATCGAGCGATATCCGACCACTGATCCAAGTCGGGGGCTCTGGGGACCGAAGTCCCCGGGCTCGGAGCTATCGGACCTCACGATCACC"]

def Count(Motifs):
    count = {}
    k = len(Motifs[0])
    for symbol in "ACGT":
    	count[symbol] = []
    	for j in range(k):
    		count[symbol].append(0)
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count

def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = Count(Motifs)
    for i in "ACTG":
        for j in range(k):
            profile[i][j] = profile[i][j]/t
    return profile

def Consensus(Motifs):
    k = len(Motifs[0])
    counts = Count(Motifs)
    consensus = ""
    for j in range(k):
        max_num = max(counts["A"][j], counts["C"][j], counts["G"][j], counts["T"][j]) - 1
        for symbol in "ACGT":
            if counts[symbol][j] > max_num:
                max_num = counts[symbol][j]
                consensus += symbol
    return consensus

def Score(Motifs):
    con_seq = Consensus(Motifs)
    counts = Count(Motifs)
    score = 0
    
    for x in range(len(Motifs[0])):
        for symbol in "ACGT":
            if symbol == con_seq[x]:
                col_score = len(Motifs) - counts[symbol][x]
                score += col_score
    return score

def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n - k + 1):
        Pattern = Text[i:i + k]
        freq[Pattern] = 0
        for j in range(n - k + 1):
            if Text[j:j + k] == Pattern:
                freq[Pattern] = freq[Pattern] + 1
    return freq

def Pr(Text, Profile):
    probability = 1
    for n in range(len(Text)):
        char = Text[n]
        for symbol in "ACGT":
            if char == symbol:
                prob = Profile[symbol][n]
                probability = probability * prob
    return probability

def ProfileMostProbableKmer(Text, k, Profile):
    kmers_freq = FrequencyMap(Text, k)
    kmers_prob = {}
    for key in kmers_freq:
        prob = Pr(key, Profile)
        kmers_prob[key] = prob
    max_prob = max(kmers_prob.values())
    return list(kmers_prob.keys())[list(kmers_prob.values()).index(max_prob)] # This part returns the key when given the value

def GreedyMotifSearch(Dna, k, t):
    best_motifs = []
    for x in range(t):
        best_motifs.append(Dna[x][0:k]) # The first k-mers from the DNA sequences
    for rnd in range(0, len(Dna[0]) - k + 1): # Will iterate through all possible k-mers in the first sequence
        Motifs = []
        Motifs.append(Dna[0][rnd:rnd + k]) # Grabs the next k-mer in the first sequence and adds it to a list
        for strng in range(1, t): # Iterates through the rest of the sequences
            prof = Profile(Motifs[0:strng]) # Creates a frequency profile from the k-mers from the first sequence
            Motifs.append(ProfileMostProbableKmer(Dna[strng], k, prof)) # Adds most prob k-mer from Dna[strng] according to the current profile
        if Score(Motifs) < Score(best_motifs):
            best_motifs = Motifs
    return best_motifs

Motifs = GreedyMotifSearch(Dna, k, t)
print(Motifs)
print(Score(Motifs))

# %% Using pseudocounts when calculating a string's probability
Motifs = ["AACGTA", "CCCGTT", "CACCTT", "GGATTA", "TTCCGG"]

def CountWithPseudocounts(Motifs):
    count = {}
    k = len(Motifs[0])
    for symbol in "ACGT":
    	count[symbol] = []
    	for j in range(k):
    		count[symbol].append(1)
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count

print(CountWithPseudocounts(Motifs))

def ProfileWithPseudocounts(Motifs):
    t = len(Motifs) + 4 # + 4 because one was added to each (nucleotide) row
    k = len(Motifs[0])
    profile = CountWithPseudocounts(Motifs)
    for symbol in "ACTG":
        for char in range(k):
            profile[symbol][char] = profile[symbol][char]/t
    return profile

print(ProfileWithPseudocounts(Motifs))

# %% Greedy Motif Search with Pseudocounts
k = 3
t = 5
Dna = ["GGCGTTCAGGCA", "AAGAATCAGTCA", "CAAGGAGTTCGC", "CACGTCAATCAC", "CAATAATATTCG"]

def CountWithPseudocounts(Motifs):
    count = {}
    k = len(Motifs[0])
    for symbol in "ACGT":
    	count[symbol] = []
    	for j in range(k):
    		count[symbol].append(1)
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count

def ProfileWithPseudocounts(Motifs):
    t = len(Motifs) + 4 # + 4 because one was added to each (nucleotide) row
    k = len(Motifs[0])
    profile = CountWithPseudocounts(Motifs)
    for symbol in "ACTG":
        for char in range(k):
            profile[symbol][char] = profile[symbol][char]/t
    return profile

def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n - k + 1):
        Pattern = Text[i:i + k]
        freq[Pattern] = 0
        for j in range(n - k + 1):
            if Text[j:j + k] == Pattern:
                freq[Pattern] = freq[Pattern] + 1
    return freq

def Pr(Text, Profile):
    probability = 1
    for n in range(len(Text)):
        probability = probability * ProfileWithPseudocounts[Text[n]][n]
    return probability

def ProfileMostProbableKmer(Text, k, Profile):
    p = -1
    result = Text[0:k]
    for i in range(len(Text) - k + 1):
        seq = Text[i:i + k]
        pr = Pr(seq, Profile)
        if pr > p:
            p = pr
            result = seq
    return result

def Consensus(Motifs):
    k = len(Motifs[0])
    counts = CountWithPseudocounts(Motifs)
    consensus = ""
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if counts[symbol][j] > m:
                m = counts[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus

def Score(Motifs):
    # con_seq = Consensus(Motifs)
    counts = CountWithPseudocounts(Motifs)
    score = 0
    sum1 = 0
    for x in range(len(Motifs[0])):
        m = 0
        for symbol in "ACGT":
            if counts[symbol][x] > m:
                sum1 += counts[symbol][x]
    for j in range(len(Motifs[0])):
        m = 0
        for symbol in "AGTC":
            if counts[symbol][j] > m:
                m = counts[symbol][j]
        score += m  
    return sum1 - score

def GreedyMotifSearchWithPseudocounts(Dna, k, t):
    best_motifs = []
    for x in range(t):
        best_motifs.append(Dna[x][0:k]) # The first k-mers from the DNA sequences
    for rnd in range(0, len(Dna[0]) - k + 1): # Will iterate through all possible k-mers in the first sequence
        Motifs = []
        Motifs.append(Dna[0][rnd:rnd + k]) # Grabs the next k-mer in the first sequence and adds it to a list
        for strng in range(1, t): # Iterates through the rest of the sequences
            prof = ProfileWithPseudocounts(Motifs[0:strng]) # Creates a frequency profile from the k-mers from the first sequence
            Motifs.append(ProfileMostProbableKmer(Dna[strng], k, prof)) # Adds most prob k-mer from Dna[strng] according to the current profile
        if Score(Motifs) < Score(best_motifs):
            best_motifs = Motifs
    return best_motifs

print(GreedyMotifSearchWithPseudocounts(Dna, k, t)) # Result should be TTC / ATC / TTC / ATC / TTC
print(Score(Motifs))

# %% Greedy Motif Search with Pseudocounts and the DosR Dataset
k = 15
t = 10
Dna = ["GCGCCCCGCCCGGACAGCCATGCGCTAACCCTGGCTTCGATGGCGCCGGCTCAGTTAGGGCCGGAAGTCCCCAATGTGGCAGACCTTTCGCCCCTGGCGGACGAATGACCCCAGTGGCCGGGACTTCAGGCCCTATCGGAGGGCTCCGGCGCGGTGGTCGGATTTGTCTGTGGAGGTTACACCCCAATCGCAAGGATGCATTATGACCAGCGAGCTGAGCCTGGTCGCCACTGGAAAGGGGAGCAACATC",
       "CCGATCGGCATCACTATCGGTCCTGCGGCCGCCCATAGCGCTATATCCGGCTGGTGAAATCAATTGACAACCTTCGACTTTGAGGTGGCCTACGGCGAGGACAAGCCAGGCAAGCCAGCTGCCTCAACGCGCGCCAGTACGGGTCCATCGACCCGCGGCCCACGGGTCAAACGACCCTAGTGTTCGCTACGACGTGGTCGTACCTTCGGCAGCAGATCAGCAATAGCACCCCGACTCGAGGAGGATCCCG",
       "ACCGTCGATGTGCCCGGTCGCGCCGCGTCCACCTCGGTCATCGACCCCACGATGAGGACGCCATCGGCCGCGACCAAGCCCCGTGAAACTCTGACGGCGTGCTGGCCGGGCTGCGGCACCTGATCACCTTAGGGCACTTGGGCCACCACAACGGGCCGCCGGTCTCGACAGTGGCCACCACCACACAGGTGACTTCCGGCGGGACGTAAGTCCCTAACGCGTCGTTCCGCACGCGGTTAGCTTTGCTGCC",
       "GGGTCAGGTATATTTATCGCACACTTGGGCACATGACACACAAGCGCCAGAATCCCGGACCGAACCGAGCACCGTGGGTGGGCAGCCTCCATACAGCGATGACCTGATCGATCATCGGCCAGGGCGCCGGGCTTCCAACCGTGGCCGTCTCAGTACCCAGCCTCATTGACCCTTCGACGCATCCACTGCGCGTAAGTCGGCTCAACCCTTTCAAACCGCTGGATTACCGACCGCAGAAAGGGGGCAGGAC",
       "GTAGGTCAAACCGGGTGTACATACCCGCTCAATCGCCCAGCACTTCGGGCAGATCACCGGGTTTCCCCGGTATCACCAATACTGCCACCAAACACAGCAGGCGGGAAGGGGCGAAAGTCCCTTATCCGACAATAAAACTTCGCTTGTTCGACGCCCGGTTCACCCGATATGCACGGCGCCCAGCCATTCGTGACCGACGTCCCCAGCCCCAAGGCCGAACGACCCTAGGAGCCACGAGCAATTCACAGCG",
       "CCGCTGGCGACGCTGTTCGCCGGCAGCGTGCGTGACGACTTCGAGCTGCCCGACTACACCTGGTGACCACCGCCGACGGGCACCTCTCCGCCAGGTAGGCACGGTTTGTCGCCGGCAATGTGACCTTTGGGCGCGGTCTTGAGGACCTTCGGCCCCACCCACGAGGCCGCCGCCGGCCGATCGTATGACGTGCAATGTACGCCATAGGGTGCGTGTTACGGCGATTACCTGAAGGCGGCGGTGGTCCGGA",
       "GGCCAACTGCACCGCGCTCTTGATGACATCGGTGGTCACCATGGTGTCCGGCATGATCAACCTCCGCTGTTCGATATCACCCCGATCTTTCTGAACGGCGGTTGGCAGACAACAGGGTCAATGGTCCCCAAGTGGATCACCGACGGGCGCGGACAAATGGCCCGCGCTTCGGGGACTTCTGTCCCTAGCCCTGGCCACGATGGGCTGGTCGGATCAAAGGCATCCGTTTCCATCGATTAGGAGGCATCAA",
       "GTACATGTCCAGAGCGAGCCTCAGCTTCTGCGCAGCGACGGAAACTGCCACACTCAAAGCCTACTGGGCGCACGTGTGGCAACGAGTCGATCCACACGAAATGCCGCCGTTGGGCCGCGGACTAGCCGAATTTTCCGGGTGGTGACACAGCCCACATTTGGCATGGGACTTTCGGCCCTGTCCGCGTCCGTGTCGGCCAGACAAGCTTTGGGCATTGGCCACAATCGGGCCACAATCGAAAGCCGAGCAG",
       "GGCAGCTGTCGGCAACTGTAAGCCATTTCTGGGACTTTGCTGTGAAAAGCTGGGCGATGGTTGTGGACCTGGACGAGCCACCCGTGCGATAGGTGAGATTCATTCTCGCCCTGACGGGTTGCGTCTGTCATCGGTCGATAAGGACTAACGGCCCTCAGGTGGGGACCAACGCCCCTGGGAGATAGCGGTCCCCGCCAGTAACGTACCGCTGAACCGACGGGATGTATCCGCCCCAGCGAAGGAGACGGCG",
       "TCAGCACCATGACCGCCTGGCCACCAATCGCCCGTAACAAGCGGGACGTCCGCGACGACGCGTGCGCTAGCGCCGTGGCGGTGACAACGACCAGATATGGTCCGAGCACGCGGGCGAACCTCGTGTTCTGGCCTCGGCCAGTTGTGTAGAGCTCATCGCTGTCATCGAGCGATATCCGACCACTGATCCAAGTCGGGGGCTCTGGGGACCGAAGTCCCCGGGCTCGGAGCTATCGGACCTCACGATCACC"]

Motifs = GreedyMotifSearchWithPseudocounts(Dna, k, t)
print(Motifs)
print(Score(Motifs))

# %% Going back and retesting my algorithms
### Count ###########################################################################################################################################
Motifs = ["AACGTA", "CCCGTT", "CACCTT", "GGATTA", "TTCCGG"]
Motifs2 = ["GTACAACTGT", "CAACTATGAA", "TCCTACAGGA", "AAGCAAGGGT", "GCGTACGACC", "TCGTCAGCGT", "AACAAGGTCA", "CTCAGGCGTC", "GGATCCAGGT", "GGCAAGTACC"]
Output = {"A": [1, 2, 1, 0, 0, 2], 
          "C": [2, 1, 4, 2, 0, 0], 
          "G": [1, 1, 0, 2, 1, 1], 
          "T": [1, 1, 0, 1, 4, 2]}
Output2 = {"A": [2, 3, 3, 3, 6, 4, 2, 2, 1, 3], 
           "C": [2, 3, 4, 3, 2, 3, 2, 1, 3, 3], 
           "G": [4, 2, 3, 0, 1, 3, 4, 5, 5, 0], 
           "T": [2, 2, 0, 4, 1, 0, 2, 2, 1, 4]}

def Count(Motifs):
    count = {}
    k = len(Motifs[0])
    for symbol in "ACGT":
    	count[symbol] = []
    	for j in range(k):
    		count[symbol].append(0)
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count

Output == Count(Motifs)
Output2 == Count(Motifs2)

### Profile #########################################################################################################################################
Motifs = ["AACGTA", "CCCGTT", "CACCTT", "GGATTA", "TTCCGG"]
Motifs2 = ["GTACAACTGT", "CAACTATGAA", "TCCTACAGGA", "AAGCAAGGGT", "GCGTACGACC", "TCGTCAGCGT", "AACAAGGTCA", "CTCAGGCGTC", "GGATCCAGGT", "GGCAAGTACC"]
Output = {"A": [0.2, 0.4, 0.2, 0.0, 0.0, 0.4], 
          "C": [0.4, 0.2, 0.8, 0.4, 0.0, 0.0], 
          "G": [0.2, 0.2, 0.0, 0.4, 0.2, 0.2], 
          "T": [0.2, 0.2, 0.0, 0.2, 0.8, 0.4]}
Output2 = {"A": [0.2, 0.3, 0.3, 0.3, 0.6, 0.4, 0.2, 0.2, 0.1, 0.3], 
           "C": [0.2, 0.3, 0.4, 0.3, 0.2, 0.3, 0.2, 0.1, 0.3, 0.3], 
           "G": [0.4, 0.2, 0.3, 0.0, 0.1, 0.3, 0.4, 0.5, 0.5, 0.0], 
           "T": [0.2, 0.2, 0.0, 0.4, 0.1, 0.0, 0.2, 0.2, 0.1, 0.4]}

def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = Count(Motifs)
    for symbol in "ACTG":
        for char in range(k):
            profile[symbol][char] = profile[symbol][char]/t
    return profile

Output == Profile(Motifs)
Output2 == Profile(Motifs2)

### Consensus #######################################################################################################################################
Motifs = ["AACGTA", "CCCGTT", "CACCTT", "GGATTA", "TTCCGG"]
Motifs2 = ["GTACAACTGT", "CAACTATGAA", "TCCTACAGGA", "AAGCAAGGGT", "GCGTACGACC", "TCGTCAGCGT", "AACAAGGTCA", "CTCAGGCGTC", "GGATCCAGGT", "GGCAAGTACC"]
Output = "CACCTA"
Output2 = "GACTAAGGGT"

def Consensus(Motifs):
    k = len(Motifs[0])
    counts = Count(Motifs)
    consensus = ""
    for j in range(k):
        m = 0
        for symbol in "ACGT":
            if counts[symbol][j] > m: # If the count for this symbol is greater than 0 or that from the previous letter
                m = counts[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus

Output == Consensus(Motifs)
Output2 == Consensus(Motifs2)

### Score ###########################################################################################################################################
Motifs = ["AACGTA", "CCCGTT", "CACCTT", "GGATTA", "TTCCGG"]
Motifs2 = ["GTACAACTGT", "CAACTATGAA", "TCCTACAGGA", "AAGCAAGGGT", "GCGTACGACC", "TCGTCAGCGT", "AACAAGGTCA", "CTCAGGCGTC", "GGATCCAGGT", "GGCAAGTACC"]
Output = 14
Output2 = 57

def Score(Motifs):
    con_seq = Consensus(Motifs)
    counts = Count(Motifs)
    score = 0
    for x in range(len(Motifs[0])):
        for symbol in "ACGT":
            if symbol == con_seq[x]:
                col_score = len(Motifs) - counts[symbol][x]
                score += col_score
    return score

Output == Score(Motifs)
Output2 == Score(Motifs2)
    
### Pr ##############################################################################################################################################
Text = "ACGGGGATTACC"
Profile = {"A": [0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.9, 0.1, 0.1, 0.1, 0.3, 0.0],
           "C": [0.1, 0.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.4, 0.1, 0.2, 0.4, 0.6],
           "G": [0.0, 0.0, 1.0, 1.0, 0.9, 0.9, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0],
           "T": [0.7, 0.2, 0.0, 0.0, 0.1, 0.1, 0.0, 0.5, 0.8, 0.7, 0.3, 0.4]}
Output = 0.0008398080000000002
Text2 = "TCGGGGGCCACC"
Profile2 = {"A": [0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.9, 0.1, 0.1, 0.1, 0.3, 0.0],
            "C": [0.1, 0.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.4, 0.1, 0.2, 0.4, 0.6],
            "G": [0.0, 0.0, 1.0, 1.0, 0.9, 0.9, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0],
            "T": [0.7, 0.2, 0.0, 0.0, 0.1, 0.1, 0.0, 0.5, 0.8, 0.7, 0.3, 0.4]}
Output2 = 3.265920000000001e-05

def Pr(Text, Profile):
    probability = 1
    for n in range(len(Text)):
        probability = probability * Profile[Text[n]][n]
    return probability

Output == Pr(Text, Profile)
Output2 == Pr(Text2, Profile2)

### ProfileMostProbableKmer #########################################################################################################################
Text = "ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT"
k = 5
Profile = {"A": [0.2, 0.2, 0.3, 0.2, 0.3],
           "C": [0.4, 0.3, 0.1, 0.5, 0.1],
           "G": [0.3, 0.3, 0.5, 0.2, 0.4],
           "T": [0.1, 0.2, 0.1, 0.1, 0.2]}
Output = "CCGAG"

Text2 = "AGCAGCTTTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATCTGAACTGGTTACCTGCCGTGAGTAAAT"
k2 = 8
Profile2 = {"A": [0.7, 0.2, 0.1, 0.5, 0.4, 0.3, 0.2, 0.1],
            "C": [0.2, 0.2, 0.5, 0.4, 0.2, 0.3, 0.1, 0.6],
            "G": [0.1, 0.3, 0.2, 0.1, 0.2, 0.1, 0.4, 0.2],
            "T": [0.0, 0.3, 0.2, 0.0, 0.2, 0.3, 0.3, 0.1]}
Output2 = "AGCAGCTT"

Text3 = "TTACCATGGGACCGCTGACTGATTTCTGGCGTCAGCGTGATGCTGGTGTGGATGACATTCCGGTGCGCTTTGTAAGCAGAGTTTA"
k3 = 12
Profile3 = {"A": [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.1, 0.2, 0.3, 0.4, 0.5],
            "C": [0.3, 0.2, 0.1, 0.1, 0.2, 0.1, 0.1, 0.4, 0.3, 0.2, 0.2, 0.1],
            "G": [0.2, 0.1, 0.4, 0.3, 0.1, 0.1, 0.1, 0.3, 0.1, 0.1, 0.2, 0.1],
            "T": [0.3, 0.4, 0.1, 0.1, 0.1, 0.1, 0.0, 0.2, 0.4, 0.4, 0.2, 0.3]}
Output3 = "AAGCAGAGTTTA"

Text4 = "AACCGGTT"
k4 = 3
Profile4 = {"A": [1.0, 1.0, 1.0],
            "C": [0.0, 0.0, 0.0],
            "G": [0.0, 0.0, 0.0],
            "T": [0.0, 0.0, 0.0]}
Output4 = "AAC"

Text5 = "TTACCATGGGACCGCTGACTGATTTCTGGCGTCAGCGTGATGCTGGTGTGGATGACATTCCGGTGCGCTTTGTAAGCAGAGTTTA"
k5 = 5
Profile5 = {"A": [0.2, 0.2, 0.3, 0.2, 0.3],
            "C": [0.4, 0.3, 0.1, 0.5, 0.1],
            "G": [0.3, 0.3, 0.5, 0.2, 0.4],
            "T": [0.1, 0.2, 0.1, 0.1, 0.2]}
Output5 = "CAGCG"

def FrequencyMap(Text, k):                                                 # This func. keeps only the unique patterns
    freq = {}
    n = len(Text)
    for i in range(n - k + 1):
        Pattern = Text[i:i + k]
        freq[Pattern] = 0                                                  # This line adds the pattern as key and 0 as value
        for j in range(n - k + 1):                                         # We're going through the string AGAIN
            if Text[j:j + k] == Pattern:
                freq[Pattern] = freq[Pattern] + 1
    return freq

def ProfileMostProbableKmer(Text, k, Profile):
    kmers_freq = FrequencyMap(Text, k)
    kmers_prob = {}
    for key in kmers_freq:
        prob = Pr(key, Profile)
        kmers_prob[key] = prob
    max_prob = max(kmers_prob.values())
    return list(kmers_prob.keys())[list(kmers_prob.values()).index(max_prob)] # This part returns the key when given the value

Output == ProfileMostProbableKmer(Text, k, Profile)
Output2 == ProfileMostProbableKmer(Text2, k2, Profile2)
Output3 == ProfileMostProbableKmer(Text3, k3, Profile3)
Output4 == ProfileMostProbableKmer(Text4, k4, Profile4)
Output5 == ProfileMostProbableKmer(Text5, k5, Profile5)

### GreedyMotifSearch ###############################################################################################################################
k = 3
t = 5
Dna = ["GGCGTTCAGGCA", "AAGAATCAGTCA", "CAAGGAGTTCGC", "CACGTCAATCAC", "CAATAATATTCG"]
Output = ["CAG", "CAG", "CAA", "CAA", "CAA"]

k2 = 3
t2 = 4
Dna2 = ["GCCCAA", "GGCCTG", "AACCTA", "TTCCTT"]
Output2 = ["GCC", "GCC", "AAC", "TTC"]

k3 = 5
t3 = 8
Dna3 = ["GAGGCGCACATCATTATCGATAACGATTCGCCGCATTGCC", "TCATCGAATCCGATAACTGACACCTGCTCTGGCACCGCTC", 
        "TCGGCGGTATAGCCAGAAAGCGTAGTGCCAATAATTTCCT", "GAGTCGTGGTGAAGTGTGGGTTATGGGGAAAGGCAGACTG", 
        "GACGGCAACTACGGTTACAACGCAGCAACCGAAGAATATT", "TCTGTTGTTGCTAACACCGTTAAAGGCGGCGACGGCAACT", 
        "AAGCGGCCAACGTAGGCGCGGCTTGGCATCTCGGTGTGTG", "AATTGAAAGGCGCATCTTACTCTTTTCGCTTTCAAAAAAA"]
Output3 = ["GAGGC", "TCATC", "TCGGC", "GAGTC", "GCAGC", "GCGGC", "GCGGC", "GCATC"]

k4 = 6
t4 = 5
Dna4 = ["GCAGGTTAATACCGCGGATCAGCTGAGAAACCGGAATGTGCGT", "CCTGCATGCCCGGTTTGAGGAACATCAGCGAAGAACTGTGCGT", "GCGCCAGTAACCCGTGCCAGTCAGGTTAATGGCAGTAACATTT", 
        "AACCCGTGCCAGTCAGGTTAATGGCAGTAACATTTATGCCTTC", "ATGCCTTCCGCGCCAATTGTTCGTATCGTCGCCACTTCGAGTG"]
Output4 = ["GTGCGT", "GTGCGT", "GCGCCA", "GTGCCA", "GCGCCA"]

k5 = 5
t5 = 8
Dna5 = ["GACCTACGGTTACAACGCAGCAACCGAAGAATATTGGCAA", "TCATTATCGATAACGATTCGCCGGAGGCCATTGCCGCACA", "GGAGTCTGGTGAAGTGTGGGTTATGGGGCAGACTGGGAAA",
        "GAATCCGATAACTGACACCTGCTCTGGCACCGCTCTCATC", "AAGCGCGTAGGCGCGGCTTGGCATCTCGGTGTGTGGCCAA", "AATTGAAAGGCGCATCTTACTCTTTTCGCTTAAAATCAAA",
        "GGTATAGCCAGAAAGCGTAGTTAATTTCGGCTCCTGCCAA", "TCTGTTGTTGCTAACACCGTTAAAGGCGGCGACGGCAACT"]
Output5 = ["GCAGC", "TCATT", "GGAGT", "TCATC", "GCATC", "GCATC", "GGTAT", "GCAAC"]

k6 = 4
t6 = 8
Dna6 = ["GACCTACGGTTACAACGCAGCAACCGAAGAATATTGGCAA", "TCATTATCGATAACGATTCGCCGGAGGCCATTGCCGCACA", "GGAGTCTGGTGAAGTGTGGGTTATGGGGCAGACTGGGAAA",
        "GAATCCGATAACTGACACCTGCTCTGGCACCGCTCTCATC", "AAGCGCGTAGGCGCGGCTTGGCATCTCGGTGTGTGGCCAA", "AATTGAAAGGCGCATCTTACTCTTTTCGCTTAAAATCAAA",
        "GGTATAGCCAGAAAGCGTAGTTAATTTCGGCTCCTGCCAA", "TCTGTTGTTGCTAACACCGTTAAAGGCGGCGACGGCAACT"]
Output6 = ["CGCA", "CGCA", "GGAG", "GGCA", "GGCA", "CGCA", "GGTA", "GGCA"]

def GreedyMotifSearch(Dna, k, t):
    best_motifs = []
    for x in range(t):
        best_motifs.append(Dna[x][0:k]) # The first k-mers from the DNA sequences
    for rnd in range(0, len(Dna[0]) - k + 1): # Will iterate through all possible k-mers in the first sequence
        Motifs = []
        Motifs.append(Dna[0][rnd:rnd + k]) # Grabs the next k-mer in the first sequence and adds it to a list
        for strng in range(1, t): # Iterates through the rest of the sequences
            prof = Profile(Motifs[0:strng]) # Creates a frequency profile from the k-mers from the first sequence
            Motifs.append(ProfileMostProbableKmer(Dna[strng], k, prof)) # Adds most prob k-mer from Dna[strng] according to the current profile
        if Score(Motifs) < Score(best_motifs):
            best_motifs = Motifs
    return best_motifs

Output == GreedyMotifSearch(Dna, k, t)
Output2 == GreedyMotifSearch(Dna2, k2, t2)
Output3 == GreedyMotifSearch(Dna3, k3, t3)
Output4 == GreedyMotifSearch(Dna4, k4, t4)
Output5 == GreedyMotifSearch(Dna5, k5, t5)
Output6 == GreedyMotifSearch(Dna6, k6, t6)

### Pseudocounts ####################################################################################################################################
Motifs = ["AACGTA", "CCCGTT", "CACCTT", "GGATTA", "TTCCGG"]
Output = {"A": [2, 3, 2, 1, 1, 3], "C": [3, 2, 5, 3, 1, 1], "G": [2, 2, 1, 3, 2, 2], "T": [2, 2, 1, 2, 5, 3]}

Motifs2 = ["GTACAACTGT", "CAACTATGAA", "TCCTACAGGA", "AAGCAAGGGT", "GCGTACGACC", "TCGTCAGCGT", "AACAAGGTCA", "CTCAGGCGTC", "GGATCCAGGT", "GGCAAGTACC"]
Output2 = {"A": [3, 4, 4, 4, 7, 5, 3, 3, 2, 4], "C": [3, 4, 5, 4, 3, 4, 3, 2, 4, 4], 
           "G": [5, 3, 4, 1, 2, 4, 5, 6, 6, 1], "T": [3, 3, 1, 5, 2, 1, 3, 3, 2, 5]}

def CountWithPseudocounts(Motifs):
    count = {}
    k = len(Motifs[0])
    for symbol in "ACGT":
    	count[symbol] = []
    	for j in range(k):
    		count[symbol].append(1)
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count

Output == CountWithPseudocounts(Motifs)
Output2 == CountWithPseudocounts(Motifs2)

### ProfileWithPseudocounts #########################################################################################################################
Motifs = ["AACGTA", "CCCGTT", "CACCTT", "GGATTA", "TTCCGG"]
Output = {"A": [0.2222222222222222, 0.3333333333333333, 0.2222222222222222, 0.1111111111111111, 0.1111111111111111, 0.3333333333333333], 
          "C": [0.3333333333333333, 0.2222222222222222, 0.5555555555555556, 0.3333333333333333, 0.1111111111111111, 0.1111111111111111],
          "G": [0.2222222222222222, 0.2222222222222222, 0.1111111111111111, 0.3333333333333333, 0.2222222222222222, 0.2222222222222222],
          "T": [0.2222222222222222, 0.2222222222222222, 0.1111111111111111, 0.2222222222222222, 0.5555555555555556, 0.3333333333333333]}

Motifs2 = ["GTACAACTGT", "CAACTATGAA", "TCCTACAGGA", "AAGCAAGGGT", "GCGTACGACC", "TCGTCAGCGT", "AACAAGGTCA", "CTCAGGCGTC", "GGATCCAGGT", "GGCAAGTACC"]
Output2 = {"A": [0.21428571428571427, 0.2857142857142857, 0.2857142857142857, 0.2857142857142857, 0.5, 0.35714285714285715, 0.21428571428571427, 0.21428571428571427, 0.14285714285714285, 0.2857142857142857], 
           "C": [0.21428571428571427, 0.2857142857142857, 0.35714285714285715, 0.2857142857142857, 0.21428571428571427, 0.2857142857142857, 0.21428571428571427, 0.14285714285714285, 0.2857142857142857, 0.2857142857142857], 
           "G": [0.35714285714285715, 0.21428571428571427, 0.2857142857142857, 0.07142857142857142, 0.14285714285714285, 0.2857142857142857, 0.35714285714285715, 0.42857142857142855, 0.42857142857142855, 0.07142857142857142],
           "T": [0.21428571428571427, 0.21428571428571427, 0.07142857142857142, 0.35714285714285715, 0.14285714285714285, 0.07142857142857142, 0.21428571428571427, 0.21428571428571427, 0.14285714285714285, 0.35714285714285715]}

def ProfileWithPseudocounts(Motifs):
    t = len(Motifs) + 4 # + 4 because one was added to each (nucleotide) row
    k = len(Motifs[0])
    profile = CountWithPseudocounts(Motifs)
    for symbol in "ACTG":
        for char in range(k):
            profile[symbol][char] = profile[symbol][char]/t
    return profile

Output == ProfileWithPseudocounts(Motifs)
Output2 == ProfileWithPseudocounts(Motifs2)

# %% Return probable k-mers given profile and sequences
Profile = {"A": [0.8, 0.0, 0.0, 0.2], 
           "C": [0.0, 0.6, 0.2, 0.0], 
           "G": [0.2, 0.2, 0.8, 0.0], 
           "T": [0.0, 0.2, 0.0, 0.8]}
Dna = ["TTACCTTAAC", "GATGTCTGTC", "ACGGCGTTAG", "CCCTAACGAG", "CGTCAGAGGT"]
Output = ["ACCT", "ATGT", "GCGT", "ACGA", "AGGT"]

Profile2 = {"A": [0.5, 0.0, 0.2, 0.2], 
            "C": [0.3, 0.6, 0.2, 0.0], 
            "G": [0.2, 0.2, 0.6, 0.0], 
            "T": [0.0, 0.2, 0.0, 0.8]}
Dna2 = ["TTACCTTAAC", "GATGTCTGTC", "ACGGCGTTAG", "CCCTAACGAG", "CGTCAGAGGT"]
Output2 = ["ACCT", "ATGT", "GCGT", "ACGA", "AGGT"]

def FrequencyMap(Text, k):                                                 # This func. keeps only the unique patterns
    freq = {}
    n = len(Text)
    for i in range(n - k + 1):
        Pattern = Text[i:i + k]
        freq[Pattern] = 0                                                  # This line adds the pattern as key and 0 as value
        for j in range(n - k + 1):                                         # We're going through the string AGAIN
            if Text[j:j + k] == Pattern:
                freq[Pattern] = freq[Pattern] + 1
    return freq

def Pr(Text, Profile):
    probability = 1
    for n in range(len(Text)):
        probability = probability * Profile[Text[n]][n]
    return probability

def ProfileMostProbableKmer(Text, k, Profile):
    kmers_freq = FrequencyMap(Text, k)
    kmers_prob = {}
    for key in kmers_freq:
        prob = Pr(key, Profile)
        kmers_prob[key] = prob
    max_prob = max(kmers_prob.values())
    return list(kmers_prob.keys())[list(kmers_prob.values()).index(max_prob)] # This part returns the key when given the value

def Motifs(Profile, Dna):
    prob_kmers = []
    for n in range(len(Dna)):
        prob_kmers.append(ProfileMostProbableKmer(Dna[n], 4, Profile))
    return prob_kmers

Output == Motifs(Profile, Dna)
Output2 == Motifs(Profile2, Dna2)

# %% Selecting the Random Motifs
import random

k = 3
t = 5
Dna = ["TTACCTTAAC", "GATGTCTGTC", "ACGGCGTTAG", "CCCTAACGAG", "CGTCAGAGGT"]

def RandomMotifs(Dna, k, t):
    rand_kmers = []
    for seq in range(len(Dna)):
        ran_num = random.randint(0, len(Dna[0]) - k)
        rand_kmers.append(Dna[seq][ran_num:ran_num + k])
    return rand_kmers

print(RandomMotifs(Dna, k, t))

# %% Randomized Motif Search
# import random

k = 8
t = 5
Dna = ["CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA", "GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG", "TAGTACCGAGACCGAAAGAAGTATACAGGCGT", 
       "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC", "AATCCACCAGCTCCACGTGCAATGTTGGCCTA"]

def RandomMotifs(Dna, k, t):
    rand_kmers = []
    for seq in range(len(Dna)):
        ran_num = random.randint(0, len(Dna[0]) - k)
        rand_kmers.append(Dna[seq][ran_num:ran_num + k])
    return rand_kmers

def CountWithPseudocounts(Motifs):
    count = {}
    k = len(Motifs[0])
    for symbol in "ACGT":
    	count[symbol] = []
    	for j in range(k):
    		count[symbol].append(1)
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count

def ProfileWithPseudocounts(Motifs):
    t = len(Motifs) + 4 # + 4 because one was added to each (nucleotide) row
    k = len(Motifs[0])
    profile = CountWithPseudocounts(Motifs)
    for symbol in "ACTG":
        for char in range(k):
            profile[symbol][char] = profile[symbol][char]/t
    return profile

def FrequencyMap(Text, k):                                                 # This func. keeps only the unique patterns
    freq = {}
    n = len(Text)
    for i in range(n - k + 1):
        Pattern = Text[i:i + k]
        freq[Pattern] = 0                                                  # This line adds the pattern as key and 0 as value
        for j in range(n - k + 1):                                         # We're going through the string AGAIN
            if Text[j:j + k] == Pattern:
                freq[Pattern] = freq[Pattern] + 1
    return freq

def Pr(Text, Profile):
    probability = 1
    for n in range(len(Text)):
        probability = probability * Profile[Text[n]][n]
    return probability

def ProfileMostProbableKmer(Text, k, Profile):
    kmers_freq = FrequencyMap(Text, k)
    kmers_prob = {}
    for key in kmers_freq:
        prob = Pr(key, Profile)
        kmers_prob[key] = prob
    max_prob = max(kmers_prob.values())
    return list(kmers_prob.keys())[list(kmers_prob.values()).index(max_prob)] # This part returns the key when given the value

def Motifs(Profile, k, Dna):
    prob_kmers = []
    for n in range(len(Dna)):
        prob_kmers.append(ProfileMostProbableKmer(Dna[n], k, Profile))
    return prob_kmers

def Consensus(Motifs):
    k = len(Motifs[0])
    counts = CountWithPseudocounts(Motifs)
    consensus = ""
    for j in range(k):
        m = 0
        for symbol in "ACGT":
            if counts[symbol][j] > m: # If the count for this symbol is greater than 0 or that from the previous letter
                m = counts[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus

def Score(Motifs):
    con_seq = Consensus(Motifs)
    counts = CountWithPseudocounts(Motifs)
    score = 0
    for x in range(len(Motifs[0])):
        for symbol in "ACGT":
            if symbol == con_seq[x]:
                col_score = len(Motifs) - counts[symbol][x]
                score += col_score
    return score

def RandomizedMotifSearch(Dna, k, t):
    ranMotifs = RandomMotifs(Dna, k, t)
    bestMotifs = ranMotifs
    while True:
        profile = ProfileWithPseudocounts(ranMotifs)
        ranMotifs = Motifs(profile, k, Dna)
        if Score(ranMotifs) < Score(bestMotifs):
            bestMotifs = ranMotifs
        else:
            return bestMotifs 

print(RandomizedMotifSearch(Dna, k, t))

# %% Set a number of runs to the RandomizedMotifSearch
k = 3
t = 5
N = 100
Dna = ["GGCGTTCAGGCA", "AAGAATCAGTCA", "CAAGGAGTTCGC", "CACGTCAATCAC", "CAATAATATTCG"]

def RandomMotifs(Dna, k, t):
    rand_kmers = []
    for seq in range(len(Dna)):
        ran_num = random.randint(0, len(Dna[0]) - k)
        rand_kmers.append(Dna[seq][ran_num:ran_num + k])
    return rand_kmers

def CountWithPseudocounts(Motifs):
    count = {}
    k = len(Motifs[0])
    for symbol in "ACGT":
    	count[symbol] = []
    	for j in range(k):
    		count[symbol].append(1)
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count

def ProfileWithPseudocounts(Motifs):
    t = len(Motifs) + 4 # + 4 because one was added to each (nucleotide) row
    k = len(Motifs[0])
    profile = CountWithPseudocounts(Motifs)
    for symbol in "ACTG":
        for char in range(k):
            profile[symbol][char] = profile[symbol][char]/t
    return profile

def FrequencyMap(Text, k):                                                 # This func. keeps only the unique patterns
    freq = {}
    n = len(Text)
    for i in range(n - k + 1):
        Pattern = Text[i:i + k]
        freq[Pattern] = 0                                                  # This line adds the pattern as key and 0 as value
        for j in range(n - k + 1):                                         # We're going through the string AGAIN
            if Text[j:j + k] == Pattern:
                freq[Pattern] = freq[Pattern] + 1
    return freq

def Pr(Text, Profile):
    probability = 1
    for n in range(len(Text)):
        probability = probability * Profile[Text[n]][n]
    return probability

def ProfileMostProbableKmer(Text, k, Profile):
    kmers_freq = FrequencyMap(Text, k)
    kmers_prob = {}
    for key in kmers_freq:
        prob = Pr(key, Profile)
        kmers_prob[key] = prob
    max_prob = max(kmers_prob.values())
    return list(kmers_prob.keys())[list(kmers_prob.values()).index(max_prob)] # This part returns the key when given the value

def Motifs(Profile, k, Dna):
    prob_kmers = []
    for n in range(len(Dna)):
        prob_kmers.append(ProfileMostProbableKmer(Dna[n], k, Profile))
    return prob_kmers

def Consensus(Motifs):
    k = len(Motifs[0])
    counts = CountWithPseudocounts(Motifs)
    consensus = ""
    for j in range(k):
        m = 0
        for symbol in "ACGT":
            if counts[symbol][j] > m: # If the count for this symbol is greater than 0 or that from the previous letter
                m = counts[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus

def Score(Motifs):
    con_seq = Consensus(Motifs)
    counts = CountWithPseudocounts(Motifs)
    score = 0
    for x in range(len(Motifs[0])):
        for symbol in "ACGT":
            if symbol == con_seq[x]:
                col_score = len(Motifs) - counts[symbol][x]
                score += col_score
    return score

def RandomizedMotifSearch(Dna, k, t, N):
    ranMotifs = RandomMotifs(Dna, k, t)
    bestMotifs = ranMotifs
    while N > 0:
        profile = ProfileWithPseudocounts(ranMotifs)
        ranMotifs = Motifs(profile, k, Dna)
        if Score(ranMotifs) < Score(bestMotifs):
            bestMotifs = ranMotifs
            N -= 1
        else:
            return bestMotifs

print(RandomizedMotifSearch(Dna, k, t, N))

# %% Normalize probabilities
Probabilities = {"A": 0.1, "C": 0.1, "G": 0.1, "T": 0.1}
Output = {"A": 0.25, "C": 0.25, "G": 0.25, "T": 0.25}

def Normalize(Probabilities):
    sum_prob = sum(Probabilities.values())
    adj_prob = {}
    for x in Probabilities.keys():
        adj_prob[x] = Probabilities[x] / sum_prob
    return adj_prob

print(Normalize(Probabilities))

# %% Weighted die probabilities
# import random

Probabilities = {"A": 0.25, "C": 0.25, "G": 0.25, "T": 0.25}

def WeightedDie(Probabilities):
    n = random.uniform(0, 1)
    for prob in Probabilities:
        n -= Probabilities[prob]
        if n <= 0:
            return prob

print(WeightedDie(Probabilities))

# %% Most Probable String Using Gibbs Sampling
# import random
Text = "AAACCCAAACCC"
Profile = {"A": [0.5, 0.1], "C": [0.3, 0.2], "G": [0.2, 0.4], "T": [0.0, 0.3]}
k = 2

def Pr(Text, Profile):
    probability = 1
    for n in range(len(Text)):
        probability = probability * Profile[Text[n]][n]
    return probability

def Normalize(Probabilities):
    sum_prob = sum(Probabilities.values())
    adj_prob = {}
    for x in Probabilities.keys():
        adj_prob[x] = Probabilities[x] / sum_prob
    return adj_prob

def WeightedDie(Probabilities):
    n = random.uniform(0, 1)
    for prob in Probabilities:
        n -= Probabilities[prob]
        if n <= 0:
            return prob

def ProfileGeneratedString(Text, Profile, k):
    n = len(Text)
    Prob = {} 
    for i in range(0, n - k + 1):
        Prob[Text[i:i + k]] = Pr(Text[i:i + k], Profile)
    Prob = Normalize(Prob)
    return WeightedDie(Prob)

# %% Gibbs Sampling
# import random
k = 8
t = 5
N = 100
Dna = ["CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA", "GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG", "TAGTACCGAGACCGAAAGAAGTATACAGGCGT", 
       "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC", "AATCCACCAGCTCCACGTGCAATGTTGGCCTA"]

def GibbsSampler(Dna, k, t, N):
    motifs = RandomMotifs(Dna, k, t) # Grabs one random motif per sequence
    best_motifs = motifs
    for iteration in range(1, N):
        ran_seq = random.randint(0, t-1) # Which sequence will be excluded
        red_motifs = []
        for red in range(0, t):
            if red != ran_seq:
                red_motifs.append(motifs[red])
        Profile = ProfileWithPseudocounts(red_motifs)
        motifs[ran_seq] = ProfileGeneratedString(Dna[ran_seq], Profile, k)
        if Score(motifs) < Score(best_motifs):
                best_motifs = motifs
    return best_motifs
        
def RandomMotifs(Dna, k, t):
    rand_kmers = []
    for seq in range(len(Dna)):
        ran_num = random.randint(0, len(Dna[0]) - k)
        rand_kmers.append(Dna[seq][ran_num:ran_num + k])
    return rand_kmers

def CountWithPseudocounts(Motifs):
    count = {}
    k = len(Motifs[0])
    for symbol in "ACGT":
    	count[symbol] = []
    	for j in range(k):
    		count[symbol].append(1)
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count

def ProfileWithPseudocounts(Motifs):
    t = len(Motifs) + 4 # + 4 because one was added to each (nucleotide) row
    k = len(Motifs[0])
    profile = CountWithPseudocounts(Motifs)
    for symbol in "ACTG":
        for char in range(k):
            profile[symbol][char] = profile[symbol][char]/t
    return profile

def Pr(Text, Profile):
    probability = 1
    for n in range(len(Text)):
        probability = probability * Profile[Text[n]][n]
    return probability

def Normalize(Probabilities):
    sum_prob = sum(Probabilities.values())
    adj_prob = {}
    for x in Probabilities.keys():
        adj_prob[x] = Probabilities[x] / sum_prob
    return adj_prob

def WeightedDie(Probabilities):
    n = random.uniform(0, 1)
    for prob in Probabilities:
        n -= Probabilities[prob]
        if n <= 0:
            return prob

def ProfileGeneratedString(Text, Profile, k):
    n = len(Text)
    Prob = {} 
    for i in range(0, n - k + 1):
        Prob[Text[i:i + k]] = Pr(Text[i:i + k], Profile)
    Prob = Normalize(Prob)
    return WeightedDie(Prob)

def Consensus(Motifs):
    k = len(Motifs[0])
    counts = CountWithPseudocounts(Motifs)
    consensus = ""
    for j in range(k):
        m = 0
        for symbol in "ACGT":
            if counts[symbol][j] > m: # If the count for this symbol is greater than 0 or that from the previous letter
                m = counts[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus

def Score(Motifs):
    con_seq = Consensus(Motifs)
    counts = CountWithPseudocounts(Motifs)
    score = 0
    for x in range(len(Motifs[0])):
        for symbol in "ACGT":
            if symbol == con_seq[x]:
                col_score = len(Motifs) - counts[symbol][x]
                score += col_score
    return score