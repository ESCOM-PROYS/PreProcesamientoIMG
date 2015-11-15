'''
Created on 27/11/2015

@author: isaac
'''
import os
import numpy
import Image
import ImageFilter
import traceback
from os.path import expanduser

class Procesador:
    
    def __init__(self, listaDirectorios , listaClases , 
                 listFiltros=None , modo=None , w=32 , h=32 , 
                 dirDestino = None , nombreCSV='CSV_TRAIN'):
        
        self.listaDirectorios = listaDirectorios
        self.listaClases = listaClases
        self.listaFiltros = listFiltros
        self.modo = modo
        self.width  = w 
        self.height = h
        self.homeDir = expanduser("~")
        self.dirDestino = dirDestino or (self.homeDir + '\\TRAIN\\')
        self.nombreCSV = nombreCSV
        self.CSV = None
        
      
    def RUN(self):
        print 'Comenzando Proceso...'
        self.crearDirectorio(self.dirDestino)
        self.crearCSV(self.nombreCSV)
        gruposIMG = self.getZIPListasDeRutas(self.listaDirectorios)
        self.mezclarDirectorios(gruposIMG, self.listaClases)
        self.cerrarCSV()
        print 'Fin de procesamiento'
        
    
    def crearDirectorio(self,ruta):
        print 'Verificando directorio destino: ' , ruta
        dir = os.path.dirname(ruta)
        if not os.path.exists(dir):
            os.makedirs(dir)
            print 'Directorio creado'
        else:
            print 'ALERTA: El directorio ya existe'
            
    
    def crearCSV(self, nombreCSV):
        try:
            self.CSV = open(self.dirDestino+nombreCSV , "w")
        except IOError as io:
            print 'No fue posible crear el archivo CSV: ', io.message
        
    def escribirCSV(self,etiqueta):
        try:
            self.CSV.write(etiqueta+'\n')
        except Exception as e:
            print 'Error al intentar escribir en CSV' , e.message
        
    
    def cerrarCSV(self):
        try:
            self.CSV.close()
        except Exception as e:
            print 'Error al intentar cerrar CSV', e.message
    
    
    #Genera una lista A que contiene listas Bi, donde Bi es una lista con todas las rutas de las imagenes que corresponden a una clase.
    #@return gruposIMG=[[img11,img12,img13,...,img1n],[img21,img22,img23,...,img2n],...[imgn1,imgn2,imgn3,...,imgnm]] 
    #@listaDirectorios Es una lista que contiene las rutas de los directorios que van a mezclarse
    def getZIPListasDeRutas(self,listaDirectorios):
        gruposIMG = []
        for directorio in listaDirectorios:
            listaIMG = []
            for img in os.listdir(directorio):
                if(img.endswith("png") or img.endswith("jpg") or img.endswith("JPG") or img.endswith("PNG") or img.endswith("JPEG") or img.endswith("jpeg") ):
                    listaIMG.append(directorio+os.path.sep+img)
            gruposIMG.append(listaIMG)
        return gruposIMG
          
          
    #Metodo principal para la generacion del directorio de imagenes de entrenamiento.
    # @rutasDirectorios Una lista con las rutas de los directorios de imagenes y 
    # @listaClases Una lista con los nombres de clase que les corresponden.
    def mezclarDirectorios(self,gruposIMG,listaClases):
        numGrupos = len(listaClases)
        numImagen = 1 #Se usa para nombrar a la imagen procesada
        while(gruposIMG): #mientras haya grupos en la lista
            try:
                indxElmGrup = numpy.random.randint(0,numGrupos, size=None)
                if(not gruposIMG[indxElmGrup]): # si ya no hay elementos en el grupo
                    if(gruposIMG): # si hay elementos en lista de grupos
                        gruposIMG.pop(indxElmGrup)  # eliminar espacio de grupo de la lista de grupos
                        listaClases.pop(indxElmGrup)# eliminar clase de lista de clases
                        numGrupos -=1               # actualizar tamanio de grupo
                else:
                    rutaImg = gruposIMG[indxElmGrup].pop()
                    print listaClases[indxElmGrup],'>>',rutaImg
                    imagen = self.getImagenPIL(rutaImg)
                    imagen = self.redimensionarIMG(self.width, self.height, imagen)
                    if(self.listaFiltros):
                        imagen = self.aplicarFiltros(imagen, self.listaFiltros)
                    if(self.modo):
                        imagen = self.cambiarModo(imagen, self.modo)
                    self.guardarImagen(self.dirDestino, imagen, numImagen)
                    self.escribirCSV(listaClases[indxElmGrup])
                    numImagen +=1
            except Exception as e:
                print 'Error en operaciones con listas: ',e.message
                traceback.print_exc()
     
    
    #Carga una imagen en memoria con PIL
    def getImagenPIL(self,ruta):
        im = None
        try:
            print 'Abriendo: ', ruta
            im = Image.open(ruta)
        except Exception as e:
            print e.message
        return im
    
    #Redimensiona la @imagen al tamanio indicado
    def redimensionarIMG(self,w,h,imagen):
        imagen = imagen.resize((w, h),Image.ANTIALIAS)
        #imagen = imagen.resize((w, h))
        return imagen
    
    #Aplica a la imagen todos los filtros contenidos en @listaFiltros
    def aplicarFiltros(self,imagen,listaFiltros):
        try:
            for filtro in listaFiltros:
                imagen = imagen.filter(filtro)
        except Exception as e:
            print 'Error en aplicacion de filtros'
            raise e;
        return imagen
    
    #Cambia el modo de color de la Imagen. Por ejemplo: RGB -> L(grayScale), RGB -> 1 (black and white)
    def cambiarModo(self,imagen,modo):
        try:
            imagen = imagen.convert(modo)
        except Exception as e:
            print "Error al cambiar modo de imagen. Modo: ",modo, " Modo actual: ",imagen.mode
            raise e
        return imagen
    
    def guardarImagen(self, dirDestino, imagen, nombre):
        try:
            imagen.save(dirDestino+str(nombre)+".png", "PNG")
        except IOError:
            print 'ERROR: No fue posible crear la imagen'
    
    #Aplica todos los filtros diponibles de PIL en una imagen
   
    
#rutas = ['C:\Users\Isaac\Desktop\gatos','C:\Users\Isaac\Desktop\camaleones','C:\Users\Isaac\Desktop\dogs']
#clases  = ['gatos','camaleones','dogs']
#listaFiltros = [ImageFilter.BLUR]
#listaFiltros.append(ImageFilter.CONTOUR)
#listaFiltros = []
#destino = 'C:\Users\Isaac\Desktop\Otro\\'
#modo = 'RGB;L'
#proceso = Procesador(rutas,clases,listaFiltros,modo,32, 32, destino, 'Ent1.csv')
#proceso.RUN()



