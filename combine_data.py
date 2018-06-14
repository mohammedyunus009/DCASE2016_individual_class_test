import os
import sys
import config as cfg
import csv

#combines all the data into 1 fold
def combine_data(rd_path,wr_path):		
	data1 = []
	data = []
	for l in rd_path:
			
		with open(l,'r') as r:
			reader = csv.reader(r)
			lis=list(reader)
			for l in lis:
				data.append(l)
			
			lis=[]
	print len(data)
	for i in range(len(data)):
		if not data[i] in data[:i]:
			data1.append(data[i])
	print len(data1)
				#sys.exit()
	with open(wr_path[0],'w') as l:
		for li in data1:
						#[na, lb] = li[0].split('\t')
			wr = csv.writer(l)
			wr.writerow(li)
if sys.argv[1]=='--combine':
	if sys.argv[2]=='-all':
		combine_data(cfg.bdev_tr_csv,cfg.dev_tr_csv)
		print "done"
		combine_data(cfg.bdev_te_csv,cfg.dev_te_csv)
		print "done"
		#combine_meta(cfg.bdev_meta_csv,cfg.dev_meta_csv)
		print "done"
		#combine_meta(cfg.beva_meta_csv,cfg.eva_meta_csv)
		print "done"

if sys.argv[1]=='--prepare':
	if sys.argv[2]=='1':
		sys.exit()