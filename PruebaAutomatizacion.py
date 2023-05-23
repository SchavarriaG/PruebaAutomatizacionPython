from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path=r"C:\RepositorioPruebas\PythonSelenium\chromedriver\chromedriver.exe")
driver.get("https://tasks.evalartapp.com/automatization/")

#Iniciar Sesión
try:
    username = driver.find_element_by_xpath("/html/body/div/div[2]/form/input[1]")
    username.send_keys("611091")
    password = driver.find_element_by_xpath("/html/body/div/div[2]/form/input[2]")
    password.send_keys("10df2f32286b7120MS00LTE5MDExNg==30e0c83e6c29f1c3")
    password.send_keys(Keys.ENTER)


    #ciclos =  driver.find_element(By.CLASS_NAME, "text-xl text-center text-green-500")
    ciclos = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/p[2]")
    print(ciclos.get_attribute("outerHTML"))
except:
    print("Error.")

print("Cierro el driver.")
driver.close()
