from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime
import login


import csv

file = open('crash_data_'+str(datetime.date.today())+'.csv', 'a', newline = '')
fieldnames = ['odd', 'players', 'prize_pool', 'duration', 'time_span']
writer = csv.DictWriter(file, fieldnames=fieldnames)
writer.writeheader()


def save_data_csv(odd, players, prize_pool, time_span):
    writer.writerow({'odd':odd, 'players':players, 'prize_pool':prize_pool, 'time_span':time_span})

driver = webdriver.Chrome()


url = 'https://blaze.com/en/provably-fair/crash?modal=auth&tab=login'
    
driver.get(url)

elem = driver.find_element_by_name("username")
elem.clear()
elem.send_keys(login.username)


elem = driver.find_element_by_name("password")
elem.clear()
elem.send_keys(login.password)

elem.send_keys(Keys.RETURN)



driver.get('https://blaze.com/en/games/crash')

elem = driver.find_element_by_class_name('entries')
atual=elem.text
anterior=atual

start = time.time()
while(True):
    atual = driver.find_element_by_class_name('entries').text
    pool = driver.find_element_by_class_name('crash-bottom').text
    end = time.time()
    if(atual == anterior):
        pass
    else:
        if(len(atual.split('\n')) == 12):
            print('--------------------')
            anterior = atual
            duracao = end-start
            print('Odd:'+anterior.split('\n')[0],'\n'+pool.split('\n')[0],'\nPool: '+pool.split('\n')[1],'\nDuração: '+str(duracao))
            start = time.time()
            save_data_csv(anterior, pool.split('\n')[0], pool.split('\n')[1], duracao)


