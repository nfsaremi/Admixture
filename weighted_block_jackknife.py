### JAC July, 11 2012
###
### weighted_block_jackknife_0.1.py
###
### command line format
### python file.py d_stat_file block_size > output
###
### calculate the weighted block jackknife standard error of the D statistic.
### Input D statistic files generated by D_stat_0.6.py should be in the appropraite block size


### imports

import sys,os

### help!

if sys.argv[1] == "-h" or sys.argv[1] == "--help" or len(sys.argv) == 1:
	print "Insert help messege!"

### load files

file = open(sys.argv[1])
line = file.readline()
line = file.readline()
line = file.readline()


### vars

block_size = int(sys.argv[2])
auto_blocks = []
X_blocks = []


### defs

def D_calc(A,B):
	A=float(A)
	B=float(B)
	#print A,B
	D=(A-B)/(A+B)
	#print D
	return D

def knife(blocks):
	ABBA = 0
	BABA = 0
	size = 0
	count = 0
	jack_ABBA = 0
	jack_BABA = 0
	line_size = 0
	Dstat = 0.0
	pre_i = []
	p_i = []
	weight = []
	p_dot = 0
	while count < len(blocks):
		ABBA += int(blocks[count][3])
		BABA += int(blocks[count][4])
		size += ABBA + BABA
		count += 1
	count = 0
	#print blocks
	Dstat = D_calc(ABBA,BABA)
	
	while count < len(blocks):
		jack_ABBA = ABBA - int(blocks[count][3])
		jack_BABA = BABA - int(blocks[count][4])
		jack_count = ABBA + BABA
		weight.append(float(jack_count)/float(size))
		Djack = D_calc(jack_ABBA,jack_BABA)
		pre_i.append(Djack)
		count += 1
	count = 0
	#print p_i
	while count < len(pre_i):
		tally = 0
		sum = 0.0
	#	print sum
		while tally < len(pre_i):
			if tally != count:
				sum = sum + pre_i[tally]
			tally += 1
	#	print sum, "post"
		p_i.append(sum)
		p_dot += sum
		count += 1
	#print p_dot
	p_dot = p_dot/count
	#print p_dot
	count = 0
#	while count < len(p_i):
#		p_i[count] = p_dot-p_i[count]
#		count += 1
	#print "both", p_i, p_dot
	count = 0
	sigma = 0
	while count < len(p_i):
		sigma += weight[count]*((p_dot - p_i[count])**2)
		count += 1
	#print sigma
	sigma = sigma*(count+1)
	sigma = (float((len(p_i) - 1))/float(len(p_i))) * sigma
	sigma = sigma**.5
	return sigma
		
		
		
		
		
		
		#difference = difference * (line_size/size)
### body





# filter down to useable blocks
while line:
	split = line.split("\t")
	#print int(split[1])%block_size
	if int(split[1])%block_size == 0:
	#	print split[0]
		if split[0] == "scaffold20 " or split[0] == "scaffold100 " or split[0] == "scaffold105 " or split[0] == "scaffold113 " or split[0] == "scaffold115 " or split[0] == "scaffold122 " or split[0] == "scaffold134 " or split[0] == "scaffold141 " or split[0] == "scaffold167 " or split[0] == "scaffold170 " or split[0] == "scaffold179 " or split[0] == "scaffold184 ":
			X_blocks.append(split)
		else:
			auto_blocks.append(split)
	line = file.readline()
#sys.exit()
#print auto_blocks
#print X_blocks
all_blocks = auto_blocks + X_blocks
#print all_blocks
#print sys.argv[1]
out =  sys.argv[1] +"\t"+ str(knife(all_blocks))
#print "auto\t" + out
#out = str(knife(X_blocks))
#print "X\t" + out
#out = str(knife(all_blocks))
#print "all\t" + out
print out	

	
# sort the array
	

	
		
		