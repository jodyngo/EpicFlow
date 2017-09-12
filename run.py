import os
import sys

if __name__ == "__main__":
	pimg1, pimg2 = sys.argv[1:3]
	print pimg1
	print pimg2
	path = os.path.abspath('.')
	print 'current dir:', path
	os.system('matlab -nodesktop -nojvm -r 					\
			\"addpath(\'%s\'); 									\
		 	addpath(genpath(\'%s\'));							\
		 	load(\'EpicFlow_v1.00/modelFinal.mat\');						\
		 	I = imread(\'%s\');									\
		 	if size(I,3)==1, I = cat(3,I,I,I); end; 		\
		 	edges = edgesDetect(I, model); 					\
		 	fid=fopen(\'%s\',\'wb\'); 							\
		 	fwrite(fid,transpose(edges),\'single\');		\
		 	fclose(fid); exit\" 							\
		 	'%(path + '/SED', path + '/pdollar-toolbox',
		 		pimg1, 'edgefile'))
	print 'edgefile created'
	os.system('deepmatching_1.2.2_c++/deepmatching-static \
				%s %s -png_settings -out %s'%(pimg1, pimg2, 'matchfile'))
	print 'matchfile created'
	os.system('EpicFlow_v1.00/epicflow %s %s %s %s %s'%(pimg1, pimg2, 'edgefile', 'matchfile', 'outfile'))
	print 'successfully created ./outfile'