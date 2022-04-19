import subprocess

def startServer():

    try:
        bashCommand = "curl localhost:8080"
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
    except :
        print("Some error occur")

for i in range(100):
    startServer()
