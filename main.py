import requests
from bs4 import BeautifulSoup
import smtplib
from threading import Thread
from time import sleep
import time
import tweepy




headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}









auth = tweepy.OAuthHandler('B4crkoej1UCWysTkTUTg9sDep', 'R0ROCnKEtJM0THMZ44PHQWEwYmKC0jXjJCZpreBc3qIYtrAZrO')
auth.set_access_token('846334865226248192-LjnuWowOL9OVokcsI22rcHwBGC8STuZ','73eKPiyXB4AhF6WUhd67PAI00J6xVPp49a4LnLdP8lBjl')


api = tweepy.API(auth)




try:
    api.verify_credentials()
    print("Autenticação aceita")
except:
    print("Um erro ocorreu durante a autenticação.")







#CPU

def KabumR51600AF():
    while True:
        try:
    

            kabum_R51600AF = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=107545'
            page_kabum_R51600AF = requests.get(kabum_R51600AF, headers=headers)
            soup_kabum_R51600AF = BeautifulSoup(page_kabum_R51600AF.content,'html.parser')
       
            try:
                status_kabum_R51600AF = soup_kabum_R51600AF.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
            except:
                status_kabum_R51600AF = soup_kabum_R51600AF.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")


        except:
            kabum_R51600AF = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=107545'
            page_kabum_R51600AF = requests.get(kabum_R51600AF, headers=headers)
            soup_kabum_R51600AF = BeautifulSoup(page_kabum_R51600AF.content,'html.parser')
            print('a')

        
           
            
       
            price_kabum_R51600AF = soup_kabum_R51600AF.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()
            status_kabum_R51600AF = 'PROMOÇÃO'
        
            oldPrice_kabum_R51600AF = soup_kabum_R51600AF.find('div', class_='preco_antigo-cm').get_text()
            newPrice_kabum_R51600AF = soup_kabum_R51600AF.find('div', class_='preco_desconto-cm').find('strong').get_text()
            kabum_R51600AF_Promocao = api.update_status('''
            
PROMOÇÃO:

R5 1600(AF)

''' + oldPrice_kabum_R51600AF + '''
''' + newPrice_kabum_R51600AF + '''


Preço: R$''' + price_kabum_R51600AF + '''
Á vista no boleto bancário com 15% de desconto



''' + kabum_R51600AF + '''
                                            ''')

            

            
            break
            while True:
                time.sleep(1)
                try:
    
                    kabum_R51600AF = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=107545'
                    page_kabum_R51600AF = requests.get(kabum_R51600AF, headers=headers)
                    soup_kabum_R51600AF = BeautifulSoup(page_kabum_R51600AF.content,'html.parser')

                    price_kabum_R51600AF = soup_kabum_R51600AF.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()
                except:
                    
                    kabum_R51600AF = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=107545'
                    page_kabum_R51600AF = requests.get(kabum_R51600AF, headers=headers)
                    soup_kabum_R51600AF = BeautifulSoup(page_kabum_R51600AF.content,'html.parser')

                    api.destroy_status(kabum_R51600AF_Promocao)
                    return KabumR51600AF()
                    


def KabumR32200G():
    
  
    while True:
        time.sleep(2) 


        try:
    

            kabum_R32200G = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=94723'
            page_kabum_R32200G = requests.get(kabum_R32200G, headers=headers)
            soup_kabum_R32200G = BeautifulSoup(page_kabum_R32200G.content,'html.parser')

            try:
                status_kabum_R32200G = soup_kabum_R32200G.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
            except:
                status_kabum_R32200G = soup_kabum_R32200G.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")

        except:
            kabum_R32200G = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=94723'
            page_kabum_R32200G = requests.get(kabum_R32200G, headers=headers)
            soup_kabum_R32200G = BeautifulSoup(page_kabum_R32200G.content,'html.parser')
    

        
            price_kabum_R32200G = soup_kabum_R32200G.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

    
        


        
            status_kabum_R32200G = 'PROMOÇÃO'
    
            oldPrice_kabum_R32200G = soup_kabum_R32200G.find('div', class_='preco_antigo-cm').get_text()
            newPrice_kabum_R32200G = soup_kabum_R32200G.find('div', class_='preco_desconto-cm').find('strong').get_text()
   
    
       
        
            kabum_R32200G_Promocao = api.update_status('''
            
PROMOÇÃO:

R3 2200G

''' + oldPrice_kabum_R32200G + '''
''' + newPrice_kabum_R32200G + '''


Preço: R$''' + price_kabum_R32200G + '''
Á vista no boleto bancário com 15% de desconto



''' + kabum_R32200G + '''
                                            ''')

            

            
            break
            while True:
                time.sleep(2)
                try:
    
                    kabum_R32200G = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=94723'
                    page_kabum_R32200G = requests.get(kabum_R32200G, headers=headers)
                    soup_kabum_R32200G = BeautifulSoup(page_kabum_R32200G.content,'html.parser')

                    price_kabum_R32200G = soup_kabum_R32200G.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()
                    
                except:
                    kabum_R32200G = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=94723'
          
                    api.destroy_status(kabum_R32200G_Promocao)
                    return KabumR32200G()















def KabumR52600():
    
    
    while True:
        time.sleep(3)
        try:
    

            kabum_R52600 = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=95557'
            page_kabum_R52600 = requests.get(kabum_R52600, headers=headers)
            soup_kabum_R52600 = BeautifulSoup(page_kabum_R52600.content,'html.parser')

            try:
                status_kabum_R52600 = soup_kabum_R52600.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
            except:
                status_kabum_R52600 = soup_kabum_R52600.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")

        except:
            kabum_R52600 = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=95557'
            page_kabum_R52600 = requests.get(kabum_R52600, headers=headers)
            soup_kabum_R52600 = BeautifulSoup(page_kabum_R52600.content,'html.parser')
    

        
            price_kabum_R52600 = soup_kabum_R52600.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

    
        


        
            status_kabum_R52600 = 'PROMOÇÃO'
    
            oldPrice_kabum_R52600 = soup_kabum_R52600.find('div', class_='preco_antigo-cm').get_text()
            newPrice_kabum_R52600 = soup_kabum_R52600.find('div', class_='preco_desconto-cm').find('strong').get_text()
   
        
            kabum_R52600_Promocao = api.update_status('''
            
PROMOÇÃO:

R5 2600

''' + oldPrice_kabum_R52600 + '''
''' + newPrice_kabum_R52600 + '''


Preço: R$''' + price_kabum_R52600 + '''
Á vista no boleto bancário com 15% de desconto



''' + kabum_R52600 + '''
                                            ''')

            

            
            break
            while True:
                time.sleep(3)
                try:
    
                    kabum_R52600 = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=94723'
                    page_kabum_R52600 = requests.get(kabum_R52600, headers=headers)
                    soup_kabum_R52600 = BeautifulSoup(page_kabum_R52600.content,'html.parser')

                    price_kabum_R52600 = soup_kabum_R52600.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

                

                    
                except:
                    kabum_R52600 = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=94723'
          
                    api.destroy_status(kabum_R52600_Promocao)
                    return KabumR52600()


            
def KabumR53600():
    
    while True:
        time.sleep(4)
        try:
    

            kabum_R53600 = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=102438'
            page_kabum_R53600 = requests.get(kabum_R53600, headers=headers)
            soup_kabum_R53600 = BeautifulSoup(page_kabum_R53600.content,'html.parser')

            try:
                status_kabum_R53600 = soup_kabum_R53600.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
            except:
                status_kabum_R53600 = soup_kabum_R53600.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")

        except:
            kabum_R53600 = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=102438'
            page_kabum_R53600 = requests.get(kabum_R53600, headers=headers)
            soup_kabum_R53600 = BeautifulSoup(page_kabum_R53600.content,'html.parser')
    

        
            price_kabum_R53600 = soup_kabum_R53600.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

    
        


        
            status_kabum_R53600 = 'PROMOÇÃO'
    
            oldPrice_kabum_R53600 = soup_kabum_R53600.find('div', class_='preco_antigo-cm').get_text()
            newPrice_kabum_R53600 = soup_kabum_R53600.find('div', class_='preco_desconto-cm').find('strong').get_text()
   
        
            kabum_R53600_Promocao = api.update_status('''
            
PROMOÇÃO:

R5 3600

''' + oldPrice_kabum_R53600 + '''
''' + newPrice_kabum_R53600 + '''


Preço: R$''' + price_kabum_R53600 + '''
Á vista no boleto bancário com 15% de desconto



''' + kabum_R53600 + '''
                                            ''')

            

            
            break
            while True:
                time.sleep(4)
                try:
    
                    kabum_R53600 = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=102438'
                    page_kabum_R53600 = requests.get(kabum_R53600, headers=headers)
                    soup_kabum_R53600 = BeautifulSoup(page_kabum_R53600.content,'html.parser')

                    price_kabum_R53600 = soup_kabum_R53600.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()
                    
                except:
                    kabum_R53600 = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=102438'
         
                    api.destroy_status(kabum_R53600_Promocao)
                    return KabumR53600()




                
def KabumR73700X():
    
    while True:
        time.sleep(5)

        try:
    

            kabum_R73700X = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=102436'
            page_kabum_R73700X = requests.get(kabum_R73700X, headers=headers)
            soup_kabum_R73700X = BeautifulSoup(page_kabum_R73700X.content,'html.parser')

            try:
                status_kabum_R73700X = soup_kabum_R73700X.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
            except:
                status_kabum_R73700X = soup_kabum_R73700X.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")

        except:
            kabum_R73700X = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=102436'
            page_kabum_R73700X = requests.get(kabum_R73700X, headers=headers)
            soup_kabum_R73700X = BeautifulSoup(page_kabum_R73700X.content,'html.parser')
    

        
            price_kabum_R73700X = soup_kabum_R73700X.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

    
        


        
            status_kabum_R73700X = 'PROMOÇÃO'
    
            oldPrice_kabum_R73700X = soup_kabum_R73700X.find('div', class_='preco_antigo-cm').get_text()
            newPrice_kabum_R73700X = soup_kabum_R73700X.find('div', class_='preco_desconto-cm').find('strong').get_text()
   
        
            kabum_R73700X_Promocao = api.update_status('''
            
PROMOÇÃO:

R7 3700X

''' + oldPrice_kabum_R73700X + '''
''' + newPrice_kabum_R73700X + '''


Preço: R$''' + price_kabum_R73700X + '''
Á vista no boleto bancário com 15% de desconto



''' + kabum_R73700X + '''
                                            ''')

            

            
            break
            while True:
                time.sleep(5)
                try:
    
                    kabum_R73700X = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=102436'
                    page_kabum_R73700X = requests.get(kabum_R73700X, headers=headers)
                    soup_kabum_R73700X = BeautifulSoup(page_kabum_R73700X.content,'html.parser')

                    price_kabum_R73700X = soup_kabum_R73700X.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

                except:
                    kabum_R73700X = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=102436'
         
                    api.destroy_status(kabum_R73700X_Promocao)
                    return KabumR73700X()




















def KabumR73800X():
    
    while True:
        time.sleep(6)
        try:
    

            kabum_R73800X = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=102435'
            page_kabum_R73800X = requests.get(kabum_R73800X, headers=headers)
            soup_kabum_R73800X = BeautifulSoup(page_kabum_R73800X.content,'html.parser')

            try:
                status_kabum_R73800X = soup_kabum_R73800X.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
            except:
                status_kabum_R73800X = soup_kabum_R73800X.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")

        except:
            kabum_R73800X = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=102435'
            page_kabum_R73800X = requests.get(kabum_R73800X, headers=headers)
            soup_kabum_R73800X = BeautifulSoup(page_kabum_R73800X.content,'html.parser')
    

        
            price_kabum_R73800X = soup_kabum_R73800X.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

    
        


        
            status_kabum_R73800X = 'PROMOÇÃO'
    
            oldPrice_kabum_R73800X = soup_kabum_R73800X.find('div', class_='preco_antigo-cm').get_text()
            newPrice_kabum_R73800X = soup_kabum_R73800X.find('div', class_='preco_desconto-cm').find('strong').get_text()
   
        
            kabum_R73800X_Promocao = api.update_status('''
            
PROMOÇÃO:

R7 3800X

''' + oldPrice_kabum_R73800X + '''
''' + newPrice_kabum_R73800X + '''


Preço: R$''' + price_kabum_R73800X + '''
Á vista no boleto bancário com 15% de desconto



''' + kabum_R73800X + '''
                                            ''')

            

            
            break
            while True:
                time.sleep(6)
                try:
    
                    kabum_R73800X = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=102435'
                    page_kabum_R73800X = requests.get(kabum_R73800X, headers=headers)
                    soup_kabum_R73800X = BeautifulSoup(page_kabum_R73800X.content,'html.parser')
                    price_kabum_R73800X = soup_kabum_R73800X.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

                        
                except:
                    kabum_R73800X = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=102435'
         
                    api.destroy_status(kabum_R73800X_Promocao)
                    return KabumR73800X()












                


def KabumR93900X():
    
    while True:
        time.sleep(7)

        try:
    

            kabum_R93900X = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=102434'
            page_kabum_R93900X = requests.get(kabum_R93900X, headers=headers)
            soup_kabum_R93900X = BeautifulSoup(page_kabum_R93900X.content,'html.parser')

            try:
                status_kabum_R93900X = soup_kabum_R93900X.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
            except:
                status_kabum_R93900X = soup_kabum_R93900X.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")

        except:
            kabum_R93900X = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=102434'
            page_kabum_R93900X = requests.get(kabum_R93900X, headers=headers)
            soup_kabum_R93900X = BeautifulSoup(page_kabum_R93900X.content,'html.parser')
    

        
            price_kabum_R93900X = soup_kabum_R93900X.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

    
        


        
            status_kabum_R93900X = 'PROMOÇÃO'
    
            oldPrice_kabum_R93900X = soup_kabum_R93900X.find('div', class_='preco_antigo-cm').get_text()
            newPrice_kabum_R93900X = soup_kabum_R93900X.find('div', class_='preco_desconto-cm').find('strong').get_text()
   
        
            kabum_R93900X_Promocao = api.update_status('''
            
PROMOÇÃO:

R9 3900X

''' + oldPrice_kabum_R93900X + '''
''' + newPrice_kabum_R93900X + '''


Preço: R$''' + price_kabum_R93900X + '''
Á vista no boleto bancário com 15% de desconto



''' + kabum_R93900X + '''
                                            ''')

            

            
            break
            while True:
                time.sleep(7)
                try:
                    kabum_R93900X = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=102434'
                    page_kabum_R93900X = requests.get(kabum_R93900X, headers=headers)
                    soup_kabum_R93900X = BeautifulSoup(page_kabum_R93900X.content,'html.parser')
                    price_kabum_R93900X = soup_kabum_R93900X.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()


                except:
                    kabum_R93900X = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=102434'
         
                    api.destroy_status(kabum_R93900X_Promocao)
                    return KabumR93900X()

















        
def KabumR33300X():
    
    while True:
        time.sleep(8)
        try:
    

            kabum_R33300X = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=113391'
            page_kabum_R33300X = requests.get(kabum_R33300X, headers=headers)
            soup_kabum_R33300X = BeautifulSoup(page_kabum_R33300X.content,'html.parser')

            try:
                status_kabum_R33300X = soup_kabum_R33300X.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
            except:
                status_kabum_R33300X = soup_kabum_R33300X.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")

        except:
            kabum_R33300X = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=113391'
            page_kabum_R33300X = requests.get(kabum_R33300X, headers=headers)
            soup_kabum_R33300X = BeautifulSoup(page_kabum_R33300X.content,'html.parser')
    

        
            price_kabum_R33300X = soup_kabum_R33300X.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

    
        


        
            status_kabum_R33300X = 'PROMOÇÃO'
    
            oldPrice_kabum_R33300X = soup_kabum_R33300X.find('div', class_='preco_antigo-cm').get_text()
            newPrice_kabum_R33300X = soup_kabum_R33300X.find('div', class_='preco_desconto-cm').find('strong').get_text()
   
        
            kabum_R33300X_Promocao = api.update_status('''
            
PROMOÇÃO:

R3 3300X

''' + oldPrice_kabum_R33300X + '''
''' + newPrice_kabum_R33300X + '''


Preço: R$''' + price_kabum_R33300X + '''
Á vista no boleto bancário com 15% de desconto



''' + kabum_R33300X + '''
                                            ''')

            

            
            break
            while True:
                time.sleep(8)
                try:
    

                    kabum_R33300X = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=113391'
                    page_kabum_R33300X = requests.get(kabum_R33300X, headers=headers)
                    soup_kabum_R33300X = BeautifulSoup(page_kabum_R33300X.content,'html.parser')
                    price_kabum_R33300X = soup_kabum_R33300X.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()


                except:
                    kabum_R33300X = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=113391'
         
                    api.destroy_status(kabum_R33300X_Promocao)
                    return KabumR33300X()
















                
def KabumR53600X():
    
    while True:
        time.sleep(9)
        try:
    

            kabum_R53600X = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=102437'
            page_kabum_R53600X = requests.get(kabum_R53600X, headers=headers)
            soup_kabum_R53600X = BeautifulSoup(page_kabum_R53600X.content,'html.parser')

            try:
                status_kabum_R53600X = soup_kabum_R53600X.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
            except:
                status_kabum_R53600X = soup_kabum_R53600X.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")

        except:
            kabum_R53600X = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=102437'
            page_kabum_R53600X = requests.get(kabum_R53600X, headers=headers)
            soup_kabum_R53600X = BeautifulSoup(page_kabum_R53600X.content,'html.parser')
    

        
            price_kabum_R53600X = soup_kabum_R53600X.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

    
        


        
            status_kabum_R53600X = 'PROMOÇÃO'
    
            oldPrice_kabum_R53600X = soup_kabum_R53600X.find('div', class_='preco_antigo-cm').get_text()
            newPrice_kabum_R53600X = soup_kabum_R53600X.find('div', class_='preco_desconto-cm').find('strong').get_text()
   
        
            kabum_R53600X_Promocao = api.update_status('''
            
PROMOÇÃO:

R5 3600X

''' + oldPrice_kabum_R53600X + '''
''' + newPrice_kabum_R53600X + '''


Preço: R$''' + price_kabum_R53600X + '''
Á vista no boleto bancário com 15% de desconto



''' + kabum_R53600X + '''
                                            ''')

            

            
            break
            while True:
                time.sleep(9)
                try:
    

                    kabum_R53600X = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=102437'
                    page_kabum_R53600X = requests.get(kabum_R53600X, headers=headers)
                    soup_kabum_R53600X = BeautifulSoup(page_kabum_R53600X.content,'html.parser')
                    price_kabum_R53600X = soup_kabum_R53600X.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

                except:
                    kabum_R53600X = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=102437'
         
                    api.destroy_status(kabum_R53600X_Promocao)
                    return KabumR53600X()

def KabumRx5704gb_PhantomGaming():
    
    while True:
        time.sleep(10)
        try:
    

            kabum_Rx5704gb_PhantomGaming = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=102833'
            page_kabum_Rx5704gb_PhantomGaming = requests.get(kabum_Rx5704gb_PhantomGaming, headers=headers)
            soup_kabum_Rx5704gb_PhantomGaming = BeautifulSoup(page_kabum_Rx5704gb_PhantomGaming.content,'html.parser')

            try:
                status_kabum_Rx5704gb_PhantomGaming = soup_kabum_Rx5704gb_PhantomGaming.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
            except:
                status_kabum_Rx5704gb_PhantomGaming = soup_kabum_Rx5704gb_PhantomGaming.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")

        except:
            kabum_Rx5704gb_PhantomGaming = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=102833'



            page_kabum_Rx5704gb_PhantomGaming = requests.get(kabum_Rx5704gb_PhantomGaming, headers=headers)
            soup_kabum_Rx5704gb_PhantomGaming = BeautifulSoup(page_kabum_Rx5704gb_PhantomGaming.content,'html.parser')
    

        
            price_kabum_Rx5704gb_PhantomGaming = soup_kabum_Rx5704gb_PhantomGaming.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

    
        


        
            status_kabum_Rx5704gb_PhantomGaming = 'PROMOÇÃO'
    
            oldPrice_kabum_Rx5704gb_PhantomGaming = soup_kabum_Rx5704gb_PhantomGaming.find('div', class_='preco_antigo-cm').get_text()
            newPrice_kabum_Rx5704gb_PhantomGaming = soup_kabum_Rx5704gb_PhantomGaming.find('div', class_='preco_desconto-cm').find('strong').get_text()
   
        
            kabum_Rx5704gb_PhantomGaming_Promocao = api.update_status('''
            
PROMOÇÃO:

Rx570 4gb (PhantomGaming - Asrock)

''' + oldPrice_kabum_Rx5704gb_PhantomGaming + '''
''' + newPrice_kabum_Rx5704gb_PhantomGaming + '''


Preço: R$''' + price_kabum_Rx5704gb_PhantomGaming + '''
Á vista no boleto bancário com 15% de desconto



''' + kabum_Rx5704gb_PhantomGaming + '''
                                            ''')

            

            
            break
            while True:
                time.sleep(10)
                try:
    

                    kabum_Rx5704gb_PhantomGaming = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=102833'
                    page_kabum_Rx5704gb_PhantomGaming = requests.get(kabum_Rx5704gb_PhantomGaming, headers=headers)
                    soup_kabum_Rx5704gb_PhantomGaming = BeautifulSoup(page_kabum_Rx5704gb_PhantomGaming.content,'html.parser')
                    price_kabum_Rx5704gb_PhantomGaming = soup_kabum_Rx5704gb_PhantomGaming.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

                except:
                    kabum_Rx5704gb_PhantomGaming = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=102833'
         
                    api.destroy_status(kabum_Rx5704gb_PhantomGaming_Promocao)
                    return KabumRx5704gb_PhantomGaming()














def KabumRx5704gb_Gaming4G():
    
    while True:
        time.sleep(11)
        try:
    

            kabum_Rx5704gb_Gaming4G = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=88748'
            page_kabum_Rx5704gb_Gaming4G = requests.get(kabum_Rx5704gb_Gaming4G, headers=headers)
            soup_kabum_Rx5704gb_Gaming4G = BeautifulSoup(page_kabum_Rx5704gb_Gaming4G.content,'html.parser')

            try:
                status_kabum_Rx5704gb_Gaming4G = soup_kabum_Rx5704gb_Gaming4G.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
            except:
                status_kabum_Rx5704gb_Gaming4G = soup_kabum_Rx5704gb_Gaming4G.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")

        except:
            kabum_Rx5704gb_Gaming4G = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=88748'


            page_kabum_Rx5704gb_Gaming4G = requests.get(kabum_Rx5704gb_Gaming4G, headers=headers)
            soup_kabum_Rx5704gb_Gaming4G = BeautifulSoup(page_kabum_Rx5704gb_Gaming4G.content,'html.parser')
    

        
            price_kabum_Rx5704gb_Gaming4G = soup_kabum_Rx5704gb_Gaming4G.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

    
        


        
            status_kabum_Rx5704gb_Gaming4G = 'PROMOÇÃO'
    
            oldPrice_kabum_Rx5704gb_Gaming4G = soup_kabum_Rx5704gb_Gaming4G.find('div', class_='preco_antigo-cm').get_text()
            newPrice_kabum_Rx5704gb_Gaming4G = soup_kabum_Rx5704gb_Gaming4G.find('div', class_='preco_desconto-cm').find('strong').get_text()
   
        
            kabum_Rx5704gb_Gaming4G_Promocao = api.update_status('''
            
PROMOÇÃO:

Rx570 4gb (Gaming4G - Gigabyte)

''' + oldPrice_kabum_Rx5704gb_Gaming4G + '''
''' + newPrice_kabum_Rx5704gb_Gaming4G + '''


Preço: R$''' + price_kabum_Rx5704gb_Gaming4G + '''
Á vista no boleto bancário com 15% de desconto



''' + kabum_Rx5704gb_Gaming4G + '''
                                            ''')

            

            
            break
            while True:
                time.sleep(11)
                try:
    

                    kabum_Rx5704gb_Gaming4G = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=88748'
                    page_kabum_Rx5704gb_Gaming4G = requests.get(kabum_Rx5704gb_Gaming4G, headers=headers)
                    soup_kabum_Rx5704gb_Gaming4G = BeautifulSoup(page_kabum_Rx5704gb_Gaming4G.content,'html.parser')
                    price_kabum_Rx5704gb_Gaming4G = soup_kabum_Rx5704gb_Gaming4G.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

                except:
                    kabum_Rx5704gb_Gaming4G = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=88748'
         
                    api.destroy_status(kabum_Rx5704gb_Gaming4G_Promocao)
                    return KabumRx5704gb_Gaming4G()










def KabumRx5808gb_ArezDual():
    
    while True:
        time.sleep(12)
        try:
    

            kabum_Rx5808gb_ArezDual = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=110342'
            page_kabum_Rx5808gb_ArezDual = requests.get(kabum_Rx5808gb_ArezDual, headers=headers)
            soup_kabum_Rx5808gb_ArezDual = BeautifulSoup(page_kabum_Rx5808gb_ArezDual.content,'html.parser')

            try:
                status_kabum_Rx5808gb_ArezDual = soup_kabum_Rx5808gb_ArezDual.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
            except:
                status_kabum_Rx5808gb_ArezDual = soup_kabum_Rx5808gb_ArezDual.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")

        except:
            kabum_Rx5808gb_ArezDual = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=110342'


            page_kabum_Rx5808gb_ArezDual = requests.get(kabum_Rx5808gb_ArezDual, headers=headers)
            soup_kabum_Rx5808gb_ArezDual = BeautifulSoup(page_kabum_Rx5808gb_ArezDual.content,'html.parser')
    

        
            price_kabum_Rx5808gb_ArezDual = soup_kabum_Rx5808gb_ArezDual.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

    
        


        
            status_kabum_Rx5808gb_ArezDual = 'PROMOÇÃO'
    
            oldPrice_kabum_Rx5808gb_ArezDual = soup_kabum_Rx5808gb_ArezDual.find('div', class_='preco_antigo-cm').get_text()
            newPrice_kabum_Rx5808gb_ArezDual = soup_kabum_Rx5808gb_ArezDual.find('div', class_='preco_desconto-cm').find('strong').get_text()
   
        
            kabum_Rx5808gb_ArezDual_Promocao = api.update_status('''
            
PROMOÇÃO:

Rx580 8gb (Arez Dual - Asus)

''' + oldPrice_kabum_Rx5808gb_ArezDual + '''
''' + newPrice_kabum_Rx5808gb_ArezDual + '''


Preço: R$''' + price_kabum_Rx5808gb_ArezDual + '''
Á vista no boleto bancário com 15% de desconto



''' + kabum_Rx5808gb_ArezDual + '''
                                            ''')

            

            
            break
            while True:
                time.sleep(12)
                try:
    

                    kabum_Rx5808gb_ArezDual = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=110342'
                    page_kabum_Rx5808gb_ArezDual = requests.get(kabum_Rx5808gb_ArezDual, headers=headers)
                    soup_kabum_Rx5808gb_ArezDual = BeautifulSoup(page_kabum_Rx5808gb_ArezDual.content,'html.parser')
                    price_kabum_Rx5808gb_ArezDual = soup_kabum_Rx5808gb_ArezDual.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

                except:
                    kabum_Rx5808gb_ArezDual = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=110342'
         
                    api.destroy_status(kabum_Rx5808gb_ArezDual_Promocao)
                    return KabumRx5808gb_ArezDual()















                
def KabumRx5704gb_XFXRSXXX():
    
    while True:
        time.sleep(13)
        try:
    

            kabum_Rx5704gb_XFXRSXXX = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=93572'
            page_kabum_Rx5704gb_XFXRSXXX = requests.get(kabum_Rx5704gb_XFXRSXXX, headers=headers)
            soup_kabum_Rx5704gb_XFXRSXXX = BeautifulSoup(page_kabum_Rx5704gb_XFXRSXXX.content,'html.parser')

            try:
                status_kabum_Rx5704gb_XFXRSXXX = soup_kabum_Rx5704gb_XFXRSXXX.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
            except:
                status_kabum_Rx5704gb_XFXRSXXX = soup_kabum_Rx5704gb_XFXRSXXX.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")

        except:
            kabum_Rx5704gb_XFXRSXXX = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=93572'

            page_kabum_Rx5704gb_XFXRSXXX = requests.get(kabum_Rx5704gb_XFXRSXXX, headers=headers)
            soup_kabum_Rx5704gb_XFXRSXXX = BeautifulSoup(page_kabum_Rx5704gb_XFXRSXXX.content,'html.parser')
    

        
            price_kabum_Rx5704gb_XFXRSXXX = soup_kabum_Rx5704gb_XFXRSXXX.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

    
        


        
            status_kabum_Rx5704gb_XFXRSXXX = 'PROMOÇÃO'
    
            oldPrice_kabum_Rx5704gb_XFXRSXXX = soup_kabum_Rx5704gb_XFXRSXXX.find('div', class_='preco_antigo-cm').get_text()
            newPrice_kabum_Rx5704gb_XFXRSXXX = soup_kabum_Rx5704gb_XFXRSXXX.find('div', class_='preco_desconto-cm').find('strong').get_text()
   
        
            kabum_Rx5704gb_XFXRSXXX_Promocao = api.update_status('''
            
PROMOÇÃO:

Rx570 4gb (RS XXX - XFX)

''' + oldPrice_kabum_Rx5704gb_XFXRSXXX + '''
''' + newPrice_kabum_Rx5704gb_XFXRSXXX + '''


Preço: R$''' + price_kabum_Rx5704gb_XFXRSXXX + '''
Á vista no boleto bancário com 15% de desconto



''' + kabum_Rx5704gb_XFXRSXXX + '''
                                            ''')

            

            
            break
            while True:
                time.sleep(13)
                try:
    

                    kabum_Rx5704gb_XFXRSXXX = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=93572'
                    page_kabum_Rx5704gb_XFXRSXXX = requests.get(kabum_Rx5704gb_XFXRSXXX, headers=headers)
                    soup_kabum_Rx5704gb_XFXRSXXX = BeautifulSoup(page_kabum_Rx5704gb_XFXRSXXX.content,'html.parser')
                    price_kabum_Rx5704gb_XFXRSXXX = soup_kabum_Rx5704gb_XFXRSXXX.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

                except:
                    kabum_Rx5704gb_XFXRSXXX = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=93572'
         
                    api.destroy_status(kabum_Rx5704gb_XFXRSXXX_Promocao)
                    return KabumRx5704gb_XFXRSXXX()










def KabumRx5500XT4gb_GamingOC():
    
    while True:
        time.sleep(14)
        try:
    

            kabum_Rx5500XT4gb_GamingOC = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=109644'
            page_kabum_Rx5500XT4gb_GamingOC = requests.get(kabum_Rx5500XT4gb_GamingOC, headers=headers)
            soup_kabum_Rx5500XT4gb_GamingOC = BeautifulSoup(page_kabum_Rx5500XT4gb_GamingOC.content,'html.parser')

            try:
                status_kabum_Rx5500XT4gb_GamingOC = soup_kabum_Rx5500XT4gb_GamingOC.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
            except:
                status_kabum_Rx5500XT4gb_GamingOC = soup_kabum_Rx5500XT4gb_GamingOC.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")

        except:
            kabum_Rx5500XT4gb_GamingOC = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=109644'

            page_kabum_Rx5500XT4gb_GamingOC = requests.get(kabum_Rx5500XT4gb_GamingOC, headers=headers)
            soup_kabum_Rx5500XT4gb_GamingOC = BeautifulSoup(page_kabum_Rx5704gb_XFXRSXXX.content,'html.parser')
    

        
            price_kabum_Rx5500XT4gb_GamingOC = soup_kabum_Rx5500XT4gb_GamingOC.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

    
        


        
            status_kabum_Rx5500XT4gb_GamingOC = 'PROMOÇÃO'
    
            oldPrice_kabum_Rx5500XT4gb_GamingOC = soup_kabum_Rx5500XT4gb_GamingOC.find('div', class_='preco_antigo-cm').get_text()
            newPrice_kabum_Rx5500XT4gb_GamingOC = soup_kabum_Rx5500XT4gb_GamingOC.find('div', class_='preco_desconto-cm').find('strong').get_text()
   
        
            kabum_Rx5500XT4gb_GamingOC_Promocao = api.update_status('''
            
PROMOÇÃO:

Rx5500XT 4gb (GamingOC - Gigabyte)

''' + oldPrice_kabum_Rx5500XT4gb_GamingOC + '''
''' + newPrice_kabum_Rx5500XT4gb_GamingOC + '''


Preço: R$''' + price_kabum_Rx5500XT4gb_GamingOC + '''
Á vista no boleto bancário com 15% de desconto



''' + kabum_Rx5500XT4gb_GamingOC + '''
                                            ''')

            

            
            break
            while True:
                time.sleep(14)
                try:
    

                    kabum_Rx5500XT4gb_GamingOC = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=109644'
                    page_kabum_Rx5500XT4gb_GamingOC = requests.get(kabum_Rx5500XT4gb_GamingOC, headers=headers)
                    soup_kabum_Rx5500XT4gb_GamingOC = BeautifulSoup(page_kabum_Rx5500XT4gb_GamingOC.content,'html.parser')
                    price_kabum_Rx5500XT4gb_GamingOC = soup_kabum_Rx5500XT4gb_GamingOC.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

                except:
                    kabum_Rx5500XT4gb_GamingOC = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=109644'
         
                    api.destroy_status(kabum_Rx5500XT4gb_GamingOC_Promocao)
                    return KabumRx5500XT4gb_GamingOC()







                
                
def KabumRx5500XT8gb_Pulse():
    
    while True:
        time.sleep(15)
        try:
            kabum_Rx5500XT8gb_Pulse = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=109852'
            page_kabum_Rx5500XT8gb_Pulse = requests.get(kabum_Rx5500XT8gb_Pulse, headers=headers)
            soup_kabum_Rx5500XT8gb_Pulse = BeautifulSoup(page_kabum_Rx5500XT8gb_Pulse.content,'html.parser')

            try:
                status_kabum_Rx5500XT8gb_Pulse = soup_kabum_Rx5500XT4gb_GamingOC.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
            except:
                status_kabum_Rx5500XT8gb_Pulse = soup_kabum_Rx5500XT4gb_GamingOC.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")

        except:
            kabum_Rx5500XT8gb_Pulse = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=109852'

            page_kabum_Rx5500XT8gb_Pulse = requests.get(kabum_Rx5500XT8gb_Pulse, headers=headers)
            soup_kabum_Rx5500XT8gb_Pulse = BeautifulSoup(page_kabum_Rx5500XT8gb_Pulse.content,'html.parser')
    

        
            price_kabum_Rx5500XT8gb_Pulse = soup_kabum_Rx5500XT8gb_Pulse.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

    
        


        
            status_kabum_Rx5500XT8gb_Pulse = 'PROMOÇÃO'
    
            oldPrice_kabum_Rx5500XT8gb_Pulse = soup_kabum_Rx5500XT8gb_Pulse.find('div', class_='preco_antigo-cm').get_text()
            newPrice_kabum_Rx5500XT8gb_Pulse = soup_kabum_Rx5500XT8gb_Pulse.find('div', class_='preco_desconto-cm').find('strong').get_text()
   
        
            kabum_Rx5500XT8gb_Pulse_Promocao = api.update_status('''
            
PROMOÇÃO:

Rx5500XT 8gb (Pulse - Sapphire)

''' + oldPrice_kabum_Rx5500XT8gb_Pulse + '''
''' + newPrice_kabum_Rx5500XT8gb_Pulse + '''


Preço: R$''' + price_kabum_Rx5500XT8gb_Pulse + '''
Á vista no boleto bancário com 15% de desconto



''' + kabum_Rx5500XT8gb_Pulse + '''
                                            ''')

            

            
            break
            while True:
                time.sleep(15)
                try:
    

                    kabum_Rx5500XT8gb_Pulse = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=109852'
                    page_kabum_Rx5500XT8gb_Pulse = requests.get(kabum_Rx5500XT8gb_Pulse, headers=headers)
                    soup_kabum_Rx5500XT8gb_Pulse = BeautifulSoup(page_kabum_Rx5500XT8gb_Pulse.content,'html.parser')

                except:
                    kabum_Rx5500XT8gb_Pulse = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=109852'
         
                    api.destroy_status(kabum_Rx5500XT8gb_Pulse_Promocao)
                    return KabumRx5500XT8gb_Pulse()















def KabumRx5600XT_Windforce():
    
    while True:
        time.sleep(16)
        
        try:
            kabum_Rx5600XT_Windforce = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=113296'
            page_kabum_Rx5600XT_Windforce = requests.get(kabum_Rx5600XT_Windforce, headers=headers)
            soup_kabum_Rx5600XT_Windforce = BeautifulSoup(page_kabum_Rx5600XT_Windforce.content,'html.parser')

            try:
                status_kabum_Rx5600XT_Windforce = soup_kabum_Rx5600XT_Windforce.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
            except:
                status_kabum_Rx5600XT_Windforce = soup_kabum_Rx5600XT_Windforce.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")

        except:
            kabum_Rx5600XT_Windforce = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=113296'

            page_kabum_Rx5600XT_Windforce = requests.get(kabum_Rx5600XT_Windforce, headers=headers)
            soup_kabum_Rx5600XT_Windforce = BeautifulSoup(page_kabum_Rx5600XT_Windforce.content,'html.parser')
    

        
            price_kabum_Rx5600XT_Windforce = soup_kabum_Rx5600XT_Windforce.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

    
        


        
            status_kabum_Rx5600XT_Windforce = 'PROMOÇÃO'
    
            oldPrice_kabum_Rx5600XT_Windforce = soup_kabum_Rx5600XT_Windforce.find('div', class_='preco_antigo-cm').get_text()
            newPrice_kabum_Rx5600XT_Windforce = soup_kabum_Rx5600XT_Windforce.find('div', class_='preco_desconto-cm').find('strong').get_text()
   
        
            kabum_Rx5600XT_Windforce_Promocao = api.update_status('''
            
PROMOÇÃO:

Rx5600XT (Windforce - Gigabyte)

''' + oldPrice_kabum_Rx5600XT_Windforce + '''
''' + newPrice_kabum_Rx5600XT_Windforce + '''


Preço: R$''' + price_kabum_Rx5600XT_Windforce + '''
Á vista no boleto bancário com 15% de desconto



''' + kabum_Rx5600XT_Windforce + '''
                                            ''')

            

            
            break
            while True:
                time.sleep(16)
                try:
    

                    kabum_Rx5600XT_Windforce = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=113296'
                    page_kabum_Rx5600XT_Windforce = requests.get(kabum_Rx5600XT_Windforce, headers=headers)
                    soup_kabum_Rx5600XT_Windforce = BeautifulSoup(page_kabum_Rx5600XT_Windforce.content,'html.parser')
                    price_kabum_Rx5600XT_Windforce = soup_kabum_Rx5600XT_Windforce.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

                except:
                    kabum_Rx5600XT_Windforce = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=113296'
         
                    api.destroy_status(kabum_Rx5600XT_Windforce_Promocao)
                    return KabumRx5600XT_Windforce()


                
def KabumRx5700_TUF():
    
    while True:
        time.sleep(17)
        try:
            kabum_Rx5700_TUF = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=103786'
            page_kabum_Rx5700_TUF = requests.get(kabum_Rx5700_TUF, headers=headers)
            soup_kabum_Rx5700_TUF = BeautifulSoup(page_kabum_Rx5700_TUF.content,'html.parser')

            try:
                status_kabum_Rx5700_TUF = soup_kabum_Rx5700_TUF.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
            except:
                status_kabum_Rx5700_TUF = soup_kabum_Rx5700_TUF.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")

        except:
            kabum_Rx5700_TUF = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=103786'
            page_kabum_Rx5700_TUF = requests.get(kabum_Rx5700_TUF, headers=headers)
            soup_kabum_Rx5700_TUF = BeautifulSoup(page_kabum_Rx5700_TUF.content,'html.parser')
    

        
            price_kabum_Rx5700_TUF = soup_kabum_Rx5700_TUF.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

    
        


        
            status_kabum_Rx5700_TUF = 'PROMOÇÃO'
    
            oldPrice_kabum_Rx5700_TUF = soup_kabum_Rx5700_TUF.find('div', class_='preco_antigo-cm').get_text()
            newPrice_kabum_Rx5700_TUF = soup_kabum_Rx5700_TUF.find('div', class_='preco_desconto-cm').find('strong').get_text()
   
        
            kabum_Rx5700_TUF_Promocao = api.update_status('''
            
PROMOÇÃO:

Rx5700 (TUF - Asus)

''' + oldPrice_kabum_Rx5700_TUF + '''
''' + newPrice_kabum_Rx5700_TUF + '''


Preço: R$''' + price_kabum_Rx5700_TUF + '''
Á vista no boleto bancário com 15% de desconto



''' + kabum_Rx5700_TUF + '''
                                            ''')

            

            
            break
            while True:
                time.sleep(17)
                try:
    

                    kabum_Rx5700_TUF = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=103786'
                    page_kabum_Rx5700_TUF = requests.get(kabum_Rx5700_TUF, headers=headers)
                    soup_kabum_Rx5700_TUF = BeautifulSoup(page_kabum_Rx5700_TUF.content,'html.parser')
                    price_kabum_Rx5700_TUF = soup_kabum_Rx5700_TUF.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

                except:
                    kabum_Rx5700_TUF = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=103786'
         
                    api.destroy_status(kabum_Rx5700_TUF_Promocao)
                    return KabumRx5700_TUF()












def KabumRx5700XT_TUF():
    
    while True:
        time.sleep(18)
        try:
            kabum_Rx5700XT_TUF = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=111842'
            page_kabum_Rx5700XT_TUF = requests.get(kabum_Rx5700XT_TUF, headers=headers)
            soup_kabum_Rx5700XT_TUF = BeautifulSoup(page_kabum_Rx5700XT_TUF.content,'html.parser')

            try:
                status_kabum_Rx5700XT_TUF = soup_kabum_Rx5700XT_TUF.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
            except:
                status_kabum_Rx5700XT_TUF = soup_kabum_Rx5700XT_TUF.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")

        except:
            kabum_Rx5700XT_TUF = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=111842'
            page_kabum_Rx5700XT_TUF = requests.get(kabum_Rx5700XT_TUF, headers=headers)
            soup_kabum_Rx5700XT_TUF = BeautifulSoup(page_kabum_Rx5700XT_TUF.content,'html.parser')
    

        
            price_kabum_Rx5700XT_TUF = soup_kabum_Rx5700XT_TUF.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

    
        


        
            status_kabum_Rx5700XT_TUF = 'PROMOÇÃO'
    
            oldPrice_kabum_Rx5700XT_TUF = soup_kabum_Rx5700XT_TUF.find('div', class_='preco_antigo-cm').get_text()
            newPrice_kabum_Rx5700XT_TUF = soup_kabum_Rx5700XT_TUF.find('div', class_='preco_desconto-cm').find('strong').get_text()
   
        
            kabum_Rx5700XT_TUF_Promocao = api.update_status('''
            
PROMOÇÃO:

Rx5700XT (TUF - Asus)

''' + oldPrice_kabum_Rx5700XT_TUF + '''
''' + newPrice_kabum_Rx5700XT_TUF + '''


Preço: R$''' + price_kabum_Rx5700XT_TUF + '''
Á vista no boleto bancário com 15% de desconto



''' + kabum_Rx5700XT_TUF + '''
                                            ''')

            

            
            break
            while True:
                time.sleep(18)
                try:
    

                    kabum_Rx5700XT_TUF = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=111842'
                    page_kabum_Rx5700XT_TUF = requests.get(kabum_Rx5700XT_TUF, headers=headers)
                    soup_kabum_Rx5700XT_TUF = BeautifulSoup(page_kabum_Rx5700XT_TUF.content,'html.parser')
                    price_kabum_Rx5700XT_TUF = soup_kabum_Rx5700XT_TUF.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

                except:
                    kabum_Rx5700XT_TUF = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=111842'
         
                    api.destroy_status(kabum_Rx5700XT_TUF_Promocao)
                    return KabumRx5700XT_TUF()





























def Kabuma320M_KBR():
    
    while True:
        time.sleep(19)
        try:
            kabum_a320M_KBR = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=93427'
            page_kabum_a320M_KBR = requests.get(kabum_a320M_KBR, headers=headers)
            soup_kabum_a320M_KBR = BeautifulSoup(page_kabum_a320M_KBR.content,'html.parser')

            try:
                status_kabum_a320M_KBR = soup_kabum_a320M_KBR.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
            except:
                status_kabum_a320M_KBR = soup_kabum_a320M_KBR.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")

        except:
            kabum_a320M_KBR = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=93427'
            page_kabum_a320M_KBR = requests.get(kabum_a320M_KBR, headers=headers)
            soup_kabum_a320M_KBR = BeautifulSoup(page_kabum_a320M_KBR.content,'html.parser')
    

        
            price_kabum_a320M_KBR = soup_kabum_a320M_KBR.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

    
        


        
            status_kabum_a320M_KBR = 'PROMOÇÃO'
    
            oldPrice_kabum_a320M_KBR = soup_kabum_a320M_KBR.find('div', class_='preco_antigo-cm').get_text()
            newPrice_kabum_a320M_KBR = soup_kabum_a320M_KBR.find('div', class_='preco_desconto-cm').find('strong').get_text()
   
        
            kabum_a320M_KBR_Promocao = api.update_status('''
            
PROMOÇÃO:

a320M (Prime KBR - Asus)

''' + oldPrice_kabum_a320M_KBR + '''
''' + newPrice_kabum_a320M_KBR + '''


Preço: R$''' + price_kabum_a320M_KBR + '''
Á vista no boleto bancário com 15% de desconto



''' + kabum_a320M_KBR + '''
                                            ''')

            

            
            break
            while True:
                time.sleep(19)
                try:
    

                    kabum_a320M_KBR = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=93427'
                    page_kabum_a320M_KBR = requests.get(kabum_a320M_KBR, headers=headers)
                    soup_kabum_a320M_KBR = BeautifulSoup(page_kabum_a320M_KBR.content,'html.parser')
                    price_kabum_a320M_KBR = soup_kabum_a320M_KBR.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

                except:
                    kabum_a320M_KBR = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=93427'
         
                    api.destroy_status(kabum_a320M_KBR_Promocao)
                    return Kabuma320M_KBR()















def Kabumb450M_SteelLegend():
    
    while True:
        time.sleep(19)
        try:
            kabum_b450M_SteelLegend = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=100672'
            page_kabum_b450M_SteelLegend = requests.get(kabum_b450M_SteelLegend, headers=headers)
            soup_kabum_b450M_SteelLegend = BeautifulSoup(page_kabum_b450M_SteelLegend.content,'html.parser')

            try:
                status_kabum_b450M_SteelLegend = soup_kabum_b450M_SteelLegend.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
            except:
                status_kabum_b450M_SteelLegend = soup_kabum_b450M_SteelLegend.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")

        except:
            kabum_b450M_SteelLegend = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=100672'
            page_kabum_b450M_SteelLegend = requests.get(kabum_b450M_SteelLegend, headers=headers)
            soup_kabum_b450M_SteelLegend = BeautifulSoup(page_kabum_b450M_SteelLegend.content,'html.parser')
    

        
            price_kabum_b450M_SteelLegend = soup_kabum_b450M_SteelLegend.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

    
        


        
            status_kabum_b450M_SteelLegend = 'PROMOÇÃO'
    
            oldPrice_kabum_b450M_SteelLegend = soup_kabum_b450M_SteelLegend.find('div', class_='preco_antigo-cm').get_text()
            newPrice_kabum_b450M_SteelLegend = soup_kabum_b450M_SteelLegend.find('div', class_='preco_desconto-cm').find('strong').get_text()
   
        
            kabum_b450M_SteelLegend_Promocao = api.update_status('''
            
PROMOÇÃO:

B450M (Steel Legend - Asrock)

''' + oldPrice_kabum_b450M_SteelLegend + '''
''' + newPrice_kabum_b450M_SteelLegend + '''


Preço: R$''' + price_kabum_b450M_SteelLegend + '''
Á vista no boleto bancário com 15% de desconto



''' + kabum_b450M_SteelLegend + '''
                                            ''')

            

            
            break
            while True:
                time.sleep(19)
                try:
    

                    kabum_b450M_SteelLegend = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=100672'
                    page_kabum_b450M_SteelLegend = requests.get(kabum_b450M_SteelLegend, headers=headers)
                    soup_kabum_b450M_SteelLegend = BeautifulSoup(page_kabum_b450M_SteelLegend.content,'html.parser')
                    price_kabum_b450M_SteelLegend = soup_kabum_b450M_SteelLegend.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

                except:
                    kabum_b450M_SteelLegend = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=100672'
         
                    api.destroy_status(kabum_b450M_SteelLegend_Promocao)
                    return Kabumb450M_SteelLegend()




















def Kabumi39100F():
    
    while True:
        time.sleep(20)
        try:
            kabum_i39100F = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=101918'
            page_kabum_i39100F = requests.get(kabum_i39100F, headers=headers)
            soup_kabum_i39100F = BeautifulSoup(page_kabum_i39100F.content,'html.parser')

            try:
                status_kabum_i39100F = soup_kabum_i39100F.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
            except:
                status_kabum_i39100F = soup_kabum_i39100F.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")

        except:
            kabum_i39100F = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=101918'
            page_kabum_i39100F = requests.get(kabum_i39100F, headers=headers)
            soup_kabum_i39100F = BeautifulSoup(page_kabum_i39100F.content,'html.parser')
    

        
            price_kabum_i39100F = soup_kabum_i39100F.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

    
        


        
            status_kabum_i39100F = 'PROMOÇÃO'
    
            oldPrice_kabum_i39100F = soup_kabum_i39100F.find('div', class_='preco_antigo-cm').get_text()
            newPrice_kabum_i39100F = soup_kabum_i39100F.find('div', class_='preco_desconto-cm').find('strong').get_text()
   
        
            kabum_i39100F_Promocao = api.update_status('''
            
PROMOÇÃO:

i3 9100F

''' + oldPrice_kabum_i39100F + '''
''' + newPrice_kabum_i39100F + '''


Preço: R$''' + price_kabum_i39100F + '''
Á vista no boleto bancário com 15% de desconto



''' + kabum_i39100F + '''
                                            ''')

            

            
            break
            while True:
                time.sleep(20)
                try:
    

                    kabum_i39100F = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=101918'
                    page_kabum_i39100F = requests.get(kabum_i39100F, headers=headers)
                    soup_kabum_i39100F = BeautifulSoup(page_kabum_i39100F.content,'html.parser')
                    price_kabum_i39100F = soup_kabum_i39100F.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

                except:
                    kabum_i39100F = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=101918'
         
                    api.destroy_status(kabum_i39100F_Promocao)
                    return Kabumi39100F()


                


def Kabumi59400F():
    
    while True:
        time.sleep(21)  
        try:
            kabum_i59400F = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=99683'
            page_kabum_i59400F = requests.get(kabum_i59400F, headers=headers)
            soup_kabum_i59400F = BeautifulSoup(page_kabum_i59400F.content,'html.parser')

            try:
                status_kabum_i59400F = soup_kabum_i59400F.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
            except:
                status_kabum_i59400F = soup_kabum_i59400F.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")

        except:
            kabum_i59400F = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=99683'
            page_kabum_i59400F = requests.get(kabum_i59400F, headers=headers)
            soup_kabum_i59400F = BeautifulSoup(page_kabum_i59400F.content,'html.parser')
    

        
            price_kabum_i59400F = soup_kabum_i59400F.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

    
        


        
            status_kabum_i59400F = 'PROMOÇÃO'
    
            oldPrice_kabum_i59400F = soup_kabum_i59400F.find('div', class_='preco_antigo-cm').get_text()
            newPrice_kabum_i59400F = soup_kabum_i59400F.find('div', class_='preco_desconto-cm').find('strong').get_text()
   
        
            kabum_i59400F_Promocao = api.update_status('''
            
PROMOÇÃO:

i5 9400F

''' + oldPrice_kabum_i59400F + '''
''' + newPrice_kabum_i59400F + '''


Preço: R$''' + price_kabum_i59400F + '''
Á vista no boleto bancário com 15% de desconto



''' + kabum_i59400F + '''
                                            ''')

            

            
            break
            while True:
                time.sleep(21)
                try:
    

                    kabum_i59400F = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=99683'
                    page_kabum_i59400F = requests.get(kabum_i59400F, headers=headers)
                    soup_kabum_i59400F = BeautifulSoup(page_kabum_i59400F.content,'html.parser')
                    price_kabum_i59400F = soup_kabum_i59400F.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

                except:
                    kabum_i59400F = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=99683'
         
                    api.destroy_status(kabum_i59400F_Promocao)
                    return Kabumi59400F()










                

def Kabumi59600K():
    
    while True:
        time.sleep(22)
        try:
    
            kabum_i59600K = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=98765'
            page_kabum_i59600K = requests.get(kabum_i59600K, headers=headers)
            soup_kabum_i59600K = BeautifulSoup(page_kabum_i59600K.content,'html.parser')

            try:
                status_kabum_i59600K = soup_kabum_i59600K.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
            except:
                status_kabum_i59600K = soup_kabum_i59600K.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")

        except:
            kabum_i59600K = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=98765'
            page_kabum_i59600K = requests.get(kabum_i59600K, headers=headers)
            soup_kabum_i59600K = BeautifulSoup(page_kabum_i59600K.content,'html.parser')
    

        
            price_kabum_i59600K = soup_kabum_i59600K.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

    
        


        
            status_kabum_i59600K = 'PROMOÇÃO'
    
            oldPrice_kabum_i59600K = soup_kabum_i59600K.find('div', class_='preco_antigo-cm').get_text()
            newPrice_kabum_i59600K = soup_kabum_i59600K.find('div', class_='preco_desconto-cm').find('strong').get_text()
   
        
            kabum_i59600K_Promocao = api.update_status('''
            
PROMOÇÃO:

i5 9600K

''' + oldPrice_kabum_i59600K + '''
''' + newPrice_kabum_i59600K + '''


Preço: R$''' + price_kabum_i59600K + '''
Á vista no boleto bancário com 15% de desconto



''' + kabum_i59600K + '''
                                            ''')

            

            
            break
            while True:
                time.sleep(22)
                try:
    

                    kabum_i59600K = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=98765'

                except:
                    kabum_i59600K = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=98765'
         
                    api.destroy_status(kabum_i59600K_Promocao)
                    return Kabumi59600K()


                
def Kabumi59600KF():
    
    while True:
        time.sleep(23)
        try:
    
            kabum_i59600KF = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=102809'
            page_kabum_i59600KF = requests.get(kabum_i59600KF, headers=headers)
            soup_kabum_i59600KF = BeautifulSoup(page_kabum_i59600KF.content,'html.parser')

            try:
                status_kabum_i59600KF = soup_kabum_i59600KF.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
            except:
                status_kabum_i59600KF = soup_kabum_i59600KF.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")

        except:
            kabum_i59600KF = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=102809'
            page_kabum_i59600KF = requests.get(kabum_i59600KF, headers=headers)
            soup_kabum_i59600KF = BeautifulSoup(page_kabum_i59600KF.content,'html.parser')
    

        
            price_kabum_i59600KF = soup_kabum_i59600KF.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

    
        


        
            status_kabum_i59600KF = 'PROMOÇÃO'
    
            oldPrice_kabum_i59600KF = soup_kabum_i59600KF.find('div', class_='preco_antigo-cm').get_text()
            newPrice_kabum_i59600KF = soup_kabum_i59600KF.find('div', class_='preco_desconto-cm').find('strong').get_text()
   
        
            kabum_i59600KF_Promocao = api.update_status('''
            
PROMOÇÃO:

i5 9600KF

''' + oldPrice_kabum_i59600KF + '''
''' + newPrice_kabum_i59600KF + '''


Preço: R$''' + price_kabum_i59600K + '''
Á vista no boleto bancário com 15% de desconto



''' + kabum_i59600KF + '''
                                            ''')

            

            
            break
            while True:
                time.sleep(23)
                try:
    

                    kabum_i59600KF = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=102809'
                    page_kabum_i59600K = requests.get(kabum_i59600K, headers=headers)
                    soup_kabum_i59600K = BeautifulSoup(page_kabum_i59600K.content,'html.parser')
                    price_kabum_i59600KF = soup_kabum_i59600KF.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

                except:
                    kabum_i59600KF = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=102809'
         
                    api.destroy_status(kabum_i59600KF_Promocao)
                    return Kabumi59600KF()








            
def Kabumi79700F():
    
    while True:
        time.sleep(24)
        try:
            kabum_i79700F = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=104144'
            page_kabum_i79700F = requests.get(kabum_i79700F, headers=headers)
            soup_kabum_i79700F = BeautifulSoup(page_kabum_i79700F.content,'html.parser')

            try:
                status_kabum_i79700F = soup_kabum_i79700F.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
            except:
                status_kabum_i79700F = soup_kabum_i79700F.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")

        except:
            kabum_i79700F = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=104144'
            page_kabum_i79700F = requests.get(kabum_i79700F, headers=headers)
            soup_kabum_i79700F = BeautifulSoup(page_kabum_i79700F.content,'html.parser')
    

        
            price_kabum_i79700F = soup_kabum_i79700F.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

    
        


        
            status_kabum_i79700F = 'PROMOÇÃO'
    
            oldPrice_kabum_i79700F = soup_kabum_i79700F.find('div', class_='preco_antigo-cm').get_text()
            newPrice_kabum_i79700F = soup_kabum_i79700F.find('div', class_='preco_desconto-cm').find('strong').get_text()
   
        
            kabum_i79700F_Promocao = api.update_status('''
            
PROMOÇÃO:

i7 9700F

''' + oldPrice_kabum_i79700F + '''
''' + newPrice_kabum_i79700F + '''


Preço: R$''' + price_kabum_i79700F + '''
Á vista no boleto bancário com 15% de desconto



''' + kabum_i79700F + '''
                                            ''')

            

            
            break
            while True:
                time.sleep(24)
                try:
    

                    kabum_i79700F = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=104144'
                    page_kabum_i79700F = requests.get(kabum_i79700F, headers=headers)
                    soup_kabum_i79700F = BeautifulSoup(page_kabum_i79700F.content,'html.parser')
                    price_kabum_i79700F = soup_kabum_i79700F.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

                except:
                    kabum_i79700F = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=104144'
         
                    api.destroy_status(kabum_i79700F_Promocao)
                    return Kabumi79700F()

                

def Kabumi79700K():
    
    while True:
        time.sleep(25)

        try:
            kabum_i79700K = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=98808'
            page_kabum_i79700K = requests.get(kabum_i79700K, headers=headers)
            soup_kabum_i79700K = BeautifulSoup(page_kabum_i79700K.content,'html.parser')

            try:
                status_kabum_i79700K = soup_kabum_i79700K.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
            except:
                status_kabum_i79700K = soup_kabum_i79700K.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")

        except:
            kabum_i79700K = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=98808'
      

        
            price_kabum_i79700K = soup_kabum_i79700K.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

    
        


        
            status_kabum_i79700K = 'PROMOÇÃO'
    
            oldPrice_kabum_i79700K = soup_kabum_i79700K.find('div', class_='preco_antigo-cm').get_text()
            newPrice_kabum_i79700K = soup_kabum_i79700K.find('div', class_='preco_desconto-cm').find('strong').get_text()
   
        
            kabum_i79700K_Promocao = api.update_status('''
            
PROMOÇÃO:

i7 9700K

''' + oldPrice_kabum_i79700K + '''
''' + newPrice_kabum_i79700K + '''


Preço: R$''' + price_kabum_i79700K + '''
Á vista no boleto bancário com 15% de desconto



''' + kabum_i79700K + '''
                                            ''')

            

            
            break
            while True:
                time.sleep(25)
                try:
    

                    kabum_i79700K = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=98808'
                    page_kabum_i79700K = requests.get(kabum_i79700K, headers=headers)
                    soup_kabum_i79700K = BeautifulSoup(page_kabum_i79700K.content,'html.parser')
                    price_kabum_i79700K = soup_kabum_i79700K.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

                except:
                    kabum_i79700K = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=98808'
         
                    api.destroy_status(kabum_i79700K_Promocao)
                    return Kabumi79700K()








                
def Kabumi79700KF():
    
    while True:
        time.sleep(26)
        try:
            kabum_i79700KF = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=102522'
            page_kabum_i79700KF = requests.get(kabum_i79700KF, headers=headers)
            soup_kabum_i79700KF = BeautifulSoup(page_kabum_i79700KF.content,'html.parser')

            try:
                status_kabum_i79700KF = soup_kabum_i79700KF.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
            except:
                status_kabum_i79700KF = soup_kabum_i79700KF.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")

        except:
            kabum_i79700KF = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=102522'
 

        
            price_kabum_i79700KF = soup_kabum_i79700KF.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

    
        


        
            status_kabum_i79700KF = 'PROMOÇÃO'
    
            oldPrice_kabum_i79700KF = soup_kabum_i79700KF.find('div', class_='preco_antigo-cm').get_text()
            newPrice_kabum_i79700KF = soup_kabum_i79700KF.find('div', class_='preco_desconto-cm').find('strong').get_text()
   
        
            kabum_i79700KF_Promocao = api.update_status('''
            
PROMOÇÃO:

i7 9700KF

''' + oldPrice_kabum_i79700KF + '''
''' + newPrice_kabum_i79700KF + '''


Preço: R$''' + price_kabum_i79700KF + '''
Á vista no boleto bancário com 15% de desconto



''' + kabum_i79700KF + '''
                                            ''')

            

            
            break
            while True:
                time.sleep(26)
                try:
    

                    kabum_i79700KF = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=102522'
                    page_kabum_i79700KF = requests.get(kabum_i79700KF, headers=headers)
                    soup_kabum_i79700KF = BeautifulSoup(page_kabum_i79700KF.content,'html.parser')
                    price_kabum_i79700KF = soup_kabum_i79700KF.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

                except:
                    kabum_i79700KF = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=102522'
         
                    api.destroy_status(kabum_i79700KF_Promocao)
                    return Kabumi79700KF()
















                

                
                    
def Kabumi99900K():
    
    while True:
        time.sleep(27)
        try:
    
            kabum_i99900K = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=98994'
            page_kabum_i99900K = requests.get(kabum_i99900K, headers=headers)
            soup_kabum_i99900K = BeautifulSoup(page_kabum_i99900K.content,'html.parser')

            try:
                status_kabum_i99900K = soup_kabum_i99900K.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
            except:
                status_kabum_i99900K = soup_kabum_i99900K.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")

        except:
            kabum_i99900K = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=98994'

        
            price_kabum_i99900K = soup_kabum_i99900K.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

    
        


        
            status_kabum_i99900K = 'PROMOÇÃO'
    
            oldPrice_kabum_i99900K = soup_kabum_i99900K.find('div', class_='preco_antigo-cm').get_text()
            newPrice_kabum_i99900K = soup_kabum_i99900K.find('div', class_='preco_desconto-cm').find('strong').get_text()
   
        
            kabum_i99900K_Promocao = api.update_status('''
            
PROMOÇÃO:

i9 9900K

''' + oldPrice_kabum_i99900K + '''
''' + newPrice_kabum_i99900K + '''


Preço: R$''' + price_kabum_i99900K + '''
Á vista no boleto bancário com 15% de desconto



''' + kabum_i99900K + '''
                                            ''')

            

            
            break
            while True:
                time.sleep(27)
                try:
    

                    kabum_i99900K = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=98994'
                    page_kabum_i99900K = requests.get(kabum_i99900K, headers=headers)
                    soup_kabum_i99900K = BeautifulSoup(page_kabum_i99900K.content,'html.parser')
                    price_kabum_i99900K = soup_kabum_i99900K.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

                except:
                    kabum_i99900K = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=98994'
         
                    api.destroy_status(kabum_i99900K_Promocao)
                    return Kabumi99900K()




                


def Kabumi99900KF():
    
    while True:
        time.sleep(28)
        try:
    
            kabum_i99900KF = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=102808'
            page_kabum_i99900KF = requests.get(kabum_i99900KF, headers=headers)
            soup_kabum_i99900KF = BeautifulSoup(page_kabum_i99900KF.content,'html.parser')

            try:
                status_kabum_i99900KF = soup_kabum_i99900KF.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
            except:
                status_kabum_i99900KF = soup_kabum_i99900KF.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")

        except:
            kabum_i99900KF = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=102808'

        
            price_kabum_i99900KF = soup_kabum_i99900KF.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

    
        


        
            status_kabum_i99900KF = 'PROMOÇÃO'
    
            oldPrice_kabum_i99900KF = soup_kabum_i99900KF.find('div', class_='preco_antigo-cm').get_text()
            newPrice_kabum_i99900KF = soup_kabum_i99900KF.find('div', class_='preco_desconto-cm').find('strong').get_text()
   
        
            kabum_i99900KF_Promocao = api.update_status('''
            
PROMOÇÃO:

i9 9900KF

''' + oldPrice_kabum_i99900KF + '''
''' + newPrice_kabum_i99900KF + '''


Preço: R$''' + price_kabum_i99900KF + '''
Á vista no boleto bancário com 15% de desconto



''' + kabum_i99900KF + '''
                                            ''')

            

            
            break
            while True:
                time.sleep(28)
                try:
    

                    kabum_i99900KF = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=102808'
                    page_kabum_i99900KF = requests.get(kabum_i99900KF, headers=headers)
                    soup_kabum_i99900KF = BeautifulSoup(page_kabum_i99900KF.content,'html.parser')
                    price_kabum_i99900KF = soup_kabum_i99900KF.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

                except:
                    kabum_i99900KF = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=102808'
         
                    api.destroy_status(kabum_i99900KF_Promocao)
                    return Kabumi99900KF()





                

def Kabumi310100():
    
    while True:
        time.sleep(29)
        try:
            kabum_i310100 = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=112989'
            page_kabum_i310100 = requests.get(kabum_i310100, headers=headers)
            soup_kabum_i310100 = BeautifulSoup(page_kabum_i310100.content,'html.parser')

            try:
                status_kabum_i310100 = soup_kabum_i310100.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
            except:
                status_kabum_i310100 = soup_kabum_i310100.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")

        except:
            kabum_i310100 = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=112989'

        
            price_kabum_i310100 = soup_kabum_i310100.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

    
        


        
            status_kabum_i310100 = 'PROMOÇÃO'
    
            oldPrice_kabum_i310100 = soup_kabum_i310100.find('div', class_='preco_antigo-cm').get_text()
            newPrice_kabum_i310100 = soup_kabum_i310100.find('div', class_='preco_desconto-cm').find('strong').get_text()
   
        
            kabum_i310100_Promocao = api.update_status('''
            
PROMOÇÃO:

i3 10100

''' + oldPrice_kabum_i310100 + '''
''' + newPrice_kabum_i310100 + '''


Preço: R$''' + price_kabum_i310100 + '''
Á vista no boleto bancário com 15% de desconto



''' + kabum_i310100 + '''
                                            ''')

            

            
            break
            while True:
                time.sleep(29)
                try:
    

                    kabum_i310100 = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=112989'
                    page_kabum_i310100 = requests.get(kabum_i310100, headers=headers)
                    soup_kabum_i310100 = BeautifulSoup(page_kabum_i310100.content,'html.parser')
                    price_kabum_i310100 = soup_kabum_i310100.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

                except:
                    kabum_i310100 = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=112989'
         
                    api.destroy_status(kabum_i310100_Promocao)
                    return Kabumi310100()









                
def Kabumi510400():
    
    while True:

        time.sleep(30)

        try:
            kabum_i510400 = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=112990'
            page_kabum_i510400 = requests.get(kabum_i510400, headers=headers)
            soup_kabum_i510400 = BeautifulSoup(page_kabum_i510400.content,'html.parser')

            try:
                status_kabum_i510400 = soup_kabum_i510400.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
            except:
                status_kabum_i510400 = soup_kabum_i510400.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")

        except:
            kabum_i510400 = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=112990'

        
            price_kabum_i510400 = soup_kabum_i510400.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

    
        


        
            status_kabum_i510400 = 'PROMOÇÃO'
    
            oldPrice_kabum_i510400 = soup_kabum_i510400.find('div', class_='preco_antigo-cm').get_text()
            newPrice_kabum_i510400 = soup_kabum_i510400.find('div', class_='preco_desconto-cm').find('strong').get_text()
   
        
            kabum_i510400_Promocao = api.update_status('''
            
PROMOÇÃO:

i5 10400

''' + oldPrice_kabum_i510400 + '''
''' + newPrice_kabum_i510400 + '''


Preço: R$''' + price_kabum_i510400 + '''
Á vista no boleto bancário com 15% de desconto



''' + kabum_i510400 + '''
                                            ''')

            

            
            break
            while True:
                time.sleep(30)
                try:
    

                    kabum_i510400 = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=112990'
                    page_kabum_i510400 = requests.get(kabum_i510400, headers=headers)
                    soup_kabum_i510400 = BeautifulSoup(page_kabum_i510400.content,'html.parser')
                    price_kabum_i510400 = soup_kabum_i510400.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

                except:
                    kabum_i510400 = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=112990'
         
                    api.destroy_status(kabum_i510400_Promocao)
                    return Kabumi510400()







                

def Kabumi510400F():
    
    while True:

        time.sleep(31)
        try:
            kabum_i510400F = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=112991'
            page_kabum_i510400F = requests.get(kabum_i510400F, headers=headers)
            soup_kabum_i510400F = BeautifulSoup(page_kabum_i510400F.content,'html.parser')

            try:
                status_kabum_i510400F = soup_kabum_i510400F.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
            except:
                status_kabum_i510400F = soup_kabum_i510400F.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")

        except:
            kabum_i510400F = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=112991'

        
            price_kabum_i510400F = soup_kabum_i510400F.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

    
        


        
            status_kabum_i510400F = 'PROMOÇÃO'
    
            oldPrice_kabum_i510400F = soup_kabum_i510400F.find('div', class_='preco_antigo-cm').get_text()
            newPrice_kabum_i510400F = soup_kabum_i510400F.find('div', class_='preco_desconto-cm').find('strong').get_text()
   
        
            kabum_i510400F_Promocao = api.update_status('''
            
PROMOÇÃO:

i5 10400F

''' + oldPrice_kabum_i510400F + '''
''' + newPrice_kabum_i510400F + '''


Preço: R$''' + price_kabum_i510400F + '''
Á vista no boleto bancário com 15% de desconto



''' + kabum_i510400F + '''
                                            ''')

            

            
            break
            while True:
                time.sleep(31)
                try:
    

                    kabum_i510400F = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=112991'
                    page_kabum_i510400F = requests.get(kabum_i510400F, headers=headers)
                    soup_kabum_i510400F = BeautifulSoup(page_kabum_i510400F.content,'html.parser')
                    price_kabum_i510400F = soup_kabum_i510400F.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

                except:
                    kabum_i510400F = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=112991'
         
                    api.destroy_status(kabum_i510400F_Promocao)
                    return Kabumi510400F()

                
                

def Kabumi710700():
    
    while True:
        time.sleep(32)
        try:
            kabum_i710700 = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=112994'
            page_kabum_i710700 = requests.get(kabum_i710700, headers=headers)
            soup_kabum_i710700 = BeautifulSoup(page_kabum_i710700.content,'html.parser')

            try:
                status_kabum_i710700 = soup_kabum_i710700.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
            except:
                status_kabum_i710700 = soup_kabum_i710700.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")

        except:
            kabum_i710700 = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=112994'

        
            price_kabum_i710700 = soup_kabum_i710700.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

    
        


        
            status_kabum_i710700 = 'PROMOÇÃO'
    
            oldPrice_kabum_i710700 = soup_kabum_i710700.find('div', class_='preco_antigo-cm').get_text()
            newPrice_kabum_i710700 = soup_kabum_i710700.find('div', class_='preco_desconto-cm').find('strong').get_text()
   
        
            kabum_i710700_Promocao = api.update_status('''
            
PROMOÇÃO:

i7 10700

''' + oldPrice_kabum_i710700 + '''
''' + newPrice_kabum_i710700 + '''


Preço: R$''' + price_kabum_i710700 + '''
Á vista no boleto bancário com 15% de desconto



''' + kabum_i710700 + '''
                                            ''')

            

            
            break
            while True:
                time.sleep(32)
                try:
    

                    kabum_i710700 = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=112994'
                    page_kabum_i710700 = requests.get(kabum_i710700, headers=headers)
                    soup_kabum_i710700 = BeautifulSoup(page_kabum_i710700.content,'html.parser')
                    price_kabum_i710700 = soup_kabum_i710700.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

                except:
                    kabum_i710700 = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=112994'
         
                    api.destroy_status(kabum_i710700_Promocao)
                    return Kabumi710700()











                
def Kabumi710700K():
    
    while True:
        time.sleep(33)
        try:
            kabum_i710700K = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=112996'
            page_kabum_i710700K = requests.get(kabum_i710700K, headers=headers)
            soup_kabum_i710700K = BeautifulSoup(page_kabum_i710700K.content,'html.parser')

            try:
                status_kabum_i710700K = soup_kabum_i710700K.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
            except:
                status_kabum_i710700K = soup_kabum_i710700K.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")

        except:
            kabum_i710700K = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=112996'

        
            price_kabum_i710700K = soup_kabum_i710700K.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

    
        


        
            status_kabum_i710700K = 'PROMOÇÃO'
    
            oldPrice_kabum_i710700K = soup_kabum_i710700K.find('div', class_='preco_antigo-cm').get_text()
            newPrice_kabum_i710700K = soup_kabum_i710700K.find('div', class_='preco_desconto-cm').find('strong').get_text()
   
        
            kabum_i710700K_Promocao = api.update_status('''
            
PROMOÇÃO:

i7 10700K

''' + oldPrice_kabum_i710700K + '''
''' + newPrice_kabum_i710700K + '''


Preço: R$''' + price_kabum_i710700K + '''
Á vista no boleto bancário com 15% de desconto



''' + kabum_i710700K + '''
                                            ''')

            

            
            break
            while True:
                time.sleep(33)
                try:
    

                    kabum_i710700K = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=112996'
                    page_kabum_i710700K = requests.get(kabum_i710700K, headers=headers)
                    soup_kabum_i710700K = BeautifulSoup(page_kabum_i710700K.content,'html.parser')
                    price_kabum_i710700K = soup_kabum_i710700K.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

                except:
                    kabum_i710700K = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=112996'
         
                    api.destroy_status(kabum_i710700K_Promocao)
                    return Kabumi710700K()





def Kabumi910900K():
    time.sleep(38)
    while True:
        try:
            kabum_i910900K = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=113000'
            page_kabum_i910900K = requests.get(kabum_i910900K, headers=headers)
            soup_kabum_i910900K = BeautifulSoup(page_kabum_i910900K.content,'html.parser')

            try:
                status_kabum_i910900K = soup_kabum_i910900K.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
            except:
                status_kabum_i910900K = soup_kabum_i910900K.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")

        except:
            kabum_i910900K = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=113000'

        
            price_kabum_i910900K = soup_kabum_i910900K.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

    
        


        
            status_kabum_i910900K = 'PROMOÇÃO'
    
            oldPrice_kabum_i910900K = soup_kabum_i910900K.find('div', class_='preco_antigo-cm').get_text()
            newPrice_kabum_i910900K = soup_kabum_i910900K.find('div', class_='preco_desconto-cm').find('strong').get_text()
   
        
            kabum_i910900K_Promocao = api.update_status('''
            
PROMOÇÃO:

i9 10900K

''' + oldPrice_kabum_i910900K + '''
''' + newPrice_kabum_i910900K + '''


Preço: R$''' + price_kabum_i910900K + '''
Á vista no boleto bancário com 15% de desconto



''' + kabum_i910900K + '''
                                            ''')

            

            
            break
            while True:
                time.sleep(33)
                try:
    

                    kabum_i910900K = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=113000'
                    page_kabum_i910900K = requests.get(kabum_i910900K, headers=headers)
                    soup_kabum_i910900K = BeautifulSoup(page_kabum_i910900K.content,'html.parser')
                    price_kabum_i910900K = soup_kabum_i910900K.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

                except:
                    kabum_i910900K = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=113000'
         
                    api.destroy_status(kabum_i910900K_Promocao)
                    return Kabumi910900K()
                    


def KabumGTX1650Super_XCBlackGaming():
    time.sleep(34)
    while True:
        try:
            kabum_GTX1650Super_XCBlackGaming = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=113183'
            page_kabum_GTX1650Super_XCBlackGaming = requests.get(kabum_GTX1650Super_XCBlackGaming, headers=headers)
            soup_kabum_GTX1650Super_XCBlackGaming = BeautifulSoup(page_kabum_GTX1650Super_XCBlackGaming.content,'html.parser')

            try:
                status_kabum_GTX1650Super_XCBlackGaming = soup_kabum_GTX1650Super_XCBlackGaming.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
            except:
                status_kabum_GTX1650Super_XCBlackGaming = soup_kabum_GTX1650Super_XCBlackGaming.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")

        except:
            kabum_GTX1650Super_XCBlackGaming = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=113183'

        
            price_kabum_GTX1650Super_XCBlackGaming = soup_kabum_GTX1650Super_XCBlackGaming.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

    
        


        
            status_kabum_GTX1650Super_XCBlackGaming = 'PROMOÇÃO'
    
            oldPrice_kabum_GTX1650Super_XCBlackGaming = soup_kabum_GTX1650Super_XCBlackGaming.find('div', class_='preco_antigo-cm').get_text()
            newPrice_kabum_GTX1650Super_XCBlackGaming = soup_kabum_GTX1650Super_XCBlackGaming.find('div', class_='preco_desconto-cm').find('strong').get_text()
   
        
            kabum_GTX1650Super_XCBlackGaming_Promocao = api.update_status('''
            
PROMOÇÃO:

GTX 1650 Super (XC Black Gaming - EVGA)

''' + oldPrice_kabum_GTX1650Super_XCBlackGaming + '''
''' + newPrice_kabum_GTX1650Super_XCBlackGaming + '''


Preço: R$''' + price_kabum_GTX1650Super_XCBlackGaming + '''
Á vista no boleto bancário com 15% de desconto



''' + kabum_GTX1650Super_XCBlackGaming + '''
                                            ''')

            

            
            break
            while True:
                time.sleep(34)
                try:
    

                    kabum_GTX1650Super_XCBlackGaming = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=113183'
                    page_kabum_GTX1650Super_XCBlackGaming = requests.get(kabum_GTX1650Super_XCBlackGaming, headers=headers)
                    soup_kabum_GTX1650Super_XCBlackGaming = BeautifulSoup(page_kabum_GTX1650Super_XCBlackGaming.content,'html.parser')
                    price_kabum_GTX1650Super_XCBlackGaming = soup_kabum_GTX1650Super_XCBlackGaming.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

                except:
                    kabum_GTX1650Super_XCBlackGaming = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=113183'
         
                    api.destroy_status(kabum_GTX1650Super_XCBlackGaming_Promocao)
                    return KabumGTX1650Super_XCBlackGaming()













                
def KabumGTX1660_GigabyteOC():
    time.sleep(35)
    while True:
        try:
            kabum_GTX1660_GigabyteOC = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=101039'
            page_kabum_GTX1660_GigabyteOC = requests.get(kabum_GTX1660_GigabyteOC, headers=headers)
            soup_kabum_GTX1660_GigabyteOC = BeautifulSoup(page_kabum_GTX1660_GigabyteOC.content,'html.parser')

            try:
                status_kabum_GTX1660_GigabyteOC = soup_kabum_GTX1660_GigabyteOC.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
            except:
                status_kabum_GTX1660_GigabyteOC = soup_kabum_GTX1660_GigabyteOC.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")

        except:
            kabum_GTX1660_GigabyteOC = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=101039'

        
            price_kabum_GTX1660_GigabyteOC = soup_kabum_GTX1660_GigabyteOC.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

    
        


        
            status_kabum_GTX1660_GigabyteOC = 'PROMOÇÃO'
    
            oldPrice_kabum_GTX1660_GigabyteOC = soup_kabum_GTX1660_GigabyteOC.find('div', class_='preco_antigo-cm').get_text()
            newPrice_kabum_GTX1660_GigabyteOC = soup_kabum_GTX1660_GigabyteOC.find('div', class_='preco_desconto-cm').find('strong').get_text()
   
        
            kabum_GTX1660_GigabyteOC_Promocao = api.update_status('''
            
PROMOÇÃO:

GTX 1660 (GigabyteOC - Gigabyte)

''' + oldPrice_kabum_GTX1660_GigabyteOC + '''
''' + newPrice_kabum_GTX1660_GigabyteOC + '''


Preço: R$''' + price_kabum_GTX1660_GigabyteOC + '''
Á vista no boleto bancário com 15% de desconto



''' + kabum_GTX1660_GigabyteOC + '''
                                            ''')

            

            
            break
            while True:
                time.sleep(35)
                try:
    

                    kabum_GTX1660_GigabyteOC = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=101039'
                    page_kabum_GTX1660_GigabyteOC = requests.get(kabum_GTX1660_GigabyteOC, headers=headers)
                    soup_kabum_GTX1660_GigabyteOC = BeautifulSoup(page_kabum_GTX1660_GigabyteOC.content,'html.parser')
                    price_kabum_GTX1660_GigabyteOC = soup_kabum_GTX1660_GigabyteOC.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

                except:
                    kabum_GTX1660_GigabyteOC = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=101039'
         
                    api.destroy_status(kabum_GTX1660_GigabyteOC_Promocao)
                    return KabumGTX1660_GigabyteOC()





def KabumGTX1660Super_TUF():
    
    while True:
        time.sleep(36)
        try:
            kabum_GTX1660Super_TUF = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=104752'
            page_kabum_GTX1660Super_TUF = requests.get(kabum_GTX1660Super_TUF, headers=headers)
            soup_kabum_GTX1660Super_TUF = BeautifulSoup(page_kabum_GTX1660Super_TUF.content,'html.parser')

            try:
                status_kabum_GTX1660Super_TUF = soup_kabum_GTX1660Super_TUF.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
            except:
                status_kabum_GTX1660Super_TUF = soup_kabum_GTX1660Super_TUF.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")

        except:
            kabum_GTX1660Super_TUF = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=104752'

        
            price_kabum_GTX1660Super_TUF = soup_kabum_GTX1660Super_TUF.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

    
        


        
            status_kabum_GTX1660Super_TUF = 'PROMOÇÃO'
    
            oldPrice_kabum_GTX1660Super_TUF = soup_kabum_GTX1660Super_TUF.find('div', class_='preco_antigo-cm').get_text()
            newPrice_kabum_GTX1660Super_TUF = soup_kabum_GTX1660Super_TUF.find('div', class_='preco_desconto-cm').find('strong').get_text()
   
        
            kabum_GTX1660Super_TUF_Promocao = api.update_status('''
            
PROMOÇÃO:

GTX 1660Super (TUF - Asus)

''' + oldPrice_kabum_GTX1660Super_TUF + '''
''' + newPrice_kabum_GTX1660Super_TUF + '''


Preço: R$''' + price_kabum_GTX1660Super_TUF + '''
Á vista no boleto bancário com 15% de desconto



''' + kabum_GTX1660Super_TUF + '''
                                            ''')

            

            
            break
            while True:
                time.sleep(36)
                try:
    

                    kabum_GTX1660Super_TUF = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=104752'

                except:
                    kabum_GTX1660Super_TUF = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=104752'
         
                    api.destroy_status(kabum_GTX1660Super_TUF_Promocao)
                    return KabumGTX1660Super_TUF()






                


def KabumGTX1660Ti_GamingX():
    
    while True:
        time.sleep(37)
        try:
            kabum_GTX1660Ti_GamingX = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=100855'
            page_kabum_GTX1660Ti_GamingX = requests.get(kabum_GTX1660Ti_GamingX, headers=headers)
            soup_kabum_GTX1660Ti_GamingX = BeautifulSoup(page_kabum_GTX1660Ti_GamingX.content,'html.parser')

            try:
                status_kabum_GTX1660Ti_GamingX = soup_kabum_GTX1660Ti_GamingX.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
            except:
                status_kabum_GTX1660Ti_GamingX = soup_kabum_GTX1660Ti_GamingX.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")

        except:
            kabum_GTX1660Ti_GamingX = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=100855'
    
            price_kabum_GTX1660Ti_GamingX = soup_kabum_GTX1660Ti_GamingX.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

    
        


        
            status_kabum_GTX1660Ti_GamingX = 'PROMOÇÃO'
    
            oldPrice_kabum_GTX1660Ti_GamingX = soup_kabum_GTX1660Ti_GamingX.find('div', class_='preco_antigo-cm').get_text()
            newPrice_kabum_GTX1660Ti_GamingX = soup_kabum_GTX1660Ti_GamingX.find('div', class_='preco_desconto-cm').find('strong').get_text()
   
        
            kabum_GTX1660Ti_GamingX_Promocao = api.update_status('''
            
PROMOÇÃO:

GTX 1660Super (TUF - Asus)

''' + oldPrice_kabum_GTX1660Ti_GamingX + '''
''' + newPrice_kabum_GTX1660Ti_GamingX + '''


Preço: R$''' + price_kabum_GTX1660Ti_GamingX + '''
Á vista no boleto bancário com 15% de desconto



''' + kabum_GTX1660Ti_GamingX + '''
                                            ''')

            

            
            break
            while True:
                time.sleep(37)
                try:
    

                    kabum_GTX1660Ti_GamingX = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=100855'
                    page_kabum_GTX1660Ti_GamingX = requests.get(kabum_GTX1660Ti_GamingX, headers=headers)
                    soup_kabum_GTX1660Ti_GamingX = BeautifulSoup(page_kabum_GTX1660Ti_GamingX.content,'html.parser')
                    price_kabum_GTX1660Ti_GamingX = soup_kabum_GTX1660Ti_GamingX.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

                except:
                    kabum_GTX1660Ti_GamingX = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=100855'
         
                    api.destroy_status(kabum_GTX1660Ti_GamingX_Promocao)
                    return KabumGTX1660Ti_GamingX()



















def KabumRTX2060_TUF():
    
    while True:
        time.sleep(38)
        try:
            kabum_RTX2060_TUF = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=101228'
            page_kabum_RTX2060_TUF = requests.get(kabum_RTX2060_TUF, headers=headers)
            soup_kabum_RTX2060_TUF = BeautifulSoup(page_kabum_RTX2060_TUF.content,'html.parser')

            try:
                status_kabum_RTX2060_TUF = soup_kabum_RTX2060_TUF.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_on.gif").get("alt")
            except:
                status_kabum_RTX2060_TUF = soup_kabum_RTX2060_TUF.find(src="https://static.kabum.com.br/conteudo/temas/001/imagens/descricao/bot_disponibilidade_off.gif").get("alt")

        except:
            kabum_RTX2060_TUF = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=101228'
  
            price_kabum_RTX2060_TUF = soup_kabum_RTX2060_TUF.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

    
        


        
            status_kabum_RTX2060_TUF = 'PROMOÇÃO'
    
            oldPrice_kabum_RTX2060_TUF = soup_kabum_RTX2060_TUF.find('div', class_='preco_antigo-cm').get_text()
            newPrice_kabum_RTX2060_TUF = soup_kabum_RTX2060_TUF.find('div', class_='preco_desconto-cm').find('strong').get_text()
   
        
            kabum_RTX2060_TUF_Promocao = api.update_status('''
            
PROMOÇÃO:

RTX 2060 (TUF - Asus)

''' + oldPrice_kabum_RTX2060_TUF + '''
''' + newPrice_kabum_RTX2060_TUF + '''


Preço: R$''' + price_kabum_RTX2060_TUF + '''
Á vista no boleto bancário com 15% de desconto



''' + kabum_RTX2060_TUF + '''
                                            ''')

            

            
            break
            while True:
                time.sleep(38)
                try:
    

                    kabum_RTX2060_TUF = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=101228'
                    page_kabum_RTX2060_TUF = requests.get(kabum_RTX2060_TUF, headers=headers)
                    soup_kabum_RTX2060_TUF = BeautifulSoup(page_kabum_RTX2060_TUF.content,'html.parser')
                    price_kabum_RTX2060_TUF = soup_kabum_RTX2060_TUF.find('div', class_='preco_normal-cm').find('span', class_='preco_desconto_avista-cm').get_text()

                except:
                    kabum_RTX2060_TUF = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=101228'
         
                    api.destroy_status(kabum_RTX2060_TUF_Promocao)
                    return KabumRTX2060_TUF()

















                
def KabumRTX2060_GamingOCPro():
    time.sleep(45)
    while True:
        if Kabum.RTX2060_GamingOCPro.status() != PROMOÇÃO:
            print('')


        else:
            kabum_RTX2060_GamingOCPro_Promocao = api.update_status('''

PROMOÇÃO:

RTX2060 (GamingOCPro - Gigabyte)

''' + Kabum.RTX2060_GamingOCPro.oldPrice() + '''
''' + Kabum.RTX2060_GamingOCPro.newPrice() + '''


Preço: R$''' + Kabum.RTX2060_GamingOCPro.price() + '''
Á vista no boleto bancário com 15% de desconto



''' + Kabum.RTX2060_GamingOCPro.link() + '''


                                                                    ''')
            
            break
            while True:
          
                if Kabum.RTX2060_GamingOCPro.status() == indisponivel:
                    api.destroy_status(kabum_RTX2060_GamingOCPro_Promocao)
                    return KabumRTX2060_GamingOCPRO()









def KabumRTX2060KO_UltraGaming():
    time.sleep(46)
    while True:
        if Kabum.RTX2060KO_UltraGaming.status() != PROMOÇÃO:
            print('')


        else:
            kabum_RTX2060KO_UltraGaming_Promocao = api.update_status('''

PROMOÇÃO:

RTX2060KO (Ultra Gaming - EVGA)

''' + Kabum.RTX2060KO_UltraGaming.oldPrice() + '''
''' + Kabum.RTX2060KO_UltraGaming.newPrice() + '''


Preço: R$''' + Kabum.RTX2060KO_UltraGaming.price() + '''
Á vista no boleto bancário com 15% de desconto



''' + Kabum.RTX2060KO_UltraGaming.link() + '''


                                                                    ''')
            
            break
            while True:
          
                if Kabum.RTX2060KO_UltraGaming.status() == indisponivel:
                    api.destroy_status(kabum_RTX2060KO_UltraGaming_Promocao)
                    return KabumRTX2060KO_UltraGaming()







                


def KabumRTX2060Super_OneClickOC():
    time.sleep(47)
    while True:
        if Kabum.RTX2060Super_OneClickOC.status() != PROMOÇÃO:
            print('')


        else:
            kabum_RTX2060Super_OneClickOC_Promocao = api.update_status('''
PROMOÇÃO:

RTX2060Super (1Click OC - Galax)

''' + Kabum.RTX2060Super_OneClickOC.oldPrice() + '''
''' + Kabum.RTX2060Super_OneClickOC.newPrice() + '''


Preço: R$''' + Kabum.RTX2060Super_OneClickOC.price() + '''
Á vista no boleto bancário com 15% de desconto



''' + Kabum.RTX2060Super_OneClickOC.link() + '''


                                                                    ''')
            
            break
            while True:
          
                if Kabum.RTX2060Super_OneClickOC.status() == indisponivel:
                    api.destroy_status(kabum_RTX2060Super_OneClickOC_Promocao)
                    return KabumRTX2060Super_OneClickOC()


def KabumRTX2070Super_DualEvo():
    time.sleep(48)
    while True:
        if Kabum.RTX2070Super_DualEvo.status() != PROMOÇÃO:
            print('')


        else:
            kabum_RTX2070Super_DualEvo_Promocao = api.update_status('''
PROMOÇÃO:

RTX2070Super (Dual Evo - Asus)

''' + Kabum.RTX2070Super_DualEvo.oldPrice() + '''
''' + Kabum.RTX2070Super_DualEvo.newPrice() + '''


Preço: R$''' + Kabum.RTX2070Super_DualEvo.price() + '''
Á vista no boleto bancário com 15% de desconto



''' + Kabum.RTX2070Super_DualEvo.link() + '''


                                                                    ''')
            
            break
            while True:
          
                if Kabum.RTX2070Super_DualEvo.status() == indisponivel:
                    api.destroy_status(kabum_RTX2070Super_DualEvo_Promocao)
                    return KabumRTX2070Super_DualEvo()








def KabumRTX2080Super_GamingOCWhite():
    time.sleep(49)
    while True:
        if Kabum.RTX2080Super_GamingOCWhite.status() != PROMOÇÃO:
            print('')


        else:
            kabum_RTX2080Super_GamingOCWhite_Promocao = api.update_status('''
PROMOÇÃO:

RTX2080Super (Gaming OC White - Gigabyte)

''' + Kabum.RTX2080Super_GamingOCWhite.oldPrice() + '''
''' + Kabum.RTX2080Super_GamingOCWhite.newPrice() + '''


Preço: R$''' + Kabum.RTX2080Super_GamingOCWhite.price() + '''
Á vista no boleto bancário com 15% de desconto



''' + Kabum.RTX2080Super_GamingOCWhite.link() + '''


                                                                    ''')
            
            break
            while True:
          
                if Kabum.RTX2080Super_GamingOCWhite.status() == indisponivel:
                    api.destroy_status(kabum_RTX2080Super_GamingOCWhite_Promocao)
                    return KabumRTX2080Super_GamingOCWhite()    








def KabumRTX2080Super_ROGStrix():
    time.sleep(50)
    while True:
        if Kabum.RTX2080Super_ROGStrix.status() != PROMOÇÃO:
            print('')


        else:
            kabum_RTX2080Super_ROGStrix_Promocao = api.update_status('''
PROMOÇÃO:

RTX2080Super (ROG Strix - Asus)

''' + Kabum.RTX2080Super_ROGStrix.oldPrice() + '''
''' + Kabum.RTX2080Super_ROGStrix.newPrice() + '''


Preço: R$''' + Kabum.RTX2080Super_ROGStrix.price() + '''
Á vista no boleto bancário com 15% de desconto



''' + Kabum.RTX2080Super_ROGStrix.link() + '''


                                                                    ''')
            
            break
            while True:
          
                if Kabum.RTX2080Super_ROGStrix.status() == indisponivel:
                    api.destroy_status(kabum_RTX2080Super_ROGStrix_Promocao)
                    return KabumRTX2080Super_ROGStrix() 




def KabumRTX2080Super_HOFBlack():
    time.sleep(51)
    while True:
        if Kabum.RTX2080Super_HOFBlack.status() != PROMOÇÃO:
            print('{}'.format(status_kabum_RTX2080Super_HOFBlack))


        else:
            kabum_RTX2080Super_HOFBlack_Promocao = api.update_status('''
PROMOÇÃO:

RTX2080Super (Hall Of Fame Black Edition - Galax)

''' + Kabum.RTX2080Super_HOFBlack.oldPrice() + '''
''' + Kabum.RTX2080Super_HOFBlack.newPrice() + '''


Preço: R$''' + Kabum.RTX2080Super_HOFBlack.price() + '''
Á vista no boleto bancário com 15% de desconto



''' + Kabum.RTX2080Super_HOFBlack.link + '''


                                                                    ''')
            
            break
            while True:
          
                if Kabum.RTX2080Super_HOFBlack.status() == indisponivel:
                    api.destroy_status(kabum_RTX2080Super_HOFBlack_Promocao)
                    return KabumRTX2080Super_HOFBlack()






def TerabyteB450M_TufPlusGaming():
    while True:
        terabyte_B450M_TufPlusGaming = 'https://www.terabyteshop.com.br/produto/10223/placa-mae-asus-tuf-b450m-plus-gaming-usb-31-am4?p=231814'

        page_terabyte_B450M_TufPlusGaming = requests.get(terabyte_B450M_TufPlusGaming, headers=headers)
        soup_terabyte_B450M_TufPlusGaming = BeautifulSoup(page_terabyte_B450M_TufPlusGaming.content,'html.parser')
  
    
  
    
        try:
            oferta_terabyte_B450M_TufPlusGaming = soup_terabyte_B450M_TufPlusGaming.find('div', class_='areaEmPromo')
            price_terabyte_B450M_TufPlusGaming = soup_terabyte_B450M_TufPlusGaming.find('p', id="valVista", class_="val-prod valVista").get_text()
            oldPrice_terabyte_B450M_TufPlusGaming = soup_terabyte_B450M_TufPlusGaming.find('p', class_='precode').find('del').get_text()
            newPrice_terabyte_B450M_TufPlusGaming = soup_terabyte_B450M_TufPlusGaming.find('span', id='valParc', class_='valParc').get_text()

            terabyte_B450M_TufPlusGaming_Promocao = api.update_status('''

PROMOÇÃO:

B450M (TUF Plus Gaming - Asus)

De ''' + oldPrice_terabyte_B450M_TufPlusGaming + ''' por:
''' + newPrice_terabyte_B450M_TufPlusGaming + '''


Preço: R$''' + terabyte_B450M_TufPlusGaming + '''
Á vista no boleto bancário com 13% de desconto



''' + terabyte_B450M_TufPlusGaming + '''
      
''')
            
            break
            while True:
                try:
                    terabyte_B450M_TufPlusGaming = 'https://www.terabyteshop.com.br/produto/10223/placa-mae-asus-tuf-b450m-plus-gaming-usb-31-am4?p=231814'
                    page_terabyte_B450M_TufPlusGaming = requests.get(terabyte_B450M_TufPlusGaming, headers=headers)
                    soup_terabyte_B450M_TufPlusGaming = BeautifulSoup(page_terabyte_B450M_TufPlusGaming.content,'html.parser')
                    oferta_terabyte_B450M_TufPlusGaming = soup_terabyte_B450M_TufPlusGaming.find('div', class_='areaEmPromo')
                except:
                    api.destroy_status(terabyte_B450M_TufPlusGaming_Promocao)
                    return TerabyteB450M_TufPlusGaming()
       
            

        except:
            return TerabyteB450M_TufPlusGaming()





def TerabyteB450M_TufPROGaming():
    while True:
        terabyte_B450M_TufPROGaming = 'https://www.terabyteshop.com.br/produto/11278/placa-mae-asus-tuf-b450m-pro-gaming-chipset-b450-amd-am4-ddr4?gclid=CjwKCAjwj975BRBUEiwA4whRB3Bjf7ex16j1UaNS5qP5sgJ5rlR4VNKDrK8GE8gjJbe-Rtf62p5wHxoCk_wQAvD_BwE'

        page_terabyte_B450M_TufPROGaming = requests.get(terabyte_B450M_TufPROGaming, headers=headers)
        soup_terabyte_B450M_TufPROGaming = BeautifulSoup(page_terabyte_B450M_TufPROGaming.content,'html.parser')
  
    
  
    
        try:
            oferta_terabyte_B450M_TufPROGaming = soup_terabyte_B450M_TufPROGaming.find('div', class_='areaEmPromo')
            price_terabyte_B450M_TufPROGaming = soup_terabyte_B450M_TufPROGaming.find('p', id="valVista", class_="val-prod valVista").get_text()
            oldPrice_terabyte_B450M_TufPROGaming = soup_terabyte_B450M_TufPROGaming.find('p', class_='precode').find('del').get_text()
            newPrice_terabyte_B450M_TufPROGaming = soup_terabyte_B450M_TufPROGaming.find('span', id='valParc', class_='valParc').get_text()

            terabyte_B450M_TufPROGaming_Promocao = api.update_status('''

PROMOÇÃO:

B450M (TUF PRO Gaming - Asus)

De ''' + oldPrice_terabyte_B450M_TufPROGaming + ''' por:
''' + newPrice_terabyte_B450M_TufPROGaming + '''


Preço: R$''' + terabyte_B450M_TufPROGaming + '''
Á vista no boleto bancário com 13% de desconto



''' + terabyte_B450M_TufPROGaming + '''
      
                                                                 ''')
            
            break
            while True:
                try:
                    terabyte_B450M_TufPROGaming = 'https://www.terabyteshop.com.br/produto/11278/placa-mae-asus-tuf-b450m-pro-gaming-chipset-b450-amd-am4-ddr4?gclid=CjwKCAjwj975BRBUEiwA4whRB3Bjf7ex16j1UaNS5qP5sgJ5rlR4VNKDrK8GE8gjJbe-Rtf62p5wHxoCk_wQAvD_BwE'

                    page_terabyte_B450M_TufPROGaming = requests.get(terabyte_B450M_TufPROGaming, headers=headers)
                    soup_terabyte_B450M_TufPROGaming = BeautifulSoup(page_terabyte_B450M_TufPROGaming.content,'html.parser')
                    oferta_terabyte_B450M_TufPROGaming = soup_terabyte_B450M_TufPROGaming.find('div', class_='areaEmPromo')
                except:
                    
                    api.destroy_status(terabyteB450M_TufPROGaming_Promocao)


        except:
            return TerabyteB450M_TufPROGaming()
def TerabyteRTX2070Super_DualEvo():
    while True:
        terabyte_RTX2070Super_DualEvo = 'https://www.terabyteshop.com.br/produto/12555/placa-de-video-asus-geforce-rtx-2070-super-evo-dual-8gb-gddr6-256bit-dual-rtx2070s-8g-evo'

        page_terabyte_RTX2070Super_DualEvo = requests.get(terabyte_RTX2070Super_DualEvo, headers=headers)
        soup_terabyte_RTX2070Super_DualEvo = BeautifulSoup(page_terabyte_RTX2070Super_DualEvo.content,'html.parser')
  
    
  
    
        try:
            oferta_terabyte_RTX2070Super_DualEvo = soup_terabyte_RTX2070Super_DualEvo.find('div', class_='areaEmPromo')
            price_terabyte_RTX2070Super_DualEvo = soup_terabyte_RTX2070Super_DualEvo.find('p', id="valVista", class_="val-prod valVista").get_text()
            oldPrice_terabyte_RTX2070Super_DualEvo = soup_terabyte_RTX2070Super_DualEvo.find('p', class_='precode').find('del').get_text()
            newPrice_terabyte_RTX2070Super_DualEvo = soup_terabyte_RTX2070Super_DualEvo.find('span', id='valParc', class_='valParc').get_text()

            terabyte_RTX2070Super_DualEvo_Promocao = api.update_status('''

PROMOÇÃO:

RTX2070Super (Dual Evo - Asus)

De ''' + oldPrice_terabyte_RTX2070Super_DualEvo + ''' por:
''' + newPrice_terabyte_RTX2070Super_DualEvo + '''


Preço: R$''' + terabyte_RTX2070Super_DualEvo + '''
Á vista no boleto bancário com 13% de desconto



''' + terabyte_RTX2070Super_DualEvo + '''
      
                                                             ''')
            
            break
            while True:
                try:
                    terabyte_RTX2070Super_DualEvo = 'https://www.terabyteshop.com.br/produto/12555/placa-de-video-asus-geforce-rtx-2070-super-evo-dual-8gb-gddr6-256bit-dual-rtx2070s-8g-evo'

                    page_terabyte_RTX2070Super_DualEvo = requests.get(terabyte_RTX2070Super_DualEvo, headers=headers)
                    soup_terabyte_RTX2070Super_DualEvo = BeautifulSoup(page_terabyte_RTX2070Super_DualEvo.content,'html.parser')
                    oferta_terabyte_RTX2070Super_DualEvo = soup_terabyte_RTX2070Super_DualEvo.find('div', class_='areaEmPromo')
                except:
                    
                    api.destroy_status(terabyte_RTX2070Super_DualEvo_Promocao)



        except:
            return TerabyteRTX2070Super_DualEvo()

def TerabyteR52600():
    while True:
        terabyte_R52600 = 'https://www.terabyteshop.com.br/produto/9264/processador-amd-ryzen-5-2600-34ghz-39ghz-max-turbo-yd2600bbafbox-r2l-six-core-16mb-cooler-wraith-stealth-imp'

        page_terabyte_R52600 = requests.get(terabyte_R52600, headers=headers)
        soup_terabyte_R52600 = BeautifulSoup(page_terabyte_R52600.content,'html.parser')
  
    
  
    
        try:
            oferta_terabyte_R52600 = soup_terabyte_R52600.find('div', class_='areaEmPromo')
            price_terabyte_R52600 = soup_terabyte_R52600.find('p', id="valVista", class_="val-prod valVista").get_text()
            oldPrice_terabyte_R52600 = soup_terabyte_R52600.find('p', class_='precode').find('del').get_text()
            newPrice_terabyte_R52600 = soup_terabyte_R52600.find('span', id='valParc', class_='valParc').get_text()

            terabyte_R52600_Promocao = api.update_status('''

PROMOÇÃO:

R5 2600

De ''' + oldPrice_terabyte_R52600 + ''' por:
''' + newPrice_terabyte_R52600 + '''


Preço: R$''' + terabyte_R52600 + '''
Á vista no boleto bancário com 13% de desconto



''' + terabyte_R52600 + '''
      
                                                        ''')
            
            break
            while True:
                try:
                    terabyte_R52600 = 'https://www.terabyteshop.com.br/produto/9264/processador-amd-ryzen-5-2600-34ghz-39ghz-max-turbo-yd2600bbafbox-r2l-six-core-16mb-cooler-wraith-stealth-imp'

                    page_terabyte_R52600 = requests.get(terabyte_R52600, headers=headers)
                    soup_terabyte_R52600 = BeautifulSoup(page_terabyte_R52600.content,'html.parser')
                    oferta_terabyte_R52600 = soup_terabyte_R52600.find('div', class_='areaEmPromo').get_text()

                except:
                    api.destroy_status(terabyte_R52600_Promocao)
        except:
            return TerabyteR52600()

def TerabyteR33100():
    while True:
        terabyte_R33100 = 'https://www.terabyteshop.com.br/produto/13369/processador-amd-ryzen-3-3100-36ghz-39ghz-turbo-4-cores-8-threads-cooler-wraith-stealth-am4-100-100000284box'

        page_terabyte_R33100 = requests.get(terabyte_R33100, headers=headers)
        soup_terabyte_R33100 = BeautifulSoup(page_terabyte_R33100.content,'html.parser')
  
    
  
    
        try:
            oferta_terabyte_R33100 = soup_terabyte_R33100.find('div', class_='areaEmPromo')
            price_terabyte_R33100 = soup_terabyte_R33100.find('p', id="valVista", class_="val-prod valVista").get_text()
            oldPrice_terabyte_R33100 = soup_terabyte_R33100.find('p', class_='precode').find('del').get_text()
            newPrice_terabyte_R33100 = soup_terabyte_R33100.find('span', id='valParc', class_='valParc').get_text()

            terabyte_R33100_Promocao = api.update_status('''

PROMOÇÃO:

R3 3100

De ''' + oldPrice_terabyte_R33100 + ''' por:
''' + newPrice_terabyte_R33100 + '''


Preço: R$''' + terabyte_R33100 + '''
Á vista no boleto bancário com 13% de desconto



''' + terabyte_R33100 + '''
      
                                                        ''')
            
            break
            while True:
                try:
                    terabyte_R33100 = 'https://www.terabyteshop.com.br/produto/13369/processador-amd-ryzen-3-3100-36ghz-39ghz-turbo-4-cores-8-threads-cooler-wraith-stealth-am4-100-100000284box'

                    page_terabyte_R33100 = requests.get(terabyte_R33100, headers=headers)
                    soup_terabyte_R33100 = BeautifulSoup(page_terabyte_R33100.content,'html.parser')
                    oferta_terabyte_R33100 = soup_terabyte_R33100.find('div', class_='areaEmPromo').get_text()
                except:
                    
                    api.destroy_status(terabyte_R33100_Promocao)


        except:
            return TerabyteR33100()













                    
if __name__ == '__main__':

    KabumRyzen51600AF = Thread(target = KabumR51600AF)
    KabumRyzen32200G = Thread(target = KabumR32200G)
    KabumRyzen52600 = Thread(target = KabumR52600)
    KabumRyzen53600 = Thread(target = KabumR53600)
    KabumRyzen53600X = Thread(target = KabumR53600X)
    KabumRyzen73700X = Thread(target = KabumR73700X)
    KabumRyzen73800X = Thread(target = KabumR73800X)
    KabumRyzen93900X = Thread(target = KabumR93900X)
    KabumRyzen33300X = Thread(target = KabumR33300X)
    
    KabumRyzen51600AF.start()
    KabumRyzen32200G.start()
    KabumRyzen52600.start()
    KabumRyzen53600.start()
    KabumRyzen53600X.start()
    KabumRyzen73700X.start()
    KabumRyzen73800X.start()
    KabumRyzen93900X.start()
    KabumRyzen33300X.start()
    
    KabumRadeonRx5704gb_PhantomGaming = Thread(target = KabumRx5704gb_PhantomGaming)
    KabumRadeonRx5704gb_Gaming4G = Thread(target = KabumRx5704gb_Gaming4G)
    KabumRadeonRx5808gb_ArezDual = Thread(target = KabumRx5808gb_ArezDual)
    KabumRadeonRx5704gb_XFXRSXXX = Thread(target = KabumRx5704gb_XFXRSXXX)
    KabumRadeonRx5500XT4gb_GamingOC = Thread(target = KabumRx5500XT4gb_GamingOC)
    #KabumRadeonRx5500XT8gb_Pulse = Thread(target = KabumRx5500XT8gb_Pulse)    
    KabumRadeonRx5600XT_Windforce = Thread(target = KabumRx5600XT_Windforce)
    KabumRadeonRx5700_TUF = Thread(target = KabumRx5700_TUF)
    KabumRadeonRx5700XT_TUF = Thread(target = KabumRx5700XT_TUF)
    KabumMOBOa320M_KBR = Thread(target = Kabuma320M_KBR)
    KabumMOBOb450M_SteelLegend = Thread(target = Kabumb450M_SteelLegend)
    KabumCorei39100F = Thread(target = Kabumi39100F)
    KabumCorei59400F = Thread(target = Kabumi59400F)
    KabumCorei59600K = Thread(target = Kabumi59600K)
    KabumCorei59600KF = Thread(target = Kabumi59600KF)
    KabumCorei79700F = Thread(target = Kabumi79700F)
    KabumCorei79700K = Thread(target = Kabumi79700K)
    KabumCorei79700KF = Thread(target = Kabumi79700KF)
    KabumCorei99900K = Thread(target = Kabumi99900K)
    KabumCorei99900KF = Thread(target = Kabumi99900KF)
    KabumCorei310100 = Thread(target = Kabumi310100)
    KabumCorei510400 = Thread(target = Kabumi510400)
    KabumCorei510400F = Thread(target = Kabumi510400F)
    KabumCorei710700 = Thread(target = Kabumi710700)
    KabumCorei710700K = Thread(target = Kabumi710700K)
    KabumCorei910900K = Thread(target = Kabumi910900K)
    
    TerabyteMOBOB450M_TufPlusGaming = Thread(target = TerabyteB450M_TufPlusGaming)
    TerabyteMOBOB450M_TufPROGaming  = Thread(target = TerabyteB450M_TufPROGaming)
    TerabyteMOBOB450M_TufPlusGaming.start()
    TerabyteMOBOB450M_TufPROGaming.start()
    TerabyteRyzen52600 = Thread(target = TerabyteR52600)
    TerabyteRyzen33100 = Thread(target = TerabyteR33100)
    TerabyteRyzen52600.start()
    TerabyteRyzen33100.start()

    TerabyteGeForceRTX2070Super_DualEvo = Thread(target = TerabyteRTX2070Super_DualEvo)
    TerabyteGeForceRTX2070Super_DualEvo.start()
    KabumRadeonRx5704gb_PhantomGaming.start()
    KabumRadeonRx5704gb_Gaming4G.start()
    KabumRadeonRx5704gb_XFXRSXXX.start()
    KabumRadeonRx5500XT4gb_GamingOC.start()
    #KabumRadeonRx5500XT8gb_Pulse.start()
    KabumRadeonRx5600XT_Windforce.start()
    KabumRadeonRx5700_TUF.start()
    KabumRadeonRx5700XT_TUF.start()
    KabumMOBOa320M_KBR.start()
    #KabumMOBOb450M_SteelLegend.start()
    KabumCorei39100F.start()
    KabumCorei59400F.start()
    KabumCorei59600K.start()
    KabumCorei59600KF.start()
    KabumCorei79700F.start()
    KabumCorei79700K.start()
    KabumCorei79700KF.start()
    KabumCorei99900K.start()
    KabumCorei99900KF.start()
    KabumCorei310100.start()
    KabumCorei510400.start()
    KabumCorei510400F.start()
    KabumCorei710700.start()
    KabumCorei910900K.start()

    #KabumMOBOb450M_SteelLegend.start()
    KabumGeForceGTX1660_GigabyteOC = Thread(target = KabumGTX1660_GigabyteOC)
    KabumGeForceRTX2060_TUF = Thread(target = KabumRTX2060_TUF)
    KabumGeForceRTX2060_TUF.start()
    KabumGeForceGTX1660_GigabyteOC.start()

    TerabyteMOBOB450M_TufPlusGaming = Thread(target = TerabyteB450M_TufPlusGaming)
    TerabyteMOBOB450M_TufPROGaming  = Thread(target = TerabyteB450M_TufPROGaming)
    TerabyteMOBOB450M_TufPlusGaming.start()
    TerabyteMOBOB450M_TufPROGaming.start()
    TerabyteRyzen52600 = Thread(target = TerabyteR52600)
    TerabyteRyzen33100 = Thread(target = TerabyteR33100)
    TerabyteRyzen52600.start()
    TerabyteRyzen33100.start()

    TerabyteGeForceRTX2070Super_DualEvo = Thread(target = TerabyteRTX2070Super_DualEvo)
    TerabyteGeForceRTX2070Super_DualEvo.start()
    
