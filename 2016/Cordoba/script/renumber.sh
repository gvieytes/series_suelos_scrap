# Script simple para volver a numerar los archivos una vez que los tengo todos
# organizados pero quedaron algunos "a-mano" o "sin-tabla" mezclados
#
# Se debe ejecutar desde el directorio donde solo haya archivos de serie de la forma
# XXX-nombre_de_archivo.txt[sin_tabla]
# Este script removera todo lo que esta antes del guion medio y armara nuevos archivos poniendo al principio la nueva numeracion

numero=1

#for i in `(ls *.txt | awk -F- '{print $2}')`
for i in `(ls *.txt*)`
do 
	nombreArchivo=$(echo ${i} | awk -F- '{print $2}')
	indice=$(printf '%03d\n' ${numero})
	cp ${i} unificados-numerados/${indice}-${nombreArchivo}
	let numero++

done
