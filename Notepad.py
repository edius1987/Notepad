#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 15:59:53 2023

@author: Edius Ferreira
email: ediusferreira@gmail.com
Github: edius1987

MIT License

Copyright (c) 2023 Edius Ferreira


"""

import tkinter
import os
import webbrowser
import enchant
import html
import reportlab
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter import font
from tkinter import colorchooser 


class Notepad:

	__root = Tk()
	# largura e altura padrão da janela
	__thisWidth = 500
	__thisHeight = 500
	__thisTextArea = Text(__root)
	__thisMenuBar = Menu(__root)
	__thisFileMenu = Menu(__thisMenuBar, tearoff=0)
	__thisEditMenu = Menu(__thisMenuBar, tearoff=0)
	__thisHelpMenu = Menu(__thisMenuBar, tearoff=0)
	# largura e altura padrão da janela
	__thisScrollBar = Scrollbar(__thisTextArea)
	__file = None

	def __init__(self,**kwargs):
		# largura e altura padrão da janela
		try:
			self.__root.wm_iconbitmap("Notepad.ico")
		except:
			pass
		# largura e altura padrão da janela
		try:
			self.__thisWidth = kwargs['width']
		except KeyError:
			pass
		try:
			self.__thisHeight = kwargs['height']
		except KeyError:
			pass

		# Defina o texto da janela
		self.__root.title("Indefinido - Bloco de notas")
		# Centraliza a janela
		screenWidth = self.__root.winfo_screenwidth()
		screenHeight = self.__root.winfo_screenheight()
		# Para esquerda
		left = (screenWidth / 2) - (self.__thisWidth / 2)
		# Para alinhamento à direita
		top = (screenHeight / 2) - (self.__thisHeight /2)
		# Para superior e inferior

		self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth,
						      self.__thisHeight,
						      left, top))
		# Para tornar a área de texto redimensionável automaticamente
		self.__root.grid_rowconfigure(0, weight=3)
		self.__root.grid_columnconfigure(0, weight=3)

		# Adicionar controles (widget)
		self.__thisTextArea.grid(sticky = N + E + S + W)
		# Para abrir um novo arquivo
		self.__thisFileMenu.add_command(label="Novo",
						command=self.__newFile)
		# Para abrir um arquivo já existente
		self.__thisFileMenu.add_command(label="Abrir",
						command=self.__openFile)
		# Para salvar o arquivo atual
		self.__thisFileMenu.add_command(label="Salvar",
						command=self.__saveFile)
		# Para salvar o arquivo atual
		self.__thisFileMenu.add_separator()
		self.__thisFileMenu.add_command(label="Sair",
						command=self.__quitApplication)
		self.__thisMenuBar.add_cascade(label="Arquivo",
					       menu=self.__thisFileMenu)
		# Para dar um recurso de corte
		self.__thisEditMenu.add_command(label="Recortar",
						command=self.__cut)
		# para dar um recurso de cópia
		self.__thisEditMenu.add_command(label="Copiar",
						command=self.__copy)
		# para dar um recurso de colar
		self.__thisEditMenu.add_command(label="Colar",
						command=self.__paste)
        # para dar um recurso de desfazer
		self.__thisEditMenu.add_command(label="Desfazer",
						command=self.__undo)
        #para dar um recurso de refazer
		self.__thisEditMenu.add_command(label="Refazer",
						command=self.__redo)
        # Para dar um recurso de edição
		self.__thisMenuBar.add_cascade(label="Editar",
					       menu=self.__thisEditMenu)
		# Para criar um recurso de descrição do bloco de notas
		self.__thisHelpMenu.add_command(label="Ajuda",
						command=self.__showAbout)
		self.__thisMenuBar.add_cascade(label="Ajuda",
					       menu=self.__thisHelpMenu)
		self.__root.config(menu=self.__thisMenuBar)
		self.__thisScrollBar.pack(side=RIGHT,fill=Y)
		# A barra de rolagem se ajustará automaticamente de acordo com o conteúdo
		self.__thisScrollBar.config(command=self.__thisTextArea.yview)
		self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)
	def __quitApplication(self):
		self.__root.destroy()
		# saída()
	def __showAbout(self):
		showinfo("Bloco de Notas",view =webbrowser.open("https://www.google.com/search?q=bloco+de+notas"))
	def __openFile(self):
		self.__file = askopenfilename(defaultextension=".txt",
					      filetypes=[("Todos Arquivos","*.*"),
							 ("Documentos de texto","*.txt")])
		if self.__file == "":
			# nenhum arquivo para abrir
			self.__file = None
		else:
			# Tente abrir o arquivo
			# define o título da janela
			self.__root.title(os.path.basename(self.__file) + " - Bloco de notas")
			self.__thisTextArea.delete(1.0,END)
			file = open(self.__file,"r")
			self.__thisTextArea.insert(1.0,file.read())
			file.close()

	def __newFile(self):
		self.__root.title("Indefinido - Bloco de notas")
		self.__file = None
		self.__thisTextArea.delete(1.0,END)

	def __saveFile(self):

		if self.__file == None:
			# Salve como novo arquivo
			self.__file = asksaveasfilename(initialfile='indefinido.txt',
							defaultextension=".txt",
							filetypes=[("Todos os arquivos","*.*"),
								   ("Documentos de texto","*.txt")])

			if self.__file == "":
				self.__file = None
			else:
				# Tente salvar o arquivo
				file = open(self.__file,"Sem titulo")
				file.write(self.__thisTextArea.get(1.0,END))
				file.close()

				# Altere o título da janela
				self.__root.title(os.path.basename(self.__file) + " - Bloco de notas")

		else:
			file = open(self.__file,"w")
			file.write(self.__thisTextArea.get(1.0,END))
			file.close()

	def __cut(self):
		self.__thisTextArea.event_generate("<<Cortar>>")

	def __copy(self):
		self.__thisTextArea.event_generate("<<Copiar>>")

	def __paste(self):
		self.__thisTextArea.event_generate("<<Colar>>")
    
	def __undo(self):
		self.__thisTextArea.event_generate("<<Desfazer>>")
        
	def __redo(self):
		self.__thisTextArea.event_generate("<<Refazer>>")
        
	def run(self):
		# Execute o aplicativo principal
		self.__root.mainloop()

# Execute o aplicativo principal
notepad = Notepad(width=700,height=500)
notepad.run()
