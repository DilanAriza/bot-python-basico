from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, json
import py2exe

tiempoEspera = 10

print("Buscando el driver de firefox");
driver = webdriver.Firefox(executable_path="./geckodriver.exe");

with open("main.json") as json_file: 
    data = json.load(json_file)
    
    for p in data["employes"]:
        print (p["name"] + " is loading!")

        driver.get("https://www.segurossura.com.co/covid-19/encuestas/paginas/sintomas.aspx")
        print("Abriendo Navegador")
        time.sleep(tiempoEspera)

        nextPageBtn = driver.find_element_by_name("data[page3SiAutorizo]")
        nextPageBtn.click()
        print("Pasando a la pagina de formulario")

        time.sleep(2)
        userId = driver.find_element_by_name("data[identificacion_usuario]")
        userId.send_keys(p["id"])
        print("Añadiendo cedula")

        time.sleep(2)
        userName = driver.find_element_by_name("data[nombre_usuario]")
        userName.send_keys(p["name"])
        print("Añadiendo Nombre")

        time.sleep(tiempoEspera)
        print("Cerrando navegador y empezando de nuevo")

driver.close()