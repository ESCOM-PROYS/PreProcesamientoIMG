# -*- coding: utf8 -*-
'''
Created on 10/11/2015

@author: Isaac
'''


import ttk              
import Tkinter as tk
from Tkinter import *    
import Tkconstants, tkFileDialog


########################################################################
class Principal(tk.Frame):
    '''
    Frame que muestra la ventana principal de la aplicacion
    '''
    #-------------------------------------------------------------------------------
    def __init__(self, master=None,  *args, **kw):
        tk.Frame.__init__(self, master, *args, **kw)
        self.padre = master
        self.padre.geometry('700x600+10+10')
        self.listaDirectorios = []
        self.initUI()

    #-------------------------------------------------------------------------------
    def initUI(self):
        self.padre.title("PRPEPROCESAMIENTO")

        button_opt = {'fill': Tkconstants.BOTH, 'padx': 5, 'pady': 5}
        
        frmCenter = ttk.Frame(self.padre)
        frmCenterOeste = ttk.Labelframe(frmCenter, text = "PARAMETROS")
        frmCenterOeste.pack(fill = tk.BOTH, side = tk.LEFT, expand = tk.TRUE, padx = 5)
        frmCenterEste = ttk.Labelframe(frmCenter, text = "LISTA DE RUTAS")
        frmCenterEste.pack(fill = tk.BOTH, side = tk.LEFT, expand = tk.TRUE, padx = 5)
        frmCenter.pack(fill = tk.BOTH, side = tk.TOP, expand= tk.TRUE)
        
        ttk.Button(frmCenterOeste, text='Agregar Nuevo Directorio de Clases', command=self.agregarDirectorioClase).pack(**button_opt)
        ttk.Button(frmCenterOeste, text='Agregar Nuevo Archivo de Clases', command=self.agregarArchivoClase).pack(**button_opt)
        
        scrollbary = Scrollbar(frmCenterEste, orient=VERTICAL)
        scrollbarx = Scrollbar(frmCenterEste, orient=HORIZONTAL)
        self.listaRutasGUI = tk.Listbox(frmCenterEste,selectmode=EXTENDED,yscrollcommand=scrollbary.set,xscrollcommand=scrollbarx.set)
        scrollbary.config(command=self.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=self.xview)
        scrollbarx.pack(fill=X)
        self.listaRutasGUI.pack(side=LEFT, fill=BOTH, expand=1)
        
        
    
    def agregarDirectorioClase(self):
        self.optDialogoDir = opciones = {}
        opciones['initialdir'] = '/home/ivan/Escritorio/'
        opciones['parent'] = self
        opciones['title'] = 'Elija un directorio de Clase'
        directorio = tkFileDialog.askdirectory(**self.optDialogoDir)
        if(directorio not in self.listaDirectorios and directorio != ''):
            self.listaDirectorios.append(directorio)
            self.cargarDirectorio(directorio)
    
    
    def agregarArchivoClase(self):
        self.optDialogoDir = opciones = {}
        opciones['parent'] = self
        opciones['title'] = 'Elija un archivo de rutas'
        archivo = tkFileDialog.askopenfile(**self.optDialogoDir)
        if(archivo != ''):
            print archivo.name
            self.cargarRutasDesdeArchivo(archivo)
            
                
    def cargarDirectorio(self, elemento):
        if(elemento not in self.listaDirectorios):
            self.listaDirectorios.append(elemento)
            self.listaRutasGUI.insert(END, elemento)
    

    def cargarRutasDesdeArchivo(self, archivo):
        with open(archivo) as archivoClases:
            lines = archivoClases.readlines()
        
    
    def yview(self, *args):
        apply(self.listaRutasGUI.yview, args)
    
    def xview(self, *args):
        apply(self.listaRutasGUI.xview, args)
    
    
########################################################################        
if __name__ == '__main__':
    root = tk.Tk()
    app = Principal(master=root)
    app.mainloop()