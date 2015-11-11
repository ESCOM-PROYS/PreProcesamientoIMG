'''
Created on 18/09/2015

@author: ivan
'''

import os
import tkFileDialog
import tkMessageBox
import ttk

import Tkinter as tk
from os.path import expanduser


#########################################################################################
class VistaGuardarDirectorioImgs(tk.Toplevel):
    '''
    Ventana en la que se ofrece la posibilidad de crear una clase
    '''
    
    def __init__(self, master = None):
        '''
        Constructor
        '''
        tk.Toplevel.__init__(self, master)
        self.padre = master
        self.title("Guarda Nombre Del Directorio Principal")
        self.initUI()
        self.hide()
        
    #----------------------------------------------------------------------
    
    def initUI(self):
        '''
        Crea y empaqueta los windgets de la ventana, tambien se establecen las propiedades
        de la ventana 
        '''
        
        #Opciones para el dialogo de imagenes para abrir un directorio con imagenes de tkinter
        self.pathDirPrin = ''
        self.optDialogoDir = opciones = {}
        opciones['initialdir'] = expanduser("~")
        opciones['parent'] = self
        opciones['title'] = 'Direccion del Directorio Principal'
        
        self.geometry('450x250+300+100')
        self.protocol("WM_DELETE_WINDOW", "onexit")
        self.resizable(0,0)
        
        frmFondo = ttk.Frame(self, relief = "groove")
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        frmNorte = ttk.Labelframe(frmFondo, text = "Elige el nombre del Directorio Principal")
        
        ttk.Label(frmNorte, 
                  text = 'Nombre del directorio Principal: ').pack(side = tk.LEFT,
                                                                   padx = 5,
                                                                   pady=10)
                  
        self.strVarNomDirPrincipal = tk.StringVar()
        ttk.Entry(frmNorte, textvariable = self.strVarNomDirPrincipal).pack(fill = tk.X,
                                                                      expand = tk.TRUE,
                                                                      side = tk.LEFT,
                                                                      padx = 5,
                                                                      pady=10)
        frmNorte.pack(expand=tk.TRUE, side=tk.TOP, fill=tk.X,pady=10)
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        frmCentro = ttk.Labelframe(frmFondo, text="Direccion del Directorio Principal")
        
        self.strVarPathDirPrin = tk.StringVar()
        ttk.Entry(frmCentro, textvariable = self.strVarPathDirPrin).pack(fill= tk.X,
                                                                         expand = tk.TRUE,
                                                                         padx=10,
                                                                         pady=10,
                                                                         side = tk.LEFT)
        
        ttk.Button(frmCentro, text="Buscar", command=self.buscarPathDirPrin).pack(side = tk.LEFT, padx=10,pady=10)
        
        frmCentro.pack(expand = tk.TRUE, side = tk.TOP, fill = tk.X, pady=10)
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        frmSur = ttk.Frame(frmFondo)
                   
        ttk.Button(frmSur, 
                   text = 'Cancelar', 
                   command = self.hide).pack(padx = 5, side = tk.RIGHT)
        
        ttk.Button(frmSur, 
                   text = 'Crear Directorio Principal',
                   command = self.crearDirPrincipal).pack(padx = 5, side = tk.RIGHT)
                   
        frmSur.pack(side = tk.TOP, expand = tk.TRUE, fill = tk.X)
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        frmFondo.pack(fill = tk.BOTH, expand = tk.TRUE)
        
    #----------------------------------------------------------------------
    def buscarPathDirPrin(self):
        self.strVarPathDirPrin.set(tkFileDialog.askdirectory(**self.optDialogoDir))
    
    #----------------------------------------------------------------------
    def crearDirPrincipal(self):
        self.strVarNomDirPrincipal.set(self.strVarNomDirPrincipal.get().strip())
        self.strVarPathDirPrin.set(self.strVarPathDirPrin.get().strip())
        
        if " " in self.strVarNomDirPrincipal.get():
            tkMessageBox.showerror("Nombre Directorio Principal Erroneo",
                                    "El Nombre del Directorio Principal no puede contener Espacios")
            return
        
        self.pathDirPrin = self.strVarPathDirPrin.get()+os.path.sep+self.strVarNomDirPrincipal.get()
        if os.path.exists(self.pathDirPrin):
            respuesta = tkMessageBox.askyesno("Directorio Existente",
                                  'El directorio '+self.pathDirPrin+' existe. \n Desea limpiar el directorio y crear el directorio de imagenes?')
            if not respuesta:
                return 
            
        self.hide()
        tkMessageBox.showinfo("Directorio Creado", "El directorio "+self.strVarNomDirPrincipal.get()+" fue creado")
        
    
    def getDirYRuta(self):
        return self.pathDirPrin 
      
    #----------------------------------------------------------------------
    def hide(self):
        """
        Ocula la ventana 
        """
        self.withdraw()
        
    #----------------------------------------------------------------------
    def show(self):
        """
        Mustra la ventana
        """
        self.update()
        self.deiconify()
        
#########################################################################################
        
if __name__ == "__main__":
    
    class SampleApp(tk.Tk):
        
        def __init__(self,*args, **kwargs):
            root = tk.Tk.__init__(self, *args, **kwargs)

            self.frmTabla = VistaGuardarDirectorioImgs(root)
            
        
    app = SampleApp()
    app.mainloop()
        
        
    
        
