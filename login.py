from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time

caminho_driver = 'C:/Users/luisa/Downloads/edgedriver_win64/msedgedriver.exe'
service = Service(executable_path=caminho_driver)

navegador = webdriver.Edge(service=service)
navegador.maximize_window()

navegador.get('https://the-internet.herokuapp.com/login')

time.sleep(2)

campo_usuario = navegador.find_element(By.ID, 'username')

campo_senha = navegador.find_element(By.ID, 'password')

campo_usuario.send_keys('tomsmith')

campo_senha.send_keys('SuperSecretPassword!')

botao_login = navegador.find_element(By.CLASS_NAME, 'radius')

botao_login.click()

time.sleep(2)

mensagem = navegador.find_element(By.ID, 'flash').text.strip()
mensagem = mensagem.replace('\n', ' ').replace('×', '').strip()

print(f"Mensagem capturada: '{mensagem}'")

if 'logged into a secure area' in mensagem.lower():
    print('Login realizado com sucesso!')
else:
    print('Falha no login. Verifique as credenciais.')

navegador.quit()