###### DNA PROJECT #####


class Sequence:

	def __init__(self, dna_seq):
		"""This is the constructor class. This __init__ class makes the input case insensitive"""

		self.dna_seq = dna_seq.lower()


	def base_count(self):
		"""base_count returns the number of bases in the input sequence object"""

		count = len(self.dna_seq)

		return(count)

	
	def is_dna(self):
		"""Checks whether the input Sequence object is a DNA"""

		valid_dna = "atgc"
		validity = all(i in valid_dna for i in self.dna_seq)

		return(validity)

	
	def __eq__(self,other):
		"""Overrides the default __eq__ with the newly defined comparison function"""

		if isinstance(self,Sequence) == isinstance(other,Sequence) and self.dna_seq == other.dna_seq:
			return(True)

		else:
			return(False)

	
	def comp_seq(self):
		"""Generates complementary sequence object for the input sequence object"""

		comp_base = str.maketrans("atgc","tacg")
		comp_dna = self.dna_seq.translate(comp_base)
		comp_dna = Sequence(comp_dna)

		return(comp_dna)

	
	def mis_match(self,other):
		"""Returns the first mismatch index value"""

		seq1 = self.dna_seq
		seq2 = other.dna_seq

		if len(seq1) != len(seq2):
			raise Exception('Cannot compare sequences of different lengths')

		else:
			for i in range(0,len(seq1)):
				if seq1[i] != seq2[i]:
					return(i)
					break
			else:
				return(-1)

	
	def gene_finder(self):
		"""Split the genome file into individual genes based on the full stop sequence and generates a list"""
		seq = self.dna_seq
		stop_code = 'AAAAAAAAAATTTTTTTTTT' 
		genes = seq.split(stop_code.lower())
		genes = [Sequence(gene) for gene in genes]
		return(genes)


	
	def swap_mut(self,other):
		"""Counts the number of swap mutation for two sequence objects being compared and returns the count"""

		seq1 = self.dna_seq
		seq2 = other.dna_seq

		mut_count = 0

		if len(seq1) != len(seq2):
			raise Exception('Cannot compare sequences of different lengths')

		else:
			for i in range(0,len(seq1)):
				if seq1[i] != seq2[i]:
					mut_count += 1
			return(mut_count)

###########################################################################################################################################################


def read_genome(file):    #reads a genome file and creates sequence object containing the DNA sequence

	from itertools import islice

	with open(file,mode = "r", encoding = "ascii") as genome:
		for line in islice(genome,2):
			seq_dat = line
	
	seq_dat = Sequence(seq_dat)
	seq_len = Sequence.base_count(seq_dat)

	print("Number of bases in this file",seq_len)
	return(seq_dat)
		































