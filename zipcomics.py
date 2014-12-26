#!/usr/bin/env python
from  __future__  import with_statement
from contextlib import closing 
import os
import  imghdr
from zipfile import ZipFile , ZIP_DEFLATED

#pegando o caminho
input_var = os.path.dirname(os.path.abspath(__file__))
#ando pelas pastas
for root, dirs, files in os.walk(input_var):
	filename = os.path.split(root)[1]+r".cbz"
	
	has_imgs = False
	for name in files:
		page  =  os.path.join(root,name)
		if (imghdr.what(page)) == "jpeg":
			has_imgs = True

	if  has_imgs:
		with  closing ( ZipFile(filename, "w",  ZIP_DEFLATED) )as zipcomic:	
			for name in files:
				page  =  os.path.join(root,name)
			 	if (imghdr.what(page)) == "jpeg":
			 		zfn = page[len(input_var)+len(os.sep):]
			 		zipcomic.write(page,zfn)