from PIL import Image, ImageDraw

'''
Voy a usar la libreria PIL para poder analizar las imagenes, para instalarla tengo que poner "pip install pillow".
red_image = Image.open("red.png") -->cargo la imagen a red_image
red_image_rgb = red_image.convert("RGB") --> creo un array[x][y] con la información de cada pixel
rgb_pixel_value = red_image_rgb.getpixel((10,15)) --> de esta forma obtengo los valores rgb del pixel, y lo cargo a rgb_pixel_value
print(rgb_pixel_value) #Prints (255, 0, 0)
'''
url_imagen="images/1918.gif"
image = Image.open(url_imagen)
image_rgb=image.convert("RGB") #Cargo la imagen a la variable para poder trabajar con ella

'''
analizarPixel funciona recibiendo las coordenadas del pixel y la imagen y extrae los valores rgb. Devuelve True si el pixel
se encuentra dentro de los valores de rgb de las distintas densidades de nubes (de la imagen dBZ 39 a 80).
los valores minimos y maximos se ven alterados por toleranciaRGB. Esa variable determina cuanta tolerancia hay
entre el color recibido (el que está en la nube) y el color base de nube, es necesario puesto que el color del pixel
puede acarrear cierto "ruido"
'''
def analizarPixel(x, y, imagen):
    pixelRGB=imagen.getpixel((x,y))#extraigo los valores rgb del pixel
    r=pixelRGB[0]
    g=pixelRGB[1]
    b=pixelRGB[2]

    toleranciaRGB=60
    rmin=r-toleranciaRGB
    rmax=r+toleranciaRGB
    gmin=g-toleranciaRGB
    gmax=g+toleranciaRGB
    bmin=b-toleranciaRGB
    bmax=b+toleranciaRGB

    rgb=[
        [199,15,134],
        [190,100,134],  #45-42 dBZ
        [208,138,59],   #48-45 dBZ
        [249,196,48],   #51-48 dBZ
        [254,252,5],    #54-51 dBZ
        [252,154,59],   #57-54 dBZ
        [252,95,6],     #60-57 dBZ
        [251,52,27],    #65-60 dBZ
        [190,190,190],  #70-65 dBZ
        [211,211,211]   #80-70 dBZ
    ]
    for i in range(9):
        if ((rmin <= rgb[i][0] <= rmax) and (gmin <= rgb[i][1] <= gmax) and (bmin <= rgb[i][2] <= bmax)):
            return True
    return False


#340 54 inicio
#420 120 fin


#Creo una lista con TODOS los pixeles que son piedras
pixelPiedra=[]
for x in range(110,700):
    for y in range(55,450):
        if(analizarPixel(x,y,image_rgb)): #Analizo el pixel
            pixelPiedra.append([x,y])


'''
En este apartado, lo que hago es analizar la nube, para encontrar el minimo y le maximo. Primero agrego el pixel de la primer
nube a la lista [nube]. Luego, y gracias al modulo enumerate(nube), voy analizando pixel por pixel tanto a la izquierda, a la derecha
arriba y abajo... si el pixel en cuestion SE ENCUENTRA en la lista de pixeles [pixelPiedra], y NO SE ENCUENTRA en la nube, lo agrego.
El ciclo se va a cumplir hasta que ya no encuentre más pixeles... ésto lo logro gracias al ya mencionado enumerate... me permite trabajar
en un rango no definido, o sea que si agrego un nuevo elemento a la lista, lo va a recorrer (al contrario de range(len(list)), que
me recorre una lista con elementos YA definidos)
Elimino los pixeles cargados para que a la proxima iteración empiece con una nueva nube
Luego calculo los minimos y máximos, y los agrego a una lista
'''
listaNubes=[]
while(len(pixelPiedra)>0):
    nube=[pixelPiedra[0]]
    for indice,i in enumerate(nube):
        x=nube[indice][0]
        y=nube[indice][1]
        pixelPiedra.remove([x,y])#Elimino de la lista de pixelPiedra el pixel cargado en la nube
        
        for j in range (1,5):
            if (([x+j,y] in pixelPiedra) and ([x+j,y] not in nube)):
                nube.append([x+j,y])
            if ([x-j,y] in pixelPiedra and ([x-j,y] not in nube)):
                nube.append([x-j,y])
            if ([x,y+j] in pixelPiedra and ([x,y+j] not in nube)):
                nube.append([x,y+j])
            if ([x,y-j] in pixelPiedra and ([x,y-j] not in nube)):
                nube.append([x,y-j])

    def minimo(nube,eje):
        lista=[]
        for i in range(len(nube)):
            if (nube[i][eje] not in lista):
                lista.append(nube[i][eje])
        return min(lista)
    def maximo(nube,eje):
        lista=[]
        for i in range(len(nube)):
            if (nube[i][eje] not in lista):
                lista.append(nube[i][eje])
        return max(lista)
    xmin=minimo(nube,0)
    ymin=minimo(nube,1)
    xmax=maximo(nube,0)
    ymax=maximo(nube,1)
    if (((xmax-xmin)>16) and ((ymax-ymin)>16)):
        listaNubes.append([xmin,xmax,ymin,ymax]) #Creo una lista con las coordenadas de todas las nubes dentro

print("Cantidad de nubes: ",len(listaNubes))
for i in range(len(listaNubes)):
    print(listaNubes[i])
'''
importamos el modulo "ImageDraw", para crear cada linea se usa la función "line" la cual toma como argumento 3 argumentos, 
los 2 primero son las coordenadas en su eje X e Y, el segundo (fill) seria la intensidad del color de cada linea, 
y el argumento width, seria la anchura de la linea.
'''
draw = ImageDraw.Draw(image) #Con draw puedo dibujar en la imagen
for i in range (len(listaNubes)):
    xmin=listaNubes[i][0]
    xmax=listaNubes[i][1]
    ymin=listaNubes[i][2]
    ymax=listaNubes[i][3]
    draw.line( (xmin,ymin,xmax,ymin), fill="#ffff00",width=2 )
    draw.line( (xmin,ymax,xmax,ymax), fill="#ffff00",width=2 )
    draw.line( (xmin,ymin,xmin,ymax), fill="#ffff00",width=2 )
    draw.line( (xmax,ymin,xmax,ymax), fill="#ffff00",width=2 )

image.convert("RGB").save("ImagenConLineas.jpg")



