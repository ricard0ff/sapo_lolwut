#!/usr/bin/python2.7 

import os, re, sys
from pyblake2 import blake2b #pip install pyblake
imagesList = []
blake2List = []

#passing arguments a list containing images and the location of the folder
def criaHTMLPortavel(image,fold):
	l=open("test.html",'w')
	for x in image:
		datos = open(os.path.abspath(fold)+'/'+x, 'rb').read().encode('base64').replace('\n', '')
		img_tag = '<img src="data:image/png;base64,{0}">'.format(datos)
        	l.write(img_tag)
	l.close()

if (len(sys.argv) != 2):
	print "  python <folder name> "
	sys.exit()

folderName = sys.argv[1]
filesInDir = os.listdir(folderName)

Rjpg = re.compile('[.]jpg$', re.IGNORECASE)
jpgFilesInDir = [x for x in filesInDir if Rjpg.search(x)]

with open('hashlist','a+') as ff:
	for line in ff:
		blake2List.append(line)

#normalizing stuff                
blake2List=filter(lambda b: b != '\n',blake2List)
blake2List=list(set(blake2List))
blake2List=map(lambda s: s.strip(), blake2List)
	
for x in jpgFilesInDir:
	if blake2b(x).hexdigest()  not in blake2List:
		blake2List.append(blake2b(x).hexdigest())
		imagesList.append(x)


#clearing file contents since what we need is in mem @ this point...
open('hashlist', 'w').close()

for item in blake2List:
	with open ('hashlist','a+') as ff:
		ff.write(item+"\n")

criaHTMLPortavel(imagesList,folderName)
print "[I] done :)"

