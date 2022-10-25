from PIL import Image, ImageDraw


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

def imgAnalyzer(imgName):
    image = Image.open(imgName)
    image_rgb=image.convert("RGB")

    pixelPiedra=[]
    for x in range(110,700):
        for y in range(55,700):
            if(analizarPixel(x,y,image_rgb)): #Analizo el pixel
                pixelPiedra.append([x,y])

    listaNubes=[]
    while(len(pixelPiedra)>0):
        nube=[pixelPiedra[0]]
        for indice,i in enumerate(nube):
            x=nube[indice][0]
            y=nube[indice][1]
            pixelPiedra.remove([x,y])#Elimino de la lista de pixelPiedra el pixel cargado en la nube
            
            for j in range (5):
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
        if (((xmax-xmin)>35) and ((ymax-ymin)>35)):
            listaNubes.append([xmin,xmax,ymin,ymax]) #Creo una lista con las coordenadas de todas las nubes dentro
    
    return listaNubes
