<?php
$tol=60;
$tama�o_nube=1;
$pasos_nube=5;
$rgb=0;
$r=0;
$g=0;
$b=0;
$contar=0;
$xnube=array();
$ynube=array();
$xinicio=317;
$xfin=455;
$yinicio=564;
$yfin=680;


$im=imagecreatefromjpeg("sur.jpg");
$x=0;
while ($x<2){
    for($y=$yinicio;$y<=$yfin;$y++){
        for($x=$xinicio;$x<=$xfin;$x++){
        
            $rgb=imagecolorat($im,$x,$y);
            $r=($rgb >> 16) & 0xFF;
            $g=($rgb >> 8) & 0xFF; 
            $b=$rgb & 0xFF;
            
            $check=es_piedra($r,$g,$b,$tol);   
            
            if ($check == "SI"){
        //        echo "$r   $g   $b   |   $x  $y<br />";
                $xnube[]=$x; //agrego todos los pixeles a un array de x
                $ynube[]=$y;
                $contar++;
                
            }   
        }  
    }
    $x++;
}
//echo "Hay $contar pixeles nube<br />";
echo "$contar<br />";

$xmin=array();
$xmax=array();
$ymin=array();
$ymax=array();
$pix_enjambres=array();

$dbpx=array();
$dbpy=array();

$contar_nubes=0;

$px=$xnube[0];
$py=$ynube[0];
//echo "$px - $py<br />";

$pixel_total=0;
for ($numero=0;$numero<$contar;$numero++){
    $px=$xnube[$numero];
    $py=$ynube[$numero];
//    echo "Pixel seleccionado para analizar:   $px - $py<br />";
    if (hay_coincidencias($px,$py,$dbpx,$dbpy,$pixel_total)){}
    else{
//        echo "El pixel no esta dentro del enjambre<br />";
        echo "SE HA ENCONTRADO UNA NUEVA NUBE<br />";
        
        unset($enjambre_x);
        unset($enjambre_y);
        $enjambre_x=array();
        $enjambre_y=array();
        
        $contar_p=0;
        $nube_cerrada=0;
        while ($nube_cerrada<1){
            if ($contar_p==0){
                $pax=$px;
                $pay=$py;
                $enjambre_x[]=$pax;
                $enjambre_y[]=$pay;
                $pixel_en_nube=1;
            }else{
                $pax=$enjambre_x[$contar_p];
                $pay=$enjambre_y[$contar_p];
            }
     //       echo "PIXEL MADRE: $pax - $pay<br />";
            //Analizar pixel izquierda
            $contador=1;
            while($contador<=$pasos_nube){
                $paxd=$pax-$contador;
                $payd=$pay;
          //      echo "coordenadas pixel iz: - - $paxd - $payd<br />";
                if (hay_coincidencias($paxd,$payd,$xnube,$ynube,$contar)){
           //         echo "Es pixel nube.<br />";
                    if (hay_coincidencias($paxd,$payd,$enjambre_x,$enjambre_y,$pixel_en_nube)){
           //             echo "Ya se encuentra en enjambre<br />";
                    }else{
           //             echo "--Se agrega a enjambre--<br />";
                        $enjambre_x[]=$paxd;
                        $enjambre_y[]=$payd;
                        $pixel_en_nube++;
                    }
                }
                $contador++;
            }
            //Analizar pixel derecha
            $contador=1;
                while($contador<=$pasos_nube){
                $paxd=$pax+$contador;
                $payd=$pay;
          //      echo "coordenadas pixel de: - - $paxd - $payd<br />";
                if (hay_coincidencias($paxd,$payd,$xnube,$ynube,$contar)){
            //        echo "Es pixel nube.<br />";
                    if (hay_coincidencias($paxd,$payd,$enjambre_x,$enjambre_y,$pixel_en_nube)){
           //             echo "Ya se encuentra en enjambre<br />";
                    }else{
          //              echo "--Se agrega a enjambre--<br />";
                        $enjambre_x[]=$paxd;
                        $enjambre_y[]=$payd;
                        $pixel_en_nube++;
                    }
                }
                $contador++;
            }
            //Analizar pixel arriba
            $contador=1;
                while($contador<=$pasos_nube){
                $paxd=$pax;
                $payd=$pay-$contador;
         //       echo "coordenadas pixel ar: - - $paxd - $payd<br />";
                if (hay_coincidencias($paxd,$payd,$xnube,$ynube,$contar)){
          //          echo "Es pixel nube.<br />";
                    if (hay_coincidencias($paxd,$payd,$enjambre_x,$enjambre_y,$pixel_en_nube)){
         //               echo "Ya se encuentra en enjambre<br />";
                    }else{
         //               echo "--Se agrega a enjambre--<br />";
                        $enjambre_x[]=$paxd;
                        $enjambre_y[]=$payd;
                        $pixel_en_nube++;
                    }
                }
                $contador++;
            }
            //Analizar pixel abajo
            $contador=1;
                while($contador<=$pasos_nube){
                $paxd=$pax;
                $payd=$pay+$contador;
        //        echo "coordenadas pixel ab: - - $paxd - $payd<br />";
                if (hay_coincidencias($paxd,$payd,$xnube,$ynube,$contar)){
       ///             echo "Es pixel nube.<br />";
                    if (hay_coincidencias($paxd,$payd,$enjambre_x,$enjambre_y,$pixel_en_nube)){
       ///                 echo "Ya se encuentra en enjambre<br />";
                    }else{
       //                 echo "--Se agrega a enjambre--<br />";
                        $enjambre_x[]=$paxd;
                        $enjambre_y[]=$payd;
                        $pixel_en_nube++;
                    }
                }
                $contador++;
            }
            $contar_p++;
            if ($contar_p==$pixel_en_nube){
                $pixel_total=$pixel_total+$contar_p;
                $nube_cerrada=1;
                $contar_nubes++;
                
                echo "-------------------------------------------<br />";
                echo "Se ha cerrado la nube<br /> Pixeles en nube: $pixel_en_nube<br />";
                echo "Pixeles analizados: $contar_p<br />";
                echo "-------------------------------------------<br />";
                
                $xm=min($enjambre_x);
                $xmx=max($enjambre_x);
                $ym=min($enjambre_y);
                $ymx=max($enjambre_y);
            
                $xmin[]=$xm;
                $xmax[]=$xmx;
                $ymin[]=$ym;
                $ymax[]=$ymx;
                
                $pix_enjambres[]=$contar_p;
                
                for ($n=0;$n<$contar_p;$n++){
                    $dbpx[]=$enjambre_x[$n];
                    $dbpy[]=$enjambre_y[$n];  
                }
            }
        }
    }
}

echo "-------------------------------------------<br />";
echo "TOTAL NUBES: $contar_nubes<br />";
for ($n=0;$n<$contar_nubes;$n++){
    if ($pix_enjambres[$n]>500){
        echo "Nube N: $n --- xmin: $xmin[$n] - xmax: $xmax[$n] - ymin: $ymin[$n] - ymax: $ymax[$n] - PIXELES: $pix_enjambres[$n]<br />";
    }
}


////////////FUNCIONES

function hay_coincidencias($x,$y,$ax,$ay,$p){
    for($n=0;$n<$p;$n++){
        $xtemp=$ax[$n];
        $ytemp=$ay[$n];
        if ($x==$xtemp && $y==$ytemp){
            return TRUE;
        }
    }
    return FALSE;
}


function in_array_r($needle, $haystack, $strict = false) {
    foreach ($haystack as $item) {
        if (($strict ? $item === $needle : $item == $needle) || (is_array($item) && in_array_r($needle, $item, $strict))) {
            return true;
        }
    }

    return false;
}


function es_piedra($r,$g,$b,$tol){
    $rmin=$r-$tol;
    $rmax=$r+$tol;
    $gmin=$g-$tol;
    $gmax=$g+$tol;
    $bmin=$b-$tol;
    $bmax=$b+$tol;
    $si="SI";
    $no="NO";
    if (199 <= $rmax && 199 >= $rmin && 15 <= $gmax && 15>= $gmin && 134 <= $bmax && 134 >= $bmin){
 //       echo "pixel nube clase 1 - ";
        return $si;
    }else if (190 <= $rmax && 190 >= $rmin && 100 <= $gmax && 100 >= $gmin && 134 <= $bmax && 134 >= $bmin){
//        echo "pixel nube clase 2 - ";
        return $si;
    }else if (208 <= $rmax && 208 >= $rmin && 135 <= $gmax && 135 >= $gmin && 59 <= $bmax && 59 >= $bmin){
//        echo "pixel nube clase 3 - ";
        return $si;
    }else if (249 <= $rmax && 249 >= $rmin && 196 <= $gmax && 196 >= $gmin && 48 <= $bmax && 48 >= $bmin){
//        echo "pixel nube clase 4 - ";
        return $si;
    }else if (254 <= $rmax && 254 >= $rmin && 252 <= $gmax && 252 >= $gmin && 5 <= $bmax && 5 >= $bmin){
//        echo "pixel nube clase 5 - ";
        return $si;
    }else if (252 <= $rmax && 252 >= $rmin && 154 <= $gmax && 154 >= $gmin && 89 <= $bmax && 89 >= $bmin){
 //       echo "pixel nube clase 6 - ";
        return $si;
    }else if (252 <= $rmax && 252 >= $rmin && 95 <= $gmax && 95 >= $gmin && 6 <= $bmax && 6 >= $bmin){
 //       echo "pixel nube clase 7 - ";
        return $si;
    }else if (251 <= $rmax && 251 >= $rmin && 52 <= $gmax && 52 >= $gmin && 27 <= $bmax && 27 >= $bmin){
 //       echo "pixel nube clase 8 - ";
        return $si;
    }else if (190 <= $rmax && 190 >= $rmin && 190 <= $gmax && 190 >= $gmin && 190 <= $bmax && 190 >= $bmin){
 //       echo "pixel nube clase 9 - ";
        return $si;
    }else if (211 <= $rmax && 211 >= $rmin && 211 <= $gmax && 211 >= $gmin && 211 <= $bmax && 211 >= $bmin){
  //      echo "pixel nube clase 10 - ";
       return $si;
    }else{
        return $no;
    }
}


?>