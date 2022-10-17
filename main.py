import requests
import os
import json
import time

#by LinuxLeaks Skid = U Like men fortnite battle pass peter grifin

cosmeticname = input("Cosmetic name: ")
r = requests.get(f'https://fortnite-api.com/v2/cosmetics/br/search?name={cosmeticname}')
data = r.json()
print(data)
name = data["data"]["name"]
description = data["data"]["description"]
set = data["data"]["set"]["value"]
type = data["data"]["type"]["value"]
id = data["data"]["id"]
path = data["data"]["path"]
icon = data["data"]["images"]["icon"]
smallIcon = data["data"]["images"]["smallIcon"]
featured = data["data"]["images"]["featured"]
print("ㅤ")
print("ㅤ")
print("ㅤ")
print("ㅤ")
print("ㅤ")
print("ㅤ")
print("ㅤ")
print("ㅤ")
print("ㅤ")
print("ㅤ")
print("ㅤ")
print("ㅤ")
print("ㅤ")
print("ㅤ")
print("ㅤ")
print("ㅤ")
print("ㅤ")
print("ㅤ")
print("ㅤ")
print("ㅤ")
print("ㅤ")
print("ㅤ")
print("ㅤ")

print("Cosmetic's Info")
print(f'Name: {name}')
print(f'Description: {description}')
#print(f'Type: {type}')
if set == None:
      print("Set: Null")
else:
  print(f'Set: {set}')
print(f'Type: {type}')
print(f'ID: {id}')
print(f'path: {path}')
print(f'Icon: {icon}')
print(f'smallIcon: {smallIcon}')
print(f'Featured: {featured}')

time.sleep(int(1))
