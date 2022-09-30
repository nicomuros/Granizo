from operator import truediv
from PIL import Image 

'''
Voy a usar la libreria PIL para poder analizar las imagenes, para instalarla tengo que poner "pip install pillow".
red_image = Image.open("red.png") -->cargo la imagen a red_image
red_image_rgb = red_image.convert("RGB") --> creo un array[x][y] con la información de cada pixel
rgb_pixel_value = red_image_rgb.getpixel((10,15)) --> de esta forma obtengo los valores rgb del pixel, y lo cargo a rgb_pixel_value
print(rgb_pixel_value) #Prints (255, 0, 0)
'''

def cargarImagen(url_imagen):
    image = Image.open(url_imagen)
    return(image.convert("RGB"))

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
url_imagen="images/1918.gif"
image_rgb=cargarImagen(url_imagen) #Cargo la imagen a la variable para poder trabajar con ella

#Creo una lista con TODOS los pixeles que son piedras
pixelPiedra=[]
for x in range(340,420):
    for y in range(54,121):
        if(analizarPixel(x,y,image_rgb)): #Analizo el pixel
            pixelPiedra.append([x,y])

#print (pixelPiedra[0])
x = pixelPiedra[0][0]
y = pixelPiedra[0][1]

print(f'''
    Pixel base: {x},{y}
    Pixel {x-1},{y}: {[x-1,y] in pixelPiedra}
    Pixel {x+1},{y}: {[x+1,y] in pixelPiedra}
    Pixel {x},{y-1}: {[x,y-1] in pixelPiedra}
    Pixel {x},{y+1}: {[x,y+1] in pixelPiedra}
''')
nube=[pixelPiedra[0]]

for indice,i in enumerate(nube):
    x=nube[indice][0]
    y=nube[indice][1]
    if (([x+1,y] in pixelPiedra) and ([x+1,y] not in nube)):
        nube.append([x+1,y])
    if ([x-1,y] in pixelPiedra and ([x-1,y] not in nube)):
        nube.append([x-1,y])
    if ([x,y+1] in pixelPiedra and ([x,y+1] not in nube)):
        nube.append([x,y+1])
    if ([x,y-1] in pixelPiedra and ([x,y-1] not in nube)):
        nube.append([x,y-1])

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
minx=minimo(nube,0)
miny=minimo(nube,1)
maxx=maximo(nube,0)
maxy=maximo(nube,1)
print(f'''
    Inicio: [{minx},{miny}]
    Fin: [{maxx},{maxy}]
''')



