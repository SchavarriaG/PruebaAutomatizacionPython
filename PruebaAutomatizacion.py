from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExpectedConditions
from datetime import datetime
from datetime import timedelta
import time
import emoji as Emoji

def buscarPregunta(pregunta):
    if(len(pregunta.split(" ")) > 7 and pregunta == "¿Cuál de estos números es múltiplo de "+pregunta.split(" ")[7]):
        return "Es la pregunta múltiplos."
    elif(len(pregunta.split(" ")) > 2 and pregunta == "Indique cuantos "+ pregunta.split(" ")[2] +" hay en la siguiente secuencia:" ):
        return "Es la pregunta de buscar emojis."
    elif(pregunta == "Indique la fecha que corresponde a 104 dias contados desde antes de : " + datetime.now().strftime('%d/%m/%Y')):
        return "Es la pregunta de buscar fecha para atrás."
    elif(pregunta == "Complete la siguiente operación matemática:"):
        return "Es la pregunta de operación matemática."
    elif(pregunta == "Escriba 199 veces la letra 'X'"):
        return "Es la pregunta de escribir la X varias veces"
    elif(pregunta == "Indique la fecha que corresponde a 50 dias contados desde el : "+ datetime.now().strftime('%d/%m/%Y')):
        return "Es la pregunta de buscar fecha para adelante."
    else:
        return"No se encontró."
    
def resolverPreguntaUno(pregunta):
    return null

def clickBotonEnviar(driver):
    driver.find_element_by_xpath("/html/body/div[2]/form/div[2]/button").send_keys(Keys.ENTER)

#options = Options()
#options.add_argument("--headless")
#driver = webdriver.Chrome(chrome_options=options, executable_path=r"C:\RepositorioPruebas\PythonSelenium\chromedriver\chromedriver.exe")
driver = webdriver.Chrome(executable_path=r"C:\RepositorioPruebas\PythonSelenium\chromedriver\chromedriver.exe")
driver.get("https://tasks.evalartapp.com/automatization/")

#Iniciar Sesión
#try:
username = driver.find_element_by_xpath("/html/body/div/div[2]/form/input[1]")
username.send_keys("611091")
password = driver.find_element_by_xpath("/html/body/div/div[2]/form/input[2]")
password.send_keys("10df2f32286b7120MS00LTE5MDExNg==30e0c83e6c29f1c3")
password.send_keys(Keys.ENTER)

##CICLO 1
#ciclos =  driver.find_element(By.CLASS_NAME, "text-xl text-center text-green-500")
ciclos = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/p[2]")
print(ciclos.text)

pregunta1 = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[1]//p")
pregunta2 = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[2]//p")

print(buscarPregunta(pregunta1.text))
print(buscarPregunta(pregunta2.text))

#PREGUNTA 1
grid = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[1]/div")
lista = grid.find_elements(By.NAME, "checkbox")

for elemento in lista:
    if int(elemento.get_attribute("value")) % 5 == 0:
        elemento.click()

#PREGUNTA 2
animalsEmojiGroup = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[2]/div/p[2]")
#print(str(len(animalsEmojiGroup.text)))
#inputButton = driver.find_element(By.CLASS_NAME, "border-2 border-black rounded-sm p-2")
inputButton = driver.find_element(By.XPATH, "/html/body/div[2]/form/div[1]/div[2]/input")
countEmojis = 0
for emojiFind in Emoji.demojize(animalsEmojiGroup.text).split(":"):
    if emojiFind == Emoji.demojize(pregunta2.text).split(":")[1]:
        countEmojis += 1
inputButton.send_keys(str(countEmojis)) 
print(countEmojis)
#inputButton.send_keys(Keys.ENTER)
clickBotonEnviar(driver)

###CICLO2
ciclos = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/p[2]")
print(ciclos.text)
pregunta1 = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[1]//p")
pregunta2 = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[2]//p")
#/html/body/div[2]/form/div[1]/div[2]/p
#/html/body/div[2]/form/div[1]/div[2]/p
print(buscarPregunta(pregunta1.text))
print(buscarPregunta(pregunta2.text))

#PREGUNTA 1
fecha = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[1]/input")

WebDriverWait(driver, 20).until(
    ExpectedConditions.element_to_be_clickable((By.XPATH, "/html/body/div[2]/form/div[1]/div[1]/input"))
                                ).send_keys((datetime.now() - timedelta(days=int(pregunta1.text.split(" ")[6]))).strftime('%m/%d/%Y'))

#PREGUNTA 2
grid = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[2]/div")
lista = grid.find_elements(By.NAME, "checkbox")

for elemento in lista:
    if int(elemento.get_attribute("value")) % 5 == 0:
        elemento.click()

#Enter al botón Enviar
clickBotonEnviar(driver)

###CICLO3
ciclos = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/p[2]")
print(ciclos.text)
pregunta1 = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[1]//p")
pregunta2 = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[2]//p")
#/html/body/div[2]/form/div[1]/div[2]/p
#/html/body/div[2]/form/div[1]/div[2]/p
print(buscarPregunta(pregunta1.text))
print(buscarPregunta(pregunta2.text))

#PREGUNTA 1
x = eval(driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[1]//p[2]").text[:-2])
grid = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[1]/div")
lista = grid.find_elements(By.NAME, "radio")

for elemento in lista:
    if int(elemento.get_attribute("value")) == int(x):
        elemento.click()

#PREGUNTA 2
grid = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[2]/div")
lista = grid.find_elements(By.NAME, "checkbox")

for elemento in lista:
    if int(elemento.get_attribute("value")) % 5 == 0:
        elemento.click()

#Enter al botón Enviar
clickBotonEnviar(driver)

###CICLO4
ciclos = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/p[2]")
print(ciclos.text)
pregunta1 = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[1]//p")
pregunta2 = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[2]//p")
print(buscarPregunta(pregunta1.text))
print(buscarPregunta(pregunta2.text))

#PREGUNTA 1
animalsEmojiGroup = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[1]/div/p[2]")
#print(str(len(animalsEmojiGroup.text)))
#inputButton = driver.find_element(By.CLASS_NAME, "border-2 border-black rounded-sm p-2")
inputButton = driver.find_element(By.XPATH, "/html/body/div[2]/form/div[1]/div[1]/input")
countEmojis = 0
for emojiFind in Emoji.demojize(animalsEmojiGroup.text).split(":"):
    if emojiFind == Emoji.demojize(pregunta1.text).split(":")[1]:
        countEmojis += 1
inputButton.send_keys(str(countEmojis)) 
print(countEmojis)


#PREGUNTA 2
if driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[1]//p[2]").text[:2] == "=?":
    print("Pregunta de suma tipo 1")
else: 
    print("Pregunta de suma tipo 2")
    x = eval(driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[2]/p[2]").text)
    selectButton = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[2]/select")
    options = selectButton.find_elements_by_tag_name("option")
    
    print("la suma es "+ str(x))
    for option in options:
        if option.get_attribute("value") == str(x):
            option.click()
    

#Enter al botón Enviar
clickBotonEnviar(driver)

###CICLO5
ciclos = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/p[2]")
print(ciclos.text)
pregunta1 = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[1]//p")
pregunta2 = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[2]//p")
print(buscarPregunta(pregunta1.text))
print(pregunta1.text)
print(buscarPregunta(pregunta2.text))
print(pregunta2.text)

#PREGUNTA 1
cadena = ""
for i in range(int(pregunta1.text.split(" ")[1])):
    cadena += "X"
textArea = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[1]/textarea")
textArea.send_keys(cadena)
print(cadena)

#PREGUNTA 2 
dias = int(pregunta2.text.split(" ")[6])
WebDriverWait(driver, 20).until(
    ExpectedConditions.element_to_be_clickable((By.XPATH, "/html/body/div[2]/form/div[1]/div[2]/input"))
                                ).send_keys((datetime.now() - timedelta(days=dias)).strftime('%m/%d/%Y'))
print((datetime.now() - timedelta(days=dias)).strftime('%m/%d/%Y'))

#Enter al botón Enviar
clickBotonEnviar(driver)


####CICLO6
ciclos = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/p[2]")
print(ciclos.text)
pregunta1 = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[1]//p")
pregunta2 = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[2]//p")
print(buscarPregunta(pregunta1.text))
print(pregunta1.text)
print(buscarPregunta(pregunta2.text))
print(pregunta2.text)

#PREGUNTA 1
texto = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[1]/p[2]").text

if texto[:2] == "=?":
    print("Pregunta de suma tipo 1")
else: 
    print("Pregunta de suma tipo 2")
    x = eval(texto)
    selectButton = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[1]/select")
    options = selectButton.find_elements_by_tag_name("option")
    
    print("la operación es "+ str(x))
    for option in options:
        if option.get_attribute("value") == str(x):
            option.click()

#PREGUNTA 2
dias = int(pregunta2.text.split(" ")[6])
WebDriverWait(driver, 20).until(
    ExpectedConditions.element_to_be_clickable((By.XPATH, "/html/body/div[2]/form/div[1]/div[2]/input"))
                                ).send_keys((datetime.now() + timedelta(days=dias)).strftime('%m/%d/%Y'))
print((datetime.now() + timedelta(days=dias)).strftime('%m/%d/%Y'))
    

#Enter al botón Enviar
clickBotonEnviar(driver)

###CICLO7
ciclos = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/p[2]")
print(ciclos.text)
pregunta1 = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[1]//p")
pregunta2 = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[2]//p")
print(buscarPregunta(pregunta1.text))
print(pregunta1.text)
print(buscarPregunta(pregunta2.text))
print(pregunta2.text)
#PREGUNTA 1
operacion = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[1]/p[2]").text

if operacion[-2:] == "=?":
    print("Pregunta de suma tipo 1")
    x = eval(operacion[:-2])
    grid = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[1]/div")
    lista = grid.find_elements(By.NAME, "radio")
    print("la operación es "+ str(x))
    for elemento in lista:
        if int(elemento.get_attribute("value")) == int(x):
            elemento.click()
else: 
    print("Pregunta de suma tipo 2")
    x = eval(operacion)
    selectButton = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[1]/select")
    options = selectButton.find_elements_by_tag_name("option")
    
    print("la operación es "+ str(x))
    for option in options:
        if option.get_attribute("value") == str(x):
            option.click()

##PREGUNTA 2
operacion = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[2]/p[2]").text

if operacion[-2:] == "=?":
    print("Pregunta de suma tipo 1")
    x = eval(operacion[:-2])
    grid = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[1]/div")
    lista = grid.find_elements(By.NAME, "radio")
    print("la operación es "+ str(x))
    for elemento in lista:
        if int(elemento.get_attribute("value")) == int(x):
            elemento.click()
else: 
    print("Pregunta de suma tipo 2")
    x = eval(operacion)
    selectButton = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[2]/select")
    options = selectButton.find_elements_by_tag_name("option")
    
    print("la operación es "+ str(x))
    for option in options:
        if option.get_attribute("value") == str(x):
            option.click()
  

#Enter al botón Enviar
clickBotonEnviar(driver)

###CICLO8
ciclos = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/p[2]")
print(ciclos.text)
pregunta1 = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[1]//p")
pregunta2 = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[2]//p")
print(buscarPregunta(pregunta1.text))
print(pregunta1.text)
print(buscarPregunta(pregunta2.text))
print(pregunta2.text)
#PREGUNTA 1
grid = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[1]/div")
lista = grid.find_elements(By.NAME, "checkbox")

for elemento in lista:
    if int(elemento.get_attribute("value")) % int(pregunta1.text.split(" ")[7][:-1]) == 0:
        elemento.click()

#PREGUNTA 2
cadena = ""
for i in range(int(pregunta2.text.split(" ")[1])):
    cadena += pregunta2.text.split(" ")[5][1]
textArea = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[2]/textarea")
textArea.send_keys(cadena)
print(cadena)
    

#Enter al botón Enviar
clickBotonEnviar(driver)

###CICLO9
ciclos = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/p[2]")
print(ciclos.text)
pregunta1 = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[1]//p")
pregunta2 = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[2]//p")
print(buscarPregunta(pregunta1.text))
print(pregunta1.text)
print(buscarPregunta(pregunta2.text))
print(pregunta2.text)
#PREGUNTA 1
grid = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[1]/div")
lista = grid.find_elements(By.NAME, "checkbox")

for elemento in lista:
    if int(elemento.get_attribute("value")) % int(pregunta1.text.split(" ")[7][:-1]) == 0:
        elemento.click()

#PREGUNTA 2
operacion = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[2]/p[2]").text

if operacion[-2:] == "=?":
    print("Pregunta de suma tipo 1")
    x = eval(operacion[:-2])
    grid = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[1]/div")
    lista = grid.find_elements(By.NAME, "radio")
    print("la operación es "+ str(x))
    for elemento in lista:
        if int(elemento.get_attribute("value")) == int(x):
            elemento.click()
else: 
    print("Pregunta de suma tipo 2")
    x = eval(operacion)
    selectButton = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[2]/select")
    options = selectButton.find_elements_by_tag_name("option")
    
    print("la operación es "+ str(x))
    for option in options:
        if option.get_attribute("value") == str(x):
            option.click()
    

#Enter al botón Enviar
clickBotonEnviar(driver)

###CICLO10
ciclos = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/p[2]")
print(ciclos.text)
pregunta1 = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[1]//p")
pregunta2 = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[2]//p")
print(buscarPregunta(pregunta1.text))
print(pregunta1.text)
print(buscarPregunta(pregunta2.text))
print(pregunta2.text)
#PREGUNTA 1
operacion = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[1]/p[2]").text

if operacion[-2:] == "=?":
    print("Pregunta de suma tipo 1")
    x = eval(operacion[:-2])
    grid = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[1]/div")
    lista = grid.find_elements(By.NAME, "radio")
    print("la operación es "+ str(x))
    for elemento in lista:
        if int(elemento.get_attribute("value")) == int(x):
            elemento.click()
else: 
    print("Pregunta de suma tipo 2")
    x = eval(operacion)
    selectButton = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[1]/select")
    options = selectButton.find_elements_by_tag_name("option")
    
    print("la operación es "+ str(x))
    for option in options:
        if option.get_attribute("value") == str(x):
            option.click()

#PREGUNTA 2
animalsEmojiGroup = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[2]/div/p[2]")
inputButton = driver.find_element(By.XPATH, "/html/body/div[2]/form/div[1]/div[2]/input")
countEmojis = 0
for emojiFind in Emoji.demojize(animalsEmojiGroup.text).split(":"):
    if emojiFind == Emoji.demojize(pregunta2.text).split(":")[1]:
        countEmojis += 1
inputButton.send_keys(str(countEmojis)) 
print(countEmojis)

#Enter al botón Enviar
clickBotonEnviar(driver)

print(driver.find_element_by_xpath("/html/body/div/div/div/p").text)

time.sleep(10)

#except:
#    print("Error.")

print("Cierro el driver.")
driver.close()


