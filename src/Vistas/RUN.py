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
        '''
        Crea y empaqueta todos low widgets de la ventana
        '''
        self.padre.title("PRPEPROCESAMIENTO")
        '''
        frmHeader = ttk.Frame(self.padre, relief = tk.RAISED)
        frmHeader.pack(side = tk.TOP, fill = tk.X, expand = tk.TRUE)
        frmNorte = ttk.Frame(self.padre)
        frmNorteOeste  = ttk.Frame(frmNorte)        
        frmNorteOeste.grid(column = 0, row = 0)
        frmNorteEste = ttk.Frame(frmNorte)
        frmNorteEste.grid(column = 1, row = 0)
        frmNorte.grid_columnconfigure(0,weight = 1)
        frmNorte.grid_columnconfigure(1,weight = 1)
        frmNorte.pack(fill = tk.X, side=tk.TOP)
        ttk.Separator(self.padre, orient = tk.HORIZONTAL).pack()
        '''
        
        button_opt = {'fill': Tkconstants.BOTH, 'padx': 5, 'pady': 5}
        
        
        frmCenter = ttk.Frame(self.padre)
        frmCenterOeste = ttk.Labelframe(frmCenter, text = "PARAMETROS")
        frmCenterOeste.pack(fill = tk.BOTH, side = tk.LEFT, expand = tk.TRUE, padx = 5)
        frmCenterEste = ttk.Labelframe(frmCenter, text = "LISTA DE RUTAS")
        frmCenterEste.pack(fill = tk.BOTH, side = tk.LEFT, expand = tk.TRUE, padx = 5)
        frmCenter.pack(fill = tk.BOTH, side = tk.TOP, expand= tk.TRUE)
        
        ttk.Button(frmCenterOeste, text='Seleccione el directorio que desea agregar.', command=self.agregarDirectorioClase).pack(**button_opt)
        
        scrollbary = Scrollbar(frmCenterEste, orient=VERTICAL)
        scrollbarx = Scrollbar(frmCenterEste, orient=HORIZONTAL)
        self.listaRutasGUI = tk.Listbox(frmCenterEste,selectmode=EXTENDED,yscrollcommand=scrollbary.set)
        scrollbary.config(command=self.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        self.listaRutasGUI.pack(side=LEFT, fill=BOTH, expand=1)
        
        
    
    def agregarDirectorioClase(self):
        self.optDialogoDir = opciones = {}
        opciones['initialdir'] = '/home/ivan/Escritorio/'
        opciones['parent'] = self
        opciones['title'] = 'Escoge un directorio con imagenes'
        directorio = tkFileDialog.askdirectory(**self.optDialogoDir)
        self.listaDirectorios.append(directorio)
        self.insertarEnListaGUI(directorio)
    
    
    def insertarEnListaGUI(self, elemento):
        self.listaRutasGUI.insert(END, elemento)
    
    
    def yview(self, *args):
        apply(self.listaRutasGUI.yview, args)
    
    
########################################################################        
if __name__ == '__main__':
    root = tk.Tk()
    app = Principal(master=root)
    app.mainloop()