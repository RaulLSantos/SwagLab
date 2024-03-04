from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException 

class SwagLab:
    def __init__(self):
        
        # Link do site
        self.site_link = "https://www.saucedemo.com/inventory.html"

        # Biblioteca de XPATH
        self.site_maps = {
            "links":{
                "itens":{
                    "xpath":"/html/body/div/div/div/div[2]/div/div/div/div[$$item$$]/div[2]/div[2]/button",
                            #/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button
                    "cart":"/html/body/div/div/div/div[1]/div[1]/div[3]/a"
                }
                
            }
        }
        

        # Inicia o driver com opções
        opened = webdriver.ChromeOptions()

        # Permite que o navegador se mantenha aberto após executar todos os comandos
        opened.add_experimental_option("detach", True)

        # Inicia a instância do driver
        self.driver = webdriver.Chrome(options=opened)

        # Maximiza o navegador
        self.driver.maximize_window()

        
    
    def opensite(self):

        # Captura o link que informamos na variável 
        self.driver.get(self.site_link)   

       
        user = "standard_user"
        pwd = "secret_sauce"

        # Intervalo de 1 segundo. Em seguida encontra o elemento pelo ID e adiciona no campo texto o valor da variável "user"
        time.sleep(1)
        inputUser = self.driver.find_element(By.ID,"user-name")
        inputUser.send_keys(user)

        # Intervalo de 1 segundo. Em seguida encontra o elemento pelo ID e adiciona no campo texto o valor da variável "pwd"
        time.sleep(1)
        inputPwd = self.driver.find_element(By.ID,"password")
        inputPwd.send_keys(pwd)


        # Intervalo de 1 segundo. Em seguida encontra o elemento pelo ID e clica para fazer o login
        time.sleep(1)
        login = self.driver.find_element(By.ID,'login-button')
        self.driver.execute_script("arguments[0].click();", login)


    def changeitem(self):
        # Variável para a Repetição se basear. Quando o item tiver uma classe igual a informada abaixo, então irá clicar para add ao carrinho
        classe = "btn btn_primary btn_small btn_inventory "

        newitem = False

        # Variável para indicar por onde começar a adicionar os itens no carrinho
        firstItem = 1
        
        
        while not newitem:
            # Try execept para quando chegar ao final dos itens seja direcionado para o método do carrinho. Sem isso, será acusado erro
            try:
                # Busca o XPATH na biblioteca e substitui a variável $$item$$ pela variável "firstitem"
                item = self.site_maps["links"]["itens"]["xpath"].replace("$$item$$",str(firstItem))
                
                # Busca o elemento pelo XPATH da variável acima e captura o atributo "class"
                searchclass = self.driver.find_element(By.XPATH,item).get_attribute("class")
        
            except NoSuchElementException:
                self.closeshopping()
            
            # Quando encontrar a classe igual à informada na variável vai adicionar ao carrinho.
            if searchclass == classe:
                # Espera 1 segundo e clica para adicionar ao carrinho,
                time.sleep(1)
                self.driver.find_element(By.XPATH,item).click()
                firstItem += 1             
            else:
                newitem = True
                
            
        
    # Método para adicionar ao carrinho, buscando pelo XPATH na biblioteca
    def addtocart(self):
        self.opensite()
        buyitem = self.site_maps["links"]["itens"]["xpath"].replace("$$item$$",str(self.changeitem()))
        
        
    # Método para fazer o checkout no carrinho e finalizar a compra
    def closeshopping(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.site_maps["links"]["itens"]["cart"]).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div/div[2]/button[2]').click()
        

        name = "Raul"
        lastName = "Santos"
        postalCode = '00000-00'
        time.sleep(1)
        inputName = self.driver.find_element(By.ID,"first-name")
        inputName.send_keys(name)
        time.sleep(1)
        inputLastName = self.driver.find_element(By.ID,"last-name")
        inputLastName.send_keys(lastName)
        time.sleep(1)
        inputPostalCode = self.driver.find_element(By.ID,"postal-code")
        inputPostalCode.send_keys(postalCode)
        
        time.sleep(1)
        self.driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div/form/div[2]/input').click()


        time.sleep(2)
        self.driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div/div[2]/div[9]/button[2]').click()



Swag = SwagLab()
Swag.addtocart()


