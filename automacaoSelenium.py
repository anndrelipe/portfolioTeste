from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

navegador = webdriver.Chrome()
navegador.get(r'https://www.google.com/search?q=cota%C3%A7%C3%A3o+dolar&oq=cota%C3%A7%C3%A3o+dolar&aqs=chrome..69i57j0i67j0i512l8.4387j1j7&sourceid=chrome&ie=UTF-8')
dolar = navegador.find_element(By.XPATH, r'//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
dolar = float(dolar)

navegador.get(r'https://www.google.com/search?q=cota%C3%A7%C3%A3o+euro&oq=cota%C3%A7%C3%A3o+euro&aqs=chrome..69i57j0i512l9.3232j0j4&sourceid=chrome&ie=UTF-8')
euro = navegador.find_element(By.XPATH, r'//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
euro = float(euro)

navegador.get(r'https://www.melhorcambio.com/ouro-hoje')
ouro = navegador.find_element(By.XPATH, r'//*[@id="comercial"]').get_attribute('value')
ouro = ouro.replace(',','.')
ouro = float(ouro)

tabela = pd.read_excel(r'C:\Users\ppeix\OneDrive\Área de Trabalho\Produtos.xlsx')

print(f'OURO: R$ {ouro}, DOLAR: R$ {dolar}, EURO: R$ {euro}')
print(tabela)

tabela.loc[tabela['Moeda'] == 'Dólar', 'Cotação'] = dolar
tabela.loc[tabela['Moeda'] == 'Euro', 'Cotação'] = euro
tabela.loc[tabela['Moeda'] == 'Ouro', 'Cotação'] = ouro

tabela['Preço de Compra'] = tabela['Cotação']*tabela['Preço Original']
tabela['Preço de Venda'] = tabela['Preço de Compra']*tabela['Margem']

tabela.to_excel('Nova Tabela.xlsx')