import os, sys
from collections import defaultdict
import itertools

genome_reps = defaultdict(list)
unique_reps = defaultdict(list)

input = open(sys.argv[1])
tally = 0
all3 = 0
for i in input.readlines():
	line = i.rstrip()
	tabs = line.split("\t")

	if line.startswith("#"):
		genome_names = tabs[3:len(tabs)]

	else:
		tally +=1
		if tabs[0] == "3":
			all3 +=1

		cluster_name = "cluster_"+str(tally)	
		occurrence = tabs[3:len(tabs)]

		for index, j in enumerate(occurrence):
			if j == "*":
				pass
			else:
				genome_reps[genome_names[index]].append(cluster_name)
				if int(tabs[0]) == int(1):
					unique_reps[genome_names[index]].append(cluster_name)
				
keys = genome_reps.keys()
combinations = list(itertools.combinations(keys, 2))

for i in unique_reps:
	print("Orthologs unique to", i, " = ", len(unique_reps[i]))

print("\n")

for i in combinations:
	set1 = set(genome_reps[i[0]])
	set2 = set(genome_reps[i[1]])
	print("Shared clusters between "+ i[0] +" and "+ i[1] +" = "+ str(len(set1.intersection(set2))))

print("\nShared between all genomes = " +str(all3))


