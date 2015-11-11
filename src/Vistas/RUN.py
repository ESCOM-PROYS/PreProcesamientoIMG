# -*- coding: utf8 -*-
'''
Created on 10/11/2015

@author: Isaac
'''


import ttk              
import Tkinter as tk
from Tkinter import *    
import Tkconstants, tkFileDialog
import os
import ImageFilter

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
        #--------------------------------------------
        self.listaDirectorios = []
        self.listaDeClases = []
        self.FILTROS = [ImageFilter.BLUR,ImageFilter.CONTOUR,ImageFilter.DETAIL,ImageFilter.EDGE_ENHANCE,ImageFilter.EDGE_ENHANCE_MORE,ImageFilter.EMBOSS,ImageFilter.FIND_EDGES,ImageFilter.SMOOTH,ImageFilter.SMOOTH_MORE,ImageFilter.SHARPEN]
        self.initUI()

    #-------------------------------------------------------------------------------
    def initUI(self):
        self.padre.title("PRPEPROCESAMIENTO")
        #Frames ---------------------------------------------------------
        frmGRAL   = ttk.Frame(self.padre)
        frmEstado = ttk.Frame(frmGRAL)
        frmPARAM  = ttk.Labelframe(frmGRAL, text = "PARAMETROS")
        frmRUTAS  = ttk.Labelframe(frmEstado, text = "LISTA DE RUTAS")
        frmCLASES = ttk.Labelframe(frmEstado, text = "LISTA DE CLASES")
        frmFILTROS = ttk.Labelframe(frmPARAM, text = "Filtros")
        frmESCCOL = ttk.Labelframe(frmPARAM, text = "Escala y modo de color")
        
        frmGRAL.pack  (fill = tk.BOTH, side = tk.TOP, expand= tk.TRUE)
        frmEstado.pack(fill = tk.BOTH, side = tk.RIGHT, expand = tk.TRUE, padx = 5)
        frmPARAM.pack (fill = tk.BOTH, side = tk.LEFT, expand = tk.TRUE, padx = 5)
        frmRUTAS.pack (fill = tk.BOTH, side = tk.TOP, expand = tk.TRUE, padx = 5)
        frmCLASES.pack(fill = tk.BOTH, side = tk.BOTTOM, expand= tk.TRUE,padx = 5)
        frmESCCOL.pack(fill  = tk.BOTH, side = tk.BOTTOM, expand= tk.TRUE,padx = 5)
        frmFILTROS.pack(fill = tk.BOTH, side = tk.BOTTOM, expand= tk.TRUE,padx = 5)
        
        # BUTTONS -------------------------------------------------------     
        button_opt = {'fill': Tkconstants.BOTH, 'padx': 5, 'pady': 5}  
        ttk.Button(frmPARAM,  text='Agregar Nuevo Directorio de Clases', command=self.agregarDirectorioClase).pack(**button_opt)
        ttk.Button(frmPARAM,  text='Agregar Nuevo Archivo de Clases', command=self.agregarArchivoClase).pack(**button_opt)
        ttk.Button(frmEstado, text='INICIAR PROCESAMIENTO',command=self.agregarArchivoClase).pack(**button_opt)
        
        scrollbarx,scrollbary = self.getScrollBars(frmRUTAS) 
        self.listaRutasGUI    = tk.Listbox(frmRUTAS,selectmode=EXTENDED,yscrollcommand=scrollbary.set,xscrollcommand=scrollbarx.set)
        self.confScrollbars(scrollbarx, scrollbary,0)
        self.packScrollBars(scrollbarx,scrollbary)
        self.listaRutasGUI.pack(side=LEFT, fill=BOTH, expand=1)
        
        scrollbarxC,scrollbaryC = self.getScrollBars(frmCLASES) 
        self.listaClasesGUI    = tk.Listbox(frmCLASES,selectmode=EXTENDED,yscrollcommand=scrollbaryC.set,xscrollcommand=scrollbarxC.set)
        self.confScrollbars(scrollbarxC, scrollbaryC,1)
        self.packScrollBars(scrollbarxC,scrollbaryC)
        self.listaClasesGUI.pack(side=LEFT, fill=BOTH, expand=1)
        
        self.listaFiltrosGUI = tk.Listbox(frmFILTROS,selectmode=EXTENDED,yscrollcommand=scrollbaryC.set,xscrollcommand=scrollbarxC.set)
        self.listaFiltrosGUI.pack(side=LEFT, fill=BOTH, expand=1)
        self.llenarListaFiltros(self.listaFiltrosGUI)
        
    #-------------------------------------------------------------------------------------------------------------------
    
    def agregarDirectorioClase(self):
        self.optDialogoDir = opciones = {}
        opciones['parent'] = self
        opciones['title'] = 'Elija un directorio de Clase'
        directorio = tkFileDialog.askdirectory(**self.optDialogoDir)
        self.cargarInfoDirectorio(directorio)
    
    
    def agregarArchivoClase(self):
        self.optDialogoDir = opciones = {}
        opciones['parent'] = self
        opciones['title'] = 'Elija un Archivo de Rutas'
        archivo = tkFileDialog.askopenfile(**self.optDialogoDir)
        if(archivo != None and archivo != ''):
            print archivo.name
            self.cargarRutasDesdeArchivo(archivo.name)


    def cargarInfoDirectorio(self, elemento):
        if(elemento not in self.listaDirectorios and elemento != ''):
            self.listaDirectorios.append(elemento)
            self.listaRutasGUI.insert(END, elemento)
            clase = self.getClaseDesdeRuta(elemento)
            if(clase): #La clase siempre se inserta en la lista de clases, pero en la lista de la GUI sólo se muestra una vez
                self.listaClasesGUI.insert(END,clase)
    
    
    def cargarRutasDesdeArchivo(self, archivo):
        with open(archivo) as archivoClases:
            rutas = archivoClases.readlines()
            for ruta in rutas:
                if(ruta!='' and ruta!='\n'):
                    self.cargarInfoDirectorio(ruta)
        archivoClases.close()       
    
    
    def getClaseDesdeRuta(self,ruta):
        mostrarEnLista = None
        separador = os.path.sep
        clase = ruta.split(separador)[-1]
        clase = clase.lower()
        if(clase not in self.listaDeClases): #para saber si se mostrará en la lista de la GUI
            mostrarEnLista = clase
        self.listaDeClases.append(clase) # La clase Simepre se agrega a la lista @self.listaDeClases
        return mostrarEnLista
    
    def llenarListaFiltros(self,listaGUI):
        for filtro in self.FILTROS:
            self.listaFiltrosGUI.insert(END,filtro.name)
            
    
    
    def getScrollBars(self,frameToStroll):
        scrollbary = Scrollbar(frameToStroll, orient=VERTICAL)
        scrollbarx = Scrollbar(frameToStroll, orient=HORIZONTAL)
        return scrollbarx,scrollbary
    
    def confScrollbars(self,sbx,sby,listaActiva):
        if(listaActiva == 0):
            sbx.config(command=self.xview)
            sby.config(command=self.yview)
        else:    
            sbx.config(command=self.xview2)
            sby.config(command=self.yview2)


    def packScrollBars(self,sbx,sby):
        sbx.pack(fill=X)
        sby.pack(side=RIGHT, fill=Y)
     
    def yview(self,*args):
        apply(self.listaRutasGUI.yview, args)
  
    def yview2(self,*args):
        apply(self.listaClasesGUI.yview, args)

    def xview(self,*args):
        apply(self.listaRutasGUI.xview, args)
        
    def xview2(self,*args):
        apply(self.listaClasesGUI.xview, args)
    
    
########################################################################        
if __name__ == '__main__':
    root = tk.Tk()
    app = Principal(master=root)
    app.mainloop()