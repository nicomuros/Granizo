<?php

    
    $imagen_previa_gif="sur.gif";
    $imagen_previa_jpg="sur.jpg";
    $imagen_temporal_gif="temp.gif";
    $imagen_previa_jpg="sur.jpg";
    
    $image = imagecreatefromgif($imagen_previa_gif);
    imagejpeg($image, $imagen_previa_jpg);

    
?>