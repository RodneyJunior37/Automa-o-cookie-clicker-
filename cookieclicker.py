from selenium import webdriver
import time

class CookieClicker:
    def __init__(self) -> None:
        self.link = "https://orteil.dashnet.org/cookieclicker/"
        self.map = {
            "buttons":{
                "lingua": {
                    "xpath" : "/html/body/div[2]/div[2]/div[12]/div/div[1]/div[1]/div[10]"
                },
                "bisc": {
                    "xpath":"/html/body/div[2]/div[2]/div[15]/div[8]/button"
               }, 
               "upgrade": {
                    "xpath":"/html/body/div[2]/div[2]/div[19]/div[3]/div[6]/div[3]"
               },
               "upgrade2": {
                    "xpath":"/html/body/div[2]/div[2]/div[19]/div[3]/div[6]/div[2]" 
                }
            }
        }
        
        

        self.driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
        self.driver.maximize_window()
    def abrir_site(self):
        time.sleep(2)
        self.driver.get(self.link)
        time.sleep(5)
    def selecionar_linguagem(self):
        self.driver.find_element("xpath", self.map["buttons"]['lingua']["xpath"]).click()
        time.sleep(8)
    def clicar_biscoito(self):
        self.driver.find_element("xpath", self.map["buttons"]['bisc']["xpath"]).click()
    '''def melhor_upgrade(self):
        encontrei = False
        elemento_atual = 2

        while not encontrei:
            object = self.map["buttons"]['upgrade']["xpath"].replace("$$NUMBER$$",str(elemento_atual))
            classe_objeto = self.driver.find_element("xpath",object).get_attribute("class")

            if not "enable" in classe_objeto:
                encontrei = True
            else:
                elemento_atual += 1
        return elemento_atual - 1'''
    def comprar(self):
        self.driver.find_element("xpath", self.map["buttons"]['upgrade']["xpath"]).click()
        self.driver.find_element("xpath", self.map["buttons"]['upgrade2']["xpath"]).click()
        '''object = self.map["buttons"]['upgrade']["xpath"].replace("$$NUMBER$$",str(self.melhor_upgrade()))
        self.driver.find_element("xpath",object).click()'''

biscoito = CookieClicker()
biscoito.abrir_site()
biscoito.selecionar_linguagem()
i = 0 
while True:
    if i % 500 == 0 and i != 0:
        time.sleep(1)
        biscoito.comprar()
        time.sleep(1)
    biscoito.clicar_biscoito()
    i += 1
