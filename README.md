# README.md

Execute google_news.py with crontab on Linux:

1. crear un archivo .sh al mismo nivel que el archivo .py para más facilidad a la hora de indicar
las rutas

en la cabecera debe ir SIEMPRE:
!# bin/bash

2. para saber la ruta del archivo .py, ejecutar en la terminal pwd

/home/maca/Documentos/exercises-python/webscrapper, in our case

3. copiar esa ruta en el archivo .sh, donde irían las instrucciones junto con el comando cd delante de todo

cd /home/maca/Documentos/exercises-python/webscrapper

4. luego comando para ejecurtar cualquier archivo .py

python3 google_news.py

al final quedaría:

!# bin/bash

cd /home/maca/Documentos/exercises-python/webscrapper
python3 google_news.py

5. dar permisos de ejecución con chmod +x file.sh

para hacer una prueba de que .sh funciona ejecutar: ./file.sh

6. ejecutar en la terminal crontab -e, escribir en el editor que se abre

09*** /home/maca/Documentos/exercises-python/webscrapper/file.sh

el file.sh se va a ejecutar a las 0(minutos)9(horas) de la mañana todos los días del año

first asterisco = día del mes
second asterisco = mes del año
third asterisco = día de la semana

7. Save and exit
