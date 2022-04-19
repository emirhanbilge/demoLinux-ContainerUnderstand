import subprocess
import threading
import time 


global beforeNumber
beforeNumber = 4



try:
    bashCommand = "/home/pi/./instanceWriter.sh"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
except :
    print("Some error occur")

def startServer(compress):
    
    
    try:
        bashCommand = "/home/pi/./instanceWriter.sh"
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
    except :
        print("Some error occur")

    f = open("numberofservers.txt","r")
    readed = f.read()
    print(readed)
    f.close()
    numberofservices = len(readed.split(" "))
    if 4 == numberofservices:
        print("Sistem Normal ve Defaultta çalışıyor")
    elif numberofservices> 4 :
        print("Instance sayısı artmış halde çalışıyor")
        compress = numberofservices
    else:
        print("Instance Sayısı Azaltıldı")
    
compress = 4
while(True):
    startServer(compress)
    time.sleep(2)
