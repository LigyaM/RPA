# Passo a passo do projeto 

# Passo 1 - Entrar no sistema da empresa
import pyautogui
import time

pyautogui.PAUSE = 1
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.click(x=673, y=442)

pyautogui.click(x=255, y=58)
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(2)

# Passo 2 - Fazer login
pyautogui.click(x=746, y=377)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("minha senha")
pyautogui.press("enter")

pyautogui.click(x=524, y=259)
time.sleep(3)

# Passo 3 - Importar a base de dados
import pandas
tabela = pandas.read_csv("produtos.csv")
print(tabela)

# Passo 4 - Cadastrar os produtos
for linha in tabela.index:

    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs): 
        pyautogui.write(obs) 

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)
