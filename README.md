# Bot básico en Python
--- 

Este Bot se encarga de rellenar los datos de un formulario que personas con sintomas de Covid-19


### Antes de empezar

Este bot tiene varias particularidades:
- Tiene que tener el driver del navegador añadido al path de rutas de las variables de entorno.
- Tiene que añadir la ruta del driver al código en la linea 5 dentro del ` webdriver.Firefox(executable_path="Ruta del driver") `.
- Tener una buena conexión a internet, de lo contrario configurar la variable ` tiempoEspera ` con el tiempo que demore su navegador en abrir la pagina, de esta forma evitara futuros errores a la hora de ejetucar el programa.
---


## Instalación
Este programa requiere la instalación de un driver para poder utilizar un navegador, en este caso se utiliza el driver de [firefox](https://github.com/mozilla/geckodriver/releases).

Se instala la libreria de [Selenium](https://pypi.org/project/selenium/)
```
pip install selenium
``` 

o

```
pip3 install selenium
``` 


Se instala la libreria de [Py2exe](https://pypi.org/project/py2exe/)
```
pip install py2exe
``` 

o
```
pip3 install py2exe
``` 


## Correr el Bot

Luego ejecutamos el código con 
```
Python3 main.py
```


## Compilar el Bot

Luego compilamos el código con 
```
setup.py py2exe
```

y esperamos a que el programa abra el navegador y rellene los datos del formulario.

### Nota importante

Usted tiene que añadir los datos dentro del archivo `main.json` para su correcta ejecución dentro del formulario.

- El archivo `main.json` requiere un array con el nombre de "employes"
- Dentro del array tendra que asignar un un objeto por cada persona que quiera ingresar por el formulario de la pagina
- El objeto que deberá pasarle al array tiene que tener dos campos
  - El primer campo es la cedula, pero por mantenimiento futuro del código se decidio poner el nombre del campo como "id"
  - El segundo campo es el nombre de la persona a la cual corresponda la cedula
 - Tendra que tener paciencia durante la ejecución del programa, pero podrá realizar otras actividades con la maquina donde este ejecutando el bot

Muchas gracias.
