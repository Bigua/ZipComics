#!/usr/bin/env python
 # -*- coding: utf-8 -*-
from  __future__  import with_statement
import os

def help():
	import textwrap
	print textwrap.dedent("""\
	zipcomics  - script para compactação de imagens em cbz
	Uso: python zipcomics /caminho/para/as/pastas/com/img
	""")

# metodo principal  que compacta as imagens
def  zip(base_dir):

	from contextlib import closing
	from zipfile import ZipFile , ZIP_DEFLATED
	import  imghdr

	#caminhar pelas pastas
	for root, dirs, files in os.walk(base_dir):

		#nome da pasta onde estão as imagens
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

						#cortando o path do arquivo
						arc_name = page[len(base_dir) + len(os.sep):]
						zipcomic.write(page,arc_name)
					else:
						print "ignorado : " + name + " -  incompatível com img"
	move(base_dir)


#metodo que move os arquivos para o diretório de origem das imagens
def move(base_dir):
	import shutil

	#raiz de onde o script está
	root = os.path.split(os.path.abspath(__file__))[0]
	files = [f for f in os.listdir( root) if os.path.isfile(f)]
	for f in files:
		extension = os.path.splitext(f)[1]
		if extension == ".cbz":
			shutil.move( root+os.sep+f,base_dir+os.sep+f)
			print "Salvo em " + base_dir+os.sep+f

#tudo começa aqui
if __name__ ==  '__main__' :
	import sys
	if len(sys.argv) < 2:
		help()
	else:
		zip( sys.argv[1])