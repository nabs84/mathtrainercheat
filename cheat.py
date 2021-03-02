from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from random import randint


#lancer le site
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("https://www.mathtrainer.org/")
sleep(1)


#se connecter
login = driver.find_element_by_class_name("signin-btn").click() # cliquer sur login
sleep(1)
driver.find_elements_by_class_name("firebaseui-idp-button")[3].click() # cliquer sur email
sleep(1.5)
driver.find_element_by_class_name("mdl-textfield__input").send_keys("xopoi@yopmail.com", Keys.ENTER) # entrer son email
sleep(1)
driver.find_elements_by_class_name("mdl-textfield__input")[1].send_keys("xopoi12345", Keys.ENTER) # entrer son mdp
sleep(2)


#lancer la 1ere partie
train = driver.find_element_by_class_name("start-wrapper")
train.click()
first = False

#Lancer x parties :D

while first != True:
    for i in range(30):
        try:
            sleep(1)
            a = int(driver.find_element_by_class_name("a").text.replace(" ", ""))
            b = int(driver.find_element_by_class_name("b").text.replace(" ", "")) #récuperer les valeurs A et B
            operator = driver.find_element_by_class_name("operator").text # récuperer l'opperateur

            if operator == '+':
                resultat = a + b
            elif operator == '−':
                resultat = a - b
            elif operator == '×':
                resultat = a * b
            else:
                resultat = int(float(a) / float(b)) # faire le calcule
            
            driver.find_element_by_tag_name('body').send_keys(resultat) # envoyer le resultat
        except:
            try:
                sleep(1)
                train = driver.find_element_by_class_name("start-wrapper").click() # lancer une game
            except:
                pass
