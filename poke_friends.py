# %%
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import qrcode as qr
import os


# %%
browser = webdriver.Firefox()
browser.get("https://pokemon-amigos.web.app/pt-br/trainer-codes-pokemon-go")


# %%
uf = browser.find_element_by_xpath("/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-friends-code/ion-content/ion-grid/ion-row[1]/ion-col[2]/mat-card/mat-card-content/ion-row[1]/ion-col[2]/mat-form-field/div/div[1]/div/mat-select/div/div[1]/span")
uf.click()
sleep(.5)
uf = browser.find_element_by_id("mat-option-54")
uf.click()


# %%
cidade = browser.find_element_by_xpath("/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-friends-code/ion-content/ion-grid/ion-row[1]/ion-col[2]/mat-card/mat-card-content/ion-row[1]/ion-col[3]/mat-form-field/div/div[1]/div/mat-select/div/div[1]/span")
cidade.click()
sleep(.5)
cidade = browser.find_element_by_id("mat-option-117")
cidade.click()


# %%
ordem = browser.find_element_by_xpath("/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-friends-code/ion-content/ion-grid/ion-row[1]/ion-col[2]/mat-card/mat-card-content/ion-row[2]/ion-col[1]/mat-form-field/div/div[1]/div/mat-select/div/div[1]/span")
ordem.click()
sleep(.5)
ordem = browser.find_element_by_id("mat-option-1")
ordem.click()


# %%

filtrar = browser.find_element_by_xpath("/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-friends-code/ion-content/ion-grid/ion-row[1]/ion-col[2]/mat-card/mat-card-content/ion-row[2]/ion-col[2]/button")
filtrar.click()
sleep(1)


# %%
import pandas as pd


# %%
files = [x[:-4] for x  in os.listdir('qr_codes')]


# %%
df = pd.DataFrame()


# %%
for _ in range(20):
    try:
        mostrar_mais = browser.find_element_by_xpath("//*[contains(text(), 'Mostrar mais códigos')]")
        mostrar_mais.click()
        df2 = pd.read_html(browser.page_source)[0]
        df = df.append(df2)
        df.drop_duplicates(ignore_index=True)
        print(df.shape)
        sleep(1)
    except:
        sleep(10)


# %%
lista = list(df.Código)
lista = [x.replace(" ","") for x in lista]


# %%
for cod in lista:
    if cod not in files:
        img = qr.make(cod)
        img.save('qr_codes/'+str(cod)+'.png')


# %%
browser.quit()
