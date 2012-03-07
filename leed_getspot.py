import os
import os.path
in_field = ["theta :","beam :  ","axis :  ","rsample : ","cam :    ","beamX : ","beamY : ","rSphere : ","lastEnergy :","rImage0 :","vAngle1 :","vAngle2 :","over1_r :","over1_a :","over2_r :","over2_a :"]
out_field = ["theta :","beam :  ","axis :  ","rsample : ","cam :    ","beamX : ","beamY : ","rSphere : ","sigma : "]

split(path)
pathname = "C:/pubOptimas/"
filename = "HTAN.dat"
prefix = "HTAN"
suffix = ".dat"

#	Input data
infix = arange(1:120)

for item in infix:
	f = open(pathname+prefix+str(infix).zfill(3)+suffix, 'r')
	list = f.read().split(" ")
	list = filter(None, list)
	print "\t".join(list)

#	Output data
print "Output data:"
filename = ["matout1.txt","matout2.txt","matout3.txt","matout4.txt","matout5.txt","matout6.txt","matout7.txt","matout8.txt","sigma.txt"]

list = []
for item in filename:
	f = open(pathname+item, 'r')
	list.append(f.read().strip())
list = filter(None, list)
	
print "\t".join(out_field)
print "\t".join(list)
