import requests
import threading
import time 
import sys
import os
import datetime
import getpass

def logAction (erorText):
    if os.name == "nt":
        try :
            os.chdir("c:/bizarar")
        except OSError :
            os.chdir("c:/")
            os.mkdir("bizarar")
            os.chdir("c:/bizarar")
    else :
        linuxUser = getpass.getuser()
        try :
            os.chdir(f"/home/{linuxUser}/bizarar")
        except FileNotFoundError :
            os.chdir(f"/home/{linuxUser}")
            os.mkdir("bizarar")
            os.chdir(f"/home/{linuxUser}/bizarar")
    
    file = open("bizarar-log.txt" , "a")
    
    today = datetime.date.today()
    now = datetime.datetime.now()
    currentTime = now.strftime("%H:%M:%S")
    
    file.write(f"{today} {currentTime} {erorText}\n")
    file.close()
    

def timeManager():
    #time chart 
    # 6-8/8-9/9-10/10-11/11-12/12-14/14-18/18-24
    try :
        requestUrl = requests.get("https://api.keybit.ir/time/")
        apiRequest = requestUrl.json()
        timeStat = (((apiRequest["time24"])["hour"])["en"])
        originTime = (timeStat[0:2])
        
        if originTime[0] == "0" :
            originTime = originTime.replace("0" , "")
            originTime = int(originTime)
            originTime = originTime - 1

        else :
            originTime = int(originTime)
            originTime = originTime - 1
    except Exception as e:
        requestUrl = requests.get("https://api.keybit.ir/time/")
        erorController = requestUrl.status_code
        if erorController == (200):
            logAction("You have response 200 which means standard respons in time API") #standard response
        elif erorController == (400):
            logAction("You have response 400 which means bad request in time API") #bad request
        elif erorController == (401):
            logAction("You have response 401 which means unauthrozed in time API") #unauthorized
        elif erorController == (403):
            logAction("You have response 403 which means forbidden in time API") #forbidden
        elif erorController == (404):
            logAction("You have response 404 which means not found in time API") #not found
        else :
            logAction(f"You have an unknown problem with the API of time ---{e}---")
            
        originTime = None
        
    return originTime
        
        

def requestManager():
    
    # If you have an API , you can replace both API addresses     <<<<<<<<<<<<<<-------------------------------
    
    #You can get the API from the following address
    #https://www.navasan.tech/api
    
    apiUrl1 = ("http://api.navasan.tech/latest/?api_key=freeFK1ZkQ5w6xvLu120Wolyr32IGrSu")        #enter api url 1
    apiUrl2 = ("http://api.navasan.tech/latest/?api_key=freeFK1ZkQ5w6xvLu120Wolyr32IGrSu")        #enter api url 2
    
    while True :
        currentTime = timeManager()
        
        if currentTime == None :
            print("You have problem with time API")
            time.sleep(5)
            sys.exit()
        try :
            if currentTime >= 6 and currentTime < 8 :
                requestUrl1 = requests.get(apiUrl1)
                fileManager(requestUrl1)
                time.sleep(7500) # 2h && 5 min
            elif currentTime >= 8 and currentTime < 9 :
                requestUrl1 = requests.get(apiUrl2)
                fileManager(requestUrl1)
                time.sleep(3900) #1h && 5min
            elif currentTime >= 9 and currentTime < 10 :
                requestUrl1 = requests.get(apiUrl1)
                fileManager(requestUrl1)
                time.sleep(3900) #1h && 5min
            elif currentTime >= 10 and currentTime < 11 :
                requestUrl1 = requests.get(apiUrl2)
                fileManager(requestUrl1)
                time.sleep(3900) #1h && 5min
            elif currentTime >= 11 and currentTime < 12 :
                requestUrl1 = requests.get(apiUrl1)
                fileManager(requestUrl1)
                time.sleep(3900) #1h && 5min
            elif currentTime >= 12 and currentTime < 14 :
                requestUrl1 = requests.get(apiUrl2)
                fileManager(requestUrl1)
                time.sleep(7500) # 2h && 5 min
            elif currentTime >= 14 and currentTime < 18 :
                requestUrl1 = requests.get(apiUrl1)
                fileManager(requestUrl1)
                time.sleep(14700) # 4h && 5min
            elif currentTime >= 18 and currentTime < 23 :
                requestUrl1 = requests.get(apiUrl2)
                fileManager(requestUrl1)
                time.sleep(21900) # 6h && 5 min
            elif currentTime >= 0 and currentTime < 6 :
                requestUrl1 = requests.get(apiUrl2)
                fileManager(requestUrl1)
                time.sleep(18300) # 6h && 5 min
            
        except Exception as e :
            requestUrl1 = requests.get(apiUrl1)
            requestUrl1 = requests.get(apiUrl2)
            erorContlorrer = requestUrl1.status_code
            if erorContlorrer == (200):
                logAction("You have response 200 which means standard respons in price API")
            elif erorContlorrer == (400):
                logAction("You have response 400 which means bad request in price API")
            elif erorContlorrer == (401):
                logAction("You have response 401 which means unauthrozed in price API")
            elif erorContlorrer == (404):
                logAction("You have response 404 which means not found in price API") 
            elif erorContlorrer == (422):
                logAction("You have response 422 which means Unprocessable Entity in price API")
            elif erorContlorrer == (429):
                logAction("You have response 429 which means Too Many Requests in price API")
            elif erorContlorrer == (503):
                logAction("You have response 503 which means Service Unavailable in price API") 
            else :
                logAction(f"You have an unknown problem with the API of price ---{e}---")   
                
            requestUrl1 = None


exUsdValue = (0)
def exusd():
    global exUsdValue
    exUsdValue = int(exUsdValue)
    usdStatus = int(usdValue)
    if int(usdValue) > exUsdValue:
        usdStatus = int(usdValue) - exUsdValue
        exUsdValue = int(usdValue)
        return usdStatus
    elif int(usdValue) < exUsdValue:
        usdStatus = exUsdValue - int(usdValue)
        exUsdValue = int(usdValue)
        return "-" + str(usdStatus)
        
exEurValue = (0)
def exeur():
    global exEurValue
    exEurValue = int(exEurValue)
    eurStatus = int(eurValue)
    if int(eurValue) > exEurValue:
        eurStatus = int(eurValue) - exEurValue
        exEurValue = int(eurValue)
        return eurStatus
    elif int(eurValue) < exUsdValue:
        eurStatus = exEurValue - int(eurValue)
        exEurValue = int(eurValue)
        return "-" + str(eurStatus)
    
    
exDirhamValue = (0)
def exDiraham():
    global exDirhamValue
    exDirhamValue = int(exDirhamValue)
    dirhamStatus = int(dirhamDubaiValue)
    if int(dirhamDubaiValue) > exDirhamValue:
        dirhamStatus = int(dirhamDubaiValue) - exDirhamValue
        exDirhamValue = int(dirhamDubaiValue)
        return dirhamStatus
    elif int(dirhamDubaiValue) < exDirhamValue:
        dirhamStatus = exDirhamValue - int(dirhamDubaiValue)
        exDirhamValue = int(dirhamDubaiValue)
        return "-" + str(dirhamStatus)
    
exGold18Value = (0)
def exGold18():
    global exGold18Value
    exGold18Value = int(exGold18Value)
    gold18Status = int(gold18ayarValue)
    if int(gold18ayarValue) > exGold18Value:
        gold18Status = int(gold18ayarValue) - exGold18Value
        exGold18Value = int(gold18ayarValue)
        return gold18Status
    elif int(gold18ayarValue) < exGold18Value:
        gold18Status = exGold18Value - int(gold18ayarValue)
        exGold18Value = int(gold18ayarValue)
        return "-" + str(gold18Status)
    
exBaharCoinValue = (0)
def exBaharCoin():
    global exBaharCoinValue
    exBaharCoinValue = int(exBaharCoinValue)
    baharCoinStatus = int(baharCoinValue)
    if int(baharCoinValue) > exBaharCoinValue:
        baharCoinStatus = int(baharCoinValue) - exBaharCoinValue
        exBaharCoinValue = int(baharCoinValue)
        return baharCoinStatus
    elif int(baharCoinValue) < exBaharCoinValue:
        baharCoinStatus = exBaharCoinValue - int(baharCoinValue)
        exBaharCoinValue = int(baharCoinValue)
        return "-" + str(baharCoinStatus)
    
exNimCoinValue = (0)
def exNimCoin():
    global exNimCoinValue
    exNimCoinValue = int(exNimCoinValue)
    nimCoinStatus = int(nimCoinValue)
    if int(nimCoinValue) > exNimCoinValue:
        nimCoinStatus = int(nimCoinValue) - exNimCoinValue
        exNimCoinValue = int(nimCoinValue)
        return nimCoinStatus
    elif int(nimCoinValue) < exNimCoinValue:
        nimCoinStatus = exNimCoinValue - int(nimCoinValue)
        exNimCoinValue = int(nimCoinValue)
        return "-" + str(nimCoinStatus)
    
exRobCoinValue = (0)
def exRobCoin():
    global exRobCoinValue
    exRobCoinValue = int(exRobCoinValue)
    robCoinStatus = int(robCoinValue)
    if int(robCoinValue) > exRobCoinValue:
        robCoinStatus = int(robCoinValue) - exRobCoinValue
        exRobCoinValue = int(robCoinValue)
        return robCoinStatus
    elif int(robCoinValue) < exRobCoinValue:
        robCoinStatus = exRobCoinValue - int(robCoinValue)
        exRobCoinValue = int(robCoinValue)
        return "-" + str(robCoinStatus)

def fileManager(requestUrl1):
    if requestUrl1 == None :
        print("You have problem with time API")
        time.sleep(5)
        sys.exit()
    
    try :
        apiResponse = requestUrl1.json()

        global usdValue
        usdValue = ((apiResponse["usd"])["value"])
        usdDate = ((apiResponse["usd"])["date"])
        usdStatus = exusd()
        
        global eurValue
        eurValue = ((apiResponse["eur"])["value"])
        eurDate = ((apiResponse["eur"])["date"])
        eurStatus = exeur()

        global dirhamDubaiValue
        dirhamDubaiValue = ((apiResponse["dirham_dubai"])["value"])
        dirhamDubaiDate =  ((apiResponse["dirham_dubai"])["date"])
        dirhamStatus = exDiraham()

        global gold18ayarValue
        gold18ayarValue = ((apiResponse["18ayar"])["value"])
        gold18ayarDate = ((apiResponse["18ayar"])["date"])
        gold18Status = exGold18()

        global baharCoinValue
        baharCoinValue = ((apiResponse["bahar"])["value"])
        baharCoinDate = ((apiResponse["bahar"])["date"])
        baharCoinStatus = exBaharCoin()

        global nimCoinValue
        nimCoinValue = ((apiResponse["nim"])["value"])
        nimCoinDate = ((apiResponse["nim"])["date"])
        nimCoinStatus = exNimCoin()
        
        global robCoinValue
        robCoinValue = ((apiResponse["rob"])["value"])
        robCoinDate = ((apiResponse["rob"])["date"])  
        robCoinStatus = exRobCoin()
        
        finalData = {"usdValue":usdValue , "usdDate":usdDate , "usdStatus":usdStatus,
                    "eurValue":eurValue , "eurDate" :eurDate , "eurStatus":eurStatus , 
                    "dirhamValue":dirhamDubaiValue , "dirhamDate":dirhamDubaiDate , "dirhamStatus":dirhamStatus , 
                    "gold18ayarValue":gold18ayarValue , "gold18ayarDate":gold18ayarDate , "gold18Status":gold18Status , 
                    "baharCoinValue":baharCoinValue , "baharCoinDate":baharCoinDate , "baharCoinStatus":baharCoinStatus ,
                    "nimCoinValue":nimCoinValue , "nimCoinDate":nimCoinDate , "nimCoinStatus":nimCoinStatus , 
                    "robCoinValue":robCoinValue , "robCoinDate":robCoinDate , "robCoinStatus":robCoinStatus }
    except Exception as e :
        finalData = None
        print(":::(Because the data could not be found in the file, None was written):::" ,f"({e}):::")
    
    saver = open("bizarar_data.txt" ,"w")
    saver.write(str(finalData))
    saver.close()
    
    now = datetime.datetime.now()
    currentTime = now.strftime("%H:%M:%S")
    
    print(f":::(All data was copied to the file):::({currentTime}):::")
    
requestManager()


