import requests
from bs4 import BeautifulSoup
import smtplib
import openpyxl
from openpyxl import Workbook
from datetime import date

#CPUs:
try:
    

    kabum_R51600AF = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=107545'

except:
    kabum_R51600AF = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=107545'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}




page_kabum_R51600AF = requests.get(kabum_R51600AF, headers=headers)
soup_kabum_R51600AF = BeautifulSoup(page_kabum_R51600AF.content,'html.parser')


title_kabum_R51600AF = soup_kabum_R51600AF.find(itemprop='name').get_text()
price_kabum_R51600AF = soup_kabum_R51600AF.find(itemprop='price').get('content')
print(title_kabum_R51600AF)
print(price_kabum_R51600AF)



 
try:
    kabum_R32200G = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=94723'

        
        
except:
    kabum_R32200G = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=94723'


page_kabum_R32200G = requests.get(kabum_R32200G, headers=headers)
soup_kabum_R32200G = BeautifulSoup(page_kabum_R32200G.content,'html.parser')

title_kabum_R32200G = soup_kabum_R32200G.find(itemprop='name').get_text()
price_kabum_R32200G = soup_kabum_R32200G.find(itemprop='price').get('content')
print(title_kabum_R32200G)
print(price_kabum_R32200G)

try:
    
    kabum_R52600 = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=95557'
except:
    kabum_R52600 = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=95557'
page_kabum_R52600 = requests.get(kabum_R52600, headers=headers)
soup_kabum_R52600 = BeautifulSoup(page_kabum_R52600.content,'html.parser')

title_kabum_R52600 = soup_kabum_R52600.find(itemprop='name').get_text()
price_kabum_R52600 = soup_kabum_R52600.find(itemprop='price').get('content')
print(title_kabum_R52600)
print(price_kabum_R52600)

try:
    

    kabum_R53600 = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=102438'
except:
    kabum_R53600 = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=102438'
    
page_kabum_R53600 = requests.get(kabum_R53600, headers=headers)
soup_kabum_R53600 = BeautifulSoup(page_kabum_R53600.content,'html.parser')

title_kabum_R53600 = soup_kabum_R53600.find(itemprop='name').get_text()
price_kabum_R53600 = soup_kabum_R53600.find(itemprop='price').get('content')

print(title_kabum_R53600)
print(price_kabum_R53600)



try:
    
    kabum_R72700 = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=95564'
except:
    kabum_R72700 = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=95564'
    
page_kabum_R72700 = requests.get(kabum_R72700, headers=headers)
soup_kabum_R72700 = BeautifulSoup(page_kabum_R72700.content,'html.parser')

title_kabum_R72700 = soup_kabum_R72700.find(itemprop='name').get_text()
price_kabum_R72700 = soup_kabum_R72700.find(itemprop='price').get('content')
print(title_kabum_R72700)
print(price_kabum_R72700)

try:
    
    kabum_R73700X = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=102436'
except:
    kabum_R73700X = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=102436'
page_kabum_R73700X = requests.get(kabum_R73700X, headers=headers)
soup_kabum_R73700X = BeautifulSoup(page_kabum_R73700X.content,'html.parser')

title_kabum_R73700X = soup_kabum_R73700X.find(itemprop='name').get_text()
price_kabum_R73700X = soup_kabum_R73700X.find(itemprop='price').get('content')
print(title_kabum_R73700X)
print(price_kabum_R73700X)
try:
    
    kabum_R73800X = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=102435'
except:
    kabum_R73800X = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=102435'
page_kabum_R73800X = requests.get(kabum_R73800X, headers=headers)
soup_kabum_R73800X = BeautifulSoup(page_kabum_R73800X.content,'html.parser')

title_kabum_R73800X = soup_kabum_R73800X.find(itemprop='name').get_text()
price_kabum_R73800X = soup_kabum_R73800X.find(itemprop='price').get('content')
print(title_kabum_R73800X)
print(price_kabum_R73800X)
try:
    kabum_R93900X = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=102434'
except:
    kabum_R93900X = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=102434'
page_kabum_R93900X = requests.get(kabum_R93900X, headers=headers)
soup_kabum_R93900X = BeautifulSoup(page_kabum_R93900X.content,'html.parser')
title_kabum_R93900X = soup_kabum_R93900X.find(itemprop='name').get_text()
price_kabum_R93900X = soup_kabum_R93900X.find(itemprop='price').get('content')
print(title_kabum_R93900X)
print(price_kabum_R93900X)


try:
    kabum_R33300X = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=113391'
except:
    kabum_R33300X = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=113391'

page_kabum_R33300X = requests.get(kabum_R33300X, headers=headers)
soup_kabum_R33300X = BeautifulSoup(page_kabum_R33300X.content,'html.parser')
title_kabum_R33300X = soup_kabum_R33300X.find(itemprop='name').get_text()
price_kabum_R33300X = soup_kabum_R33300X.find(itemprop='price').get('content')
print(title_kabum_R33300X)
print(price_kabum_R33300X)

try:
    kabum_R33200G = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=102248'
except:
    kabum_R33200G = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=102248'


page_kabum_R33200G = requests.get(kabum_R33200G, headers=headers)
soup_kabum_R33200G = BeautifulSoup(page_kabum_R33200G.content,'html.parser')
title_kabum_R33200G = soup_kabum_R33200G.find(itemprop='name').get_text()
price_kabum_R33200G = soup_kabum_R33200G.find(itemprop='price').get('content')
print(title_kabum_R33200G)
print(price_kabum_R33200G)



try:
    kabum_R53600X = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=102437'
except:
    kabum_R53600X = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=102437'



page_kabum_R53600X = requests.get(kabum_R53600X, headers=headers)
soup_kabum_R53600X = BeautifulSoup(page_kabum_R53600X.content,'html.parser')

title_kabum_R53600X = soup_kabum_R53600X.find(itemprop='name').get_text()
price_kabum_R53600X = soup_kabum_R53600X.find(itemprop='price').get('content')

print(title_kabum_R53600X)
print(price_kabum_R53600X)


#GPUs:

try:
    kabum_Rx5704gb_PhantomGaming = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=102833'
except:
    kabum_Rx5704gb_PhantomGaming = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=102833'


page_kabum_Rx5704gb_PhantomGaming = requests.get(kabum_Rx5704gb_PhantomGaming,  headers=headers)
soup_kabum_Rx5704gb_PhantomGaming = BeautifulSoup(page_kabum_Rx5704gb_PhantomGaming.content,'html.parser')

title_kabum_Rx5704gb_PhantomGaming = soup_kabum_Rx5704gb_PhantomGaming.find(itemprop='name').get_text()
price_kabum_Rx5704gb_PhantomGaming = soup_kabum_Rx5704gb_PhantomGaming.find(itemprop='price').get('content')

print(title_kabum_Rx5704gb_PhantomGaming)
print(price_kabum_Rx5704gb_PhantomGaming)




try:
    kabum_Rx5708gb_PhantomGaming = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=102832'
except:
    kabum_Rx5708gb_PhantomGaming = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=102832'

 
page_kabum_Rx5708gb_PhantomGaming = requests.get(kabum_Rx5708gb_PhantomGaming, headers=headers)
soup_kabum_Rx5708gb_PhantomGaming = BeautifulSoup(page_kabum_Rx5708gb_PhantomGaming.content,'html.parser')

title_kabum_Rx5708gb_PhantomGaming = soup_kabum_Rx5708gb_PhantomGaming.find(itemprop='name').get_text()
price_kabum_Rx5708gb_PhantomGaming = soup_kabum_Rx5708gb_PhantomGaming.find(itemprop='price').get('content')

print(title_kabum_Rx5708gb_PhantomGaming)
print(price_kabum_Rx5708gb_PhantomGaming)

try:
    kabum_Rx5704gb_Gaming4G = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=88748'

except:
    kabum_Rx5704gb_Gaming4G = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=88748'

page_kabum_Rx5704gb_Gaming4G = requests.get(kabum_Rx5704gb_Gaming4G, headers=headers)
soup_kabum_Rx5704gb_Gaming4G = BeautifulSoup(page_kabum_Rx5704gb_Gaming4G.content,'html.parser')

title_kabum_Rx5704gb_Gaming4G = soup_kabum_Rx5704gb_Gaming4G.find(itemprop='name').get_text()
price_kabum_Rx5704gb_Gaming4G = soup_kabum_Rx5704gb_Gaming4G.find(itemprop='price').get('content')



print(title_kabum_Rx5704gb_Gaming4G)
print(price_kabum_Rx5704gb_Gaming4G)



try:
    kabum_Rx5708gb_Gaming8G = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=102040'

except:
    kabum_Rx5708gb_Gaming8G = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=102040'
    



page_kabum_Rx5708gb_Gaming8G = requests.get(kabum_Rx5708gb_Gaming8G, headers=headers)
soup_kabum_Rx5708gb_Gaming8G = BeautifulSoup(page_kabum_Rx5708gb_Gaming8G.content,'html.parser')

title_kabum_Rx5708gb_Gaming8G = soup_kabum_Rx5708gb_Gaming8G.find(itemprop='name').get_text()
price_kabum_Rx5708gb_Gaming8G = soup_kabum_Rx5708gb_Gaming8G.find(itemprop='price').get('content')



print(title_kabum_Rx5708gb_Gaming8G)
print(price_kabum_Rx5708gb_Gaming8G)



try:
    kabum_Rx5704gb_XFXRSXXX = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=93572'
except:
    kabum_Rx5704gb_XFXRSXXX = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=93572'

page_kabum_Rx5704gb_XFXRSXXX = requests.get(kabum_Rx5704gb_XFXRSXXX, headers=headers)
soup_kabum_Rx5704gb_XFXRSXXX = BeautifulSoup(page_kabum_Rx5704gb_XFXRSXXX.content,'html.parser')

title_kabum_Rx5704gb_XFXRSXXX = soup_kabum_Rx5704gb_XFXRSXXX.find(itemprop='name').get_text()
price_kabum_Rx5704gb_XFXRSXXX = soup_kabum_Rx5704gb_XFXRSXXX.find(itemprop='price').get('content')



print(title_kabum_Rx5704gb_XFXRSXXX)
print(price_kabum_Rx5704gb_XFXRSXXX)





try:
    kabum_Rx590_Gaming8G = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=104002'


except:
    kabum_Rx590_Gaming8G = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=104002'


page_kabum_Rx590_Gaming8G = requests.get(kabum_Rx590_Gaming8G, headers=headers)
soup_kabum_Rx590_Gaming8G = BeautifulSoup(page_kabum_Rx590_Gaming8G.content,'html.parser')

title_kabum_Rx590_Gaming8G = soup_kabum_Rx590_Gaming8G.find(itemprop='name').get_text()
price_kabum_Rx590_Gaming8G = soup_kabum_Rx590_Gaming8G.find(itemprop='price').get('content')



print(title_kabum_Rx590_Gaming8G)
print(price_kabum_Rx590_Gaming8G)


try:
    kabum_Rx5500XT4gb_GamingOC = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=109644'

except:
    kabum_Rx5500XT4gb_GamingOC = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=109644'


page_kabum_Rx5500XT4gb_GamingOC = requests.get(kabum_Rx5500XT4gb_GamingOC, headers=headers)
soup_kabum_Rx5500XT4gb_GamingOC = BeautifulSoup(page_kabum_Rx5500XT4gb_GamingOC.content,'html.parser')

title_kabum_Rx5500XT_GamingOC = soup_kabum_Rx5500XT4gb_GamingOC.find(itemprop='name').get_text()
price_kabum_Rx5500XT4gb_GamingOC = soup_kabum_Rx5500XT4gb_GamingOC.find(itemprop='price').get('content')
print(title_kabum_Rx5500XT_GamingOC)
print(price_kabum_Rx5500XT4gb_GamingOC)
try:
    kabum_Rx5500XT8gb_Pulse = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao.cgi?codigo=109852'

except:
    kabum_Rx5500XT8gb_Pulse = 'https://www.kabum.com.br/cgi-local/site/produtos/descricao_ofertas.cgi?codigo=109852'


page_kabum_Rx5500XT8gb_Pulse = requests.get(kabum_Rx5500XT8gb_Pulse, headers=headers)
soup_kabum_Rx5500XT8gb_Pulse = BeautifulSoup(page_kabum_Rx5500XT8gb_Pulse.content,'html.parser')

title_kabum_Rx5500XT8gb_Pulse = soup_kabum_Rx5500XT8gb_Pulse.find(itemprop='name').get_text()
price_kabum_Rx5500XT8gb_Pulse = soup_kabum_Rx5500XT8gb_Pulse.find(itemprop='price').get('content')

print(title_kabum_Rx5500XT8gb_Pulse)
print(price_kabum_Rx5500XT8gb_Pulse)
















































    
