def read_line(pattern,name_of_file):
	with open(name_of_file,"r") as fd:
	        for l in fd:
	        	if pattern in l:
	        	    	line.append(l)
	return line


def write_on_file(line,name_of_file):
    if len(patterns)>1:
		with open(name_of_file,'w+') as fd:
	    		for l in line:
			    	fd.write(l)
    else:
        with open(name_of_file,'w+') as fd:
    	    for l in line:
                fd.write(l)

import os
import sys
import config as cfg

line=[]

backupfile_path=[]
name_of_w_file=[]

#for development
for l in cfg.bdev_te_csv:
	backupfile_path.append(l)
for l in cfg.bdev_tr_csv:
	backupfile_path.append(l)
print "done"


patterns = []
patterns = sys.argv[2].split(',')
print patterns,"patterns"
if 'all' in sys.argv[2]:
    patterns = cfg.labels

print patterns,"patterns"

line=[]
if sys.argv[1]=='--meta_dev':
	for pattern in patterns:
		line=read_line(pattern,cfg.bdev_meta_csv)
	write_on_file(line,cfg.dev_meta_csv)
	print "done"
	sys.exit()




if sys.argv[1]=='--normalfiles':
	
	for pattern in patterns:
		for path in backupfile_path:
			line=read_line(pattern,path)
			path=path[0:-11]+path[-4:]
	write_on_file(line,path)
	print "done"
	sys.exit()

if sys.argv[1]=='--meta_eva':
	for pattern in patterns:
		line=read_line(pattern,cfg.beva_meta_csv)
		#print "done"
	write_on_file(line,cfg.eva_meta_csv)
	print "done"
	sys.exit()



"""
#dumps line 
if sys.argv[2]=='meta_insertion':
	pickel_out = open("pic.pickle",'wb+')
	pickle.dump(line,pickel_out)
	pickel_out.close()

#writes on meta
elif sys.argv[2]=='meta_extraction':
	pickel_out = open("pic.pickle",'rb')
	line=pickle.load(pickel_out)
	for l in line:
		if pattern in line:
"""
""" 
cwd = os.getcwd()
preee"""
