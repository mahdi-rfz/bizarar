import requests
import threading
import time
import telebot

def timeManager():
    #time chart 
    # 6-8/8-9/9-10/10-11/11-12/12-14/14-18/18-24
    request_url = requests.get("https://api.keybit.ir/time/")
    apiRequest = request_url.json()
    timeStat = (((apiRequest["time24"])["full"])["en"])
    originTime = (timeStat[0:2])
    if originTime[0] == "0" :
        originTime = originTime.replace("0" , "")
        originTime = int(originTime)
        originTime = originTime - 1
    else :
        originTime = int(originTime)
        originTime = originTime - 1
        
    return originTime
        
        

def requestManager():
    global requestUrl1
    
    apiUrl1 = ("http://api.navasan.tech/latest/?api_key=freeFK1ZkQ5w6xvLu120Wolyr32IGrSu")        #enter api url 1
    apiUrl2 = ("http://api.navasan.tech/latest/?api_key=freeFK1ZkQ5w6xvLu120Wolyr32IGrSu")        #enter api url 2
    
    while True :
        time = timeManager()
        if time > 6 and time <8 :
            requestUrl1 = requests.get(apiUrl1)
            time.sleep(7500) # 2h && 5 min
        elif time > 8 and time < 9 :
            requestUrl1 = requests.get(apiUrl2)
            time.sleep(3900) #1h && 5min
        elif time > 9 and time < 10 :
            requestUrl1 = requests.get(apiUrl1)
            time.sleep(3900) #1h && 5min
        elif time > 10 and time < 11 :
            requestUrl1 = requests.get(apiUrl2)
            time.sleep(3900) #1h && 5min
        elif time > 11 and time < 12 :
            requestUrl1 = requests.get(apiUrl1)
            time.sleep(3900) #1h && 5min
        elif time > 12 and time < 14 :
            requestUrl1 = requests.get(apiUrl2)
            time.sleep(7500) # 2h && 5 min
        elif time > 14 and time < 18 :
            requestUrl1 = requests.get(apiUrl1)
            time.sleep(14700) # 4h && 5min
        elif time > 18 and time < 24 :
            requestUrl1 = requests.get(apiUrl2)
            time.sleep(21900) # 6h && 5 min
            


def responseManager ():
    apiResponse = requestUrl1.json()
    global usdValue , usdDate
    usdValue = ((apiResponse["usd"])["value"])
    usdDate = ((apiResponse["usd"])["date"])

    global eurValue , eurDate
    eurValue = ((apiResponse["eur"])["value"])
    eurDate = ((apiResponse["eur"])["date"])
    
    global dirhamDubaiValue , dirhamDubaiDate
    dirhamDubaiValue = ((apiResponse["dirham_dubai"])["value"])
    dirhamDubaiDate =  ((apiResponse["dirham_dubai"])["date"])
    
    global gold18ayarValue , gold18ayarDate
    gold18ayarValue = ((apiResponse["18ayar"])["value"])
    gold18ayarDate = ((apiResponse["18ayar"])["date"])
    
    global baharCoinValue , baharCoinDate
    baharCoinValue = ((apiResponse["bahar"])["value"])
    baharCoinDate = ((apiResponse["bahar"])["date"])
    
    global nimCoinValue , nimCoinDate
    nimCoinValue = ((apiResponse["nim"])["value"])
    nimCoinDate = ((apiResponse["nim"])["date"])

    global robCoinValue , robCoinDate
    robCoinValue = ((apiResponse["rob"])["value"])
    robCoinDate = ((apiResponse["rob"])["date"])    

usdOldPrice =(0)
def usdSwim ():
        newPrice = int(usdValue)
        global usdOldPrice
        if usdOldPrice >  newPrice :
            usdOldPrice = newPrice
            return False
           
        elif usdOldPrice < newPrice :
            usdOldPrice = newPrice
            return True
            
eurOldPricd = (0)
def eurSwim ():
    newPrice = int(eurValue)
    global usdOldPrice
    if eurOldPricd >  newPrice :
        eurOldPricd = newPrice
        return False
        
    elif eurOldPricd < newPrice :
        eurOldPricd = newPrice
        return True
    
goldOldPrice = (0)
def goldSwim ():
    newPrice = int(gold18ayarValue)
    global usdOldPrice
    if goldOldPrice >  newPrice :
        goldOldPrice = newPrice
        return False
        
    elif goldOldPrice < newPrice :
        goldOldPrice = newPrice
        return True

task1 = threading.Thread(target=requestManager)
task2 = threading.Thread(target=responseManager)
task1.start()
task2.start()

while True :
    print(f"dollar price :{usdValue} , update time :{usdDate}")
    print(f"eur price :{eurValue} , update time :{eurDate}")
    time.sleep(120)