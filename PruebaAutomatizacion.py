from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import time

def buscarPregunta(pregunta):
    if(pregunta == "¿Cuál de estos números es múltiplo de 5?"):
        return "Es la pregunta 1."
    elif(pregunta == "Indique cuantos 🐹 hay en la siguiente secuencia:"):
        return "Es la pregunta 2."
    elif(pregunta == "Indique la fecha que corresponde a 104 dias contados desde antes de : " + datetime.now().strftime('23/%m/%Y')):#%d
        return "Es la pregunta 3."
    else:
        return"No se encontró."
    
def resolverPreguntaUno(pregunta):
    return null

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


#ciclos =  driver.find_element(By.CLASS_NAME, "text-xl text-center text-green-500")
ciclos = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/p[2]")
print(ciclos.text)

pregunta1 = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[1]//p")
pregunta2 = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[2]//p")

print(buscarPregunta(pregunta1.text))
print(buscarPregunta(pregunta2.text))


grid = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[1]/div")
lista = grid.find_elements(By.NAME, "checkbox")

for elemento in lista:
    if int(elemento.get_attribute("value")) % 5 == 0:
        elemento.click()

print("Dio los clicks.")

animalsEmojiGroup = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[2]/div/p[2]")
#print(str(len(animalsEmojiGroup.text)))
#inputButton = driver.find_element(By.CLASS_NAME, "border-2 border-black rounded-sm p-2")
inputButton = driver.find_element(By.XPATH, "/html/body/div[2]/form/div[1]/div[2]/input")
countEmojis = 0
for emoji in animalsEmojiGroup.text:
    if emoji == "🐹":
        countEmojis += 1
inputButton.send_keys(str(countEmojis)) 
inputButton.send_keys(Keys.ENTER)


###CICLO2
ciclos = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/p[2]")
print(ciclos.text)
pregunta1 = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[1]//p")
pregunta2 = driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[2]//p")
#/html/body/div[2]/form/div[1]/div[2]/p
#/html/body/div[2]/form/div[1]/div[2]/p
print(buscarPregunta(pregunta1.text))
print(buscarPregunta(pregunta2.text))
print(pregunta2.text)




time.sleep(20)

#except:
#    print("Error.")

print("Cierro el driver.")
driver.close()


