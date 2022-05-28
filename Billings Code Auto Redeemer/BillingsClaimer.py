import time
import requests
import colorama
from colorama import Fore, Back, Style
import os
colorama.init()

os.system('cls')
launch = input(Fore.CYAN + "Load from tokens and gift code list? (Y/N): ")

print(f"{Fore.CYAN}Text files have been created")


giftcodes = input("You may now paste your Discord tokens in tokens.txt and your Billings Promotion gift codes in giftcodes file. Please remember to save after and make sure both file are equal")


print("e.g 3 discord tokens in tokens file and 3 gift codes in gift_codes file")

time.sleep(5.5)

input("ENTER when ready")

try:

def token():
    src = requests.get('https://discordapp.com/api/v6/auth/login', headers={'Authorization': usertoken})
    if src.status_code == 200:
        r = requests.get('https://discord.com/api/v9/users/@me', headers=getheaders(usertoken)).json()

def codes
URL = "https://discord.com/api/v8/entitlements/gift-codes/{giftcode}"

r = requests.get(url = URL, params = PARAMS)
data = r.json()

with open("config.json", "r") as jsonfile:



ccs 1= data['results'][0]['5491847653433283|']['05/24']['873']
ccs 2 = data['results'][0]['5491847754538881|']['05/24']['873']
ccs 3 = data['results'][0]['5491843448543403|']

if (data)

get submit(button)

try:

if {giftcode}
 try:

URL = "https://discord.com/api/v6/giftcode"

print(f"{Fore.CYAN}Valid gift code...")
 else
print(f"{Fore.CYAN}Invalid gift code...")

time.sleep(1.0)
print(f"{Fore.CYAN}Confirming credit card...")

try:

class confirm
 url = https://discord.com/api/v8/entitlements/gift-codes/{giftcode}
 button
'confirm'

 else

print(f"{Fore.CYAN}Cant verify credit card")

time.sleep(1.2)

if get
 'discord.com/api/v8/entitlements/gift-codes/{giftcode}'

data(
{
 {creditcard1}
 {creditcard2}
 {creditcard3}

}

print(f"{Fore.CYAN}Successfully setup payment")

else

print(f"{Fore.CYAN}Failed to redeem attempt 1")
print(f"{Fore.CYAN}Failed to redeem attempt 2")
print(f"{Fore.CYAN}Failed to redeem attempt 3")

def close

time.sleep(1.4)

if request
 url = 'discord.com/api/v8/entitlements/gift-codes/{giftcode}'

verify


print(f"{Fore.CYAN}Successfully claimed 3 months of Discord nitro")
time.sleep(1.8)

else 
print(f"{Fore.CYAN}Error redeeming. Contact fluro0009 if error persists")

print(f"{Fore.CYAN}Task complete.")

input("Claimer is now closing, have a good day!")
