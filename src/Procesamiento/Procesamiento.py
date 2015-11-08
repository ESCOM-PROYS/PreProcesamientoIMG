'''
Created on 27/11/2015

@author: isaac
'''
import os
import numpy
import Image
import ImageFilter
from os.path import expanduser

class Procesador:
    
    def __init__(self, listaDirectorios , listaClases , w=32 , h=32 , dirDestino = None , nombreCSV='CSV_TRAIN', listFiltros):
        self.listaDirectorios = listaDirectorios
        self.listaClases = listaClases
        self.width  = w 
        self.height = h
        self.homeDir = expanduser("~")
        self.dirDestino = dirDestino or (self.homeDir + '\\TRAIN\\')
        self.nombreCSV = nombreCSV
        self.CSV = None
        self.listaFiltros = listFiltros
    
        
    def RUN(self):
        print 'Comenzando Proceso...'
        self.crearDirectorio(self.dirDestino)
        self.crearCSV(self.nombreCSV)
        gruposIMG = self.getZIPListasDeRutas(self.listaDirectorios)
        self.mezclarDirectorios(gruposIMG, self.listaClases)
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
            self.CSV = open(self.dirDestino+nombreCSV)
        except IOError:
            print 'No fue posible crear el archivo CSV'
        
    
    
    #Genera una lista A que contiene listas Bi, donde Bi es una lista con todas las rutas de las imagenes que corresponden a una clase.
    #@return gruposIMG=[[img11,img12,img13,...,img1n],[img21,img22,img23,...,img2n],...[imgn1,imgn2,imgn3,...,imgnm]] 
    #@listaDirectorios Es una lista que contiene las rutas de los directorios que van a mezclarse
    def getZIPListasDeRutas(self,listaDirectorios):
        gruposIMG = []
        for directorio in listaDirectorios:
            listaIMG = []
            for img in os.listdir(directorio):
                if(img.endswith("png") or img.endswith("jpg") or img.endswith("JPG") or img.endswith("PNG") or img.endswith("JPEG") or img.endswith("jpeg") ):
                    listaIMG.append(img)
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
            except:
                print 'Error en Generador Aleatorio'
            try:
                rutaImg = gruposIMG[indxElmGrup].pop()
                print listaClases[indxElmGrup],'>>',rutaImg
                imagen = self.getImagenPIL(rutaImg)
                imagen = self.redimensionarIMG(self.w, self.h, imagen)
                imagen = self.aplicarFiltros(imagen, self.listaFiltros)
                self.guardarImagen(self.dirDestino, imagen, numImagen.__str__())
                
                if(not gruposIMG[indxElmGrup]): # si ya no hay elementos en el grupo
                    gruposIMG.pop(indxElmGrup)  # eliminar espacio de grupo de la lista de grupos
                    listaClases.pop(indxElmGrup)# eliminar clase de lista de clases
                    numGrupos -=1               # actualizar tamanio de grupo
            except:
                print 'Error en operaciones con listas'
            numImagen +=1
     
    
    #Carga una imagen en memoria con PIL
    def getImagenPIL(self,ruta):
        try:
            im = Image.open(ruta)
        except IOError:
            pass
        return im
    
    #Redimensiona la @imagen al tamanio indicado
    def redimensionarIMG(self,w,h,imagen):
        imagen = imagen.resize((w, h),Image.ANTIALIAS)
        return imagen
    
    #Aplica a la imagen todos los filtros contenidos en @listaFiltros
    def aplicarFiltros(self,imagen,listaFiltros):
        for filtro in listaFiltros:
            imagen = imagen.filter(filtro)
        return imagen
    
    
    def guardarImagen(self, dirDestino, imagen, nombre):
        try:
            imagen.save(dirDestino+nombre, "JPEG")
        except IOError:
            print 'ERROR: No fue posible crear la imagen'
        
    
rutas = ['C:\Users\Isaac\Desktop\gatos','C:\Users\Isaac\Desktop\camaleones','C:\Users\Isaac\Desktop\dogs']
clases  = ['gatos','camaleones','dogs']
listaFiltros = [ImageFilter.BLUR, ImageFilter.SHARPEN]
listaFiltros.append(ImageFilter.CONTOUR)
destino = 'C:\Users\Isaac\Desktop\Otro\\'

proceso = Procesador(rutas, 32, 32, destino, 'Ent1')



