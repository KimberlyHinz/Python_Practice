# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 21:23:07 2022

@author: Kim
"""

# %% 1. NCBI
# Import Modules
from Bio.Blast import NCBIWWW
from Bio import SeqIO, SearchIO

help(NCBIWWW) # For more help on this module

# %% 1.1. Nucleotide BLAST

# !ls # The names of the fasta files we have in our system
### notebook.ipynb	nuc_seq.fasta  prot_seq.fasta
# This won't work in Spyder, but will in Jupyter

nuc_record = SeqIO.read("nuc_seq.fasta", format = "fasta") # Read the fasta file

len(nuc_record) # Number of base pairs
### 774

nuc_record.description # The description

nuc_record.seq # The sequence

result_handle = NCBIWWW.qblast("blastn", "nt", nuc_record.seq) # This will return xml format
blast_result = SearchIO.read(result_handle, "blast-xml")

print(blast_result[0:2])

### \u200b

### Program: blastn (2.13.0+)
###   Query: No (774)
###           definition line
###   Target: nt
###     Hits: ----  -----  ----------------------------------------------------------
###             #  # HSP  ID + description
###           ----  -----  ----------------------------------------------------------
###             0      1  gi|2209437801|gb|ON017230.1|  Severe acute respiratory ...
###             1      1  gi|2209437658|gb|ON017219.1|  Severe acute respiratory ...

Seq = blast_result[0] # Get the first result

print(f"Sequence ID: {Seq.id}")
### Sequence ID: gi|2209437801|gb|ON017230.1|

print(f"Sequence Description: {Seq.description}")
### Sequence Description: Severe acute respiratory syndrome coronavirus 2 isolate SARS-CoV-2/human/PRY/WOR12903A659_202103274_2-4710620/2020 
### ORF1ab polyprotein (ORF1ab), ORF1a polyprotein (ORF1ab), surface glycoprotein (S), ORF3a protein (ORF3a), envelope protein (E), membrane 
### glycoprotein (M), ORF6 protein (ORF6), and ORF7a protein (ORF7a) genes, complete cds; ORF7b gene, complete sequence; and ORF8 protein (ORF8), 
### nucleocapsid phosphoprotein (N), and ORF10 protein (ORF10) genes, complete cds

details = Seq[0]
print(f"E-value: {details.evalue}")
### E-value: 0.0

print(f"alignment:\n{details.aln}")
### alignment:
### Alignment with 2 rows and 774 columns
### ATCGCTCCAGGGCAAACTGGAAAGATTGCTGATTATAATTATAA...GGT No
### ATCGCTCCAGGGCAAACTGGAAAGATTGCTGATTATAATTATAA...GGT gi|2209437801|gb|ON017230.1|

# %% 1.2. Protein BLAST

prot_record = SeqIO.read("prot_seq.fasta", format = "fasta")

len(prot_record)
### 258

result_handle = NCBIWWW.qblast("blastp", "pdb", prot_record.seq)
blast_result = SearchIO.read(result_handle, "blast-xml")

print(blast_result[0:2])
### Program: blastp (2.13.0+)
###   Query: unnamed (258)
###          protein product
###  Target: pdb
###    Hits: ----  -----  ----------------------------------------------------------
###             #  # HSP  ID + description
###          ----  -----  ----------------------------------------------------------
###             0      1  pdb|7CAB|A  Chain A, Spike glycoprotein [Severe acute r...
###             1      1  pdb|7BYR|A  Chain A, Spike glycoprotein [Severe acute r...

Seq = blast_result[0]

print(f"Sequence ID: {Seq.id}")
### Sequence ID: pdb|7CAB|A
print(f"Sequence Description: {Seq.description}")
### Sequence Description: Chain A, Spike glycoprotein [Severe acute respiratory syndrome coronavirus 2]
details = Seq[0]
print(f"E-value: {details.evalue}")
### E-value: 0.0

print(f"alignment:\n {details.aln}")
### alignment:
###  Alignment with 2 rows and 258 columns
### IAPGQTGKIADYNYKLPDDFTGCVIAWNSNNLDSKVGGNYNYLY...PIG unnamed
### IAPGQTGKIADYNYKLPDDFTGCVIAWNSNNLDSKVGGNYNYLY...PIG pdb|7CAB|A

# %% 2. ENTREZ
# Import Modules
from Bio import Entrez # To fetch literature and associated sequence details

help(Entrez)

Entrez.email = "datacyclopes@gmail.com" # Required, can be your email

handle = Entrez.einfo()
record = Entrez.read(handle)
record["DbList"] # == database list
### ['pubmed', 'protein', 'nuccore', 'ipg', 'nucleotide', 'structure', 'genome', 'annotinfo', 'assembly', 'bioproject', 'biosample', 'blastdbinfo', 
### 'books', 'cdd', 'clinvar', 'gap', 'gapplus', 'grasp', 'dbvar', 'gene', 'gds', 'geoprofiles', 'homologene', 'medgen', 'mesh', 'ncbisearch', 
### 'nlmcatalog', 'omim', 'orgtrack', 'pmc', 'popset', 'proteinclusters', 'pcassay', 'protfam', 'biosystems', 'pccompound', 'pcsubstance', 
### 'seqannot', 'snp', 'sra', 'taxonomy', 'biocollections', 'gtr']

# %% 2.1. PUBMED
handle = Entrez.einfo(db = "pubmed")
record = Entrez.read(handle)
record["DbInfo"]["Description"]
### 'PubMed bibliographic record'

record["DbInfo"]["Count"]
### '33861266'

handle = Entrez.esearch(db = "pubmed", term = "biopython") # Filter literature
record = Entrez.read(handle)
record["IdList"] # All literature containing biopython in the title
### ['34735950', '34484417', '34434786', '34189012', '33994075', '33902722', '33809815', '33242467', '32044951', '31762715', '31278684', '31069053', 
### '30013827', '29641230', '28011774', '24929426', '24497503', '24267035', '24194598', '23842806']

handle = Entrez.esummary(db="pubmed", id='34735950, 34484417')
records = Entrez.parse(handle)

for record in records:
    print(record['AuthorList'], record["Title"], record["PubDate"], record["FullJournalName"])

### ['Zelenova M', 'Ivanova A', 'Semyonov S', 'Gankin Y'] Analysis of 329,942 SARS-CoV-2 records retrieved from GISAID database. 2021 Dec Computers 
### in biology and medicine
### ['Li Y', 'Wang J', 'Li Y', 'Liu C', 'Gong X', 'Zhuang Y', 'Chen L', 'Sun K'] Identification of Immune-Related Genes in Sepsis due to Community-
### Acquired Pneumonia. 2021 Computational and mathematical methods in medicine

handle = Entrez.efetch(db="pubmed", id="19811691")
print(handle.read()) # The JSON file

# %% 2.2. Nucleotide
handle = Entrez.esearch(db="nucleotide", retmax=10, term = "Severe acute respiratory syndrome") # Retrieve 10 records, 
record = Entrez.read(handle)
record["IdList"]
### ['2211361926', '2211361913', '2211361900', '2211361887', '2211361874', '2211361861', '2211361848', '2211361835', '2211361822', '2211361809']

handle = Entrez.efetch(db = "nucleotide", id = "2211361926", rettype = "gb", retmode = "text") # GenBank, Output is text
print(handle.read())
### LOCUS       ON055363               29795 bp    RNA     linear   VRL 23-MAR-2022
### DEFINITION  Severe acute respiratory syndrome coronavirus 2 isolate
###             SARS-CoV-2/human/USA/CA-OC-FG-284702/2022, complete genome.
### ACCESSION   ON055363
### ...

handle = Entrez.esearch(db='nucleotide', term='accD[Gene Name] AND "E. coli"[Organism]', retmax="20")
result_list = Entrez.read(handle)

id_list = result_list["IdList"]
count = result_list["Count"]

print(id_list)
### ['2211362512', '2211362116', '2211362109', '2211362106', '2211362101', '2211362099', '2211362095', '2211362024', '2211362021', '2211362020', 
### '2211360872', '2211357834', '2211357829', '2211355924', '2211355923', '2211355922', '2211325780', '2211295008', '2211295007', '2211295006']
print(count)
### 159536

handle.close() # To close this handle

# %% 3. PDB
# Import Modules

from Bio.PDB import PDBParser,PDBList # Get protein structure from protein sequences

# help(PDBList)

pdbl = PDBList()
pdbl.retrieve_pdb_file("7BYR", file_format = "pdb", pdir = "dir")
### Downloading PDB structure '7BYR'...
### 
### 'dir/pdb7byr.ent'

parser = PDBParser()
structure = parser.get_structure("7BYR", "dir/pdb7byr.ent") # Ignore warning

for chain in structure[0]:
    print(f"chainid: {chain.id}") # Should give 11 chains, named in alphabetical order
### chainid: A
### chainid: B
### chainid: C
### chainid: H
### chainid: L
### chainid: D
### chainid: E
### chainid: F
### chainid: G
### chainid: I
### chainid: J

resolution = structure.header["resolution"]
resolution # in angstroms
### 3.84

keywords = structure.header["keywords"]
keywords
### 'sars-cov-2, antigen, rbd, neutralizing antibody, viral protein'

# %% 4. EXPASy

# %% 4.1. PROSITE
# Import Modules
from Bio import ExPASy # ExPASy is operated by Swiss Institute of Bioinformatics
from Bio.ExPASy import Prosite 
# Prosite is a protein database and consists of entries describing the protein families,
# domains, and functional sites, as well as amino acid patterns and profiles in them

# help(Prosite)

handle = ExPASy.get_prosite_raw("PS51442")
record = Prosite.read(handle)
print(record.description)
### Coronavirus main protease (M-pro) domain profile.

print(record.pdb_structs[:10]) # Fetch the various PDB structures possessing this domain profile
### ['1LVO', '1P9S', '1P9U', '1Q2W', '1UJ1', '1UK2', '1UK3', '1UK4', '1WOF', '1Z1I']

handle = ExPASy.get_prosite_raw("PS00001")
record = Prosite.read(handle)
print(record.pattern) # Find patterns in the domain
### N-{P}-[ST]-{P}.

# %% 4.2. ScanProsite
# Import Modules
from Bio.ExPASy import ScanProsite

prot_record = SeqIO.read("prot_seq.fasta", format="fasta")
len(prot_record.seq)
### 258

handle = ScanProsite.scan(seq=prot_record.seq, mirror="https://prosite.expasy.org/")
result = ScanProsite.read(handle)

result.n_match # Number of matches
### 1

result[0]
### {'sequence_ac': 'USERSEQ1',
###  'start': 1,
###  'stop': 118,
###  'signature_ac': 'PS51921',
###  'score': '32.871',
###  'level': '0'}

# %% 5. KEGG
# Import Modules
from Bio.KEGG import REST, Enzyme 
# To procure genes and the pathways from KEGG database using the enzyme commission (EC) number, which is assigned to all the enzyme.
# KEGG == Kyoto Encyclopedia of Genes and Genomes is a collection of databases dealing with genomes, biological pathways, diseases, drugs, and 
# chemical substances.

help(Enzyme)

request = REST.kegg_get("ec:5.4.2.2")
open("ec_5.4.2.2.txt", "w").write(request.read()) # Write as text file
### 227693

records = Enzyme.parse(open("ec_5.4.2.2.txt"))
record = list(records)[0]
record.classname
### ['Isomerases;',
###  'Intramolecular transferases;',
###  'Phosphotransferases (phosphomutases)']

record.pathway
### [('PATH', 'ec00010', 'Glycolysis / Gluconeogenesis'),
###  ('PATH', 'ec00030', 'Pentose phosphate pathway'),
###  ('PATH', 'ec00052', 'Galactose metabolism'),
###  ('PATH', 'ec00230', 'Purine metabolism'),
###  ('PATH', 'ec00500', 'Starch and sucrose metabolism'),
###  ('PATH', 'ec00520', 'Amino sugar and nucleotide sugar metabolism'),
###  ('PATH', 'ec00521', 'Streptomycin biosynthesis'),
###  ('PATH', 'ec01100', 'Metabolic pathways'),
###  ('PATH', 'ec01110', 'Biosynthesis of secondary metabolites'),
###  ('PATH', 'ec01120', 'Microbial metabolism in diverse environments')]

record.genes[:10]
### [('HSA', ['5236', '55276']),
###  ('PTR', ['456908', '461162']),
###  ('PPS', ['100977295', '100993927']),
###  ('GGO', ['101128874', '101131551']),
###  ('PON', ['100190836', '100438793']),
###  ('NLE', ['100596081', '100600656']),
###  ('MCC', ['100424648', '699401']),
###  ('MCF', ['101925921', '102130622']),
###  ('CSAB', ['103224690', '103246223']),
###  ('CATY', ['105584868', '105595930'])]

# Cleaner version with just gene names
list_genes = []
for x, y in record.genes:
    list_genes += x.split("\n") # remove \n character
print(list_genes[:10])
### ['HSA', 'PTR', 'PPS', 'GGO', 'PON', 'NLE', 'MCC', 'MCF', 'CSAB', 'CATY']
