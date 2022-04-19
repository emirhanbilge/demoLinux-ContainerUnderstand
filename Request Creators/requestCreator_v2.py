
import subprocess
import threading


def startServer():

    try:
        bashCommand = "curl localhost:8080"
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
    except :
        print("Some error occur")

for i in range(100):
    startServer()





def thread_function(name):
    for i in range(100):
        startServer()

if __name__ == "__main__":


    x = threading.Thread(target=thread_function, args=(1,))
    y = threading.Thread(target=thread_function, args=(1,))
    x.start()
    y.start()
    x.join()
    y.join()

