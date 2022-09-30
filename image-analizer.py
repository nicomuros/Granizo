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
    pixelRGB=imagen.getpixel((365,73))#extraigo los valores rgb del pixel
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

    if ((rmin <= 252 <= rmax)):
        return True

url_imagen="images/1918.gif"
image_rgb=cargarImagen(url_imagen) #Cargo la imagen a la variable para poder trabajar con ella
print(analizarPixel(365,73,image_rgb))