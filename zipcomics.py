#!/usr/bin/env python
from  __future__  import with_statement
from contextlib import closing 
from zipfile import ZipFile , ZIP_DEFLATED
import  imghdr
import os

#caminho de onde o script esta rodando
input_var = os.path.dirname(os.path.abspath(__file__))

#caminhar pelas pastas
for root, dirs, files in os.walk(input_var):

	#nome da pasta onde estao as imagens
	folder_name = os.path.split(root)[1]+r".cbz"
	
	#teste para evitar zips vazios
	has_imgs = False
	for name in files:
		page  =  os.path.join(root,name)
		if (imghdr.what(page)) == "jpeg":
			has_imgs = True
	if  has_imgs:
		print "criando : " + folder_name
		#criando o zip so com imagens
		with  closing ( ZipFile(folder_name, "w",  ZIP_DEFLATED) ) as zipcomic:	
			for name in files:
				page  =  os.path.join(root,name)
			 	if (imghdr.what(page)) == "jpeg":

			 		#cordando o path do arquivo
			 		arc_name = page[len(input_var) + len(os.sep):]
			 		zipcomic.write(page,arc_name)
			 	else:
			 		print "ignorado : " + name + " -  inconpativel com img"
