import pyautogui 
import time
import pyperclip
import pandas as pd
import numpy
import openpyxl

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(3)

pyautogui.click(x=1114, y=627, clicks=2)

pyautogui.click(x=951, y=64)
time.sleep(5)
pyperclip.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
time.sleep(5)


time.sleep(2)
pyautogui.click(x=462, y=345, clicks=2)
time.sleep(5)
pyautogui.click(x=493, y=466)
time.sleep(2)
pyautogui.click(x=1664, y=192)
time.sleep(2)
pyautogui.click(x=1484, y=701)
time.sleep(5)

time.sleep(3)
tabela = pd.read_excel(r'C:\Users\Usuário\Downloads\Vendas - Dez.xlsx')

faturamento = tabela['Valor Final'].sum()
quantidade = tabela['Quantidade'].sum()
faturamento = str(faturamento)
quantidade = str(quantidade)
time.sleep(3)

pyautogui.hotkey('ctrl', 't')
pyperclip.copy('https://mail.google.com/mail/u/0/#inbox')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
time.sleep(5)

pyautogui.click(x=154, y=207)
time.sleep(2)
pyautogui.write('andrepxto.discord@gmail.com')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.write('Faturamento e Quantidade de vendas no dia.')
pyautogui.press('tab')

texto = ('Bom dia,'\
'segue, de acordo com o relatorio de vendas de ONTEM, o numero de:')
texto2 = f'Faturamento: R$,{faturamento},Numero de itens vendidos:,{quantidade}'
pyautogui.write(texto)
pyperclip.copy(texto2)
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('ctrl', 'enter')