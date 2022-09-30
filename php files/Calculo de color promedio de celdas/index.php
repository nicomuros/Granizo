<?php

    $imgtemp_gif="temp.gif";
    $animacion="radar_animacion.gif";
    $animacion_old="radar_animacion_old.gif";
    $imgtemp="temp.jpg";
    $imgprev="sur.jpg";
    $son_iguales;
    
    echo "-----------------------------------<br/> <br/>";
    echo "1. Verificar estado servidor<br/>";
    $status=check_status();
    echo "Finalizado<br/>";
    
    if ($status){
        echo "-----------------------------------<br/> <br/>";
        echo "2. Copiar imagenes desde contingencias<br/>";
        copiar_imagenes($imgtemp_gif,$animacion,$animacion_old);
        echo "Finalizado<br/>";
        
        echo "-----------------------------------<br/> <br/>";
        echo "3. Convertir imagen nueva de GIF a JPG <br/><br/>";
        gif_to_jpg($imgtemp_gif, $imgtemp); //CONVERTIR NUEVA IMAGEN GIF A JPG
        echo "Finalizado<br/>";
        
        echo "-----------------------------------<br/> <br/>";
        echo "4. Actualizar imagenes<br/>";
        $son_iguales=actualizar_imagenes($imgtemp,$imgprev);
        echo "Finalizado<br/>";
        echo "-----------------------------------<br/> <br/>";


}   
        

    //--------------- FUNCIONES FUNCIONES FUNCIONES FUNCIONES ---------------------
    


    
    function check_status(){
        $url = "http://www.contingencias.mendoza.gov.ar";
        $puerto = 80;  
        if ($fp=@fopen($url,"r"))   
        {   
            fclose($fp);   
            echo "<font color='Green'>ONLINE<br /></font>";
            return TRUE;  
        } else {         
            echo "<font color='Red'>OFFLINE<br /></font>";
            return FALSE;
        }   
    }
    
    function copiar_imagenes($nombre_imagen_sur,$animacion,$animacion_old){
        copy("http://www.contingencias.mendoza.gov.ar/radar/sur.gif",$nombre_imagen_sur);
        echo "imagen sur.gif copiada";
        copy("http://www.contingencias.mendoza.gov.ar/radar/animacion.gif","animacion_temporal.gif");
         if (file_exists("animacion_temporal.gif")){
            if (file_exists($animacion)){
                if (file_exists($animacion_old)){
                    unlink($animacion_old);
                    rename($animacion,$animacion_old);
                    rename("animacion_temporal.gif",$animacion);
                }else{
                    rename($animacion,$animacion_old);
                    rename("animacion_temporal.gif",$animacion);
                }
            } else {
                rename("animacion_temporal.gif",$animacion);
            }                                                  
        }      
    }
    
    
    function gif_to_jpg($imgtemp_gif,$imgtemp_jpg)
    {   
        echo "Leyendo imagen temporal <br />  ";
        echo "Imagen temporal: $imgtemp_gif <br />  ";
        echo "Verificando si ya existe el archivo convertido <br/>";
        if (file_exists($imgtemp_jpg)&&file_exists($imgtemp_gif)) {
              echo "El fichero $imgtemp_jpg existe, no hay necesidad de convertir <br />";
        } else {
            echo "El fichero $imgtemp_jpg no existe <br/>";
            echo "Convirtiendo imagen temopral de GIF a JPG <br />  ";
            $image = imagecreatefromgif($imgtemp_gif);
            imagejpeg($image, $imgtemp_jpg);
            
        }
        if (file_exists($imgtemp_gif)){
        echo "Eliminando GIF <br/>";
        unlink($imgtemp_gif);
        }

    }
    
    
    function actualizar_imagenes($a,$b)
    {
        $imagen_n=imagecreatefromjpeg($a);
        $imagen_v=imagecreatefromjpeg($b);
        echo "Se procedera a comprar las dos imagenes <br/>";
        $contar=0;
        for ($ancho=1;$ancho<=220;$ancho++){
            for ($largo=1;$largo<=52;$largo++){
                $imagen_nueva=imagecolorat($imagen_n, $ancho, $largo);
                $imagen_anterior=imagecolorat($imagen_v, $ancho, $largo);
                if ($imagen_nueva == $imagen_anterior){
                    $contar++;    
                }
            }
            
        }
        echo "El numero de pixeles similares en las dos imagenes son: $contar<br/";
        if ($contar >= 11400){
            echo "Las dos imagenes son iguales<br/>";
            echo "Se eliminara la imagen temporal<br/>";
            unlink($a);
            return TRUE;
        }else{
            echo "Las dos imagenes son diferentes<br/>";
            
            for ($contar=8;$contar>=0;$contar=$contar-1){
                $contar2=$contar+1;
                if ($contar==8){
                    echo "Se procedera a borrar la imagen n°5 (que pasara a ser la 6)";
                    $nombre="sur_".$contar.".jpg";
                    if (file_exists($nombre)){
                        unlink($nombre);
                    }
                }
                if ($contar>=2 || $contar <=7){
                    $nombre="sur_".$contar.".jpg";
                    $nuevo_nombre="sur_".$contar2.".jpg";
                    if (file_exists($nombre)){
                        rename ($nombre,$nuevo_nombre);
                        echo "$nombre se llamara de ahora en mas $nuevo_nombre<br/>";
                    }
                }
                if ($contar==1){
                    echo "contar = $contar<br/>";
                    if (file_exists("sur.jpg")){
                        rename ("sur.jpg","sur_1.jpg");    
                        echo "sur.jpg se llamara sur_1.jpg";
                    }
                }
                
            }
            
            echo "Se agrega la imagen nueva <br/>";
            rename ($a,"sur.jpg");
            return FALSE;
        }
    }
?>