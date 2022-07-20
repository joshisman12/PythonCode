import glob
lst=glob.glob("..\\01.reorg\\ts_????_e_g.dat")
print(lst)

for o in lst:
	fin =open(o,"r")
	n,sta,e,o=o.split("_")
	lines=fin.readlines()
	fout=open(".\\sta_time\\{}_time.dat".format(sta),"a")
	for i,line in enumerate(lines):
		time,x,y=line.split()
		fout.write("{}  0\n".format(time))
	fout.close()
	fin.close()