
import ttk              #ttk Contiene widgets con fácil modificacion en su estilo.
                        #por lo cual prefiero utilizar estos. 
import Tkinter as tk    #Tkinter(tk) Contiene los mismos widgets que ttk y unos cuantos mas
                        #, y difieren un poco wn funcionalidad
#Se pueden realizar una interfaz con combinaciones de widgets porvenientes de diferentes
#bibliotecas de ttk o de Tkinter(tk) 

########################################################################
class Principal(tk.Frame):
    '''
    Frame que muestra la ventana principal de la aplicacion
    '''
    #-------------------------------------------------------------------------------
    def __init__(self, master=None,  *args, **kw):
        '''
        Constructor de la vista e inicializacion de las propiedades de la ventana
        '''
        tk.Frame.__init__(self, master, *args, **kw)
        self.padre = master
        self.padre.geometry('1000x500+10+10')# Geometria de la ventana(Ancho X Alto + PosicionDeLaVentanaEnLaPantallaX + PosicionDeLaVentanaEnLaPantallaY)
        
        self.initUI()

    #-------------------------------------------------------------------------------
    def initUI(self):
        '''
        Crea y empaqueta todos low widgets de la ventana
        '''
        self.padre.title("Adquicicion de imagenes")
        
        '''
        Una ventana puede tener dos formas de posisicionar los elementos dentro de ella.
        1.- Por medio de una regilla que creas con configuracion (GRID)
        2.- Secuencialmente vertical u horizontal, no puede ser secuencialmente vertical y horizaontal (PACK)
        Este modo se establece cuando empaquetas el primer widget en la ventana
        Si empaquetas el primer widget con pack entonces el modo es Secuencial, 
            si lo empaquetas con grid entonces el modo es por medio de un grid
            
        Los atributos mas importantes de pack son:
            * fill : el modo en que el widget ocupara el espacio asignado dentro de la ventana
                + fill = x : El widget no tiene restricciones para ocupar el lugar en todo el eje X
                + fill = y : El widget no tiene restricciones para ocupar el lugar en todo ej eje y
                + fill = both : El widget no tiene restricciones para ocupar todo el lugar
            * expand : Especifica si el widget debe de utilizar todo el espacio asignado sin restriccioens
                + expand = true : Debe de ocupar todo el espacio
                + expand = false: Puede no ocupar todo el espacio
            * side : Especifica como se acomodaran los widgets Horizontalmente o Verticalmente
                + side = rigth, side = left : Se posicionaran Horizontalmente
                + side = top, side = bothom : Se posicionaran Verticalemnte
                +(Nota) una vez que se agrega el primer widget a la ventana se establece el modo 
                    en que se acomodaran los demás widgets, no es necesario declararle la propiedad
                    a los demás widgets
            *ipadx : relleno interior en la ventana en el eje de las x
            *ipady : relleno interior en la ventana en el eje de las y
            *padx y pady : Son lo mismo que los anterior, 
                    con excepcion que el relleno se realiza fuera de la ventana
            *anchor : Alineacion del componente
            Se puede modificar la configuracion de como se agregan los widgets en la tabal,
                esta modificacion se realiza en la ventana que contendra los widgets 
                
            Los atributos importantes de grid son:
                *(NOTA)Las filas y las columnas se crean automaticamene, dependiendo el numero maximo que 
                hayas puesto en el valor de la propiedad de column, y de igual forma para las filas.
                *column : Numero de la columna en la uqe se pondra el widget
                *row: Numero de la fila en la uqe se pondra el widget
                *stiky : Forma en que el widget ocupara el espacio de la celda que se le fue asignada
            Se puede modificar la configuracion de como se crea la regilla en la ventana,
                esta modificacion se realiza en la ventana que contendra los widgets
            
            para mas informacion 
            
            http://effbot.org/tkinterbook/grid.htm
            http://effbot.org/tkinterbook/pack.htm
            
            Para ver todas las propiedades de los widgets
            
            http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html
        
        '''
        #*****************************************************************************************
        frmHeader = ttk.Frame(self.padre, relief = tk.RAISED)
        
        frmHeader.pack(side = tk.TOP, fill = tk.X, expand = tk.TRUE)
        #*****************************************************************************************
        
        #*****************************************************************************************
        frmNorte = ttk.Frame(self.padre)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        frmNorteOeste  = ttk.Frame(frmNorte)        
        
        frmNorteOeste.grid(column = 0, row = 0)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        frmNorteEste = ttk.Frame(frmNorte)
         
        
        frmNorteEste.grid(column = 1, row = 0)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        frmNorte.grid_columnconfigure(0,weight = 1)
        frmNorte.grid_columnconfigure(1,weight = 1)
        
        frmNorte.pack(fill = tk.X, side=tk.TOP)
        #*****************************************************************************************       
        
        ttk.Separator(self.padre, orient = tk.HORIZONTAL).pack()
        
        #*****************************************************************************************
        frmCenter = ttk.Frame(self.padre)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~        
        frmCenterOeste = ttk.Labelframe(frmCenter, text = "Acciones sobre la tabla")
        
        frmCenterOeste.pack(fill = tk.BOTH, side = tk.LEFT, expand = tk.TRUE, padx = 5)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        frmCenterEste = ttk.Labelframe(frmCenter, text = "Imagenes de la clase")
        
        frmCenterEste.pack(fill = tk.BOTH, side = tk.LEFT, expand = tk.TRUE, padx = 5)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        frmCenter.pack(fill = tk.BOTH, side = tk.TOP, expand= tk.TRUE)
        #*****************************************************************************************
        
    #-------------------------------------------------------------------------------        
        
    

########################################################################        
if __name__ == '__main__':
    root = tk.Tk()
    app = Principal(master=root)
    app.mainloop()
